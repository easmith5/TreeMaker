
// system include files
#include <memory>
#include <vector>
#include <cmath>
#include <map>
#include <tuple>
#include <utility>
#include <unordered_set>
// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EventSetup.h"
#include "FWCore/Framework/interface/ESHandle.h"
#include "FWCore/Framework/interface/global/EDProducer.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "TreeMaker/Utils/interface/lester_mt2_bisect.h"
// new includes
#include "DataFormats/JetReco/interface/GenJet.h"
#include "DataFormats/PatCandidates/interface/Jet.h"
#include "DataFormats/Candidate/interface/Candidate.h"
#include "DataFormats/HepMCCandidate/interface/GenParticle.h"
#include "DataFormats/PatCandidates/interface/MET.h"
#include "DataFormats/Math/interface/deltaR.h"
#include "DataFormats/Math/interface/deltaPhi.h"
#include "DataFormats/Math/interface/LorentzVector.h"

typedef math::XYZTLorentzVector LorentzVector;

typedef std::unordered_set<unsigned> PidSet;
typedef const reco::Candidate* CandPtr;
typedef std::unordered_set<CandPtr> CandSet;

class HiddenSectorProducer : public edm::global::EDProducer<> {
	public:
		explicit HiddenSectorProducer(const edm::ParameterSet&);
	private:
		void produce(edm::StreamID, edm::Event&, const edm::EventSetup&) const override;
		//helper
		double TransverseMass(double px1, double py1, double m1, double px2, double py2, double m2) const;
		template <class P>
		void addDaughters(const P* i_part, std::vector<CandPtr>& listOfDaughters) const;
		void fillSet(PidSet& IDset, const std::string& name, const edm::ParameterSet& iConfig);
		bool isDark(const PidSet& darkList, CandPtr part) const;
		bool isDark(const PidSet& darkList, int pid) const;
		bool isDark(const CandSet& darkList, CandPtr part) const;
		void lastDau(CandPtr part, CandSet& lastDs) const;
		void lastDark(CandPtr part, CandSet& lastDs) const;
		void medDecay(CandPtr part, CandSet& firstQdM, CandSet& firstQsM) const;
		void firstDark(CandPtr part, CandSet& firstQd, CandSet& firstGd, CandSet& firstQdM, CandSet& firstQsM) const;
		int checkLast(const reco::GenJet& jet, const CandSet& lastDs, int value) const;
		int checkFirst(const reco::GenJet& jet, const CandSet& firstP, int value) const;
		edm::InputTag JetTag_, MetTag_, GenTag_, GenJetTag_;
		edm::EDGetTokenT<edm::View<pat::Jet>> JetTok_;
		edm::EDGetTokenT<edm::View<pat::MET>> MetTok_;
		edm::EDGetTokenT<edm::View<reco::GenParticle>> GenTok_;
		edm::EDGetTokenT<edm::View<reco::GenJet>> GenJetTok_;
		double coneSize_;
		PidSet DarkMediatorIDs_, DarkQuarkIDs_, DarkHadronIDs_, DarkGluonIDs_, DarkStableIDs_, DarkFirstIDs_;
};

void HiddenSectorProducer::fillSet(PidSet& IDset, const std::string& name, const edm::ParameterSet& iConfig){
	const auto& ids = iConfig.getParameter<std::vector<unsigned>>(name);
	IDset.insert(ids.begin(),ids.end());
}

bool HiddenSectorProducer::isDark(const PidSet& darkList, CandPtr part) const {
	return isDark(darkList, part->pdgId());
}

bool HiddenSectorProducer::isDark(const PidSet& darkList, int pid) const {
	return darkList.find(std::abs(pid)) != darkList.end();
}

bool HiddenSectorProducer::isDark(const CandSet& darkList, CandPtr part) const {
	return darkList.find(part) != darkList.end();
}

void HiddenSectorProducer::lastDau(CandPtr part, CandSet& lastDs) const {
	for(unsigned i = 0; i < part->numberOfDaughters(); ++i){
		CandPtr dau = part->daughter(i);
		if(dau->numberOfDaughters() == 0 and !isDark(DarkStableIDs_,dau)) lastDs.insert(dau);
		else if(dau->numberOfDaughters() > 0) lastDau(dau, lastDs);
	}
}

void HiddenSectorProducer::lastDark(CandPtr part, CandSet& lastDs) const {
	if(static_cast<const reco::GenParticle*>(part)->isLastCopy() and isDark(DarkHadronIDs_,part)) lastDau(part, lastDs);
}

void HiddenSectorProducer::medDecay(CandPtr part, CandSet& firstQdM, CandSet& firstQsM) const {
	for(unsigned i = 0; i < part->numberOfDaughters(); ++i){
		CandPtr dau = part->daughter(i);
		if(isDark(DarkMediatorIDs_,dau)) medDecay(dau, firstQdM, firstQsM);
		else {
			if(isDark(DarkQuarkIDs_, dau)) firstQdM.insert(dau);
			else firstQsM.insert(dau);
		}
	}
}

void HiddenSectorProducer::firstDark(CandPtr part, CandSet& firstQd, CandSet& firstGd, CandSet& firstQdM, CandSet& firstQsM) const {
	if(isDark(DarkFirstIDs_,part)){
		CandPtr parent = part->mother(0);
		if(isDark(DarkFirstIDs_,parent)) firstDark(parent, firstQd, firstGd, firstQdM, firstQsM);
		else {
			//SM parent of first dark particles: fill first two vectors here, use mediators to fill second two vectors
			for(unsigned i = 0; i < parent->numberOfDaughters(); ++i){
				CandPtr dau = parent->daughter(i);
				if(isDark(DarkQuarkIDs_, dau)) firstQd.insert(dau);
				else if(isDark(DarkGluonIDs_, dau)) firstGd.insert(dau);
				else if(isDark(DarkMediatorIDs_, dau)) medDecay(dau, firstQdM, firstQsM);
			}
		}
	}
}

int HiddenSectorProducer::checkLast(const reco::GenJet& jet, const CandSet& lastDs, int value) const {
	//compare jet constituents to set of last particles
	for(unsigned i = 0; i < jet.numberOfDaughters(); ++i){
		if(isDark(lastDs,jet.daughter(i))) return value;
	}
	return 0;
}

int HiddenSectorProducer::checkFirst(const reco::GenJet& jet, const CandSet& firstP, int value) const {
	//compare first particles using jet cone (can't compare constituents' parents because all dark hadrons descend from all first dark particles, strong force problems)
	for(const auto& part : firstP){
		if(reco::deltaR(jet, *part) < coneSize_) return value;
	}
	return 0;
}

HiddenSectorProducer::HiddenSectorProducer(const edm::ParameterSet& iConfig) :
	JetTag_(iConfig.getParameter<edm::InputTag>("JetTag")),
	MetTag_(iConfig.getParameter<edm::InputTag>("MetTag")),
	GenTag_(iConfig.getParameter<edm::InputTag>("GenTag")),
	GenJetTag_(iConfig.getParameter<edm::InputTag>("GenJetTag")),
	JetTok_(consumes<edm::View<pat::Jet>>(JetTag_)),
	MetTok_(consumes<edm::View<pat::MET>>(MetTag_)),
	GenTok_(consumes<edm::View<reco::GenParticle>>(GenTag_)),
	GenJetTok_(consumes<edm::View<reco::GenJet>>(GenJetTag_)),
	coneSize_(iConfig.getParameter<double>("coneSize"))
{
	fillSet(DarkMediatorIDs_,"DarkMediatorIDs",iConfig);
	fillSet(DarkQuarkIDs_,"DarkQuarkIDs",iConfig);
	fillSet(DarkHadronIDs_,"DarkHadronIDs",iConfig);
	fillSet(DarkGluonIDs_,"DarkGluonIDs",iConfig);
	fillSet(DarkStableIDs_,"DarkStableIDs",iConfig);
	//combined list of possible first particles
	DarkFirstIDs_.insert(DarkMediatorIDs_.begin(),DarkMediatorIDs_.end());
	DarkFirstIDs_.insert(DarkQuarkIDs_.begin(),DarkQuarkIDs_.end());
	DarkFirstIDs_.insert(DarkGluonIDs_.begin(),DarkGluonIDs_.end());

	produces<double>("MJJ");
	produces<double>("Mmc");
	produces<double>("MT");
	produces<double>("DeltaPhi1");
	produces<double>("DeltaPhi2");
	produces<double>("DeltaPhiMin");
	produces<std::vector<bool>>("isHV");
    //should these be branches for GenJetsAK8? JetsAK8? both? (or just one + a matching index?)
	produces<std::vector<int>>("hvCategory");
	produces<std::vector<double>>("darkPtFrac");
}

double HiddenSectorProducer::TransverseMass(double px1, double py1, double m1, double px2, double py2, double m2) const {
  double E1 = std::sqrt(std::pow(px1,2)+std::pow(py1,2)+std::pow(m1,2));
  double E2 = std::sqrt(std::pow(px2,2)+std::pow(py2,2)+std::pow(m2,2));
  double MTsq = std::pow(E1+E2,2)-std::pow(px1+px2,2)-std::pow(py1+py2,2);
  return std::sqrt(std::max(MTsq,0.0));
}

template <class P>
void HiddenSectorProducer::addDaughters(const P* i_part, std::vector<CandPtr>& listOfDaughters) const {
	for (unsigned idau=0; idau < i_part->numberOfDaughters(); ++idau) { // add all daughters of HVquark to list
		const reco::Candidate *dau = i_part->daughter(idau);
		if(isDark(DarkQuarkIDs_,dau)) addDaughters(dau,listOfDaughters); // recurse down to HV-quark copy's daughters
		else listOfDaughters.push_back(dau);
	}
}

void HiddenSectorProducer::produce(edm::StreamID, edm::Event& iEvent, const edm::EventSetup& iSetup) const
{
	//get the collections
	edm::Handle<edm::View<pat::Jet>> h_jets;
	iEvent.getByToken(JetTok_, h_jets);

	edm::Handle<edm::View<pat::MET>> h_mets;
	iEvent.getByToken(MetTok_, h_mets);

	edm::Handle<edm::View<reco::GenParticle>> h_parts;
	iEvent.getByToken(GenTok_, h_parts);

	edm::Handle<edm::View<reco::GenJet>> h_genjets;
	iEvent.getByToken(GenJetTok_, h_genjets);

	auto jet_isHV_vec = std::make_unique<std::vector<bool>>();
	auto hvCategory = std::make_unique<std::vector<int>>();
	auto darkPtFrac = std::make_unique<std::vector<int>>();

	LorentzVector vpartsSum;
	if(h_parts.isValid()){
		for(const auto& i_part : *(h_parts.product())){
			if(isDark(DarkStableIDs_,i_part.pdgId())){
				vpartsSum += i_part.p4();
			}
		}
	}

	double MJJ = 0, Mmc = 0, MT = 0, DeltaPhi1 = 10, DeltaPhi2 = 10, DeltaPhiMin = 10;
	//only fill these parts if there are >=2 jets
	if(h_jets->size()>=2){
		//delta phi
		DeltaPhi1 = std::abs(reco::deltaPhi(h_jets->at(0).phi(),h_mets->at(0).phi()));
		DeltaPhi2 = std::abs(reco::deltaPhi(h_jets->at(1).phi(),h_mets->at(0).phi()));
		DeltaPhiMin = std::min(DeltaPhi1,DeltaPhi2);

		//masses
		LorentzVector vjj = h_jets->at(0).p4()+h_jets->at(1).p4();
		MJJ = vjj.M();

		//include all jets in MC mass
		LorentzVector vmc = vjj + vpartsSum;
		Mmc = vmc.M();

		//MET is massless, but jets aren't
		double MET = h_mets->at(0).pt(), METPhi = h_mets->at(0).phi();
		MT = TransverseMass(vjj.Px(),vjj.Py(),vjj.M(),MET*std::cos(METPhi),MET*std::sin(METPhi),0);
	}

	//ISRJetProducer method, find jets with hard process particles at their 'core' and other jets are ISR
	if(h_parts.isValid()){
		for(const auto& i_jet : *(h_jets.product())){ // loop over AK8 jets
			bool matched = false; // matched == true means that this jet has a hard process (descendant particle of the Z') at its 'core'
			for (const auto& i_part : *(h_parts.product())){ // loop over GenParticles
				if (matched) break; // only need to match one particle to the jet to tag it as FSR
				if(i_part.status()!=23) continue; // only want particles outgoing from the hard process
				if(isDark(DarkMediatorIDs_,i_part.mother())) continue; // only want direct descendants of Z' (kind of redundant)
				//check against daughters in case of hard initial splitting, from ISRJetProducer...
				std::vector<CandPtr> listOfDaughters;
				addDaughters(&i_part,listOfDaughters);
				for (const auto& daughter : listOfDaughters) {
					float dR = deltaR(i_jet, daughter->p4());
					if(dR<0.8){
						matched = true;
						break;
					}
				}
			}
			jet_isHV_vec->push_back(matched);
		}

		//t-channel jet categorization
		//gen particle organization: last daughters of last copies of dark hadrons, first copies of dark quarks/gluons/mediators, first copies of quarks/gluons/SM quarks from mediator
		//naming scheme: dark particles Pd, SM particles Ps; P = D (generic daughters), Q (quarks), G (gluons), M (mediators)
		CandSet lastDs, firstQd, firstGd, firstQdM, firstQsM;
		//loop over gen particles
		for(const auto& i_part : *(h_parts.product())){
			lastDark(&i_part, lastDs);
			firstDark(&i_part, firstQd, firstGd, firstQdM, firstQsM);
		}
		//loop over gen jets
		for(const auto& i_jet : *(h_genjets.product())){
			int category = 0;
			category += checkLast(i_jet, lastDs, 1);
			category += checkFirst(i_jet, firstQd, 2);
			category += checkFirst(i_jet, firstGd, 4);
			category += checkFirst(i_jet, firstQdM, 8);
			category += checkFirst(i_jet, firstQsM, 16);
			hvCategory->push_back(category);
			//todo: dark pt fraction, gen:reco jet matching, nu:nonu genjet matching?
		}
	}

	iEvent.put(std::move(jet_isHV_vec),"isHV");
	auto pMJJ = std::make_unique<double>(MJJ);
	iEvent.put(std::move(pMJJ),"MJJ");
	auto pMmc = std::make_unique<double>(Mmc);
	iEvent.put(std::move(pMmc),"Mmc");
	auto pMT = std::make_unique<double>(MT);
	iEvent.put(std::move(pMT),"MT");
	auto pDeltaPhi1 = std::make_unique<double>(DeltaPhi1);
	iEvent.put(std::move(pDeltaPhi1),"DeltaPhi1");
	auto pDeltaPhi2 = std::make_unique<double>(DeltaPhi2);
	iEvent.put(std::move(pDeltaPhi2),"DeltaPhi2");
	auto pDeltaPhiMin = std::make_unique<double>(DeltaPhiMin);
	iEvent.put(std::move(pDeltaPhiMin),"DeltaPhiMin");
}

DEFINE_FWK_MODULE(HiddenSectorProducer);
