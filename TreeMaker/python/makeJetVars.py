import FWCore.ParameterSet.Config as cms
from TreeMaker.TreeMaker.addJetInfo import addJetInfo

def makeMHTVars(self, process, JetTag, HTJetsTag, storeProperties, suff, MHTsuff):
    from TreeMaker.Utils.subJetSelection_cfi import SubJetSelection
    MHTJets = SubJetSelection.clone(
        JetTag = JetTag,
        MinPt  = cms.double(30),
        MaxEta = cms.double(5.0),
    )
    setattr(process,"MHTJets"+MHTsuff+suff,MHTJets)
    if storeProperties>0: self.VectorBool.extend(['MHTJets'+MHTsuff+suff+':SubJetMask(Jets'+suff+'_MHT'+MHTsuff+'Mask)'])
    MHTJetsTag = cms.InputTag("MHTJets"+MHTsuff+suff)
    
    from TreeMaker.Utils.mhtdouble_cfi import mhtdouble
    MHT = mhtdouble.clone(
        JetTag  = MHTJetsTag,
    )
    setattr(process,"MHT"+MHTsuff+suff,MHT)
    self.VarsDouble.extend(['MHT'+MHTsuff+suff+':Pt(MHT'+MHTsuff+suff+')','MHT'+MHTsuff+suff+':Phi(MHTPhi'+MHTsuff+suff+')'])
    
    from TreeMaker.Utils.deltaphidouble_cfi import deltaphidouble
    DeltaPhi = deltaphidouble.clone(
        DeltaPhiJets = HTJetsTag,
        MHTPhi       = cms.InputTag('MHT'+MHTsuff+suff+':Phi'),
    )
    setattr(process,"DeltaPhi"+MHTsuff+suff,DeltaPhi)
    self.VarsDouble.extend(['DeltaPhi'+MHTsuff+suff+':DeltaPhi1(DeltaPhi1'+MHTsuff+suff+')','DeltaPhi'+MHTsuff+suff+':DeltaPhi2(DeltaPhi2'+MHTsuff+suff+')',
                                          'DeltaPhi'+MHTsuff+suff+':DeltaPhi3(DeltaPhi3'+MHTsuff+suff+')','DeltaPhi'+MHTsuff+suff+':DeltaPhi4(DeltaPhi4'+MHTsuff+suff+')'])
    
    return process

def makeGoodJets(self, process, JetTag, suff, storeProperties, SkipTag=cms.VInputTag()):
    from TreeMaker.Utils.goodjetsproducer_cfi import GoodJetsProducer
    GoodJets = GoodJetsProducer.clone(
        TagMode                   = cms.bool(True),
        JetTag                    = JetTag,
        maxJetEta                 = cms.double(5.0),
        minNconstituents          = cms.int32(1),
        minNneutrals              = cms.int32(10),
        minNcharged               = cms.int32(0),
        maxNeutralFraction        = cms.double(0.99),
        maxPhotonFraction         = cms.double(0.99),
        maxPhotonFractionHF       = cms.double(0.90),
        minChargedFraction        = cms.double(0),
        maxChargedEMFraction      = cms.double(0.99),
        jetPtFilter               = cms.double(30),
        ExcludeLepIsoTrackPhotons = cms.bool(True),
        JetConeSize               = cms.double(0.4),
        SkipTag                   = SkipTag,
        SaveAllJetsId             = True,
        SaveAllJetsPt             = False, # exclude low pt jets from good collection
    )
    if self.fastsim: GoodJets.jetPtFilter = cms.double(20)
    setattr(process,"GoodJets"+suff,GoodJets)
    GoodJetsTag = cms.InputTag("GoodJets"+suff)
    self.VarsBool.extend(['GoodJets'+suff+':JetID(JetID'+suff+')'])
    if storeProperties>0:
        self.VectorRecoCand.extend(['GoodJets'+suff+'(Jets'+suff+')'])
        self.VectorBool.extend(['GoodJets'+suff+':JetIDMask(Jets'+suff+'_ID)'])
        if len(SkipTag)>0: self.VectorBool.extend(['GoodJets'+suff+':JetLeptonMask(Jets'+suff+'_LeptonMask)'])
    return (process,GoodJetsTag)


def makeJetVars(self, process, JetTag, suff, skipGoodJets, storeProperties, SkipTag=cms.VInputTag(), onlyGoodJets=False):
    ## ----------------------------------------------------------------------------------------------
    ## GoodJets
    ## ----------------------------------------------------------------------------------------------
    if skipGoodJets:
        GoodJetsTag = JetTag
    else:
        process, GoodJetsTag = self.makeGoodJets(process,JetTag,suff,storeProperties,SkipTag)
        if onlyGoodJets:
            return process
    
    ## ----------------------------------------------------------------------------------------------
    ## HT
    ## ----------------------------------------------------------------------------------------------
    from TreeMaker.Utils.subJetSelection_cfi import SubJetSelection
    HTJets = SubJetSelection.clone(
        JetTag = GoodJetsTag,
        MinPt  = cms.double(30),
        MaxEta = cms.double(2.4),
    )
    setattr(process,"HTJets"+suff,HTJets)
    if storeProperties>0: self.VectorBool.extend(['HTJets'+suff+':SubJetMask(Jets'+suff+'_HTMask)'])
    HTJetsTag = cms.InputTag("HTJets"+suff)
    
    from TreeMaker.Utils.htdouble_cfi import htdouble
    HT = htdouble.clone(
        JetTag = HTJetsTag,
    )
    setattr(process,"HT"+suff,HT)
    self.VarsDouble.extend(['HT'+suff])
    
    ## ----------------------------------------------------------------------------------------------
    ## NJets
    ## ----------------------------------------------------------------------------------------------
    from TreeMaker.Utils.njetint_cfi import njetint
    NJets = njetint.clone(
        JetTag = HTJetsTag,
    )
    setattr(process,"NJets"+suff,NJets)
    self.VarsInt.extend(['NJets'+suff])
    
    ## ----------------------------------------------------------------------------------------------
    ## BTags
    ## ----------------------------------------------------------------------------------------------
    from TreeMaker.Utils.btagint_cfi import btagint
    BTags = btagint.clone(
        JetTag       = HTJetsTag,
        BTagInputTag = cms.string('pfCombinedInclusiveSecondaryVertexV2BJetTags'),
        BTagCutValue = cms.double(0.8484)
    )
    setattr(process,"BTags"+suff,BTags)
    self.VarsInt.extend(['BTags'+suff])
    
    ## ----------------------------------------------------------------------------------------------
    ## MHT, DeltaPhi
    ## ----------------------------------------------------------------------------------------------
    # MHT, DeltaPhi moved to separate fn (above)
    process = self.makeMHTVars(process, GoodJetsTag, HTJetsTag, storeProperties, suff, "")

    ## ----------------------------------------------------------------------------------------------
    ## ISR jets
    ## ----------------------------------------------------------------------------------------------
    if self.geninfo:
        from TreeMaker.Utils.isrjet_cfi import ISRJetProducer
        ISRJets = ISRJetProducer.clone(
            JetTag = GoodJetsTag,
            JetLeptonTag  = cms.InputTag(GoodJetsTag.value()+':JetLeptonMask'),
            GenPartTag = cms.InputTag("prunedGenParticles"),
            MinPt  = cms.double(30),
            MaxEta = cms.double(2.4),
        )
        setattr(process,"ISRJets"+suff,ISRJets)
        if storeProperties>0:
            self.VectorBool.extend(['ISRJets'+suff+':SubJetMask(Jets'+suff+'_ISRMask)'])
            self.VarsInt.extend(['ISRJets'+suff+'(NJetsISR'+suff+')'])

    ## ----------------------------------------------------------------------------------------------
    ## Jet properties
    ## ----------------------------------------------------------------------------------------------
    
    if storeProperties>0:
        # make jet properties producer
        from TreeMaker.Utils.jetproperties_cfi import jetproperties
        JetProperties = jetproperties.clone(
            JetTag       = GoodJetsTag
        )
        # provide extra info where necessary
        if storeProperties==1: 
            JetProperties.properties = cms.vstring("bDiscriminatorCSV","muonEnergyFraction","chargedHadronEnergyFraction","partonFlavor","hadronFlavor")
        if storeProperties>1 and self.geninfo:
            JetProperties.properties.extend(["jerFactor", "jerFactorUp","jerFactorDown"])
        setattr(process,"JetProperties"+suff,JetProperties)
        self.VectorDouble.extend([
            'JetProperties'+suff+':bDiscriminatorCSV(Jets'+suff+'_bDiscriminatorCSV)',
            'JetProperties'+suff+':muonEnergyFraction(Jets'+suff+'_muonEnergyFraction)',
            'JetProperties'+suff+':chargedHadronEnergyFraction(Jets'+suff+'_chargedHadronEnergyFraction)',
        ])
        self.VectorInt.extend([
            'JetProperties'+suff+':partonFlavor(Jets'+suff+'_partonFlavor)',
            'JetProperties'+suff+':hadronFlavor(Jets'+suff+'_hadronFlavor)',
        ])
        if storeProperties>1:
            self.VectorDouble.extend([
                'JetProperties'+suff+':chargedEmEnergyFraction(Jets'+suff+'_chargedEmEnergyFraction)',
                'JetProperties'+suff+':neutralEmEnergyFraction(Jets'+suff+'_neutralEmEnergyFraction)',
                'JetProperties'+suff+':neutralHadronEnergyFraction(Jets'+suff+'_neutralHadronEnergyFraction)',
                'JetProperties'+suff+':photonEnergyFraction(Jets'+suff+'_photonEnergyFraction)',
                'JetProperties'+suff+':electronEnergyFraction(Jets'+suff+'_electronEnergyFraction)',
                'JetProperties'+suff+':hfEMEnergyFraction(Jets'+suff+'_hfEMEnergyFraction)',
                'JetProperties'+suff+':hfHadronEnergyFraction(Jets'+suff+'_hfHadronEnergyFraction)',
                'JetProperties'+suff+':jecFactor(Jets'+suff+'_jecFactor)',
                'JetProperties'+suff+':jecUnc(Jets'+suff+'_jecUnc)',
                'JetProperties'+suff+':qgLikelihood(Jets'+suff+'_qgLikelihood)',
                'JetProperties'+suff+':ptD(Jets'+suff+'_ptD)',
                'JetProperties'+suff+':axisminor(Jets'+suff+'_axisminor)',
                'JetProperties'+suff+':axismajor(Jets'+suff+'_axismajor)',
            ])
            if self.geninfo:
                self.VectorDouble.extend([
                    'JetProperties'+suff+':jerFactor(Jets'+suff+'_jerFactor)',
                    'JetProperties'+suff+':jerFactorUp(Jets'+suff+'_jerFactorUp)',
                    'JetProperties'+suff+':jerFactorDown(Jets'+suff+'_jerFactorDown)',
                ])

            self.VectorInt.extend([
                'JetProperties'+suff+':chargedHadronMultiplicity(Jets'+suff+'_chargedHadronMultiplicity)',
                'JetProperties'+suff+':electronMultiplicity(Jets'+suff+'_electronMultiplicity)',
                'JetProperties'+suff+':muonMultiplicity(Jets'+suff+'_muonMultiplicity)',
                'JetProperties'+suff+':neutralHadronMultiplicity(Jets'+suff+'_neutralHadronMultiplicity)',
                'JetProperties'+suff+':photonMultiplicity(Jets'+suff+'_photonMultiplicity)',
                'JetProperties'+suff+':chargedMultiplicity(Jets'+suff+'_chargedMultiplicity)',
                'JetProperties'+suff+':neutralMultiplicity(Jets'+suff+'_neutralMultiplicity)',
                'JetProperties'+suff+':multiplicity(Jets'+suff+'_multiplicity)',
            ])
                                             
    return process

def makeJetVarsAK8(self, process, JetTag, suff, storeProperties):
    # get more substructure
    if self.semivisible>0:
        from RecoJets.JetProducers.nJettinessAdder_cfi import Njettiness
        NjettinessBeta1 = Njettiness.clone(
            src = JetTag,
            cone = cms.double(0.8),
            storeAxes = cms.bool(True),
            Njets = cms.vuint32(1),
            beta = cms.double(1.0)
        )
        setattr(process,"NjettinessBeta1"+suff,NjettinessBeta1)
        NjettinessBeta2 = NjettinessBeta1.clone(
            beta = cms.double(2.0)
        )
        setattr(process,"NjettinessBeta2"+suff,NjettinessBeta2)
        BasicSubstructure = cms.EDProducer("BasicSubstructureProducer",
            JetTag = JetTag
        )
        setattr(process,"BasicSubstructure"+suff,BasicSubstructure)
        ak8floats = [
            'BasicSubstructure'+suff+':overflow',
            'BasicSubstructure'+suff+':girth',
            'BasicSubstructure'+suff+':momenthalf',
            'BasicSubstructure'+suff+':ptD',
            'BasicSubstructure'+suff+':axismajor',
            'BasicSubstructure'+suff+':axisminor',
            'NjettinessBeta1'+suff+':tau1etaAxis1',
            'NjettinessBeta1'+suff+':tau1phiAxis1',
            'NjettinessBeta2'+suff+':tau1etaAxis1',
            'NjettinessBeta2'+suff+':tau1phiAxis1',
        ]
        ak8ints = [
            'BasicSubstructure'+suff+':multiplicity',
        ]
    
        # add discriminator and update tag
        process, JetTag = addJetInfo(process, JetTag, ak8floats, ak8ints)

    process, GoodJetsTag = self.makeGoodJets(process,JetTag,suff,storeProperties)

    if storeProperties>0:
        # AK8 jet variables - separate instance of jet properties producer
        from TreeMaker.Utils.jetproperties_cfi import jetproperties
        JetPropertiesAK8 = jetproperties.clone(
            JetTag       = GoodJetsTag,
            properties = cms.vstring(
                "prunedMass"           ,
                "softDropMass"         ,
                "NsubjettinessTau1"    ,
                "NsubjettinessTau2"    ,
                "NsubjettinessTau3"    ,
                "bDiscriminatorCSV"    ,
                "NumBhadrons"          ,
                "NumChadrons"          ,
                "subjets"              ,
            )
        )
        # specify userfloats
        JetPropertiesAK8.prunedMass = cms.vstring('ak8PFJetsCHSPrunedMass')
        JetPropertiesAK8.softDropMass = cms.vstring('SoftDrop') # computed from subjets
        JetPropertiesAK8.NsubjettinessTau1 = cms.vstring('NjettinessAK8:tau1')
        JetPropertiesAK8.NsubjettinessTau2 = cms.vstring('NjettinessAK8:tau2')
        JetPropertiesAK8.NsubjettinessTau3 = cms.vstring('NjettinessAK8:tau3')
        JetPropertiesAK8.bDiscriminatorCSV = cms.vstring('pfBoostedDoubleSecondaryVertexAK8BJetTags')
        JetPropertiesAK8.subjets = cms.vstring('SoftDrop')
        self.VectorDouble.extend([
                             'JetProperties'+suff+':prunedMass(Jets'+suff+'_prunedMass)',
                             'JetProperties'+suff+':softDropMass(Jets'+suff+'_softDropMass)',
                             'JetProperties'+suff+':bDiscriminatorCSV(Jets'+suff+'_doubleBDiscriminator)',
                             'JetProperties'+suff+':NsubjettinessTau1(Jets'+suff+'_NsubjettinessTau1)',
                             'JetProperties'+suff+':NsubjettinessTau2(Jets'+suff+'_NsubjettinessTau2)',
                             'JetProperties'+suff+':NsubjettinessTau3(Jets'+suff+'_NsubjettinessTau3)'])
        self.VectorInt.extend(['JetProperties'+suff+':NumBhadrons(Jets'+suff+'_NumBhadrons)',
                          'JetProperties'+suff+':NumChadrons(Jets'+suff+'_NumChadrons)'])
        self.VectorVectorTLorentzVector.extend([
            'JetProperties'+suff+':subjets(Jets'+suff+'_subjets)',
        ])

        if self.semivisible>0:
            JetPropertiesAK8.properties.extend([
                'overflow',
                'girth',
                'momenthalf',
                'ptD',
                'axismajor',
                'axisminor',
                'multiplicity',
                'lean',
            ])
            JetPropertiesAK8.overflow = cms.vstring('BasicSubstructure'+suff+':overflow')
            JetPropertiesAK8.girth = cms.vstring('BasicSubstructure'+suff+':girth')
            JetPropertiesAK8.momenthalf = cms.vstring('BasicSubstructure'+suff+':momenthalf')
            JetPropertiesAK8.ptD = cms.vstring('BasicSubstructure'+suff+':ptD')
            JetPropertiesAK8.axismajor = cms.vstring('BasicSubstructure'+suff+':axismajor')
            JetPropertiesAK8.axisminor = cms.vstring('BasicSubstructure'+suff+':axisminor')
            JetPropertiesAK8.multiplicity = cms.vstring('BasicSubstructure'+suff+':multiplicity')
            JetPropertiesAK8.lean = cms.vstring(
                'NjettinessBeta1'+suff+':tau1etaAxis1',
                'NjettinessBeta1'+suff+':tau1phiAxis1',
                'NjettinessBeta2'+suff+':tau1etaAxis1',
                'NjettinessBeta2'+suff+':tau1phiAxis1',
            )
            self.VectorDouble.extend([
                'JetProperties'+suff+':overflow(Jets'+suff+'_overflow)',
                'JetProperties'+suff+':girth(Jets'+suff+'_girth)',
                'JetProperties'+suff+':momenthalf(Jets'+suff+'_momenthalf)',
                'JetProperties'+suff+':ptD(Jets'+suff+'_ptD)',
                'JetProperties'+suff+':axismajor(Jets'+suff+'_axismajor)',
                'JetProperties'+suff+':axisminor(Jets'+suff+'_axisminor)',
                'JetProperties'+suff+':lean(Jets'+suff+'_lean)',
            ])
            self.VectorInt.extend([
                'JetProperties'+suff+':multiplicity(Jets'+suff+'_multiplicity)',
            ])
            if self.semivisible==2:
                JetPropertiesAK8.properties.extend(['constituents'])
                self.VectorVectorTLorentzVector.extend([
                    'JetProperties'+suff+':constituents(Jets'+suff+'_constituents)',
                ])
        setattr(process,"JetProperties"+suff,JetPropertiesAK8)

    return process        
