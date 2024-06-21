import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGamma_Dilept_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/120000/B811EBB5-EEA3-7847-A3AB-881FACA3E931.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGamma_Dilept_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/130000/0A991201-65E9-6145-BDBE-881EAC8B4039.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGamma_Dilept_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/130000/13518577-D57D-2542-B70F-6F33C432566C.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGamma_Dilept_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/130000/195AE289-95A7-1645-B745-C97F5DEE22FE.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGamma_Dilept_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/130000/1984BB73-2BAE-1C4A-B4CD-79BB8F2FEABB.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGamma_Dilept_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/130000/203D131B-0E91-8B4C-AE58-999B90EAC90E.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGamma_Dilept_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/130000/22ADCD7E-5B4D-3E4C-9306-2A7976E8C3E2.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGamma_Dilept_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/130000/28E4A989-1083-4247-BFA6-D6A95C79CA7D.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGamma_Dilept_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/130000/2A29657C-66F6-474A-A0D9-98F9A3F0ED9D.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGamma_Dilept_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/130000/2EBA6097-5668-B245-A6F6-F2A027D20F76.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGamma_Dilept_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/130000/3138D234-60D1-6241-B12E-2E530F7A59EC.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGamma_Dilept_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/130000/374DDE48-B3BC-B24A-80F0-5F2A14099413.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGamma_Dilept_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/130000/38B80EEA-09BC-3343-B77B-833A35C1910D.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGamma_Dilept_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/130000/393DE6E9-ECE2-9540-B5CA-CFDD089DEF2D.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGamma_Dilept_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/130000/413969B0-75AA-EC48-B051-32F073350239.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGamma_Dilept_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/130000/4295215F-3678-E14A-B9D5-8650499E9CDE.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGamma_Dilept_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/130000/4295A31E-88FC-4E41-9E9A-1AA6C8EE032E.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGamma_Dilept_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/130000/4481AD7D-85AC-8640-AB68-4F9FE43DAEEE.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGamma_Dilept_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/130000/47BCEEF7-3E51-6B49-911A-7372FA2D8DB3.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGamma_Dilept_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/130000/492CC502-1407-204F-A977-550970CC7F25.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGamma_Dilept_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/130000/502CC553-5EC5-D749-8F7D-DFDF58AE0B6E.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGamma_Dilept_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/130000/5E067C68-3370-5C43-86F7-90B18226FB7A.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGamma_Dilept_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/130000/652B94B3-4128-B842-AFF2-89F5C3CBE2CD.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGamma_Dilept_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/130000/65A261F5-01E3-EA43-8285-8B0030AEC02B.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGamma_Dilept_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/130000/69601C82-4A87-7041-A5F0-0FBBC30D8A4F.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGamma_Dilept_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/130000/7E705DA2-CA48-7843-AA1B-B15C867904B6.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGamma_Dilept_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/130000/80EEFFAD-7F9C-F04B-9724-05FBBF547F13.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGamma_Dilept_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/130000/83DD4244-DC91-0046-8D94-D099BDA66810.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGamma_Dilept_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/130000/864D4A8C-29F3-F442-838E-9A91470BCDE9.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGamma_Dilept_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/130000/865C41E5-5AF1-A34D-9881-7885D6B0BE2C.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGamma_Dilept_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/130000/90E1A7F0-97CF-004A-A978-B87A1802C1E8.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGamma_Dilept_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/130000/93CBAF3C-D1FD-D14D-AADF-D43A8E37D28C.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGamma_Dilept_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/130000/9CA4DCB5-3A83-3848-851E-2865E90E9D51.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGamma_Dilept_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/130000/9CB3A386-11EA-8048-BEB0-3AC3C52C1F45.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGamma_Dilept_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/130000/A283F1EF-381D-A443-B981-5C4DD3CEA972.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGamma_Dilept_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/130000/A30C4CA3-C0E4-2544-B2B0-3C9064CC03C7.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGamma_Dilept_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/130000/A3841ADE-A7CE-1D46-BDD1-7BAEBA67D5F4.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGamma_Dilept_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/130000/B028A05E-6161-A44F-A537-4B410178C555.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGamma_Dilept_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/130000/B3498B72-3D74-FB4F-835A-907EF4866E2F.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGamma_Dilept_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/130000/B8F75EA4-BF8B-C048-A9E3-078C9B0693EC.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGamma_Dilept_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/130000/BAD01061-E4F4-7F44-88AA-FA3771D2E8D4.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGamma_Dilept_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/130000/BC7541E1-5728-7240-B276-B71D7C3DA959.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGamma_Dilept_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/130000/BFD369B3-ACEB-7342-9AB0-EF7BD57125B7.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGamma_Dilept_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/130000/C03DD07B-01AB-0243-BCBE-E80571B0F18A.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGamma_Dilept_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/130000/C12A9114-CC68-9144-B6F7-A9C53BB5DDE0.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGamma_Dilept_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/130000/C2BB1DE5-6918-254C-8FC1-1B5E6648A74B.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGamma_Dilept_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/130000/C4631015-FA38-DF47-8982-B58C9B709858.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGamma_Dilept_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/130000/C9121712-E344-234D-A121-E20C6F7CC288.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGamma_Dilept_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/130000/CA22D99A-B737-FD4C-93E8-3A896CDE8946.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGamma_Dilept_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/130000/CCBE88B9-6CB3-1E4F-9810-BAA413F9CDBF.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGamma_Dilept_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/130000/CFA0A443-DD23-2A4E-BCA6-CA0422DCA9C3.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGamma_Dilept_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/130000/D05E9D29-B204-4F4C-9A88-EC2C94CDD03E.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGamma_Dilept_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/130000/D1337C0E-736F-2940-B111-F3494882C5C3.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGamma_Dilept_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/130000/D371D13F-077F-2F41-9464-6EE1554E85A6.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGamma_Dilept_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/130000/DB01130F-1998-544B-A793-7CFD367EA52F.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGamma_Dilept_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/130000/DCE6B374-D2EF-7D47-9CFB-E89524DB17EC.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGamma_Dilept_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/130000/E44FD081-0B56-FC43-AD1D-E381EB3E12C3.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGamma_Dilept_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/130000/EB66F417-3E6A-2449-BA40-AD9DFA78D80B.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGamma_Dilept_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/130000/F6B31CD2-368A-1C42-8F31-13FC2D17DA88.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGamma_Dilept_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/130000/FA1B378D-D720-4643-B871-2681C4634957.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGamma_Dilept_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/130000/FA5C6997-368A-494B-B282-686DE04EF12C.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGamma_Dilept_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/130000/FD200BCB-33F3-3D4D-83B0-A1DA52AF3109.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGamma_Dilept_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/140000/5E063417-5985-6142-843A-4E2D94B06DE2.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGamma_Dilept_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/140000/95E11F8F-FAFE-224F-98FE-0D9048B88CDF.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGamma_Dilept_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/140000/BC8C2A9B-45FF-F343-BFB0-687D406DD4EA.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGamma_Dilept_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/280000/0B92A355-0C3C-AC4E-9E9B-3BC802962F32.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGamma_Dilept_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/280000/DF25062C-F734-B944-9EB4-839EB9384FFA.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGamma_Dilept_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/70000/5A62E50F-7D85-6B49-8B18-37E01850376F.root',
] )