import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer20UL17MiniAODv2/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/240000/0D5C49C2-1C9E-A643-8CA2-063DF278DFCD.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/240000/0EA60783-DC4F-774D-B30D-42CD68CB8D21.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/240000/1215A4C4-686D-AF45-BA83-114F5A86FD8E.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/240000/18B4C3D5-D114-024A-BF93-219653CA488E.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/240000/196F290C-6B14-C34F-9E62-1B757E0FBA83.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/240000/1CB6E4E3-D276-C94F-858A-89DC7694BB4C.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/240000/20FD221D-3B0A-B743-9267-0A97CB049812.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/240000/264149FC-B075-3741-823B-656954D95E61.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/240000/2D874DEF-F3BC-6040-ADDE-6FAC5CBBF8CE.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/240000/3CB67789-D86C-9348-AFCD-C9E7ED280F05.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/240000/4049C2A3-F4F7-4444-AF7B-6B77B02094D8.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/240000/4C54767E-9754-9748-8F35-AD325BD65E88.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/240000/530CBA47-4374-184A-BEB5-63E1DCD93E64.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/240000/5F03305B-013F-CE44-A5D2-3B986CF099AE.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/240000/7D356928-E9B6-F143-9A74-78D471308E45.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/240000/825C26A5-FD81-6641-816A-DEFDAB7BBDE7.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/240000/8670BDCF-32D4-604E-980E-B6BD25FA952E.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/240000/8FE56DB6-602F-3A42-A636-E5B3FCB31E21.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/240000/95CA97C7-82E6-1E44-B1DE-3A481D1E0A18.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/240000/A2602507-EE91-544C-A147-07DF52DD0A50.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/240000/A42BC897-848E-FB49-A092-EC74356B37A8.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/240000/A917E2B5-C416-334D-BF56-D215CE54CD2A.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/240000/A976F243-487A-624D-99A9-229425B7729A.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/240000/B77CF5AE-556A-6B48-A5BE-6DD94042DFA2.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/240000/BA6D9550-CAB6-1640-A06A-92C22CC479EF.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/240000/C30994D2-972C-E84E-B4DE-1CBF00AD68ED.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/240000/C665F563-B111-F74E-8B30-0664ABCDB077.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/240000/C7488054-F27B-1F4C-A33C-E736DAC9A2DC.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/240000/D3DF1596-4FA6-324C-8852-38DD4BC8B274.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/240000/D6EDA52D-E235-8B4C-8257-1F8BC6655E23.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/240000/DAE307C0-6F02-3244-B1AD-C781A8F36AE5.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/240000/EAC751D5-F9B8-934B-A27A-75F5C3CACE3D.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/240000/ED8F688D-4A1D-0D40-8026-F8C6D45FEDFA.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/240000/EE69FADC-EF26-4843-A165-1E4D5F143091.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/240000/EE9CE666-1ADE-9145-87BB-960606373793.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/240000/F1AFD013-8E38-8E47-98E0-7A9F617B9822.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/240000/FE8B1EAE-3628-2F4F-BABE-89EB132DC862.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/30000/0030740B-0641-BA42-A5F6-7BE47AFFD829.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/30000/06645983-818E-2445-A3A2-0EEDC6AC233E.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/30000/0E577791-FC77-C344-8286-2E96EFC3F111.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/30000/0FF7CB80-6446-1D4F-9343-DB9E8C275FE7.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/30000/102828CF-6F65-424E-8A90-12A1DACA9A68.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/30000/166AA6D2-FABF-864E-9949-3DDE1FF6573B.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/30000/18F0750C-F686-344B-A613-DCE922316DBA.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/30000/1A282C9A-9991-AA4F-A7F6-AED1434A79EA.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/30000/24ECE8A7-13AD-244D-A289-1DB8F4F0FD43.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/30000/2738DFB2-B921-814C-9ACC-189894078CDD.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/30000/28E171DA-FDF1-E641-83F3-357C70D51C0D.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/30000/2D1C4A81-1BD8-6A4F-ACB8-D0C837403E0B.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/30000/2D588D0F-D75A-6A4F-94F3-349B0C46DA4B.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/30000/30779DFB-B443-0545-99EF-CFF486B8D717.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/30000/334101E7-6CF9-CA41-AFE5-CDDEFF9577B6.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/30000/351E4380-1CAE-1345-8B29-0ECF20DA7D6B.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/30000/38195A12-9A05-0C40-AD7F-FE92830581D1.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/30000/3B2F008C-1C07-2349-91BB-EA0C6BEFA490.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/30000/3BEE4F20-190A-0C4A-B989-6DA3BBE98CE9.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/30000/413D0C8B-CDA4-BB44-83DB-E729E55AB6E7.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/30000/447610FF-E6CB-4844-8E87-EC3AA5870696.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/30000/4FE55ABE-0A06-B445-8A6A-C64CA17F52A3.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/30000/535D8D55-6430-9B4F-A2FE-7F7A16421040.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/30000/576A9300-9754-B442-A3C8-CB2B86DFD5DE.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/30000/59EA13B1-27C7-4648-BEB4-5FAD34C58327.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/30000/604160EA-A69C-C042-B6A1-021E2B03255E.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/30000/63A6F2B2-19BA-4F42-AE63-2C015CD79E89.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/30000/64889149-43E7-494F-9883-1C5B2489A097.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/30000/7374FFCD-6C1C-724D-91F5-4DE1F53B42CB.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/30000/73DF4EDD-5901-0F4D-9710-F7705D093BA1.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/30000/775E847D-0884-414E-942A-E55A40E26726.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/30000/7BFCE05C-997C-C34A-8517-38221AA3B8B7.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/30000/7F4FC58F-0DC3-9B43-818D-7CCE9BB9EF5F.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/30000/80B13819-F4D3-3B4D-8533-DE8BC7ADB43E.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/30000/84914AD5-3925-2847-951B-CED4D09C9D95.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/30000/8D6F8E70-579A-6E4A-B323-30FF5F30E64E.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/30000/918E57C5-72D9-1C40-8086-D00CCC21476F.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/30000/94F27F1D-F523-BB4C-B0EC-F945C38BDAE5.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/30000/9791A66B-703B-524F-AB31-5EEA572F2838.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/30000/983BAE58-6B8A-4043-BEB0-DA35F8CCED0C.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/30000/99120187-D1CD-3D46-A5F8-2074C9FD24F9.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/30000/9CF5AF1F-B5D3-DC49-B941-EE92A4CB5442.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/30000/9D2B86F0-E89B-0440-8911-859D13DF6558.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/30000/AF426045-98BA-9E47-AA1F-B533055F0E40.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/30000/B3D592CC-E412-B346-9FE9-A783975EE467.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/30000/B4E4FAA8-49DE-AE43-881A-E01B02156909.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/30000/B7BCE016-CA7E-8B46-8378-24283B7C3866.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/30000/BEA57E12-9938-0B4E-AC04-8D146D53223C.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/30000/C1686645-DC64-0E46-B397-7D1A89763A53.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/30000/CCD3F496-B207-B04A-95A9-649474690823.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/30000/D000EEB0-889F-7441-B228-D7F26FF716A9.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/30000/D5A05086-69E6-1046-A112-CE36B0719DE1.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/30000/DD342F61-539A-3543-B351-34DED58276D1.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/30000/DD5FA1DE-B878-F24B-8EAC-9495A6D8FA83.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/30000/DF581585-BF93-C14D-8309-AE30C2ECD2D4.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/30000/E18FE9EB-C921-E147-A5A6-7DE55C0DB319.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/30000/E217F40E-C399-2A4F-83CE-5F4F1B78675F.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/30000/E78A8E85-3CC9-4C40-A3AE-597577B54839.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/30000/EA2E6793-5DB0-2D40-856D-0B0A4DF2266C.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/30000/F5A40983-0242-0944-91A6-59AACFA33353.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/30000/F934F727-C727-4646-87B4-DD6CFDD6CA90.root',
] )