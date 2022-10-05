import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer20UL17MiniAODv2/StealthSHH_2t4b_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/2520000/1B96207E-9A9D-D241-A44D-D1D233913E0D.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/StealthSHH_2t4b_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/2520000/2FAA0618-A5F1-6741-AC44-1EAD6162C1C7.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/StealthSHH_2t4b_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/2520000/38C4D845-6BAB-0849-B561-CB1059868858.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/StealthSHH_2t4b_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/2520000/3FF4F2A3-F9FA-A041-84EF-405E1265B528.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/StealthSHH_2t4b_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/2520000/47F53047-582C-4644-A5DE-3A06D94D5312.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/StealthSHH_2t4b_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/2520000/515C27EC-341D-AE44-97E6-62F99E67D3AA.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/StealthSHH_2t4b_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/2520000/5EDAD2D5-CA2F-BC42-9072-D6F318BDF125.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/StealthSHH_2t4b_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/2520000/72FCA1B8-4C01-0240-909A-A9534BA9A579.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/StealthSHH_2t4b_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/2520000/A1F08859-8017-3444-82AE-F1EEE94C7DFB.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/StealthSHH_2t4b_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/2520000/BB0B51D5-E7E0-E240-BEF5-A9F9A853FA6A.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/StealthSHH_2t4b_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/2520000/E6BEAEB2-3100-2F49-800D-C914FA423EF6.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/StealthSHH_2t4b_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/40000/01A3FFD8-7B14-FE4B-AC74-9CF542AD4931.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/StealthSHH_2t4b_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/40000/03B2406B-F057-7649-84D7-C0837623BD5A.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/StealthSHH_2t4b_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/40000/03D80915-0725-1247-AF00-80465EB47560.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/StealthSHH_2t4b_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/40000/043C2A21-F80E-E248-8B71-89A958EF1A4C.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/StealthSHH_2t4b_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/40000/072B2671-185A-4F4F-BCF2-AB4AAA3D5678.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/StealthSHH_2t4b_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/40000/07411E6E-606C-1148-969C-2BA8A13475F7.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/StealthSHH_2t4b_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/40000/0832A685-58AC-4C48-93E5-638E3CAEA083.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/StealthSHH_2t4b_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/40000/087F0207-8CF3-3D43-9F9A-0E0399A472B0.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/StealthSHH_2t4b_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/40000/0AA14F4E-F494-4C4C-88F5-4B56EB231AE2.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/StealthSHH_2t4b_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/40000/0B11A7E2-D32D-104D-A6E1-5BC600E1A59F.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/StealthSHH_2t4b_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/40000/0C4FCD47-8E10-554B-A0EC-7F968A5A48AF.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/StealthSHH_2t4b_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/40000/0E4B3E91-A2FE-CF41-9E7E-37DCA08A5EFD.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/StealthSHH_2t4b_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/40000/1459CD36-7243-5548-974D-EF3EEF729EAD.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/StealthSHH_2t4b_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/40000/18654FA9-1C4B-3B45-B5E6-54A70991CF05.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/StealthSHH_2t4b_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/40000/1F52F925-0631-DB4C-8452-F401B9B090F9.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/StealthSHH_2t4b_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/40000/1F70D3FA-393F-F246-B397-183EEDE29F83.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/StealthSHH_2t4b_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/40000/2020E094-A6F6-104A-9813-3F9FDB4E57A3.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/StealthSHH_2t4b_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/40000/22B95264-E59B-074F-B4B7-9B6F2197A0BE.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/StealthSHH_2t4b_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/40000/23018000-CB8F-C44A-89E6-F8CDFAA9272F.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/StealthSHH_2t4b_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/40000/2487A856-BC41-9A47-83D4-3377710E4E3C.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/StealthSHH_2t4b_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/40000/24961E12-A83F-8942-A5DE-55DB8EABC9BD.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/StealthSHH_2t4b_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/40000/263A03D8-2C29-AE42-9793-377EE8AA23C2.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/StealthSHH_2t4b_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/40000/26F1494C-8FE0-204E-8717-1C9E328ED61B.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/StealthSHH_2t4b_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/40000/2AF02899-6B84-A341-B74C-3DA4A2E47B47.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/StealthSHH_2t4b_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/40000/2E78F625-6350-A549-A72D-3D73C6C83E40.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/StealthSHH_2t4b_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/40000/2E9ED2A4-BEB3-0D4F-9A34-1FBA4DB88046.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/StealthSHH_2t4b_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/40000/32EBA1BD-365D-5343-8AE3-B8719560DDFA.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/StealthSHH_2t4b_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/40000/3393FFAF-ED99-4245-A534-EE73A32AF0C2.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/StealthSHH_2t4b_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/40000/34524B26-61F1-EB47-97CC-861778B0D1FB.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/StealthSHH_2t4b_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/40000/34964450-0771-6947-8E1C-1C8680D636DD.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/StealthSHH_2t4b_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/40000/375A8CAC-8749-F246-990B-58B67A522ECB.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/StealthSHH_2t4b_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/40000/3833CB62-594E-7140-9C4F-77F267BF2951.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/StealthSHH_2t4b_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/40000/39051EB9-BFB1-1940-A3CE-B4084D51009D.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/StealthSHH_2t4b_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/40000/393543B6-4B5E-7445-9645-1632543FAF65.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/StealthSHH_2t4b_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/40000/3B7D2BF5-69BA-EB43-A0FE-E091598BD0AB.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/StealthSHH_2t4b_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/40000/404F8B06-B9D2-1549-B438-29839BCD4DA0.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/StealthSHH_2t4b_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/40000/43A36306-32DE-BF41-97BC-85282A1A8D79.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/StealthSHH_2t4b_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/40000/4447AB64-8874-BD42-AE84-E41BB339AF75.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/StealthSHH_2t4b_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/40000/451A4240-C35A-B345-93AD-EA7F5BA6790E.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/StealthSHH_2t4b_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/40000/46B01295-0465-F54B-907F-886C676CC9DB.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/StealthSHH_2t4b_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/40000/505C6E99-117B-4C47-8FA8-FE9D10C339F2.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/StealthSHH_2t4b_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/40000/52085224-FE47-D443-8127-0180EA3A09F3.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/StealthSHH_2t4b_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/40000/530DD626-127A-4349-981F-E39E13A94DAA.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/StealthSHH_2t4b_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/40000/5319B40D-25D8-AC46-A424-D0C51B915CC7.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/StealthSHH_2t4b_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/40000/57CFB100-60D7-D440-A4FE-639A324E4AFE.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/StealthSHH_2t4b_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/40000/5AB2C459-E23E-FA4A-B32E-9789216EF199.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/StealthSHH_2t4b_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/40000/5DB9D135-FBB8-074C-84B7-946C3E1B0B1E.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/StealthSHH_2t4b_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/40000/5E1406D6-365C-A74D-81CC-380F205D2C49.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/StealthSHH_2t4b_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/40000/5EBDB065-77B4-9241-98F7-A5E3E11A8FC4.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/StealthSHH_2t4b_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/40000/5F25033B-86B7-2E41-9BB1-05A3B2D3007D.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/StealthSHH_2t4b_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/40000/63F77A61-520A-3C4B-8884-3C0FFE1C4004.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/StealthSHH_2t4b_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/40000/64A524CB-23D8-AB41-827D-6537C7D862D1.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/StealthSHH_2t4b_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/40000/705B388F-EFD3-F444-BDDB-2AE2662346DA.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/StealthSHH_2t4b_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/40000/70D7EE6D-0A11-3F4D-AE8D-4483F51F5C54.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/StealthSHH_2t4b_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/40000/75254075-9F72-D740-93B9-23BFD5FF014F.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/StealthSHH_2t4b_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/40000/762524F4-08AB-2C49-ACE5-3DB7F947BBAC.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/StealthSHH_2t4b_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/40000/7D41E43E-1AA0-9F41-BBFC-EBEF406EC379.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/StealthSHH_2t4b_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/40000/7EB54EFE-454E-0949-AA2B-E62DE0510498.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/StealthSHH_2t4b_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/40000/7F28F25A-AF00-B540-B599-E59D80DB4032.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/StealthSHH_2t4b_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/40000/7F956856-7151-9A4C-9205-11D69159F835.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/StealthSHH_2t4b_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/40000/821FA73D-E45B-B34D-89C8-7F1C72563001.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/StealthSHH_2t4b_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/40000/8382CA3F-EE35-7C48-8A1E-C1AD5F1D4B39.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/StealthSHH_2t4b_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/40000/8441308E-9BF3-5942-93CD-17238B0DAEFD.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/StealthSHH_2t4b_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/40000/847D1E87-4FF0-DA44-9C62-DEE9BF4AA4EC.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/StealthSHH_2t4b_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/40000/8582B4AC-5B6E-2348-8611-C8D09AEB44D4.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/StealthSHH_2t4b_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/40000/87E742E6-4EEE-8349-8CC0-DF936EBC6919.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/StealthSHH_2t4b_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/40000/8B1FE620-803B-A640-BF94-FE90EA0D5DB0.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/StealthSHH_2t4b_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/40000/8D566D18-8B29-7341-9804-726D1B6544CE.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/StealthSHH_2t4b_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/40000/967E597B-495E-3E41-8AC2-D199327E3697.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/StealthSHH_2t4b_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/40000/97991F05-B728-A84D-99B8-5A847F7FA404.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/StealthSHH_2t4b_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/40000/A01183D3-09A7-F14C-B9DC-2CEF0304DF35.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/StealthSHH_2t4b_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/40000/A118BB98-4222-D647-BE96-33E47F82881F.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/StealthSHH_2t4b_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/40000/A359865D-E409-4747-9F24-F04CAF006431.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/StealthSHH_2t4b_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/40000/A5501B5B-E408-8742-B406-F9DA47A6042E.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/StealthSHH_2t4b_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/40000/A63AC2B7-5FB9-344A-B4EA-E437DB73FA34.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/StealthSHH_2t4b_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/40000/A841B7CC-2828-FC40-B106-C0A23C5E71F9.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/StealthSHH_2t4b_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/40000/ABB17333-DB75-0F47-AFEE-789BCFCC1B04.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/StealthSHH_2t4b_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/40000/AC2683F3-44D7-0944-BD89-5A111BBD9542.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/StealthSHH_2t4b_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/40000/ACBB0715-FDB7-514C-A5E2-568918F85B86.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/StealthSHH_2t4b_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/40000/AE3CBDEC-601F-3B4D-8EBE-462619E8BE0F.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/StealthSHH_2t4b_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/40000/B13B4D4B-8393-E94D-AE4B-317252327A7A.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/StealthSHH_2t4b_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/40000/B3E7644C-CDA1-3441-95E9-53C08B519334.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/StealthSHH_2t4b_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/40000/BC95E507-73E1-4D48-841A-39DEBEDEE00B.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/StealthSHH_2t4b_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/40000/BD7DA1CC-1EE5-AF40-8475-2D54BED6F35E.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/StealthSHH_2t4b_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/40000/C0EE90F1-5BF0-7842-8E59-F6C1D0E4AAE5.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/StealthSHH_2t4b_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/40000/C5483095-CA01-5140-9574-1E2016074C3C.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/StealthSHH_2t4b_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/40000/C907AA5E-54A9-2144-9F6F-9541C098F736.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/StealthSHH_2t4b_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/40000/C91B08B9-A953-8243-8661-FEE3921D7881.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/StealthSHH_2t4b_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/40000/C9791A2B-B3F9-5440-AF92-6C89180E9AF3.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/StealthSHH_2t4b_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/40000/CB08B978-693F-0041-B417-7A05F96DB2FA.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/StealthSHH_2t4b_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/40000/CDA3339C-E29E-B045-9FF9-E4E28C86745D.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/StealthSHH_2t4b_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/40000/CE8C1117-7CDB-1A4D-9816-538C35C3376E.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/StealthSHH_2t4b_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/40000/D39EB8C5-A845-6746-A32E-7B450613E14B.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/StealthSHH_2t4b_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/40000/D597A126-765C-754C-B056-C385249BB5CC.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/StealthSHH_2t4b_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/40000/D8B8BA32-F54F-0C45-B4CF-4072FB220B5A.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/StealthSHH_2t4b_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/40000/DC921558-3B56-9B40-A066-D6FDA3D3B40F.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/StealthSHH_2t4b_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/40000/DD25561F-CBCF-B74B-9AC0-77780A0D810F.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/StealthSHH_2t4b_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/40000/DDA24FF8-3C4C-3E46-9B13-BD1F0A0086BA.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/StealthSHH_2t4b_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/40000/DECC5E4B-E8B4-F746-B713-69B12D22B4FD.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/StealthSHH_2t4b_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/40000/E299B306-3423-E948-85A7-E799DFC345F7.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/StealthSHH_2t4b_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/40000/E636D754-4973-4A4C-A101-D2950D261163.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/StealthSHH_2t4b_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/40000/E6384C27-B7DB-A240-A062-0951C5225926.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/StealthSHH_2t4b_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/40000/E87BF7E8-D1D3-7744-A90B-39AD0DFE0B51.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/StealthSHH_2t4b_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/40000/EB5EE49B-B66B-2948-955C-B14B5A7DBDA0.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/StealthSHH_2t4b_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/40000/F26AB203-66F7-C84E-A4E4-005B4CBDF3E4.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/StealthSHH_2t4b_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/40000/F43A05F4-F3CD-4B46-971D-FAB07F2C6063.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/StealthSHH_2t4b_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/40000/F443C67A-9AD3-DE4B-ACCE-60293E182B9A.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/StealthSHH_2t4b_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/40000/FBB2EB66-79A3-F14B-B53B-46E3529A8837.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/StealthSHH_2t4b_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/40000/FF6A4565-A6C9-1741-A341-B5AC0AAAB5F2.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/StealthSHH_2t4b_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/40000/FFC2F4E7-5310-2248-AA2D-01C8C4D48A16.root',
] )
