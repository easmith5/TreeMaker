import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/130000/20FCC60D-CE42-7748-A59C-9F51A2A55992.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/130000/5C694CA1-4CA9-F347-A759-384F1407F1F9.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/130000/60B9F706-A431-5346-9961-8E322DA23784.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/130000/77F3C73F-C0EC-8343-AE42-3EEB30077BC1.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/130000/7A82EFE0-B86E-9A4F-8780-27542985F644.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/130000/BA455A09-4DA1-9C48-A91E-7D58EAF87D70.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/130000/BCFF09B9-464E-3945-BDF8-24DBDBC8F353.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/130000/BF1CFAC6-AD93-3048-9F16-F5F2441604C3.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/130000/C81AAE3C-320A-C14A-9DC2-B5ECDFCB765C.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/140000/0239D79A-19C3-E240-A98A-2E671769942E.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/140000/02FA229D-A63D-484F-AF03-58073CABF6D4.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/140000/074C60B0-6849-8640-897F-0ECE72A1F3CB.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/140000/08FCB756-89B0-9247-A5E2-1E7D9646F8DB.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/140000/0AD01E76-920D-E24D-89B9-10793D7B077D.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/140000/0CF06173-2F83-BA49-A7D0-B50781453D52.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/140000/0FDDE553-9EF5-8745-98B2-9011D691C75A.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/140000/10DA9099-12B8-4244-BA03-0DE2FC7CDF24.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/140000/1215CAFD-FD4C-EF45-8FFE-4E8E770372FB.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/140000/176D9701-3CC9-A540-8206-FAE2AA1DB4E9.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/140000/19AB1613-CE17-5F41-AE61-315D13077A6F.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/140000/1D0B96B4-6833-654F-8ECC-16062B425077.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/140000/1F513BAF-7084-F047-86BA-9F3B38432389.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/140000/1F52A09A-F8EF-3140-8D21-ED1CAF44049D.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/140000/214E9197-80CB-B14A-9750-2C76377A69D3.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/140000/23384688-FF88-6C4B-9523-6D0E76C9D8B1.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/140000/31C50DD5-BBEA-324B-A189-576444EAD1F4.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/140000/34A07FA6-F0C8-5E47-B06D-CB9624F0AE01.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/140000/34D40C17-250E-544B-8E3F-BBD0D6AD40EA.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/140000/371BE47F-EFF4-F24F-97EA-B90073929DED.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/140000/371CFA4C-D85D-5844-9624-A1DF2499E51E.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/140000/3B918FC0-4ECD-064F-9912-4D42A1454936.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/140000/3DF7FDC0-6904-8D49-815F-E50E423DCD8E.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/140000/3E8B7881-3C6F-EB45-990B-204ACF683859.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/140000/507CD56A-D5F4-B44E-9BBF-25195A25D528.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/140000/514CF6FA-64D7-7845-BBF0-067E7191BE93.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/140000/5371ACE1-4C56-8140-8BB6-C6252EAA450D.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/140000/58EC6C4B-1F53-114A-926C-8BED47D4D776.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/140000/5A15D681-18DB-2646-87EB-0EEA077FF211.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/140000/5ADC05CD-4D6C-DE48-B23C-4C753E2353AA.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/140000/5B2F0963-4DC9-3947-A545-DCBBBC4CE371.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/140000/6EFEDF60-5680-8043-92F1-540D25C4557B.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/140000/7055A11F-5714-4C4A-89AC-5CB94A764BF8.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/140000/7713EAF7-AB6A-AC43-BDF4-27E5B5FCAD7F.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/140000/7907C7FA-C31A-0646-AB30-82C684A5F909.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/140000/7CE5ECA0-82CF-6545-8081-05C6A6F93116.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/140000/83DDF276-63C1-354F-B269-379B9E619030.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/140000/85202D4D-DDE1-2E4A-A23A-632B1B2576A6.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/140000/8ABCDAEB-0E33-7844-8018-26831FE00084.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/140000/8C1EE299-E0CF-014F-A406-80BD29C2C50F.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/140000/8CF0DDA0-C73F-7940-8D03-9227B913164F.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/140000/8EC15198-501E-C646-BD8A-2D3192CFACE7.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/140000/9360D67E-328E-5F4E-95ED-C4235C40CD0F.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/140000/946AAB84-74F1-B143-B49F-D5AFAC44481D.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/140000/9793CD98-4EBB-3D4F-812B-808F9E534FB9.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/140000/A17AE19E-1794-A144-AAFE-55A931D6E9DA.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/140000/A543CDE4-46D0-9445-BCA8-A4A84F2320C0.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/140000/A6CDF838-ABC1-D44E-BD8A-17E50548C72C.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/140000/AA6487C3-E67F-9B47-A258-F9807F5B4479.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/140000/ACD4F4AD-A61A-9F4C-84DA-C7B63F5B64C7.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/140000/AD14863B-F212-DC43-B7CF-8C34BA5F508A.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/140000/AD827652-D981-6546-BA7E-59ED2E8303BB.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/140000/B38886F4-F159-2344-8338-E07EFB2F49B4.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/140000/B5AB47FE-92D2-C946-8B06-60D3FEC3F4F2.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/140000/B786C1AB-830C-964D-B297-9CFED3D873FA.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/140000/BB1BBCF3-E1B8-4C4E-B952-BF8C1A69A764.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/140000/BE2B0D21-B977-B244-9DCC-42AF87F2F554.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/140000/C023B678-BEF1-C541-81C0-B1DCB7BF9483.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/140000/C77CFBEC-B209-4245-A151-26AB04B5CFF6.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/140000/C8681EFD-85DA-9149-94A7-E82DE31281A2.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/140000/CB691282-A9E1-754C-B66D-CF59A600B390.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/140000/CE715E7B-5620-224E-9B4F-4E91BAB73760.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/140000/CEA843B1-A83C-444A-B5E5-341FD2CBD59E.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/140000/CEC9787D-E6B6-614D-8EF6-935D99F80716.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/140000/D216A6AB-03C7-1044-BD32-E0B87426C764.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/140000/D6BA20BC-D7A0-4046-99D2-D9472623D279.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/140000/D8544B11-9ADE-ED48-A911-B4A1310C8660.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/140000/D8F20A03-0439-F148-A103-FBCAB4FEB167.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/140000/DB38D085-22C6-054E-A644-C1FF5E29230B.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/140000/DD41C30C-54B5-594B-8520-121F1224B60C.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/140000/DE3B2CF4-C916-3341-8A79-E41718AB3B7E.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/140000/DE7B60A9-43E2-FB4E-8A5C-8B094FA783E4.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/140000/DEC13515-0AF6-9644-972F-3516E846286B.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/140000/E1375911-E8B7-FC47-A4B1-A34309416628.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/140000/E338ACD6-DC7A-CF48-A93B-B82DBABA49A5.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/140000/E492058C-440F-E444-85DA-923AE9AE00A6.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/140000/E6D6B4AC-44F1-4A4D-B2DA-36A79ACBC87E.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/140000/E7B995C8-01B3-114E-9610-61E535A18DE6.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/140000/E8FF9D6C-E3E4-B14E-B2A5-A305CA0FBB50.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/140000/EAC122FB-C974-4345-9FE5-B0B3D84CEE07.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/140000/ED31A2FE-3D4B-AA45-9627-E5F073C0CA9C.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/140000/EE1C387E-E522-5E47-AFC5-44827BB3AC4D.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/140000/EE33B487-3493-8D4C-8D07-04022352B132.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/140000/F1F45462-C8D4-534F-95A6-958A33DB97E5.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/140000/F69F5DD7-E3E4-E54D-B4CF-9DB40E9DEE47.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/140000/F79C41C4-DEC1-2447-B302-D104872C1046.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/140000/FB3140C6-6695-584A-A450-70EA68D6AF0D.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/140000/FBC62666-7DBD-BC49-8E64-A2E897BA2586.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/140000/FCE7304F-7CA6-C34B-84A5-B42A9A587FB8.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/140000/FDD98458-F702-C74A-A89E-DF861EC58836.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/140000/FE6AFB16-D349-2248-B20C-823380AE5296.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/270000/04BB9A0E-3250-4543-8FE7-9E2AB696DCAB.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/270000/0643C38C-7658-AA4D-9843-FD6E1490EFFF.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/270000/0A46C847-C814-DD46-BADB-5F1782A372EF.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/270000/0EE4A5FD-3F8A-7743-B055-EC050EDC0A44.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/270000/1C09963D-3859-464D-AA9A-D54C30769D97.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/270000/1DD251B4-4200-324B-9E8D-FCD06EEF454A.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/270000/1DDD3823-1ABA-FA4A-8DED-9A671A17B2F1.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/270000/1F112BC6-7309-034C-AB01-CE2B2D504EB3.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/270000/221D7F53-5DE1-E544-8AF9-2E0D3749E5D4.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/270000/2309FD94-B795-6146-A69E-3DEC5D6A8095.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/270000/2A218779-841B-D74B-8CD4-76AFB695FA39.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/270000/2A6A4C64-7D92-4545-8A5C-6AD8C621B1B0.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/270000/2ADAC05A-0AB9-BC45-8E1A-8B41252BC3D2.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/270000/319AB5F8-4898-2644-A023-425593A01D23.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/270000/37174825-70F0-4542-83D7-0B54AE5DF0FA.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/270000/49BDC687-24B6-1141-A72C-C826F529FBFB.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/270000/566C7C4A-2A96-874F-AB9A-3AFE30C04F90.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/270000/5895A338-8E11-9145-B5AA-673F7D816414.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/270000/5A4D2292-523B-C940-B566-C8053DA757AF.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/270000/5BD1862A-E9DA-8740-ACB6-ADB63B2D184A.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/270000/5F9DDE4B-78CA-4241-9532-29AC166C0758.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/270000/661DD7B6-CF85-7F47-8DB6-AE40A03D4418.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/270000/68647BD0-891C-6743-B4CA-D2D231CD4289.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/270000/6CD87E89-CAFB-F34E-A373-BA44B671B8C4.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/270000/6DCC6D4E-2CEC-AB44-9DC2-46502C8E778A.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/270000/7E481028-A402-4642-9ED3-12A9D934CC47.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/270000/85B7AD9E-E8ED-B042-9299-25006A3A7C90.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/270000/8CA09C1A-7085-F541-B65F-6631EB361209.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/270000/918B3F69-43A6-A942-BBD3-F3C6C4288404.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/270000/99278823-2D64-A94F-980A-BCB81B486EDB.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/270000/9D8E083B-D15A-E647-88D5-4D8FEC5D83C8.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/270000/A3278F99-2809-AA45-ADD2-6F6044796232.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/270000/A7F4358E-B8A3-E04D-A17C-265DEB82414F.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/270000/B9062672-327A-2043-9089-99B08353E5A4.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/270000/B9A3AB53-8F45-F045-A70E-05AA79C4E379.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/270000/BA510C72-A316-BE49-AF52-70239BE2EF5E.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/270000/CA836B89-6038-7745-BA46-71372505B1C7.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/270000/D9F9418F-A0AD-4A40-98AA-B758F58CD7C8.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/270000/DD51F46F-EEBD-A148-9C23-8B3A9A5D3051.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/270000/DDDFB68A-D2C9-E84A-8B18-0FEE7AB415EB.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/270000/DE1C17E4-C293-6749-8102-BF821525A1E0.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/270000/E5E24647-ABCA-864D-8A7A-2752420ED979.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/270000/E951912F-856C-EF4A-AB09-A04617747552.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/270000/EA61087D-AFB1-AD49-ADDD-66A281BC4EA3.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/270000/EB986119-1E42-7B4D-A71D-AC2DE1D51125.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/270000/F20195D5-5027-D944-BE56-26629581E9D3.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/270000/F312494C-F166-6344-8FF2-9E1EA4BC44CE.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/270000/F645AE89-7E77-1144-9E88-5881C3307D09.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/280000/0104ADF0-20DC-A64A-B20F-2A4D2A826DCB.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/280000/0DCD5FE5-7712-B047-918E-8166F6C3637F.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/280000/23ABA937-1BFE-D54B-9FFF-E22399358DBE.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/280000/57049A4B-DCBF-5544-B965-8E6B950FAB9B.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/280000/5AF2F0D4-5DAE-5846-AE17-11C71B632556.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/280000/67D88280-51B9-9B4D-8DF4-8F6C5549C20A.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/280000/927568C6-E233-2343-BDDF-FCA91E13249F.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/280000/9FAEB9A8-2E04-7F4A-A464-3A64EA28952A.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/280000/AB981633-3F4E-9F45-9A70-94247292F15C.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/280000/AE91C006-9604-9749-BD5A-0C850FE5C089.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/280000/CC131589-97A6-9143-A4FF-EE701F51BCA3.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/280000/CE3B1BAF-8563-4F44-9F81-5CEB40948F78.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/280000/CF93CC84-019A-DF46-857A-DD0207DF9B7E.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/280000/D885FA33-BD0E-044A-A383-EE97D064A8B9.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/280000/F394AF59-992A-8F48-881A-C7121CF2A43C.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/280000/F8C38F10-257D-4D47-96D6-5278D90E5277.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/70000/5238690E-8861-6E45-890B-CB2B474E1E8E.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/70000/6B8B9E34-FA08-A540-A695-EA80305060F9.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/70000/FB4AFC5E-B4A4-A641-B28F-7BEE26A45833.root',
] )