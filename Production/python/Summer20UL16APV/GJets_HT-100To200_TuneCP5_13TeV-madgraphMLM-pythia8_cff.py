import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_preVFP_v11-v1/120000/084D89AC-718D-1943-BC90-56BFD9EC12EC.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_preVFP_v11-v1/120000/0C3E0177-035F-4140-8804-8A1861A802BF.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_preVFP_v11-v1/120000/346D8573-C62E-9446-82AC-24C9CFEAD5C4.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_preVFP_v11-v1/120000/367AC550-C5B2-B840-9203-8470EBB567D5.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_preVFP_v11-v1/120000/4149A108-74BE-3548-81A5-253792478798.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_preVFP_v11-v1/120000/43D87FEF-8A11-E44C-9F08-4C00BD43DAC9.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_preVFP_v11-v1/120000/5935AEF9-35E2-D245-AFEA-D033E0B9B9EF.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_preVFP_v11-v1/120000/5A70FB5A-0C3B-3048-B4D7-CE5EA21CAD05.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_preVFP_v11-v1/120000/6B0C4ACF-5F80-4242-848B-34B5145EEAEA.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_preVFP_v11-v1/120000/6FA871E9-BD74-0145-B941-6E43EFB42F2F.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_preVFP_v11-v1/120000/7D3F9F94-9959-7743-B87D-7697FE45485E.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_preVFP_v11-v1/120000/7F188440-7529-AC4C-928C-01E930B4CB42.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_preVFP_v11-v1/120000/8D1481F0-35D6-2845-8EF3-CA1DDA1C1E75.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_preVFP_v11-v1/120000/9371AB8A-80F0-B247-9975-E2C3E0FBDDD2.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_preVFP_v11-v1/120000/9E42E68B-FDD5-034C-8F7A-4A592CDDBD66.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_preVFP_v11-v1/120000/ABC281B0-E13E-6840-BECA-658D7D4BBFD2.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_preVFP_v11-v1/120000/AC4A0D46-90E1-3349-951D-AB9349383A60.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_preVFP_v11-v1/120000/B6E1C946-A6B2-6F45-96F0-98293248CD31.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_preVFP_v11-v1/120000/BF836DEF-6DA8-1941-AA1E-AB9C8831419B.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_preVFP_v11-v1/120000/C95CA3CB-ABC2-114F-BF54-454961AE5764.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_preVFP_v11-v1/120000/DA11782A-9712-3B4B-BD5E-52940121F387.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_preVFP_v11-v1/120000/DDD9DFB2-28D7-8E4A-8FB8-E3C5490386D6.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_preVFP_v11-v1/120000/DE11D1DE-15FF-D24F-AAE0-F1E902705670.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_preVFP_v11-v1/120000/EB5C2E30-B743-604D-8C10-A94152D99A76.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_preVFP_v11-v1/120000/F0E2CD31-B7CF-B847-9A72-2E4B1A318705.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_preVFP_v11-v1/120000/F1462FAD-24A0-544A-8129-77A3A6F5C95B.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_preVFP_v11-v1/120000/F49B75DA-ADB7-6342-861A-BD8DAD0376F8.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_preVFP_v11-v1/130000/01B80EB5-9E6D-6F4A-B129-BFD2EEC3CCF8.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_preVFP_v11-v1/130000/0407DC43-3755-8044-83E2-67FC408FC480.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_preVFP_v11-v1/130000/0611078D-C523-AB46-B6E7-75F50FC52506.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_preVFP_v11-v1/130000/0F2BA227-3D92-F944-A878-6A037B3DD50B.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_preVFP_v11-v1/130000/1C52451B-B476-A84B-AF4B-80AE8DF2B57D.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_preVFP_v11-v1/130000/1F7B5A9D-84B2-4849-B228-EDB107A5F691.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_preVFP_v11-v1/130000/2293152D-2AD3-304E-8505-FD55940E27CB.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_preVFP_v11-v1/130000/2945558E-B256-594C-8102-1203AB62EFF6.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_preVFP_v11-v1/130000/2CB031FA-B5D1-854A-9AF8-DBBF31054B05.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_preVFP_v11-v1/130000/2F6B6BEB-E3FD-CB4C-8C84-A4150F33ABB8.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_preVFP_v11-v1/130000/37D3DD9C-81D2-064F-BF75-55600C2069BF.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_preVFP_v11-v1/130000/39BCC209-C2CB-A947-B207-AEA3AD3DF7DD.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_preVFP_v11-v1/130000/3EC6FFB2-DD67-F04D-89A6-D0B2D33B118A.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_preVFP_v11-v1/130000/460A768E-C0E7-EA4F-BE6B-30EDD3B6D896.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_preVFP_v11-v1/130000/47420984-7E85-8B45-BB42-1C8E363C54C0.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_preVFP_v11-v1/130000/6A0FD006-0369-534E-9B8E-2373E2B5FAB1.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_preVFP_v11-v1/130000/6BEAF208-2AF5-1447-8BC2-A63955972F1A.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_preVFP_v11-v1/130000/70777DAF-A757-1045-8BC9-10D06CDC0C98.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_preVFP_v11-v1/130000/842F7CC8-E88B-4F44-8ADC-8B16256C1FFD.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_preVFP_v11-v1/130000/90566B05-7339-D84C-9623-30567AB6215D.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_preVFP_v11-v1/130000/99E2BA33-BE54-8E40-8E0E-9B2B1964B20C.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_preVFP_v11-v1/130000/9C3A9350-00AD-5049-B976-61064C6B126E.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_preVFP_v11-v1/130000/A11A338C-423D-B343-BD7A-2FD06BB904A7.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_preVFP_v11-v1/130000/A59DDDAD-9817-3542-B562-821C7C5200C3.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_preVFP_v11-v1/130000/A7662CBC-40A4-2E4D-BBDB-7E45C68A427E.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_preVFP_v11-v1/130000/AA025AD4-DF05-4741-83B5-2DA2DCEB5141.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_preVFP_v11-v1/130000/AA240280-4160-A649-A82F-7C50B411A861.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_preVFP_v11-v1/130000/AD50FA4A-F3D7-2C4F-9EC9-D5A9F9BD0603.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_preVFP_v11-v1/130000/B18DFB81-297C-2840-9790-C1A4795A2727.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_preVFP_v11-v1/130000/B18E6EDA-E864-AF40-8646-1908665F68F4.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_preVFP_v11-v1/130000/C34D085A-3EFE-1642-8045-70804E046BBF.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_preVFP_v11-v1/130000/CEDB3C92-06F4-B64A-B34E-FBCFA064B188.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_preVFP_v11-v1/130000/D2FB24BA-AD35-F242-B8D5-5BB6FE99F59D.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_preVFP_v11-v1/130000/D98D1EF4-D2C5-E343-9A31-8BB3F61A921A.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_preVFP_v11-v1/130000/E49AE911-0937-2444-992E-D6163BF83508.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_preVFP_v11-v1/130000/E634A53D-1E53-E047-A8B6-88BB47FF937D.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_preVFP_v11-v1/130000/F1E96176-80C6-BE40-B9A2-9DFBFA510FF9.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_preVFP_v11-v1/130000/F268318B-90A3-AC41-884E-41227B28D202.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_preVFP_v11-v1/130000/F5CB1A07-CF78-DD43-9C00-43471233CF18.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_preVFP_v11-v1/130000/F7AAD0B1-00EE-7C40-83BC-00302F6FC268.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_preVFP_v11-v1/130000/FBEE4EB4-6B4C-1D4B-9664-FDE1CCD41B77.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_preVFP_v11-v1/130000/FBF3731B-DF2F-D145-8EEC-EA484E758F41.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_preVFP_v11-v1/140000/2E692B0B-F85A-E147-A1FF-77A6846301A4.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_preVFP_v11-v1/140000/2F9C9AF4-CFFF-804C-9303-B415A86EE366.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_preVFP_v11-v1/140000/312E3BC3-9FD5-C447-90FA-B64693E8C015.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_preVFP_v11-v1/140000/31D37711-6038-754D-B83D-AC9420F3AB39.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_preVFP_v11-v1/140000/44DEA2C5-61D9-4D42-8A8C-220FF5C3854D.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_preVFP_v11-v1/140000/57D8ABAC-F275-3047-98CC-81A73380AB64.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_preVFP_v11-v1/140000/5F6093D6-009C-AA47-9BEE-AD1CBA9A9410.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_preVFP_v11-v1/140000/6A09889C-C1BE-BD49-A936-42A0C218B3CA.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_preVFP_v11-v1/140000/72E2EB87-2D19-9645-B465-1B0BD44FF80B.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_preVFP_v11-v1/140000/9BA8695D-ACFE-0D4B-A6C9-EA1D60CF2116.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_preVFP_v11-v1/140000/A0B0890A-51E5-8A41-AA1E-9C61FBF1D410.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_preVFP_v11-v1/140000/A766397B-ADF8-6D46-926C-137077065AB9.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_preVFP_v11-v1/140000/AD007C97-82BE-AD40-9928-F07350C73167.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_preVFP_v11-v1/140000/C054DB7E-ABA9-3D4F-B6FF-8D7CFF6FBB77.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_preVFP_v11-v1/140000/D2DF34AF-A080-0E41-A91E-694A69FB6557.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_preVFP_v11-v1/140000/E7D8A359-761A-8C41-BFDC-7D4186A34AC3.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_preVFP_v11-v1/140000/FD8168FA-543D-C54D-842B-82CB71D08B98.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_preVFP_v11-v1/270000/0D647D98-AEA7-A742-A24E-9686021EDD76.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_preVFP_v11-v1/270000/18FEC27D-31EB-8845-89BA-DA7B8B0C56A2.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_preVFP_v11-v1/270000/49BA2B8B-58B4-1148-AE63-E3ADF3367119.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_preVFP_v11-v1/270000/4CCC911E-B196-6B4E-9296-0F76CC6AB4D6.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_preVFP_v11-v1/270000/52E3AB76-D31C-BB45-B151-568311037345.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_preVFP_v11-v1/270000/898F4511-D430-084D-B005-676A397C9398.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_preVFP_v11-v1/270000/B26C2F30-4179-3F4B-8F92-E6BBD3C91A48.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_preVFP_v11-v1/270000/C06EA53C-DCAE-B445-A924-F46183637F13.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_preVFP_v11-v1/270000/CF701278-DE5E-5947-96B6-CE0C1A4175C7.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_preVFP_v11-v1/270000/D6279C33-3902-3A4E-BD11-C816676A1E6B.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_preVFP_v11-v1/270000/DE5C4C1B-3831-B140-886F-282D35F42E92.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_preVFP_v11-v1/280000/02B30D7A-FD85-4447-BC05-3F1E2E50A0AD.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_preVFP_v11-v1/280000/035406CB-EA96-8741-BF61-B6D5B16404D5.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_preVFP_v11-v1/280000/0B568010-4251-7A47-B7EF-954C00BF53DC.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_preVFP_v11-v1/280000/185EEFE5-9FD8-FB4C-9DD3-1D874C8F4B93.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_preVFP_v11-v1/280000/2464A8E4-7E82-BD48-8C4A-9C0D1A82C03E.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_preVFP_v11-v1/280000/2D464B75-6F49-C746-9D62-A741FB94C21B.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_preVFP_v11-v1/280000/442CECFB-640A-BC42-ABA7-7F15D7E5F585.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_preVFP_v11-v1/280000/4AD9EDD5-8945-5044-8B0F-154F4AA1DC14.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_preVFP_v11-v1/280000/56C57A2A-C29C-0E4E-BA7E-A280ABC53CE9.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_preVFP_v11-v1/280000/5862D2DA-A228-2341-9930-4951A737F384.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_preVFP_v11-v1/280000/5E3DFB34-13C1-6245-A0F9-9B923AF35243.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_preVFP_v11-v1/280000/64E03C36-CB43-7B44-A35E-5B59828C5B97.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_preVFP_v11-v1/280000/6832A52F-B185-3147-97BA-785903ACE8BC.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_preVFP_v11-v1/280000/71BD2DCE-6E8C-A74C-9F5B-B4ABCF4AC3D3.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_preVFP_v11-v1/280000/73AB6F7B-4D57-AF41-8467-CBEB827A98B8.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_preVFP_v11-v1/280000/7D6F76CB-73E4-4D49-8AEE-DF330B80D6CD.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_preVFP_v11-v1/280000/7F2847A0-E052-B84F-AF71-A5A6F3A7B65A.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_preVFP_v11-v1/280000/87869174-6A85-814B-BD29-BC287E3CA60D.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_preVFP_v11-v1/280000/8EAEC10E-2847-BA49-9B01-573E67739DFC.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_preVFP_v11-v1/280000/98913169-7FA3-5145-BAE3-10D42BC72999.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_preVFP_v11-v1/280000/A3CF8357-5805-D747-94B0-1FB77465F26A.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_preVFP_v11-v1/280000/B39321B2-10E1-064C-B8EA-7C01BBB842F5.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_preVFP_v11-v1/280000/B59C0BEF-0F17-454B-B4EB-8C2C5CB28D14.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_preVFP_v11-v1/280000/C3B9C00C-D26F-4A4A-95AC-FF0EE86F3559.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_preVFP_v11-v1/280000/CD371A62-E2D3-1347-9BF9-81B96B6F5CD9.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_preVFP_v11-v1/280000/CE074E25-901A-F74E-BE54-9B153D1507C5.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_preVFP_v11-v1/280000/E1739DDB-AE55-344E-8EC4-0E52D63427D2.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_preVFP_v11-v1/280000/E5BF1F7B-2D9D-EA46-96D1-CB519CC8803A.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_preVFP_v11-v1/280000/EAB91F9C-8070-354A-9AA4-2B5BC33E4B09.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_preVFP_v11-v1/280000/F0828F1B-F123-2D4D-9782-341ECDEDFA0E.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_preVFP_v11-v1/280000/F61DF835-FF36-524B-8B4B-564F054ABCA8.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_preVFP_v11-v1/280000/F6E6BE3A-BD84-2B48-9F9B-402E3179EDD3.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_preVFP_v11-v1/70000/02D99C7C-F291-1A45-B91E-9E927968E0FC.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_preVFP_v11-v1/70000/0387AD2D-9CF3-C943-B73E-A94D29D48648.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_preVFP_v11-v1/70000/073EB621-A971-9D46-B246-A862D7D4BF50.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_preVFP_v11-v1/70000/0BDF7C07-84AB-FE41-9AA2-A84B7EAD7DE8.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_preVFP_v11-v1/70000/14BADB1A-9BEC-D545-A772-FE110FAA9C58.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_preVFP_v11-v1/70000/178B092E-70D7-B14A-B7A9-6E83CB256BBB.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_preVFP_v11-v1/70000/207E5612-D6A0-2F4F-8A94-5B3E912A13CE.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_preVFP_v11-v1/70000/26707DB0-3307-A64A-A9F0-ED63FF09D9D7.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_preVFP_v11-v1/70000/269330D9-2B16-3F44-8BB6-B94D285BE7D7.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_preVFP_v11-v1/70000/300479C4-26D3-5946-AC76-2BEDC9634A81.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_preVFP_v11-v1/70000/31045CA5-854D-B84D-AD67-846D10B951E3.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_preVFP_v11-v1/70000/3D61EE53-634A-B54D-9841-F629C0571D48.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_preVFP_v11-v1/70000/3D962066-2D55-F546-AA55-C2C73777280B.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_preVFP_v11-v1/70000/40EA7C19-77E0-7443-80E5-A67E99EA2D68.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_preVFP_v11-v1/70000/43F4FD4B-9E74-6045-9F90-E3762F0B0E9F.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_preVFP_v11-v1/70000/47049C5B-3E3C-9245-AC8A-F1D78519B466.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_preVFP_v11-v1/70000/535432A1-8FA2-AC4B-A578-23929C92DC80.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_preVFP_v11-v1/70000/5BFCC3F5-2E1C-3743-8975-ED52CFDB0CFE.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_preVFP_v11-v1/70000/5C350B35-C493-5543-962A-3F1055744336.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_preVFP_v11-v1/70000/78E44FC4-45CB-D243-A42F-3F49835B3402.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_preVFP_v11-v1/70000/7C8C00FD-2FBE-4745-B475-7B4844C6F754.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_preVFP_v11-v1/70000/7EC0A6FB-C741-014F-8804-149E9EE2AF86.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_preVFP_v11-v1/70000/82895884-6F3E-5345-9E03-A3F730D78E80.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_preVFP_v11-v1/70000/8E059019-B459-AE48-8D4A-EF509A1882F8.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_preVFP_v11-v1/70000/909FC7DD-0A66-C643-9312-AAEF3F6D81FB.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_preVFP_v11-v1/70000/91C8A717-F5BD-5D40-96D1-E34D5B4876B1.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_preVFP_v11-v1/70000/96676ACA-052C-7446-BE2F-4232BAC01F3A.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_preVFP_v11-v1/70000/9D3DCE6F-8F26-6541-BD56-D00D93B5C177.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_preVFP_v11-v1/70000/A07A2951-D68F-4740-A02B-6E239807A4BB.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_preVFP_v11-v1/70000/A07EBE04-F1C6-2B4D-9F2E-E950B3DEFFD9.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_preVFP_v11-v1/70000/A7B8C64F-A1F0-8D49-A616-570B4D621060.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/4cores5k_106X_mcRun2_asymptotic_preVFP_v11-v1/70000/D939F204-C298-BA49-931B-EF54F8E2F65D.root',
] )