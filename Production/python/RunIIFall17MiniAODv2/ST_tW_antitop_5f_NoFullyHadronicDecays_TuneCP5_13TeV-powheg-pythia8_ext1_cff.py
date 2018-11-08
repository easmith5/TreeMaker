import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIIFall17MiniAODv2/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/00000/001C2506-1942-E811-9E7B-001E67F8FA47.root',
       '/store/mc/RunIIFall17MiniAODv2/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/00000/004C8EEC-A742-E811-9FC5-0242AC1C0503.root',
       '/store/mc/RunIIFall17MiniAODv2/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/00000/00737321-0842-E811-9405-001E6739AD61.root',
       '/store/mc/RunIIFall17MiniAODv2/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/00000/00928635-AD42-E811-8D9F-0242AC1C0500.root',
       '/store/mc/RunIIFall17MiniAODv2/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/00000/0839A209-AA42-E811-80DE-0242AC1C0500.root',
       '/store/mc/RunIIFall17MiniAODv2/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/00000/085395E5-AC42-E811-AFB5-0242AC1C0500.root',
       '/store/mc/RunIIFall17MiniAODv2/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/00000/087ED919-AA42-E811-A7E3-0242AC1C0502.root',
       '/store/mc/RunIIFall17MiniAODv2/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/00000/08C497E0-AC42-E811-A0E9-0242AC1C0504.root',
       '/store/mc/RunIIFall17MiniAODv2/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/00000/0A4AF4A2-F741-E811-A690-001E673D35A9.root',
       '/store/mc/RunIIFall17MiniAODv2/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/00000/0A72F875-DA41-E811-8AA2-9CB654AEB2C6.root',
       '/store/mc/RunIIFall17MiniAODv2/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/00000/0E4E1154-A842-E811-AE69-0242AC1C0502.root',
       '/store/mc/RunIIFall17MiniAODv2/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/00000/1030135B-0242-E811-8142-001E6739AD61.root',
       '/store/mc/RunIIFall17MiniAODv2/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/00000/14306C4B-AA42-E811-9E35-0242AC1C0503.root',
       '/store/mc/RunIIFall17MiniAODv2/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/00000/1A3E0735-AD42-E811-81D3-0242AC1C0504.root',
       '/store/mc/RunIIFall17MiniAODv2/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/00000/1CE1C925-AA42-E811-B903-0242AC1C0500.root',
       '/store/mc/RunIIFall17MiniAODv2/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/00000/1E482A7E-0B42-E811-92CC-001E67F8F7E0.root',
       '/store/mc/RunIIFall17MiniAODv2/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/00000/1E6FAD36-AD42-E811-97F4-0242AC1C0503.root',
       '/store/mc/RunIIFall17MiniAODv2/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/00000/202213E5-AC42-E811-B532-0242AC1C0500.root',
       '/store/mc/RunIIFall17MiniAODv2/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/00000/205F5BBD-0E42-E811-9377-001E673D1039.root',
       '/store/mc/RunIIFall17MiniAODv2/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/00000/2221ED2C-AD42-E811-881F-0242AC1C0500.root',
       '/store/mc/RunIIFall17MiniAODv2/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/00000/2C73472E-AA42-E811-AB1A-0242AC1C0503.root',
       '/store/mc/RunIIFall17MiniAODv2/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/00000/30C0D4CC-2842-E811-AA09-001E6739A781.root',
       '/store/mc/RunIIFall17MiniAODv2/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/00000/326E2A33-AD42-E811-A8D8-0242AC1C0502.root',
       '/store/mc/RunIIFall17MiniAODv2/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/00000/367848BD-F241-E811-9BBF-001E673C84B9.root',
       '/store/mc/RunIIFall17MiniAODv2/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/00000/36E9E055-AA42-E811-ABB5-0242AC1C0503.root',
       '/store/mc/RunIIFall17MiniAODv2/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/00000/382E4FEA-0642-E811-AE7D-001E67F8F7E0.root',
       '/store/mc/RunIIFall17MiniAODv2/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/00000/38EFFEE2-0642-E811-B89A-001E673D0C31.root',
       '/store/mc/RunIIFall17MiniAODv2/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/00000/3A48FBB7-1B42-E811-88E6-9CB65404EEF0.root',
       '/store/mc/RunIIFall17MiniAODv2/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/00000/3A4B3408-AD42-E811-AD47-0242AC1C0500.root',
       '/store/mc/RunIIFall17MiniAODv2/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/00000/3C41212B-AA42-E811-BACA-0242AC1C0500.root',
       '/store/mc/RunIIFall17MiniAODv2/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/00000/40F707E2-AC42-E811-ADA4-0242AC1C0500.root',
       '/store/mc/RunIIFall17MiniAODv2/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/00000/42E083CF-3042-E811-B5D1-001E6739AD61.root',
       '/store/mc/RunIIFall17MiniAODv2/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/00000/42FF1A1F-8042-E811-93AB-001E673D23F9.root',
       '/store/mc/RunIIFall17MiniAODv2/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/00000/46158001-E341-E811-B198-001E673D2261.root',
       '/store/mc/RunIIFall17MiniAODv2/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/00000/4EA222FA-AC42-E811-9D6C-0242AC1C0500.root',
       '/store/mc/RunIIFall17MiniAODv2/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/00000/5277152E-AD42-E811-A74F-0242AC1C0500.root',
       '/store/mc/RunIIFall17MiniAODv2/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/00000/600C31FB-0842-E811-BAB2-001E67F8F7E0.root',
       '/store/mc/RunIIFall17MiniAODv2/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/00000/62297200-AD42-E811-8F7F-0242AC1C0500.root',
       '/store/mc/RunIIFall17MiniAODv2/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/00000/62A95089-EE41-E811-A043-001E67F8F7E0.root',
       '/store/mc/RunIIFall17MiniAODv2/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/00000/64472EC0-0242-E811-BA6D-001E673C84B9.root',
       '/store/mc/RunIIFall17MiniAODv2/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/00000/6603BD70-AF42-E811-969F-0242AC1C0500.root',
       '/store/mc/RunIIFall17MiniAODv2/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/00000/6A62973A-AD42-E811-96D1-0242AC1C0503.root',
       '/store/mc/RunIIFall17MiniAODv2/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/00000/6ADF0905-AD42-E811-BA51-0242AC1C0504.root',
       '/store/mc/RunIIFall17MiniAODv2/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/00000/7044F1DF-AC42-E811-8636-0242AC1C0504.root',
       '/store/mc/RunIIFall17MiniAODv2/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/00000/724B15E5-AC42-E811-A16C-0242AC1C0500.root',
       '/store/mc/RunIIFall17MiniAODv2/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/00000/747361C4-0C42-E811-9063-001E67FA402D.root',
       '/store/mc/RunIIFall17MiniAODv2/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/00000/747D4AAD-A842-E811-8B00-0242AC1C0501.root',
       '/store/mc/RunIIFall17MiniAODv2/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/00000/769F721E-AA42-E811-BFD2-0242AC1C0503.root',
       '/store/mc/RunIIFall17MiniAODv2/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/00000/7AD1B204-AD42-E811-BBDA-0242AC1C0504.root',
       '/store/mc/RunIIFall17MiniAODv2/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/00000/7ADA4158-A842-E811-A8F3-0242AC1C0502.root',
       '/store/mc/RunIIFall17MiniAODv2/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/00000/860C1B37-AD42-E811-98D6-0242AC1C0503.root',
       '/store/mc/RunIIFall17MiniAODv2/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/00000/8A1148DC-FF41-E811-98AB-001E67F8FA47.root',
       '/store/mc/RunIIFall17MiniAODv2/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/00000/8C3D09E5-AC42-E811-80B8-0242AC1C0504.root',
       '/store/mc/RunIIFall17MiniAODv2/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/00000/907F6C20-AA42-E811-88C2-0242AC1C0500.root',
       '/store/mc/RunIIFall17MiniAODv2/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/00000/92780B32-EB41-E811-B7D6-001E6739ABB9.root',
       '/store/mc/RunIIFall17MiniAODv2/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/00000/94501A1B-AA42-E811-903C-0242AC1C0500.root',
       '/store/mc/RunIIFall17MiniAODv2/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/00000/94657032-D841-E811-A400-9CB654AEBD76.root',
       '/store/mc/RunIIFall17MiniAODv2/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/00000/9475C9E4-AC42-E811-BDF7-0242AC1C0504.root',
       '/store/mc/RunIIFall17MiniAODv2/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/00000/98E6F09E-0B42-E811-9D0B-001E67FA402D.root',
       '/store/mc/RunIIFall17MiniAODv2/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/00000/9A7197CB-2342-E811-B7F9-001E6739A751.root',
       '/store/mc/RunIIFall17MiniAODv2/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/00000/9C0A95D0-1242-E811-8871-001E67F8F7E0.root',
       '/store/mc/RunIIFall17MiniAODv2/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/00000/A2488AAD-D441-E811-9CFE-001E673C8537.root',
       '/store/mc/RunIIFall17MiniAODv2/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/00000/A2F88735-AD42-E811-8318-0242AC1C0500.root',
       '/store/mc/RunIIFall17MiniAODv2/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/00000/A46CBA32-AD42-E811-A111-0242AC1C0502.root',
       '/store/mc/RunIIFall17MiniAODv2/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/00000/AC5AD620-0842-E811-9B03-001E673D1039.root',
       '/store/mc/RunIIFall17MiniAODv2/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/00000/AE14DAFC-AC42-E811-B488-0242AC1C0500.root',
       '/store/mc/RunIIFall17MiniAODv2/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/00000/B0B62B6E-DD41-E811-8F98-001E673D2261.root',
       '/store/mc/RunIIFall17MiniAODv2/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/00000/B48C21C7-0E42-E811-B71D-001E67F8FA3D.root',
       '/store/mc/RunIIFall17MiniAODv2/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/00000/BA5612E5-AC42-E811-BA52-0242AC1C0500.root',
       '/store/mc/RunIIFall17MiniAODv2/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/00000/BC55C32B-AA42-E811-86FB-0242AC1C0500.root',
       '/store/mc/RunIIFall17MiniAODv2/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/00000/BE677E57-0A42-E811-8DE5-001E67F8FA4C.root',
       '/store/mc/RunIIFall17MiniAODv2/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/00000/BE961FDA-F841-E811-A705-9CB654AEBD76.root',
       '/store/mc/RunIIFall17MiniAODv2/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/00000/C4DB543E-FB41-E811-9BAD-001E6739C801.root',
       '/store/mc/RunIIFall17MiniAODv2/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/00000/C6BAE9E3-AC42-E811-8E2E-0242AC1C0501.root',
       '/store/mc/RunIIFall17MiniAODv2/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/00000/C6E50501-AD42-E811-B9A3-0242AC1C0502.root',
       '/store/mc/RunIIFall17MiniAODv2/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/00000/CCDF4232-AD42-E811-B29C-0242AC1C0504.root',
       '/store/mc/RunIIFall17MiniAODv2/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/00000/CE1E01AE-0542-E811-A481-001E673C84B9.root',
       '/store/mc/RunIIFall17MiniAODv2/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/00000/CE87669B-1742-E811-A607-001E67FA402D.root',
       '/store/mc/RunIIFall17MiniAODv2/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/00000/D4309205-AA42-E811-8FCE-0242AC1C0500.root',
       '/store/mc/RunIIFall17MiniAODv2/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/00000/D466975D-A842-E811-A9D5-0242AC1C0502.root',
       '/store/mc/RunIIFall17MiniAODv2/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/00000/DA40A85B-0A42-E811-A888-001E67F8FA2E.root',
       '/store/mc/RunIIFall17MiniAODv2/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/00000/DACE9E1D-AA42-E811-B0D5-0242AC1C0500.root',
       '/store/mc/RunIIFall17MiniAODv2/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/00000/DC8302F9-A942-E811-B6CF-0242AC1C0500.root',
       '/store/mc/RunIIFall17MiniAODv2/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/00000/DC981DDA-F841-E811-AD32-38EAA7A6DC58.root',
       '/store/mc/RunIIFall17MiniAODv2/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/00000/E02A6010-AD42-E811-AC73-0242AC1C0503.root',
       '/store/mc/RunIIFall17MiniAODv2/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/00000/E44B3B68-AF42-E811-BAF5-0242AC1C0500.root',
       '/store/mc/RunIIFall17MiniAODv2/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/00000/EEAEE055-AA42-E811-B50B-0242AC1C0503.root',
       '/store/mc/RunIIFall17MiniAODv2/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/00000/EEC43432-AA42-E811-A9C2-0242AC1C0503.root',
       '/store/mc/RunIIFall17MiniAODv2/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/00000/F2E6B91D-AA42-E811-AC16-0242AC1C0501.root',
       '/store/mc/RunIIFall17MiniAODv2/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/00000/F4CFC711-0442-E811-A603-001E6739C801.root',
       '/store/mc/RunIIFall17MiniAODv2/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/00000/F6BB192A-2E42-E811-8DFF-001E6739BB01.root',
       '/store/mc/RunIIFall17MiniAODv2/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/00000/F6ED5D28-AA42-E811-B157-0242AC1C0500.root',
       '/store/mc/RunIIFall17MiniAODv2/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/00000/F8A9AD35-AD42-E811-BA20-0242AC1C0504.root',
       '/store/mc/RunIIFall17MiniAODv2/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/00000/FA9A3C74-FC41-E811-A278-001E673C84B9.root',
       '/store/mc/RunIIFall17MiniAODv2/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/00000/FC259D2F-AD42-E811-9377-0242AC1C0508.root',
       '/store/mc/RunIIFall17MiniAODv2/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/00000/FC4C3057-A842-E811-A0BF-0242AC1C0502.root',
       '/store/mc/RunIIFall17MiniAODv2/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/00000/FE23D800-1542-E811-9058-001E67F8FA47.root',
       '/store/mc/RunIIFall17MiniAODv2/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/00000/FE25F528-AA42-E811-BD79-0242AC1C0500.root',
       '/store/mc/RunIIFall17MiniAODv2/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/00000/FE532559-A842-E811-B8F4-0242AC1C0502.root',
       '/store/mc/RunIIFall17MiniAODv2/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/00000/FE9602C8-1942-E811-8017-9CB65404EEF0.root',
] )