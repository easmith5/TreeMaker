import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer20UL16MiniAODv2/ZJetsToNuNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2530000/01C8EFCA-4EA1-9141-B729-488D941096FC.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZJetsToNuNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2530000/2FA3C8B6-0406-7342-9182-8F206C1B1CF5.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZJetsToNuNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2530000/5E3219F1-CDE0-6740-9FBA-D2DABEF7DBA1.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZJetsToNuNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2530000/679B4208-A131-614C-A2F9-05342B938FF7.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZJetsToNuNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2530000/781E2185-FE9F-4F4D-9B0E-9A021B4FEC95.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZJetsToNuNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2530000/BB48DE1C-72E5-0947-BF21-FCA3CF5CB643.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZJetsToNuNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2530000/D2F46B32-A44B-F34D-8482-9CE22D0B7B77.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZJetsToNuNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2530000/E5BA080B-459B-944F-A819-1BDD104FD3BF.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZJetsToNuNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2530000/F4667711-34D5-C045-9B77-06DF40C56CE7.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZJetsToNuNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2530000/F6ABF1AB-4647-634D-A919-52087DB2E113.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZJetsToNuNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/260000/00C161C4-77BB-5943-928A-072A8D11332A.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZJetsToNuNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/260000/01568D63-312C-EC4D-90E0-A6787A7FB338.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZJetsToNuNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/260000/0419CA9B-ABDE-944E-8183-B390FBC3BADF.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZJetsToNuNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/260000/0887317D-4D71-224D-9207-3FE0CFE48618.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZJetsToNuNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/260000/0962B3C4-CBEF-EB45-BCA1-731E97DE55DD.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZJetsToNuNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/260000/0B05F086-AB5D-9B48-BCC7-94412205801D.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZJetsToNuNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/260000/0DD0A6C8-E691-4E40-8EDF-E46030D1616D.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZJetsToNuNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/260000/0F65A631-866B-4B4A-9E8A-4FCA631C81B5.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZJetsToNuNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/260000/14C4A7C5-B875-9F41-B19E-43DBC3E313D6.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZJetsToNuNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/260000/157FB8E8-A250-2847-9888-EB19540137B9.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZJetsToNuNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/260000/17ED7BF4-3AAE-3441-AA41-2DE0FBFFD115.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZJetsToNuNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/260000/216DA214-6C50-7A43-8CDB-3537DC391AB8.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZJetsToNuNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/260000/25BBDB31-0F02-5B44-BD3F-C3DD02E7B312.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZJetsToNuNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/260000/27FF1C7D-9C53-D242-912D-CB0EFF721028.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZJetsToNuNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/260000/2A99EEC5-16EB-FC4A-AF04-A38AD3CB4DE0.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZJetsToNuNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/260000/30C3ADE5-8190-FF4D-A0A5-2A8452C36AD9.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZJetsToNuNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/260000/342C6382-C372-DF4C-9CE7-32F2294F1473.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZJetsToNuNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/260000/34BD5B5B-216D-0140-B04D-0B11F5EBB7D0.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZJetsToNuNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/260000/396D1D19-7DF6-A94D-BE75-755DCEB4EEDE.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZJetsToNuNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/260000/3C0D79F3-0FED-4C41-8324-AAA10AE36876.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZJetsToNuNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/260000/40F415EF-43D9-3844-B7A8-855580C3A6C8.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZJetsToNuNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/260000/4A6F844A-F55C-9B45-80C3-3E9C5555BDF3.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZJetsToNuNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/260000/4D8BF225-A769-B041-B039-05C7463EC580.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZJetsToNuNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/260000/4E0BB128-7F77-4043-8146-81EE808597FA.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZJetsToNuNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/260000/541E4903-FA1B-454E-A911-9ED8D33C4041.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZJetsToNuNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/260000/545FBDFE-6488-DE45-881A-0ED01B511197.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZJetsToNuNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/260000/56CEF5F2-4E9E-F045-A329-CF270B604086.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZJetsToNuNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/260000/58C6441C-5BA0-9948-96C3-AA46F03DF6A5.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZJetsToNuNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/260000/613514C7-E87E-A14D-B2B1-CB2FD6C08FD5.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZJetsToNuNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/260000/65881CB4-9022-944E-A7A7-AFE66699676D.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZJetsToNuNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/260000/65A5BE74-DC08-B74A-A9F3-38EEFC7EC699.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZJetsToNuNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/260000/699C2385-12A5-8E4F-BEF3-7FE9A412F814.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZJetsToNuNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/260000/6FF417BB-BBCC-6C41-9D78-69ABD162E19A.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZJetsToNuNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/260000/730F8E7D-8198-7242-899F-699E75B5E8AA.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZJetsToNuNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/260000/73AF6B37-A26F-B749-8AF5-81929D297B01.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZJetsToNuNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/260000/74E38AB9-5337-8740-833E-FAC7518CF701.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZJetsToNuNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/260000/7992738D-26A0-6244-B2A4-B61353EA6319.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZJetsToNuNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/260000/7E511EA7-6900-2E4B-B2A8-62875221A100.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZJetsToNuNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/260000/84F3E120-60F0-A24C-963F-59B00CCB95EE.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZJetsToNuNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/260000/864AE816-E746-CC41-B3FA-D6D76490A9C6.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZJetsToNuNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/260000/8CD3E7BB-4C15-B248-B182-7390B941B58F.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZJetsToNuNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/260000/8DD9A863-157A-6A40-9631-2724D0F890CA.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZJetsToNuNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/260000/91038D78-6414-ED43-8BB0-0D59121D16FC.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZJetsToNuNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/260000/93B8D6FB-573E-C643-9214-6F67CFF91A00.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZJetsToNuNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/260000/95FFFDDC-D81E-704E-83ED-774D0800CB7B.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZJetsToNuNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/260000/9C7F4F7B-C0BC-3946-A01F-714756E4D298.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZJetsToNuNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/260000/9E9008C9-2BBE-BB4D-90E5-AC8A10E16BFB.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZJetsToNuNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/260000/9F54CF32-81FE-F240-BC4E-67DC45544591.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZJetsToNuNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/260000/A1AAF676-6C05-244C-91AF-CD3CF970ED97.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZJetsToNuNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/260000/A2657448-DEE4-A34B-82EB-FF1EB8A55FF0.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZJetsToNuNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/260000/A2D125FB-50C5-8B4D-A2A1-4E83B8EBEEF9.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZJetsToNuNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/260000/A4AFFEF9-0D08-0949-BD34-1636CCFDBE26.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZJetsToNuNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/260000/ABFC93FB-410E-A049-94AC-4A5CE7524DE0.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZJetsToNuNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/260000/AF538BD8-3A39-D24B-860F-96EBE2997F54.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZJetsToNuNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/260000/BC3E1FCD-D228-9B40-821E-A58966605B7D.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZJetsToNuNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/260000/BF87F315-2470-6049-AAE8-8108E31E4399.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZJetsToNuNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/260000/CE18726D-0863-044A-A927-BE7BF13B94C9.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZJetsToNuNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/260000/D43DD808-E363-D145-9A8C-82B1C8A9520D.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZJetsToNuNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/260000/D689A967-9CFD-784F-B4C2-BDA8DA0373CE.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZJetsToNuNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/260000/D8DFA0E9-D35D-5244-AF7A-812839543139.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZJetsToNuNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/260000/E04918FF-943E-C64F-9604-3A348A0A4627.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZJetsToNuNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/260000/E0BDC010-7F34-3B47-A78C-29693C8BE128.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZJetsToNuNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/260000/E1E748C3-A3DD-154F-9175-672A23FA9B29.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZJetsToNuNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/260000/E2301D01-22D2-9747-AF71-E583AF9D4F14.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZJetsToNuNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/260000/E2384317-2EDE-354C-9A4F-D6A510353D51.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZJetsToNuNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/260000/E32807C1-A066-9B44-B98E-4BDE6399A32C.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZJetsToNuNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/260000/F85C6A36-19C7-DC47-889C-DDEAA78CDAB9.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZJetsToNuNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/270000/09911E36-CDBF-AB41-9B02-AA7608DBBE6E.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZJetsToNuNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/270000/0FDDBC64-EED8-A64E-88EE-D6113653BB0E.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZJetsToNuNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/270000/210076B1-5A74-9640-A173-4DFADA59DEB2.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZJetsToNuNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/270000/358F2AA2-3069-0F42-9B38-277F650F2CA8.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZJetsToNuNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/270000/4877889F-071E-A547-AB8A-307BE5785806.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZJetsToNuNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/270000/4A5C8483-970C-7340-956F-ED9CFD31BF1A.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZJetsToNuNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/270000/4AD0CB27-6BEE-D84C-A6DA-E3171F68C941.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZJetsToNuNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/270000/4B643D58-243B-2F48-9C84-8FEC240BB630.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZJetsToNuNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/270000/67951274-EB2B-3E4D-B32E-516D41C7FE8C.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZJetsToNuNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/270000/717137F6-678E-BC4C-A048-6174633495DC.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZJetsToNuNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/270000/7978DDC2-51A0-714A-B8F2-9A511CC75CB4.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZJetsToNuNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/270000/824D886D-152C-034C-9A73-C71798F41BDB.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZJetsToNuNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/270000/8328778B-7DA0-394A-AB8B-AADDEEAA8B43.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZJetsToNuNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/270000/90AB3EA1-2D83-F14F-B009-D16355702217.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZJetsToNuNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/270000/9585D717-00CF-A54D-A857-0E586B7CF7CC.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZJetsToNuNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/270000/A026777E-8CD4-7F4D-9E45-7879259518F2.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZJetsToNuNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/270000/B581402C-16C5-0A4D-8519-58EF501A659C.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZJetsToNuNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/270000/D0B998DB-582B-BF4D-87A5-02FA2E06C83C.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZJetsToNuNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/270000/DFE04D2E-A2D9-2E4D-9912-3C613D99D079.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZJetsToNuNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/270000/E728D182-966B-6D4C-84CD-00086DE6D991.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZJetsToNuNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/270000/EC7A407E-A386-2B49-8C19-1AF6F21450AC.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZJetsToNuNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/270000/EF5A554F-3D99-C74E-A57B-72700218D8DA.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZJetsToNuNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/270000/F098A519-10E0-544A-8CBC-F7254A419070.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZJetsToNuNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/30000/0012B31C-6E24-8F45-B222-110587B0DD27.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZJetsToNuNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/30000/0DA02E2B-55BA-174F-9C2E-F371FBDE0F0C.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZJetsToNuNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/30000/775A8D05-C464-A542-89CB-12F13A918921.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZJetsToNuNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/30000/DC5AC802-6C2C-5742-8B07-3D2A26C3A13D.root',
] )