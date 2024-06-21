import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer20UL16MiniAODv2/GJets_DR-0p4_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/100000/60B0C3C3-CDAE-274C-A90B-D589A73A13C6.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/GJets_DR-0p4_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/230000/06DE8A46-5397-574B-B127-F16C1E1E2913.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/GJets_DR-0p4_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/230000/08D23529-6B18-2A45-8254-8EAF11C42CDD.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/GJets_DR-0p4_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/230000/1258330A-64F2-3D46-9647-C34B5AAE6CCA.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/GJets_DR-0p4_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/230000/27273C82-E3F8-784A-949A-E1C68BD687E9.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/GJets_DR-0p4_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/230000/28012C73-0A4E-6A4D-B6E9-542BEBA32E99.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/GJets_DR-0p4_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/230000/523DE429-12E1-A746-BDDB-E0D0AA7A4553.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/GJets_DR-0p4_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/230000/5E68B50C-AB7C-584F-903D-ED0FB969A1A5.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/GJets_DR-0p4_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/230000/66B6E202-E72D-844C-A774-579ED201B825.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/GJets_DR-0p4_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/230000/78C45FC0-E8AF-6249-9E58-CBB9F6B9D9D4.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/GJets_DR-0p4_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/230000/98540477-DF67-9948-BBC3-A031A6D09C42.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/GJets_DR-0p4_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/230000/B4AECD7C-F06E-9D4D-BBA6-CDB80F823DEA.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/GJets_DR-0p4_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/230000/C1EA4A53-48B4-3D4A-83D0-3F6B0E3FC5CE.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/GJets_DR-0p4_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/230000/D1576FC0-D3B0-AB4E-9F58-1CFE696A096B.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/GJets_DR-0p4_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/230000/D3EE8D7E-4724-1743-9828-6C9137D38C76.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/GJets_DR-0p4_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/230000/D5B416F2-AC91-BD42-AC19-044999DF414C.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/GJets_DR-0p4_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/230000/DB6D9125-6C72-FA44-97CB-D5D07D70630B.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/GJets_DR-0p4_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/230000/E25D1ECE-E5F1-3942-9A48-D242E2DFDEC1.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/GJets_DR-0p4_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/230000/E47E6F51-3A3A-1C40-9500-7C3E63C294B5.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/GJets_DR-0p4_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/230000/F44312B8-4574-B547-A674-D8115F351A29.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/GJets_DR-0p4_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/230000/F4E76F75-89F2-E44E-83B9-5A882866AC6B.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/GJets_DR-0p4_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2430000/8BBFBC12-2E74-534C-A406-364583C9C906.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/GJets_DR-0p4_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2430000/A9A3E6A1-2BDA-DD44-871A-6E3A5892EA50.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/GJets_DR-0p4_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/250000/46D360EA-81C3-2F4B-BD4D-06A3E5DF68A3.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/GJets_DR-0p4_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/250000/5DA70F4A-9335-FF45-92C8-3159501D411F.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/GJets_DR-0p4_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/250000/95E274BB-65BE-9C4F-B8CB-F24F83FD3198.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/GJets_DR-0p4_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/250000/D644A403-F214-7E4C-9D60-12CEFE2EC411.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/GJets_DR-0p4_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/250000/E7062453-F94C-4D4C-B78E-22D7D812E7D3.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/GJets_DR-0p4_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2510000/18C1B97C-2AA3-704C-A8A4-1C1A0A5DA7D2.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/GJets_DR-0p4_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2510000/3160EC31-D48E-5947-9BD2-A75E85C615A4.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/GJets_DR-0p4_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2510000/3176A164-7430-DB4E-B316-E108F52117B2.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/GJets_DR-0p4_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2510000/43595A7A-3A89-0A4A-BDB3-25607F821778.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/GJets_DR-0p4_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2510000/6740417F-CCFE-E147-9FCB-4F24B90F1527.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/GJets_DR-0p4_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2510000/8DF04796-B468-274B-96B9-3421A6DEF6D5.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/GJets_DR-0p4_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2510000/9A68B231-485B-744E-BE84-D37F5E4B9BD7.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/GJets_DR-0p4_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2510000/A59D965E-5384-CD4B-BFC9-107B1C692653.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/GJets_DR-0p4_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2510000/B455A5E8-493A-0141-8D1E-665A5B9EB35E.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/GJets_DR-0p4_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2510000/D0D30D40-9D84-8D4F-ADAD-1DBD3F1B04C9.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/GJets_DR-0p4_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/40000/03D127B7-D891-FF45-B25B-DA7E40C37F81.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/GJets_DR-0p4_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/40000/1095CD4C-238C-B941-8C23-AE5133DADF0C.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/GJets_DR-0p4_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/40000/1419CE1D-8971-B24A-94A3-92AB50CB632B.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/GJets_DR-0p4_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/40000/1813600E-4D7A-3241-B2F8-49062F77DD8B.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/GJets_DR-0p4_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/40000/2669E509-D674-5345-A7A8-DDF78D5772BB.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/GJets_DR-0p4_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/40000/3C2C53B7-0989-5040-B17C-66E573AD15A8.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/GJets_DR-0p4_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/40000/4221CAFD-7A0A-6746-A337-9E0928548EDA.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/GJets_DR-0p4_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/40000/71F2F816-125D-4E4C-8CED-58A1118F778E.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/GJets_DR-0p4_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/40000/77E12C84-468F-7E4E-9387-AFE30E8C8A7A.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/GJets_DR-0p4_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/40000/8C1894D0-9924-8B49-9C47-DBA10A23D4D8.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/GJets_DR-0p4_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/40000/8DFF4F55-0F62-224A-A0AB-CBA52064AFF1.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/GJets_DR-0p4_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/40000/92E09BEE-A48B-F34F-B20D-4CFD85DEA3B3.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/GJets_DR-0p4_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/40000/96641A22-F9C3-D047-8CE2-AA0843A1B3FB.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/GJets_DR-0p4_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/40000/B09D7E7E-EBD2-5440-B595-622940D14D30.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/GJets_DR-0p4_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/40000/B7430F30-4DC1-B947-B87F-D5C286812983.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/GJets_DR-0p4_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/40000/C2AFD675-6B5D-C843-B16E-5DBFA0744340.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/GJets_DR-0p4_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/40000/C4226026-9BA1-BD40-A724-AA835D11C242.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/GJets_DR-0p4_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/40000/C5CA2064-F438-6F44-BB44-ADC0A1E9018F.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/GJets_DR-0p4_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/40000/C9CE0C09-64AE-834A-A72F-3B7016F1B67B.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/GJets_DR-0p4_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/40000/D6CE77B7-A38F-1641-9789-B7DAB899A01E.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/GJets_DR-0p4_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/40000/E99C105B-3639-2F4E-955B-0F747CE15ED0.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/GJets_DR-0p4_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/40000/EAFA8089-7B54-D54F-8BC7-35B57F6E6A50.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/GJets_DR-0p4_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/40000/F11125B3-7C40-A147-8D9B-1EAA40587988.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/GJets_DR-0p4_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/40000/F6356354-8B14-CF4A-87E6-4E3EAB957FFC.root',
] )