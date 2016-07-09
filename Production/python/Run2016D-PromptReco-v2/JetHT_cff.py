import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/data/Run2016D/JetHT/MINIAOD/PromptReco-v2/000/276/315/00000/208AB2DD-0145-E611-910F-02163E0144AD.root',
       '/store/data/Run2016D/JetHT/MINIAOD/PromptReco-v2/000/276/315/00000/283C90B1-0445-E611-B0AF-02163E014393.root',
       '/store/data/Run2016D/JetHT/MINIAOD/PromptReco-v2/000/276/315/00000/48DA42E9-0145-E611-B53F-02163E011A4F.root',
       '/store/data/Run2016D/JetHT/MINIAOD/PromptReco-v2/000/276/315/00000/648F89DB-0145-E611-BD37-02163E011AB7.root',
       '/store/data/Run2016D/JetHT/MINIAOD/PromptReco-v2/000/276/315/00000/6E6996E5-0145-E611-922A-02163E013663.root',
       '/store/data/Run2016D/JetHT/MINIAOD/PromptReco-v2/000/276/315/00000/78AA60DA-0145-E611-9E52-02163E0120B7.root',
       '/store/data/Run2016D/JetHT/MINIAOD/PromptReco-v2/000/276/315/00000/F05B99C3-0145-E611-A4D9-02163E014116.root',
       '/store/data/Run2016D/JetHT/MINIAOD/PromptReco-v2/000/276/317/00000/140315E2-0545-E611-A909-02163E01426B.root',
       '/store/data/Run2016D/JetHT/MINIAOD/PromptReco-v2/000/276/317/00000/98AF2032-0645-E611-8351-02163E0133EE.root',
       '/store/data/Run2016D/JetHT/MINIAOD/PromptReco-v2/000/276/317/00000/F066DDD5-0445-E611-9796-02163E0136AD.root',
       '/store/data/Run2016D/JetHT/MINIAOD/PromptReco-v2/000/276/317/00000/F8D9D2DC-0545-E611-8F01-02163E0146C8.root',
       '/store/data/Run2016D/JetHT/MINIAOD/PromptReco-v2/000/276/317/00000/FC3F41EB-0545-E611-BC87-02163E014207.root',
       '/store/data/Run2016D/JetHT/MINIAOD/PromptReco-v2/000/276/318/00000/00317F39-1B45-E611-AD6A-02163E013805.root',
       '/store/data/Run2016D/JetHT/MINIAOD/PromptReco-v2/000/276/318/00000/043A4B51-1B45-E611-850E-02163E014659.root',
       '/store/data/Run2016D/JetHT/MINIAOD/PromptReco-v2/000/276/318/00000/14076B81-1B45-E611-AAFE-02163E013466.root',
       '/store/data/Run2016D/JetHT/MINIAOD/PromptReco-v2/000/276/318/00000/1ED26624-1B45-E611-95FE-02163E0145C5.root',
       '/store/data/Run2016D/JetHT/MINIAOD/PromptReco-v2/000/276/318/00000/3026E710-1B45-E611-BCDE-02163E01376A.root',
       '/store/data/Run2016D/JetHT/MINIAOD/PromptReco-v2/000/276/318/00000/30F1E6E1-1A45-E611-8409-02163E01453C.root',
       '/store/data/Run2016D/JetHT/MINIAOD/PromptReco-v2/000/276/318/00000/52414C0F-1B45-E611-81F9-02163E0126BF.root',
       '/store/data/Run2016D/JetHT/MINIAOD/PromptReco-v2/000/276/318/00000/6E7CC534-1B45-E611-BC87-02163E011B5F.root',
       '/store/data/Run2016D/JetHT/MINIAOD/PromptReco-v2/000/276/318/00000/76263961-1945-E611-9293-02163E011ADA.root',
       '/store/data/Run2016D/JetHT/MINIAOD/PromptReco-v2/000/276/318/00000/8E0C582E-1B45-E611-ABDB-02163E014635.root',
       '/store/data/Run2016D/JetHT/MINIAOD/PromptReco-v2/000/276/318/00000/902038E3-1A45-E611-BF8C-02163E011911.root',
       '/store/data/Run2016D/JetHT/MINIAOD/PromptReco-v2/000/276/318/00000/9E90DE0E-1B45-E611-BC66-02163E01226E.root',
       '/store/data/Run2016D/JetHT/MINIAOD/PromptReco-v2/000/276/318/00000/C4A445B9-1A45-E611-BA75-02163E013992.root',
       '/store/data/Run2016D/JetHT/MINIAOD/PromptReco-v2/000/276/318/00000/CAB48E0E-1B45-E611-9700-02163E014599.root',
       '/store/data/Run2016D/JetHT/MINIAOD/PromptReco-v2/000/276/318/00000/D861B690-1A45-E611-8B16-02163E014219.root',
       '/store/data/Run2016D/JetHT/MINIAOD/PromptReco-v2/000/276/318/00000/E835023D-1B45-E611-A715-02163E0143F9.root',
       '/store/data/Run2016D/JetHT/MINIAOD/PromptReco-v2/000/276/318/00000/FC151D42-1B45-E611-8A44-02163E014330.root',
       '/store/data/Run2016D/JetHT/MINIAOD/PromptReco-v2/000/276/327/00000/525DBABB-4D45-E611-BAFA-02163E014341.root',
       '/store/data/Run2016D/JetHT/MINIAOD/PromptReco-v2/000/276/327/00000/8AD687BF-4D45-E611-B5EF-02163E0134A7.root',
       '/store/data/Run2016D/JetHT/MINIAOD/PromptReco-v2/000/276/347/00000/CC688C30-5445-E611-BBBB-02163E014760.root',
       '/store/data/Run2016D/JetHT/MINIAOD/PromptReco-v2/000/276/352/00000/C42E0433-5845-E611-BCC6-02163E01347F.root',
       '/store/data/Run2016D/JetHT/MINIAOD/PromptReco-v2/000/276/352/00000/C869C33E-5845-E611-9088-02163E013511.root',
] )
