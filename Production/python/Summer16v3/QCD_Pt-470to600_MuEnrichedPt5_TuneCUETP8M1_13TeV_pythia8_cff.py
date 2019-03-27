import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt-470to600_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/270000/0A91FA3F-DEE3-E811-9431-0242AC130002.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt-470to600_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/270000/0AAB32E0-DCE3-E811-825A-0242AC130002.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt-470to600_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/270000/12456791-DCE3-E811-870B-0242AC130002.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt-470to600_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/270000/1AC5098A-DCE3-E811-8FCB-0242AC130002.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt-470to600_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/270000/201915EC-97E3-E811-AA76-0242AC130002.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt-470to600_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/270000/2A105B40-DEE3-E811-9C00-0242AC130002.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt-470to600_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/270000/3E41DBEE-ABE3-E811-9683-D067E5F9156C.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt-470to600_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/270000/40FC3FD6-0BE4-E811-8163-0242AC130002.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt-470to600_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/270000/461380DF-DCE3-E811-B70F-0242AC130002.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt-470to600_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/270000/4A395548-0BE4-E811-AD60-0242AC130002.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt-470to600_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/270000/4AA9A523-DEE3-E811-9BDD-0242AC130002.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt-470to600_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/270000/5A854CA7-90E3-E811-BA32-0242AC130002.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt-470to600_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/270000/8075B8AE-29E4-E811-BB3D-0242AC130002.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt-470to600_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/270000/864987DF-DCE3-E811-8319-0242AC130002.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt-470to600_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/270000/901DD73D-92E3-E811-A63D-0242AC130002.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt-470to600_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/270000/92AF5607-DDE3-E811-A12A-0242AC130002.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt-470to600_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/270000/92C7FC63-95E3-E811-BE7C-0242AC130002.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt-470to600_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/270000/96EE40EE-DCE3-E811-8F25-0242AC130002.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt-470to600_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/270000/98F3B444-0BE4-E811-80A2-0242AC130002.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt-470to600_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/270000/9C4A8843-0BE4-E811-A3FC-0242AC130002.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt-470to600_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/270000/A2936AE0-0FE4-E811-8052-0242AC130002.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt-470to600_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/270000/A6427DDF-DCE3-E811-9A74-0242AC130002.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt-470to600_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/270000/A6B4D173-DCE3-E811-A11E-0242AC130002.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt-470to600_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/270000/AEF36774-BDE3-E811-8182-0242AC130002.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt-470to600_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/270000/B616189F-A8E3-E811-9C4A-0242AC130002.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt-470to600_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/270000/C2FF8352-0CE4-E811-A076-0242AC130002.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt-470to600_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/270000/C6C18210-8FE3-E811-9772-0242AC130002.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt-470to600_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/270000/C6E7501A-A0E3-E811-B433-0242AC130002.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt-470to600_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/270000/CE06E453-DEE3-E811-B2E1-0242AC130002.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt-470to600_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/270000/D089CFAF-94E3-E811-91D4-0242AC130002.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt-470to600_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/270000/D09E4F09-ABE3-E811-A207-0242AC130002.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt-470to600_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/270000/D2787288-DCE3-E811-A995-0242AC130002.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt-470to600_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/270000/D869FD2A-C1E4-E811-A216-0242AC130002.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt-470to600_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/270000/DA48CD67-DEE3-E811-BA2E-0242AC130002.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt-470to600_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/270000/DCBD5A88-DCE3-E811-8FB7-0242AC130002.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt-470to600_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/270000/DEE1CEE7-0FE4-E811-9B2F-0242AC130002.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt-470to600_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/270000/EA20D8FF-99E3-E811-AAF2-0242AC130002.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt-470to600_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/270000/EE099F3C-AEE3-E811-B024-0242AC130002.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt-470to600_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/270000/F27FE0F2-DCE3-E811-8ED6-0242AC130002.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt-470to600_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/270000/F8BBAF18-DDE3-E811-8E13-0242AC130002.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt-470to600_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/270000/FE7F25E1-29E4-E811-A227-0242AC130002.root',
] )