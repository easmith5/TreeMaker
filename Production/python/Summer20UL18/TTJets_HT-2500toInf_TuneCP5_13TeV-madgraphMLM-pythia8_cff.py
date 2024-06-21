import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer20UL18MiniAODv2/TTJets_HT-2500toInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/2530000/00BF05DF-F2BA-9E4A-BD14-80F8334BB16B.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/TTJets_HT-2500toInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/2530000/020ADE35-766A-9B42-8FF8-E3C18B8B6325.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/TTJets_HT-2500toInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/2530000/044ED6C2-2C55-E34B-AE28-A43AE2A1BDC3.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/TTJets_HT-2500toInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/2530000/06FEE771-3CA8-024D-A648-D44621ADF025.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/TTJets_HT-2500toInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/2530000/09405C73-A554-464E-BD68-00B2DB917BD2.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/TTJets_HT-2500toInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/2530000/0C735F8D-6E99-3848-9C43-723FB97FD397.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/TTJets_HT-2500toInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/2530000/11A3EC27-36E7-8B49-BBFB-33F807B278A3.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/TTJets_HT-2500toInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/2530000/19071183-BD21-204D-831A-4C914BD6156E.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/TTJets_HT-2500toInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/2530000/191ED4CE-1D6F-DC4A-A2B9-845723829B53.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/TTJets_HT-2500toInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/2530000/1AB73835-31E4-1443-94D4-4E7C11E7DD28.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/TTJets_HT-2500toInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/2530000/1AC4801B-0BE8-1749-BDBE-21AFE9BD0449.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/TTJets_HT-2500toInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/2530000/1B5BCEC6-F3C6-C64F-B38B-1C0A932F64E6.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/TTJets_HT-2500toInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/2530000/1DBCDF9D-2BA8-F740-952B-443A26770EF5.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/TTJets_HT-2500toInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/2530000/1F663375-98F8-9847-ADC4-3EC60CDB41D9.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/TTJets_HT-2500toInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/2530000/22356B57-3718-214D-9E1F-F4298FCDDA03.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/TTJets_HT-2500toInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/2530000/235F1839-4F28-B444-8C5A-7F1F8418ECEC.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/TTJets_HT-2500toInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/2530000/2565C75C-59F5-F544-83B1-AC5A400CD19E.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/TTJets_HT-2500toInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/2530000/27D6FA9C-452A-D64D-9602-61798AFDC6C2.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/TTJets_HT-2500toInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/2530000/2945AAEF-DFFF-0B48-BE70-6526E3FC3A1C.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/TTJets_HT-2500toInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/2530000/2D866240-3D0F-8546-9B5E-B19A419D63B2.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/TTJets_HT-2500toInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/2530000/2EFF3964-E945-B64F-AC25-DC1896757F64.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/TTJets_HT-2500toInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/2530000/30584E54-22B9-0242-92D8-CC40E3A33CDF.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/TTJets_HT-2500toInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/2530000/32779273-50AB-7E47-BACB-F1C9CA488DC3.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/TTJets_HT-2500toInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/2530000/34426232-4FE8-8A4C-8A20-5A554D3CE300.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/TTJets_HT-2500toInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/2530000/3472EE44-E0AD-F146-A762-225AA689F328.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/TTJets_HT-2500toInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/2530000/37EA41D7-5757-1749-84D4-07CD6AFD50F2.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/TTJets_HT-2500toInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/2530000/38E1FE7B-681C-C247-A3DE-41A12E24D48E.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/TTJets_HT-2500toInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/2530000/39A0BE98-380D-EB4B-ADD4-E9367346B54F.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/TTJets_HT-2500toInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/2530000/3F18AF24-572E-B649-86D3-91225946FBA2.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/TTJets_HT-2500toInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/2530000/41878C48-F0E9-5043-942A-CA5F63DB2281.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/TTJets_HT-2500toInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/2530000/44095BD1-75A4-5740-9697-05770FB94C1C.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/TTJets_HT-2500toInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/2530000/44242867-6478-7F4A-90A0-E4305118F655.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/TTJets_HT-2500toInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/2530000/44D17BFE-F362-AD4E-AD6E-3AC77CA6C6E3.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/TTJets_HT-2500toInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/2530000/48EAB98A-5A2C-2C4A-AE63-C1E919353E02.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/TTJets_HT-2500toInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/2530000/5062AC9F-A970-E743-8184-90304FC63130.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/TTJets_HT-2500toInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/2530000/51B8FADA-89EC-0F4C-9D67-74FEA37309CB.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/TTJets_HT-2500toInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/2530000/51C1D8D8-779E-574B-B233-ADAD4B4B9498.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/TTJets_HT-2500toInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/2530000/55F07655-169A-6D4A-AED7-2678AE13190C.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/TTJets_HT-2500toInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/2530000/56C2CFF5-4C47-2F45-8463-EFECDBD3FF0F.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/TTJets_HT-2500toInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/2530000/5B67704A-E6E7-9448-B140-76C885510A1F.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/TTJets_HT-2500toInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/2530000/68A8D800-F773-AE42-8A2F-8DB68242AC48.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/TTJets_HT-2500toInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/2530000/6A6505CD-3D39-7641-BCB6-29FD17E85AAB.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/TTJets_HT-2500toInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/2530000/7321C405-3AD0-314C-8FA2-43F0478B62C1.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/TTJets_HT-2500toInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/2530000/736294D3-8BF8-A042-AD97-156F64C29274.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/TTJets_HT-2500toInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/2530000/73A77493-58E0-6E48-8512-C5C35F756D8C.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/TTJets_HT-2500toInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/2530000/75A61BA0-B172-C84E-A0C5-319EC8FEF735.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/TTJets_HT-2500toInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/2530000/76E714F5-35C6-4E4A-9AAA-7EA948CC30CB.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/TTJets_HT-2500toInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/2530000/7B166A89-34F7-7145-9E5F-06973B9ECB67.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/TTJets_HT-2500toInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/2530000/7CFA68B9-1075-6B48-920E-ED0F4E948D5E.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/TTJets_HT-2500toInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/2530000/7F400D42-CE52-2341-9528-2482A05F6624.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/TTJets_HT-2500toInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/2530000/7F6200C5-9556-6040-A481-0F28DF131B96.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/TTJets_HT-2500toInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/2530000/7FDE304D-CEE9-D547-80AA-BA550D907B49.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/TTJets_HT-2500toInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/2530000/820BCF13-62D8-FF4A-8B0D-4F29E2411B07.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/TTJets_HT-2500toInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/2530000/85E1E106-EAE3-B64C-974E-188F5DD81510.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/TTJets_HT-2500toInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/2530000/8A59B0BB-5BCA-9A49-8F46-7306EB9B9183.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/TTJets_HT-2500toInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/2530000/8B50C956-B160-354E-888F-27BC5805A454.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/TTJets_HT-2500toInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/2530000/8DA712E2-805D-8E40-8B11-839FAABFAD88.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/TTJets_HT-2500toInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/2530000/93C99F06-2D58-CC41-B1A8-90029590F928.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/TTJets_HT-2500toInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/2530000/9AD3CE66-8894-E94F-ACD6-A14A5E743439.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/TTJets_HT-2500toInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/2530000/9E5A47C7-3043-834C-8584-F888ED1EFC0D.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/TTJets_HT-2500toInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/2530000/A11A600D-4CDE-924B-BBCD-9004C2C93CB3.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/TTJets_HT-2500toInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/2530000/A240516B-A257-7B49-987A-76EC81B269C2.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/TTJets_HT-2500toInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/2530000/A31ABD11-0084-1D48-A504-11C5E8C01F2D.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/TTJets_HT-2500toInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/2530000/A523A65E-5A6C-B040-B230-CCC3F0D1851D.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/TTJets_HT-2500toInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/2530000/A739E705-BF94-0E4F-964D-3112F4CAF8B7.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/TTJets_HT-2500toInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/2530000/ADC3111D-59AA-5440-A6DF-E6954CB59C6B.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/TTJets_HT-2500toInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/2530000/B0997757-8F53-E54B-ABB3-11F2914F9CA7.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/TTJets_HT-2500toInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/2530000/B3F524A7-3AA4-2245-8D85-D05ABDABAF6C.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/TTJets_HT-2500toInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/2530000/B5084B16-EEA0-724B-BF93-252381B96622.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/TTJets_HT-2500toInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/2530000/B54534E2-A024-FF4E-BA35-0112D93DCB5B.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/TTJets_HT-2500toInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/2530000/BE750D13-A735-5847-A190-9FBF8F6D8B80.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/TTJets_HT-2500toInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/2530000/BF82DDFD-118A-794E-8F5A-D7F37D08D3D3.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/TTJets_HT-2500toInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/2530000/C1A30D5A-F55A-E547-9C3E-D61727E8AAE7.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/TTJets_HT-2500toInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/2530000/C4E4FB84-E2B0-7F43-9817-60C9667FE6E9.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/TTJets_HT-2500toInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/2530000/CDA2137A-F383-8B47-8F91-A67C79591E9A.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/TTJets_HT-2500toInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/2530000/CEED3BDF-A9EA-B74C-A3C8-B20428A6FBF9.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/TTJets_HT-2500toInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/2530000/CF23F2B2-6664-E54A-B4F6-8780536D1A75.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/TTJets_HT-2500toInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/2530000/D24423BB-D078-3147-9986-4626665D61C9.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/TTJets_HT-2500toInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/2530000/D2AF84A3-22EE-C748-A327-1ECF52C231E9.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/TTJets_HT-2500toInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/2530000/D3294F7A-AD79-7341-B8A6-5E98E3ABA5E4.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/TTJets_HT-2500toInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/2530000/D3E9BA9A-347C-7D49-928C-E89F98AE7C53.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/TTJets_HT-2500toInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/2530000/D499302A-E23A-024E-B67D-C00D1C5DCC60.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/TTJets_HT-2500toInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/2530000/D94E29F5-67C6-C242-A924-453804379798.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/TTJets_HT-2500toInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/2530000/D9F53719-56E7-E240-BE8D-BCCE4C52C9B4.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/TTJets_HT-2500toInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/2530000/DA75C141-5B93-AE44-87BB-4C946D52FC1A.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/TTJets_HT-2500toInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/2530000/DDED2EF6-FD4D-E645-8879-D701DD3D4C83.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/TTJets_HT-2500toInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/2530000/E12007DF-6A9A-0944-AD61-6DC0AC601C1B.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/TTJets_HT-2500toInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/2530000/ED1A09D6-74D0-2D4F-8383-8B08F67A6F7C.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/TTJets_HT-2500toInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/2530000/F036DF50-B318-E64E-BAA5-E53751FEA118.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/TTJets_HT-2500toInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/2530000/F0B72D54-53B9-0E4C-BB3E-66B218E8952F.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/TTJets_HT-2500toInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/2530000/F0F74F7F-83A1-774B-A400-854696EE724C.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/TTJets_HT-2500toInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/2530000/F1DBE633-2CCA-AF40-8D2C-426ADC76CBBC.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/TTJets_HT-2500toInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/2530000/FA68C42C-C3C2-DF4B-A51D-19E92FA80BBD.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/TTJets_HT-2500toInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/2530000/FD177D84-C5AB-F74A-998F-21F7D1EB09DB.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/TTJets_HT-2500toInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/2530000/FD642B1E-2E75-DE48-8639-BDCADA56292D.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/TTJets_HT-2500toInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/2530000/FE3E56E4-03AD-BA4F-9225-38BF29330867.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/TTJets_HT-2500toInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/25310000/23911B89-4905-B542-AA8E-EF258CAAE316.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/TTJets_HT-2500toInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/25310000/8AA66653-2629-3145-A6C8-7AB7CB5A34A8.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/TTJets_HT-2500toInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/25310000/913FD0C9-9D7F-414A-A12D-1AB57F9F15B3.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/TTJets_HT-2500toInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/25310000/AA4EAEA5-5504-824F-A0A0-CED5A0D56121.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/TTJets_HT-2500toInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/25310000/B6EBBAD7-DCA6-224B-AE4B-8B79FAC9A1E1.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/TTJets_HT-2500toInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/25310000/E114640A-430F-334E-AE9E-BDEE2FA4A1E0.root',
] )