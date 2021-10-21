import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer20UL17MiniAODv2/ZZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/230000/0571FD70-4526-9F4F-BD99-769E4256D634.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/ZZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/230000/0640B513-192A-F640-B6EB-0B51A0FB9D1D.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/ZZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/230000/118DFBC9-74F9-BE40-9E98-C7BD2BDF3782.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/ZZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/230000/11F56F79-1140-C147-8701-2E75ECDDD667.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/ZZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/230000/3675A519-A4C2-FB4C-9D0A-056D04111D4A.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/ZZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/230000/370377A6-848C-8141-B131-0E6CC81B97D2.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/ZZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/230000/3B1BD3B8-6DB4-3349-96B8-8D16E8F55193.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/ZZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/230000/3BA07519-6DAD-A546-82EB-626B43C0F794.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/ZZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/230000/42E29048-A964-0B4D-823C-B5CA67625F19.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/ZZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/230000/43C93E71-2A7E-0344-BA95-A92269CDC29B.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/ZZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/230000/55A1FE53-26D6-574F-9327-26DFD42B0B6D.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/ZZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/230000/5ABF5DFE-755A-2C4C-BC4A-7447FDC2DF3E.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/ZZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/230000/66C883AB-FD5E-B34A-8D9E-66C1767BF42A.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/ZZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/230000/686DF5B7-5DC3-194B-8B14-A1F110F6D378.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/ZZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/230000/7261CDC1-97D1-5C4B-822A-D0397D3536D9.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/ZZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/230000/94D105C0-7432-6F48-B6E6-82BFEFE940D1.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/ZZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/230000/97660CFF-1655-C948-BA7B-A25B51821AE3.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/ZZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/230000/980EBA08-A7EF-8248-ADF7-87A0222F2D46.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/ZZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/230000/99E4E82F-F3E2-0D42-A58B-EF43BE694F5A.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/ZZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/230000/B1CD2EFA-0801-7A43-AC2B-A389A78EADC6.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/ZZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/230000/BE51A462-0D91-B141-8B0C-ACEFD0DEDFD2.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/ZZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/230000/BECD3F45-1550-E240-8E4C-DC736522FE64.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/ZZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/230000/C62E611B-53E8-5345-9B28-C4002A945154.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/ZZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/230000/CAA4EB68-C6B8-2A45-8083-67C85715B35F.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/ZZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/230000/CD0835C8-EC21-AE45-9BB0-50222040E41E.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/ZZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/230000/E06B4F3C-1229-D448-BE8A-22B80B8601C7.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/ZZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/230000/E992EE7E-A204-7C45-B214-650937252702.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/ZZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/230000/EB61111F-C8DE-2745-AFA8-8030A78FE11D.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/ZZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/230000/ECD3702E-4640-AD4E-B831-E43AEFCC5D72.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/ZZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/230000/EDB6EAA6-6FCB-1A4F-A79E-899146FCCFAB.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/ZZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/230000/F3AEA60C-19E0-AB42-B9A0-306738AF59B3.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/ZZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/230000/F6780E2E-6413-DB44-A690-3AABEA89981D.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/ZZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/230000/FA14B27A-72CF-8F43-BFE0-0C60F10044F7.root',
] )