import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/100000/06F8195A-E7DB-8E4A-962E-FF14EC2A9F3B.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/100000/2787B6D8-75CC-7045-B428-F9F1456220C6.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/100000/486005E9-3E18-F64F-A8F7-64FAA24195D6.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/100000/4AD9B2CA-DA6C-CA40-B1CE-8C97535C7102.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/100000/578AB28D-EDF1-AA40-A61B-921B59B4F200.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/100000/7AC55405-A391-244F-AE36-435E5EC05441.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/100000/A7E8E7DE-2B70-4341-A680-926E6D37FE5F.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/100000/D34EB4F3-3FF0-774F-966D-D622E463AF41.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/100000/E61845EE-220F-8748-A946-2E559CAC5BFE.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/100000/F76D1DB0-45E7-F04E-BE1C-C5B463E9E786.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/230000/06AD0871-ACC2-154E-9EAA-A6B41CE78CCB.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/230000/06FDFF64-F506-CA41-B5D4-9393C36FF0BF.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/230000/0C159FD0-921E-C74A-A84A-65F0FBC3B210.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/230000/0E725067-CAB6-E846-99B4-D3ED2EA0F927.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/230000/1DD5EA45-72A8-F744-847E-0FD551B8EF2B.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/230000/1EFF0E68-2F02-F24E-940E-FC9CF7F13A9E.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/230000/1F1AE097-5582-CE44-A14E-B8652F0C8C42.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/230000/21EE137E-9BFF-A549-85BA-0682E8ABE285.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/230000/22705D63-B616-EE42-A054-5626392912CC.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/230000/272AAD35-2272-584A-966B-E57D74EF61B3.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/230000/30EF1254-2F6A-554E-8CBB-C7BF25F767B9.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/230000/32E41EA4-CB9E-C74F-BBBD-DD38321478C7.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/230000/3DD061CB-231A-D74C-882A-2DDF33E75B84.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/230000/3F7F0BF9-03F6-014D-83A8-6E33AE09FDE8.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/230000/4314F065-C4F8-BE4B-8F19-213908ECA68C.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/230000/456191BF-EDE4-F946-9523-F56BCCEAC3AB.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/230000/49CDBF73-85BE-ED42-9828-6F9CF56426EE.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/230000/4BE0B17A-5854-0242-AFFE-638DDC32C55B.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/230000/4CC2461E-CB99-5C4E-A9C3-456B8A8595E9.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/230000/55B0E687-5979-F546-9E29-7A3BF260D0CA.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/230000/65345CEB-7639-9446-A037-DE7C3F570ECD.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/230000/675B91E4-E2E7-5642-B31A-93A51903FCDC.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/230000/67DEA7A3-DADB-0748-B7D5-1671399EB0F8.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/230000/6D92B6CB-8E5F-F04C-A34A-CA14CCC832B5.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/230000/6DC5764A-7884-3946-AB02-1A2AF33EEC9C.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/230000/7158309C-891F-5E4B-8453-96A4CE48D4EA.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/230000/7461F8F2-7456-E143-9E35-07F47240B81A.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/230000/7AF9688D-4BCA-D243-85A8-AD1C7A210167.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/230000/8069D971-D9B8-3F42-865A-0DD5618A70E8.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/230000/8205F6C2-169F-AD4C-A331-448CBABC40FD.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/230000/85950EBA-C8BD-754D-8F51-D979128A9780.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/230000/8A0F212C-0C81-E64A-AC3D-226762E76A85.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/230000/A39FCD05-259B-774C-8255-AB90A4DBC00E.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/230000/A78427A3-5564-1B47-82B4-0F3D032F9053.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/230000/AA74C5EC-E08C-9842-B408-344EB71A4B3B.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/230000/ABE2E04B-B442-6E4B-9D79-5498E6664AF5.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/230000/B2F977B0-519F-EC46-8FBF-AC802ADB58E9.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/230000/BD32437D-909B-3E4A-8141-ABF7252D23FE.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/230000/C1008A88-48EB-FC4E-863F-4BA001EF971A.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/230000/C14CF8C8-FD73-834E-8838-49326250F70A.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/230000/C878D85F-F5F8-DA44-B077-7544B035D442.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/230000/C93A917B-EA6F-0B44-B7C9-DF4BF7A07E69.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/230000/CBD0BCE2-0F02-3E49-A0CB-2EB06C437D11.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/230000/D392DE04-0E21-2C42-A84F-C89D158EC87A.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/230000/D4B7EE9E-3752-7142-9E75-AAD4F343AF25.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/230000/D8045EA7-97F4-8743-AC1C-1BA6AE8546E4.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/230000/DB96F9D7-729C-F243-8A1B-DB0BE8027158.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/230000/E756840B-AE75-D34F-BAFA-F35822F0CDE7.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/230000/EF994055-17DB-AF43-81E0-F0C99EF1BC41.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/230000/F373DD11-243A-3D42-B268-B0EBC12C6D00.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/230000/F54CDE18-C4D2-F140-AC60-44A847CD54DF.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/230000/F9DAB210-D884-7D41-9E8F-6A2EC6BBD94D.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/2430000/0A373D67-7835-8848-8E4E-EF92D1F8892C.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/2430000/606E6634-CC65-874B-8C71-944841C747EE.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/2430000/77610231-91E8-2B44-BEBB-52C2F3367C00.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/2430000/7BF1D285-493B-7C4E-BF32-0E16CA803D71.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/2430000/9AEC54FC-E3B6-D24E-9974-CABA536F30AB.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/2430000/D99CE51D-1CC3-C34D-9FF3-CFAD99DFA3CE.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/250000/171C9F1B-ACB8-114C-AE8B-11EB73116AF4.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/250000/1B01B4D0-3629-AC48-9383-408D9A3B86A6.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/250000/3623ECB4-89EE-1544-9C50-16DA001F3793.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/250000/3D45A345-E242-4946-A459-1EAC28932711.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/250000/43ECF13E-50AD-7D48-8A31-5ABAD0B86757.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/250000/595F3B32-C9DA-8F47-A640-D2A09F3AEC98.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/250000/6CED4D62-9581-8440-9F12-530A860D2B4C.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/250000/6EC78F39-7F3A-9642-BB91-1980C7DF4618.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/250000/6F12616E-3000-A941-A43A-B7E4BFFE8D24.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/250000/7DA6ED90-8F19-494C-BD58-1FF2C7AEC6BA.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/250000/934ED4EB-FE49-AD46-AD03-8AD1C3CCFC6C.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/250000/ABC9DC6E-7AA1-8A40-89FC-59B5757FA861.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/250000/AF5F7384-4F30-B140-8668-16A848746083.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/250000/C80564A0-0579-CA4D-A2CD-E919101A35D4.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/250000/CB1891A0-3741-A549-B9EC-0484D68B079F.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/250000/DB8D6111-4A5F-7B44-8FD7-B544B641ADCC.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/250000/E8E1DA90-C14B-4346-B4BF-55ADEFE8D822.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/250000/F69B469D-1BC1-944A-A058-775979604358.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/2500000/12895C6C-46A8-1747-B027-37C970A987B9.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/80000/20CEFED1-2757-6944-80B8-95F9A3CF05AB.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/80000/2BB927D2-F29C-214B-9FDF-72D850653A95.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/80000/6DA82AEE-9092-3344-B148-E72950D65F5E.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/80000/A48E95B8-48A0-DF41-BD90-49378444DB66.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/80000/A6B23365-2B99-2249-A4A6-29B8D60B6B79.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/80000/B86271B0-EC54-2A42-8D83-F13ACC2A648A.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/80000/B95071B2-6902-EC49-9054-C54F98E5C0B4.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/80000/BB6B65C2-5159-2240-A38F-6E560F791DA6.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/80000/D7C893C3-B5EE-8346-A57B-B2FD93155993.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/810000/A9F09F62-0422-D64E-B6DC-8ECB40897F7A.root',
] )