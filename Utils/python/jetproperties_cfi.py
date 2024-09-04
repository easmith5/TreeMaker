import FWCore.ParameterSet.Config as cms

jetproperties = cms.EDProducer('JetProperties',
    JetTag       = cms.InputTag('slimmedJets'),
    debug = cms.bool(False),
    properties = cms.vstring(
        "chargedHadronMultiplicity"  ,
        "neutralHadronMultiplicity"  ,
        "electronMultiplicity"       ,
        "photonMultiplicity"         ,
        "muonMultiplicity"           ,
        "NumBhadrons"                ,
        "NumChadrons"                ,
        "chargedMultiplicity"        ,
        "neutralMultiplicity"        ,
        "nConstituents"              ,
        "partonFlavor"               ,
        "hadronFlavor"               ,
        "jetArea"                    ,
        "chargedHadronEnergyFraction",
        "neutralHadronEnergyFraction",
        "chargedEmEnergyFraction"    ,
        "neutralEmEnergyFraction"    ,
        "electronEnergyFraction"     ,
        "photonEnergyFraction"       ,
        "muonEnergyFraction"         ,
        "hfEMEnergyFraction"         ,
        "hfHadronEnergyFraction"     ,
        "bDiscriminatorCSV"          ,
        "bJetTagDeepCSVprobb"        ,
        "bJetTagDeepCSVprobc"        ,
        "bJetTagDeepCSVprobudsg"    ,
        "bJetTagDeepCSVprobbb"       ,
        "bDiscriminatorDeepCSVBvsAll",
        "bDiscriminatorDeepCSVCvsB"  ,
        "bDiscriminatorDeepCSVCvsL"  ,
        "bJetTagDeepFlavourprobb"    ,
        "bJetTagDeepFlavourprobc"    ,
        "bJetTagDeepFlavourprobg"    ,
        "bJetTagDeepFlavourproblepb" ,
        "bJetTagDeepFlavourprobbb"   ,
        "bJetTagDeepFlavourprobuds"  ,
    ),
    bDiscriminatorCSV = cms.vstring('pfCombinedInclusiveSecondaryVertexV2BJetTags'),
    bJetTagDeepCSVprobb = cms.vstring('pfDeepCSVJetTags:probb'),
    bJetTagDeepCSVprobc = cms.vstring('pfDeepCSVJetTags:probc'),
    bJetTagDeepCSVprobudsg = cms.vstring('pfDeepCSVJetTags:probudsg'),
    bJetTagDeepCSVprobbb = cms.vstring('pfDeepCSVJetTags:probbb'),
    bDiscriminatorDeepCSVBvsAll = cms.vstring('pfDeepCSVDiscriminatorsJetTags:BvsAll'),
    bDiscriminatorDeepCSVCvsB = cms.vstring('pfDeepCSVDiscriminatorsJetTags:CvsB'),
    bDiscriminatorDeepCSVCvsL = cms.vstring('pfDeepCSVDiscriminatorsJetTags:CvsL'),
    bJetTagDeepFlavourprobb = cms.vstring('pfDeepFlavourJetTags:probb'),
    bJetTagDeepFlavourprobc = cms.vstring('pfDeepFlavourJetTags:probc'),
    bJetTagDeepFlavourprobg = cms.vstring('pfDeepFlavourJetTags:probg'),
    bJetTagDeepFlavourproblepb = cms.vstring('pfDeepFlavourJetTags:problepb'),
    bJetTagDeepFlavourprobbb = cms.vstring('pfDeepFlavourJetTags:probbb'),
    bJetTagDeepFlavourprobuds = cms.vstring('pfDeepFlavourJetTags:probuds'),
)
