import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer20UL16MiniAODv2/DYJetsToLL_M-50_HT-70to100_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/100000/9746E24F-F744-5E4B-9179-0D12EB3C1C3D.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/DYJetsToLL_M-50_HT-70to100_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/230000/036EE0A4-131A-5D4E-A25D-218881B0112D.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/DYJetsToLL_M-50_HT-70to100_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/230000/0E3CD59E-B272-BA4B-86C7-6ADDEBFAB333.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/DYJetsToLL_M-50_HT-70to100_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/230000/1C1B1B4D-D97F-D64C-A410-F55DD2D80B7C.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/DYJetsToLL_M-50_HT-70to100_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/230000/2C815046-5C61-2D4F-B9A5-3F2C893B804D.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/DYJetsToLL_M-50_HT-70to100_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/230000/36F44B00-ECFA-9143-AEB0-5D18B1D521B5.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/DYJetsToLL_M-50_HT-70to100_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/230000/3BF77AC1-C66C-324A-B87F-E38480D57937.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/DYJetsToLL_M-50_HT-70to100_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/230000/3DDDB498-0ADA-2B4F-9C88-C139B37F33F8.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/DYJetsToLL_M-50_HT-70to100_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/230000/3F202476-FFB4-3B40-8985-2C4D5BAE6ED6.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/DYJetsToLL_M-50_HT-70to100_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/230000/40CADE68-CFC9-BD49-A50C-0972129A9C62.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/DYJetsToLL_M-50_HT-70to100_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/230000/412BCB65-C71F-FE44-807C-B6A1B4CD80EC.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/DYJetsToLL_M-50_HT-70to100_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/230000/42DC810A-8526-3E43-BAEA-89BA9A28ED51.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/DYJetsToLL_M-50_HT-70to100_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/230000/44AF965C-0E62-B44E-A046-CDF815D584B2.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/DYJetsToLL_M-50_HT-70to100_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/230000/54B01D35-0647-6748-808F-377A4EAFB9CA.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/DYJetsToLL_M-50_HT-70to100_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/230000/5F614B1E-D050-8C4B-A52E-ED7CA8B42D41.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/DYJetsToLL_M-50_HT-70to100_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/230000/9FA93618-00AA-9747-A748-F3369A41ACA5.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/DYJetsToLL_M-50_HT-70to100_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/230000/A974395F-2AEB-DC42-9EC3-A221DF149296.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/DYJetsToLL_M-50_HT-70to100_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/230000/AE78E2C0-F208-F74A-8600-B352F879B057.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/DYJetsToLL_M-50_HT-70to100_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/230000/AF691D22-5486-9C42-921E-83DD8D44B8D3.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/DYJetsToLL_M-50_HT-70to100_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/230000/BCA3A084-7639-934C-B8C3-F9FFA55143D8.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/DYJetsToLL_M-50_HT-70to100_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/230000/C450E507-4D2C-734B-8133-56DDBD11C5EC.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/DYJetsToLL_M-50_HT-70to100_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/230000/D90D12AA-D657-7A40-94F2-BA6C1F4C6A30.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/DYJetsToLL_M-50_HT-70to100_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/230000/DBB2B26F-5849-E845-BB77-2561CE8CBE76.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/DYJetsToLL_M-50_HT-70to100_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/230000/DBD27A69-44C5-1A40-8460-B8FF9F9C3790.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/DYJetsToLL_M-50_HT-70to100_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/230000/E9EB3407-E9E1-CD40-BBB0-CF2511738C80.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/DYJetsToLL_M-50_HT-70to100_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/230000/ED7F3AE2-3401-C741-B559-70F28D09A5E6.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/DYJetsToLL_M-50_HT-70to100_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2430000/002B3F2F-0CBF-0D4B-8281-33CECE13905D.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/DYJetsToLL_M-50_HT-70to100_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2430000/025D07DA-A6A8-D547-A61F-CEC8461E1179.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/DYJetsToLL_M-50_HT-70to100_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2430000/0DA0A626-AE30-5E42-8A99-E31AF3493D61.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/DYJetsToLL_M-50_HT-70to100_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2430000/17398247-6A73-B846-80ED-AAB91EDC5F65.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/DYJetsToLL_M-50_HT-70to100_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2430000/35684C9A-463B-8C40-8F01-D9F9ACFCDA2C.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/DYJetsToLL_M-50_HT-70to100_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2430000/4791C8DE-3E53-3544-84AB-ED0EBC13F27E.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/DYJetsToLL_M-50_HT-70to100_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2430000/59F1F931-22B5-8449-A16A-605BC43339DB.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/DYJetsToLL_M-50_HT-70to100_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2430000/626BA4DB-BF54-0E4C-8408-6BDCE78FEA4E.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/DYJetsToLL_M-50_HT-70to100_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2430000/63F67163-574B-C044-B95A-BFF29719F426.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/DYJetsToLL_M-50_HT-70to100_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2430000/68EE3396-7924-4E42-82CE-57A2F5100E26.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/DYJetsToLL_M-50_HT-70to100_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2430000/8120B848-8CBA-1F4D-9FC8-46C65FB68214.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/DYJetsToLL_M-50_HT-70to100_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2430000/853E0569-9FD7-754B-AAAF-9D6D6FDFD06A.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/DYJetsToLL_M-50_HT-70to100_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2430000/983FEAE7-026B-A641-A0E8-E52E03714A2E.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/DYJetsToLL_M-50_HT-70to100_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2430000/98AFF3F0-F096-DC4A-B99F-A27AD09CC02F.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/DYJetsToLL_M-50_HT-70to100_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2430000/A4E62F46-C69F-4E40-8E6B-506D5D350DEC.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/DYJetsToLL_M-50_HT-70to100_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2430000/A9C186B3-4616-2745-98B7-81A89D824250.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/DYJetsToLL_M-50_HT-70to100_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2430000/CDBE912B-2162-CC46-B91E-899C8BDD1231.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/DYJetsToLL_M-50_HT-70to100_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2430000/D6E34F15-50C1-8943-BE50-64E0A1932A67.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/DYJetsToLL_M-50_HT-70to100_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2430000/D76B2593-05E2-4B4B-8526-21465FF35479.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/DYJetsToLL_M-50_HT-70to100_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2430000/DE7B5ECE-CC0A-3C41-942D-BB0C005DAFCD.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/DYJetsToLL_M-50_HT-70to100_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2430000/E2B4330B-94B7-234A-944E-240D23162938.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/DYJetsToLL_M-50_HT-70to100_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2430000/F33397B3-9045-B543-BEFB-1D62F195436F.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/DYJetsToLL_M-50_HT-70to100_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2430000/FA1F1354-7E3C-9A4E-99E7-5A0996C90E16.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/DYJetsToLL_M-50_HT-70to100_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2430000/FD73F60A-056B-AA45-985C-E84EAEB0BA73.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/DYJetsToLL_M-50_HT-70to100_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/250000/164231B5-2B94-FE48-A3B6-37B32F6832C3.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/DYJetsToLL_M-50_HT-70to100_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/250000/25D892FA-A74D-6343-829A-016A78EB8498.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/DYJetsToLL_M-50_HT-70to100_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/250000/52C48811-F08B-9D44-89DD-EB0704FBB687.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/DYJetsToLL_M-50_HT-70to100_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/250000/89FF2C3E-B038-7F4A-9CA8-C3944F8BAC93.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/DYJetsToLL_M-50_HT-70to100_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/250000/B9806D61-D61A-A848-990A-7D88A3B8D87F.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/DYJetsToLL_M-50_HT-70to100_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/250000/E1AC5478-3140-734A-A2A9-B9B84B6849F2.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/DYJetsToLL_M-50_HT-70to100_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2500000/A4EF581B-3F37-1F44-8DC0-9676392C9575.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/DYJetsToLL_M-50_HT-70to100_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/260000/048E6C4B-D023-324A-B283-1EAE943DF728.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/DYJetsToLL_M-50_HT-70to100_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/260000/14A19474-43A0-CB43-8507-C42F56E5F520.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/DYJetsToLL_M-50_HT-70to100_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/260000/163AE70E-600D-734B-90BC-0BA173B97C7F.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/DYJetsToLL_M-50_HT-70to100_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/260000/177FDA6A-B4A0-5A40-805C-73BB2D27C3F6.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/DYJetsToLL_M-50_HT-70to100_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/260000/195E8ADB-5629-9945-9355-E06D64B8C3F0.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/DYJetsToLL_M-50_HT-70to100_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/260000/1CAA1EBA-F11F-DC4B-A307-F73E1470AD4F.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/DYJetsToLL_M-50_HT-70to100_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/260000/208EB1A3-8131-CD4C-92F2-E9CF92EC5CDB.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/DYJetsToLL_M-50_HT-70to100_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/260000/24D014AB-80BE-9646-9B10-AD33B59BC266.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/DYJetsToLL_M-50_HT-70to100_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/260000/2A14BBB2-7172-AD4A-AE61-36A2F64DC886.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/DYJetsToLL_M-50_HT-70to100_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/260000/2CA76C8B-32AB-CE46-AA64-EC449C072EBB.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/DYJetsToLL_M-50_HT-70to100_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/260000/3B4CA0D6-4114-6A4F-9409-776FA4A39613.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/DYJetsToLL_M-50_HT-70to100_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/260000/41CEBE15-9A34-E344-90CB-8D0A5051D742.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/DYJetsToLL_M-50_HT-70to100_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/260000/4A6F7B4B-CFC3-5849-B80C-6D0D50B36A12.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/DYJetsToLL_M-50_HT-70to100_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/260000/4DD2E943-B5CF-DF4E-98F1-A05D65354E17.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/DYJetsToLL_M-50_HT-70to100_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/260000/4F21C96D-6627-7F42-96CB-1C76BE6A8953.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/DYJetsToLL_M-50_HT-70to100_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/260000/51B6EE01-148B-E64A-861B-6FD3AABE1F21.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/DYJetsToLL_M-50_HT-70to100_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/260000/5313B24A-BD73-C645-AE08-C76428123923.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/DYJetsToLL_M-50_HT-70to100_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/260000/58905087-FA26-F74F-9E79-8FEA8DBEAEB5.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/DYJetsToLL_M-50_HT-70to100_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/260000/5C6DE5CE-9FF1-0041-80AA-C7EEB1C0FD35.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/DYJetsToLL_M-50_HT-70to100_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/260000/62E1DB89-DFB4-9149-BB43-CC5E0E8D29FE.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/DYJetsToLL_M-50_HT-70to100_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/260000/66DB67E1-81AA-5345-8A9D-D8A00942ACD9.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/DYJetsToLL_M-50_HT-70to100_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/260000/7C6E6BE9-D6A3-8145-A83F-F8DE90D43CE5.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/DYJetsToLL_M-50_HT-70to100_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/260000/864A70AC-E1E0-374B-8233-300D20ECD17C.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/DYJetsToLL_M-50_HT-70to100_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/260000/977BCA98-CBFA-A445-9986-6EC186413D74.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/DYJetsToLL_M-50_HT-70to100_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/260000/AAC00FC1-F275-014E-B937-91ABFA3AAB8B.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/DYJetsToLL_M-50_HT-70to100_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/260000/B090E272-BAE9-3449-A435-2E041CADAE43.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/DYJetsToLL_M-50_HT-70to100_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/260000/C5B04197-65CD-CA43-9324-04768224C431.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/DYJetsToLL_M-50_HT-70to100_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/260000/C63E6BB1-28AF-664C-A2A4-95022F22F1A2.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/DYJetsToLL_M-50_HT-70to100_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/260000/CC0D34D4-AF5E-8F49-866E-B0E609A2EBC8.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/DYJetsToLL_M-50_HT-70to100_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/260000/D95A08BE-23DE-EC4D-B3F9-9CD10A13C524.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/DYJetsToLL_M-50_HT-70to100_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/260000/EDFD217A-DD82-F044-B39F-FCA832738E1D.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/DYJetsToLL_M-50_HT-70to100_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/260000/EFC90A08-3D82-C844-9792-D352140FF580.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/DYJetsToLL_M-50_HT-70to100_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/260000/FA304DBB-F199-D347-8C1D-542D4809876B.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/DYJetsToLL_M-50_HT-70to100_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/40000/1C89B064-452E-7347-AEE3-A8EC6DFE64A9.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/DYJetsToLL_M-50_HT-70to100_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/40000/C9107183-A423-5B48-9547-BE4B3DE8374D.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/DYJetsToLL_M-50_HT-70to100_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/40000/E90B361D-C3E7-6343-BD94-D43E738DDD04.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/DYJetsToLL_M-50_HT-70to100_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/40000/EEB25B18-F4BC-BA4E-92D4-A050EBF3A228.root',
] )