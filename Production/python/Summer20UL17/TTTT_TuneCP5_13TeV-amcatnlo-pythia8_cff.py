import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer20UL17MiniAODv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/260000/009A7544-02C5-CD41-8F95-4A1C073E81AD.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/260000/01088342-1D10-0440-B0F1-5725A4A11693.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/260000/010CF0A7-D334-F746-A838-FFC991838FE6.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/260000/015436DE-A910-5143-8E21-729309475E28.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/260000/017D4A6A-3FCA-2046-9F20-AD0D25A76990.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/260000/045A31AB-C4C0-F34F-B495-F8D905429E9B.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/260000/04B81232-226F-1B4C-926C-42162DF711B9.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/260000/0737C408-92DF-C844-9B83-D76557C456B4.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/260000/07DC76EB-31AE-E743-9E88-6FF9C53CF7B8.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/260000/08829FF1-D57C-2E48-8BAC-B612398665E2.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/260000/090696FA-BBD8-7341-9F5D-851479FF8524.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/260000/0C4EC6B2-8538-B74F-B280-2C5BF07900FE.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/260000/0D25A12F-5A27-2B4A-B255-10E6F5E72684.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/260000/0D459C7B-F5B0-194C-AD79-19E7C7B583C1.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/260000/0EA61FFB-3001-874C-9F5F-8A10D8ECD524.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/260000/0EC15839-2537-EB43-9FD6-B66B2BBC8246.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/260000/11A780E0-F8E2-9B42-A2FC-907B8A050687.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/260000/1220B948-D7CF-0944-8258-8E901CC97F34.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/260000/1436022A-7B17-9B43-B549-D0CA3DDCA160.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/260000/14DFBF36-A041-C243-96C9-FA225405CFB7.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/260000/14E42E5E-5D3B-C043-AC5D-6ED537841FC0.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/260000/1692B850-4CA9-6A46-A2DE-8CEE07782235.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/260000/1B3A51F8-B97A-3A4B-863B-32C7839AF6DE.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/260000/1CC95856-2785-D642-A2A9-20921BB0DE74.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/260000/1CF360F1-B9F3-D74E-90A7-3BC07D3E84DE.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/260000/1DF7B14E-62FF-E642-BBC8-FD93DA347FA7.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/260000/1E069F0A-7E2A-BC47-A5D5-25DB06278E87.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/260000/1E37C396-747C-3C4E-9996-47340D61A4CA.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/260000/1E6190F3-171A-F24B-A935-28B3A380A3EF.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/260000/1ECE46DC-AB7A-A141-A7B2-9C1F5EAC85A3.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/260000/20EFE7EC-1F6C-4C42-96F6-72E2EEE0B768.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/260000/21700608-D6E2-894E-9926-18D64A3EF3D2.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/260000/22F27B3A-F64C-7F43-A8C3-06AE52A3E3AB.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/260000/25FBE414-1AC1-9244-B15B-4BB799B0242E.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/260000/26795CC9-CD82-8E4E-806D-B0D8FFCCE54B.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/260000/26BEA57C-CA74-A34A-824B-D532D1A2DC4C.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/260000/26BF683F-1E6D-694C-878E-7E30ADF1B838.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/260000/26C9E268-046C-5E4B-9AC1-1530AFF1D21F.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/260000/2828047C-4B9D-A249-8CE7-2732C726EE76.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/260000/2882779E-2950-5744-BAE8-A87DF63CC292.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/260000/28A5E98A-DF3F-104E-8B3E-EF874195E076.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/260000/29B1F9C9-1634-B14E-B749-694B9D463694.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/260000/2A7A6682-151A-9C4F-81FA-84017AB8C2FA.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/260000/2B205D0B-066E-844E-8FA0-CC526B80BA89.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/260000/2B8EE785-D9E7-E349-874F-F43E52AEBFE5.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/260000/2C18ECF3-5F80-8D49-BBEF-4A974F3AE9B5.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/260000/2CB72714-7779-A245-BCFF-87CA2CE8542B.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/260000/2D82707C-05C3-2E47-A930-1428172FB882.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/260000/2DB537D8-AD37-6448-97B4-D777D6071812.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/260000/2EA68263-A93C-7C4C-AACE-6BED1ACE7F8E.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/260000/2FDCC12F-4345-1344-ACD6-877783CC01D1.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/260000/31052E95-F0E0-824E-8A6B-948A8B48B558.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/260000/31280AA6-FD5A-D440-BD42-78CED74D283A.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/260000/314452A7-180B-1C46-8D08-FBABA8C64301.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/260000/325596AE-17A6-014B-8D82-79B54D401D2F.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/260000/3270377A-0121-C84F-BCB1-333D74DFBA12.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/260000/33E41422-B733-974E-B900-8FE47641202E.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/260000/3642C8CF-C041-B84C-B4E4-8D2472405FBE.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/260000/368569DB-53EC-5640-BB66-525755D4593A.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/260000/372B5DFF-26B6-EC49-AE3E-B8921B8F1D8B.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/260000/37575431-535F-994E-BD7D-78060A6890AD.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/260000/3994D017-589D-3A4B-BB98-7A5ED1C1F261.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/260000/3C2B67D3-9504-E64B-84FE-1562CFF8ED55.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/260000/3DA32CBA-5D20-1B4F-933B-03349582AC86.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/260000/3DCD6DCE-D6A2-8C40-B5B7-9EA66DAC724C.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/260000/3EFDB95B-B28A-5C48-8D96-49D220534D38.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/260000/40285E1A-C550-1349-8D52-F11A32A34BB7.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/260000/40F96631-E34A-2541-9713-D9DCBB086EDC.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/260000/41A686E3-EC9B-A04F-9AB9-6E1092639EAF.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/260000/434E6646-6BE7-EC41-944B-64643FD42267.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/260000/46275D48-68C0-6647-A682-61F252AFEECD.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/260000/48024865-0EF9-2E4A-A8CB-95BEB21CE1BA.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/260000/4DCC5A7B-0C9A-8C4C-A84A-515BFC98D14C.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/260000/4E866E96-EE0F-7C4C-8A7E-D4EAB74697BE.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/260000/4EA0D4CF-03BE-884B-94E2-70078C6B6419.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/260000/4EF5D907-B485-7C47-841C-53D7A60D6C8C.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/260000/50700044-A0AA-C347-B6F0-E7EFB435AA74.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/260000/50F111EB-15FA-F84D-A305-72206227F0F4.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/260000/5219932B-3AB6-EC40-88E2-74D7B2CA92D3.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/260000/52288DD7-257F-BB41-98E3-5F68A89B7E53.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/260000/53101C99-8E10-5844-8684-7653AE262EBF.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/260000/5567D516-C80C-FE40-92E6-925CA5B503EB.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/260000/5569C982-4B86-BA46-BFE0-8C60AC14C460.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/260000/57867798-F298-F544-AFF6-5B0B69F2820A.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/260000/57FAF936-7746-F74C-BACC-43A38C117814.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/260000/57FFBC4B-63B7-974B-9B04-D2CD7DF4D4EE.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/260000/59599EEA-F543-E94A-90C7-FBF4526C87B8.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/260000/5BEC4B83-D848-2A4C-B3FF-93C3E45E0206.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/260000/5C8F1CF3-C0F9-1C48-B87D-B8CFB74DE107.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/260000/60CD3A73-0904-6D46-99C4-1F009FAAD4C6.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/260000/61848180-B7EF-EF4A-B58C-109B52CB6163.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/260000/61CBB9C9-2A01-D14D-8D19-4D0EF6EA6EAE.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/260000/61EB355E-D826-0749-B961-2915F3976120.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/260000/651CA173-31A3-FB40-891D-10F238D1D0E0.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/260000/65771A1B-5253-464C-84EE-F00BF8A78098.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/260000/65A1DE31-C3EE-6746-BF94-5D9754C7D4CD.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/260000/65B23FF1-E5A9-7945-9A63-E7926F6E1D33.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/260000/6613744C-E3F4-D047-B5E4-3998F4F0BDCE.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/260000/668808C5-31A1-D447-A33E-618202DCB91E.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/260000/67938EFC-9CD5-F242-8AC6-9E41F2C1D1AA.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/260000/68F25D11-0EF9-2A44-850F-4155B21FD99E.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/260000/69779DDD-A5A7-074E-807C-E7DA0A6348DB.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/260000/6A2EA545-1FD0-D64E-953C-726BFF3D062B.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/260000/6C75E9B8-0C1E-A34D-BE97-7A85C23FC003.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/260000/6CA8972E-74C9-6644-A075-6FCE29D9CDEC.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/260000/6D72506C-2AF9-CD4C-BDFB-BFE06FE39760.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/260000/6E493878-FAAF-3E44-A71D-EB43E73BC80C.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/260000/6EE5E7FF-B0AA-2442-A937-AA13B69FF10B.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/260000/7169A6FA-F7B9-B248-87CC-24F567FE537D.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/260000/71E0B3D8-3A50-1F42-BEAF-A9A69C669E9B.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/260000/751F0D2F-09E1-2C46-A155-9628A782A37B.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/260000/76521D52-9037-8443-ADC8-A4144E8EF64A.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/260000/7818B951-8957-6F40-8110-804C856603CB.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/260000/781A1BD0-8802-F84E-974E-D1C0BAD0A1E1.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/260000/78C7F885-F54B-144E-A4DC-1B9F241EF9AC.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/260000/7901D13D-1D23-5E4A-B7F1-A9A3618368FD.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/260000/7A7C4A30-44D2-F04C-8599-804925524BE7.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/260000/7B758C0E-74A3-5C41-8A85-1E52B7C2977D.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/260000/7C702B5F-F051-F741-A6A5-9D4B9BEF9D48.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/260000/7CC09897-19F9-9544-89E1-72529996721A.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/260000/7D29E585-512A-A24F-9A82-FD83518E8EEE.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/260000/7DB51176-950E-E946-BA92-3A51F95D8CEC.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/260000/7DB885C3-2776-DF4C-8D2E-12049517683B.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/260000/8321CE57-0446-D541-B20F-B16254214597.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/260000/83AF0744-689C-6441-BA42-58A104B728C9.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/260000/8B0B5577-8ACC-884B-B1EE-E4801445B043.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/260000/8BD256F2-60C7-CD4C-AFA2-46FBEE7796DF.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/260000/8D49AA90-3642-1B46-B18F-1F1AFF53236A.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/260000/9003F9C0-DBB4-AA4E-893B-2F51F107CF54.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/260000/90303255-A641-9343-8ABD-5A12DEFAF74A.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/260000/907E36F0-7095-494E-A11E-C1B81D9DE646.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/260000/918491EA-0BBC-FB45-91FF-DC56674405D5.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/260000/918F3201-F4FF-D44E-93F9-070301BC95D8.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/260000/921798B0-3755-3F47-AA28-6B378B9D14DA.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/260000/94CE6EC9-ECC2-7546-898D-A92EA41D20BB.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/260000/959FF355-31DC-F24D-8B3D-C6D945D547BB.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/260000/95D61809-5634-D345-AA20-207E1AFFFCEA.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/260000/97065694-AF79-0649-909D-F10AAE1E792C.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/260000/97F43BA1-5FB8-1E4D-8155-070DA63D84B2.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/260000/9B46F7D7-03EA-A944-A977-435ABD18DEF2.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/260000/9CC25D85-52F2-514D-A38D-BBB830D097E3.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/260000/9ED30DE8-DCF7-7D48-9271-D4B1E1BA2A6F.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/260000/9FC27EB2-7388-6245-91C2-3E3D6BEB48EE.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/260000/A11C0AEF-C7DF-F843-8AC8-017BA50E64EE.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/260000/A127DEE1-BDF1-2347-BE73-117B5CC32852.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/260000/A190642A-3325-0643-AC79-FFA7F502D69E.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/260000/A40855D3-FC30-5A49-9A0D-B005FF929F3B.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/260000/A5F192E5-E172-2842-93F5-5EE8153FCE01.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/260000/A6A0ABF1-1349-204C-8B24-E5BBB08055AD.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/260000/A6A1F76C-CAEF-1E4F-80BF-46AA2F76A51C.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/260000/A8D559D9-15B7-8A41-915A-A89A05A676C0.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/260000/AAD63E45-DF42-804C-843E-7AF4A22AC332.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/260000/AF6B0613-8D68-694E-B407-23F7F4769CE8.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/260000/AF83263B-AF08-6945-9AF2-61F4416B02F0.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/260000/AF9EF40F-F5D6-0E48-8F07-408E2E701908.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/260000/AFEC1058-06AE-624C-8F50-9CC4B6C48157.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/260000/AFFDFE0F-4840-EA4C-859C-C247EC8D2AC2.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/260000/B12EBD97-50A5-BE4C-ACD5-029B13AC1394.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/260000/B2C7307F-F05A-9748-B1B2-2027C731E54E.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/260000/B6F841DD-1EE4-8C46-85F3-419AB5797CA8.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/260000/B7DD9A60-391D-3440-AA1B-13F79F7FCE26.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/260000/B91D547F-81EA-E74B-8557-8D5696E8E542.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/260000/B9E55A51-D3B9-8F44-8F05-D428E9ECB134.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/260000/BA9FD432-225A-0E45-990D-47920C67D8EA.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/260000/BBC990EA-59F9-6444-BF62-4FA90D77E907.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/260000/BD151E90-385A-6C44-9B6A-CC7D65A844FB.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/260000/BD5A7A74-AF40-D34E-A25B-E275AAA3B726.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/260000/BE439AC2-F8EC-0C46-B275-4552BC5F43D1.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/260000/BF40BB69-4772-7C4D-9C43-9CA61DBA5426.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/260000/C1886005-5473-CD49-8B51-A2056FC45153.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/260000/C3295A05-643A-4345-AEE4-C54383B671E1.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/260000/C46036A8-FEF3-7C41-8821-25E3F6E6F19A.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/260000/C54E146D-FA05-B343-8DF9-20F27D6FFD0D.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/260000/C5752C09-5DF4-454B-99D1-8FF858BBD9F3.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/260000/C7E022D3-D6F0-3C48-A4A2-CA1F1CDCEB5E.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/260000/C82A7875-11F7-E047-97ED-499F64801C38.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/260000/C960A21F-A540-C84D-8EEC-FF727BB91BC0.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/260000/CDF4694F-3C63-AF40-9F45-10E7D28D1220.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/260000/CEBCB69A-F01B-C84D-AE08-F00FFE265F7C.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/260000/CFDE2FB8-7DDE-564C-AF4B-3DFF9C7933CB.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/260000/D3132F91-550B-1A40-A550-34674DF9FC20.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/260000/D429B4F7-A857-1C4B-A20E-791D0C1D9D5C.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/260000/D7147373-ED95-4D44-A9FD-E952C9996D03.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/260000/D87E396F-F302-A344-A1CB-AF654875F8A7.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/260000/D96F4AE5-7402-5B48-B6C5-E6D25C6A40E5.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/260000/DD3FCCDB-3980-BF41-BC40-A00AAB5F0C0C.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/260000/DE41DD9F-67AA-4B44-BF2F-334FFFDA4470.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/260000/DE858F45-2584-B64C-A430-8D12A14F306E.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/260000/DF3A5827-966C-7E41-A731-1D4F7A3E9416.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/260000/DFE744B9-1C4C-C04C-B7EE-6218D5874D00.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/260000/E18A2A18-3B15-2C4C-90F0-3ABFD6816280.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/260000/E1C5CEA9-D18C-5649-810B-EF12404A27CE.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/260000/E45B2E39-019C-FE45-8B0F-C978F980004F.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/260000/E515A779-DF24-6E47-95F7-B8DB87135B6B.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/260000/E8412535-F067-3A4D-AA3F-CDCD4AA30B47.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/260000/E85CA5A2-F5DB-E640-8C84-9733C598F670.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/260000/E86C057A-D588-C645-9B85-3AEAD88EAFDD.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/260000/E9809F52-9516-294C-90C3-189DE555DDE6.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/260000/EA95EA50-993D-2142-B9BA-1B467A0528C7.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/260000/EB368623-5B42-1A41-9D06-D5C4C8D8A2D3.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/260000/EB74D137-6854-904F-8E84-19AC0E95249A.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/260000/EC160E8E-1A24-3E4B-A20B-9F7A5FD78AC3.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/260000/EC776D1D-D4BE-F84B-BE3D-AB02505657E3.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/260000/EDE28060-335B-D94C-9A0E-F99FEA61324D.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/260000/EE527036-2B4A-F249-A57E-750E706F9811.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/260000/EEE562D0-E230-DD4F-ADBB-B512C5CE403F.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/260000/EF9B9F56-C63B-274E-91B5-CCBEA4F7A879.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/260000/F55D01F2-EB73-2545-98A3-252AE1880A2B.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/260000/F59DFFE0-058F-BA4F-8E51-5179D86C3F53.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/260000/F7016006-70BF-AE4D-AF85-87100E69F509.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/260000/F760C31A-26E1-344D-9237-BF0658C5A5EB.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/260000/F79EA37C-47B8-744B-9CAA-639E5D971E97.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/260000/F7BE3802-C186-7C48-A767-F9D999719E2B.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/260000/F7C7FE15-81A6-7A46-A4BC-03CB4EA0C530.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/260000/F82C79B2-8F52-1546-B2F5-AFB912EAC3AB.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/260000/F8D6B2F5-34D1-A743-A303-026198223E9D.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/260000/F93D9FC3-476F-254B-9E14-82179A4FD4ED.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/260000/FAF6DE83-57F9-2646-8584-B37C5A67A65C.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/260000/FB3EF218-521B-D84A-9B8C-776F7201D832.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/260000/FC2793EC-C078-014E-B795-860470F97F4C.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/260000/FCCF419E-658D-2C4B-BE59-C21F7DAA5E5C.root',
] )