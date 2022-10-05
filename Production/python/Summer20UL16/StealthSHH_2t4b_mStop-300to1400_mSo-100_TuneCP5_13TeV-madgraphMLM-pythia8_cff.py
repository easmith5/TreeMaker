import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer20UL16MiniAODv2/StealthSHH_2t4b_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/40000/00F0A6C2-15DC-0347-967F-CDCCCEB21D20.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/StealthSHH_2t4b_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/40000/02BD081E-6DDC-E140-9188-37CD2456AA5A.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/StealthSHH_2t4b_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/40000/0E1A056E-6D99-4448-807D-BED7DE0C25E5.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/StealthSHH_2t4b_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/40000/1096F2D3-1B7B-244F-9207-8C90149F34B2.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/StealthSHH_2t4b_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/40000/173BD9C8-C9AF-444A-8AEE-CE277927706F.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/StealthSHH_2t4b_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/40000/17B0312A-7D5B-1144-93C8-583C468D08BA.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/StealthSHH_2t4b_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/40000/22D414FA-080F-584C-8C48-E8F99197A898.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/StealthSHH_2t4b_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/40000/240C6B5B-EA6C-8E42-B96B-E5DCE4597900.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/StealthSHH_2t4b_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/40000/260EE00F-61A0-6B41-B733-7DF59C78587D.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/StealthSHH_2t4b_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/40000/2CAC4E25-A156-9740-BF92-7B5C98C86A2E.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/StealthSHH_2t4b_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/40000/2CC99E52-2855-EC4D-85B6-81DECA8F2668.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/StealthSHH_2t4b_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/40000/32A5A5F9-2B5A-DC47-9FC6-68C2973342C9.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/StealthSHH_2t4b_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/40000/3BDE2F8F-01D5-5947-8978-8211435BBAA2.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/StealthSHH_2t4b_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/40000/3DFCF725-8C99-EE44-9356-1086C80FF899.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/StealthSHH_2t4b_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/40000/41FF9D2E-2E96-444D-A0FA-3EFD28F27A70.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/StealthSHH_2t4b_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/40000/441B8610-6B45-0646-8FB8-8F82A1338104.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/StealthSHH_2t4b_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/40000/46573843-76FE-3A4C-9C4A-5D639A2CBFE0.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/StealthSHH_2t4b_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/40000/4D305CCD-3DDA-BE43-BD46-C6B3810C4850.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/StealthSHH_2t4b_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/40000/537A0841-3428-354C-9842-C1D73DD591E8.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/StealthSHH_2t4b_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/40000/57798DFE-8760-D245-A87F-7DDF5D10F660.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/StealthSHH_2t4b_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/40000/5A42C8B3-CDE8-954A-A11B-CE4B558B3F8E.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/StealthSHH_2t4b_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/40000/5B6061AD-D05A-264E-9353-1B966C6475A2.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/StealthSHH_2t4b_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/40000/5FBE91B5-9E70-444B-9600-CBFDCD61DFBB.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/StealthSHH_2t4b_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/40000/614D7847-2903-304E-8E87-4BAFCE07B37A.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/StealthSHH_2t4b_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/40000/6404A858-2983-EE4F-8859-FA7857B5ABAB.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/StealthSHH_2t4b_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/40000/67E4D788-8D71-C546-95BD-D8598CBC85A3.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/StealthSHH_2t4b_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/40000/74E498AD-29D9-6E4C-BEC7-EAF83EA2FB82.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/StealthSHH_2t4b_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/40000/7563327E-5588-1B43-BF20-5F6439DD8B57.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/StealthSHH_2t4b_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/40000/7C407B97-AA6D-804B-B925-B0A83AC32F98.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/StealthSHH_2t4b_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/40000/7EA3FCFD-BB5C-8B4D-A9DD-A67FD6D2C32A.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/StealthSHH_2t4b_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/40000/806828B5-46DD-7745-9628-1E7D1ECDEC96.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/StealthSHH_2t4b_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/40000/8334E54B-DD8D-A344-9DAA-D2C1E06B8727.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/StealthSHH_2t4b_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/40000/8A174ECD-7C44-B94A-A032-4052D26EDEE9.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/StealthSHH_2t4b_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/40000/94DADC4B-FCF6-0240-B449-1EF651C8707D.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/StealthSHH_2t4b_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/40000/9AC25EA0-8C0D-6C4B-AEBE-163E89232684.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/StealthSHH_2t4b_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/40000/9E165A8D-D472-D746-ACCE-A6568A0AE47E.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/StealthSHH_2t4b_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/40000/9F32554D-EEEB-F745-8566-5A28D4F5B0A4.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/StealthSHH_2t4b_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/40000/A16B5436-6E7F-C24C-A24C-04E05ADFFB68.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/StealthSHH_2t4b_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/40000/A92C04FA-93B2-E040-86C4-26A24E888A45.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/StealthSHH_2t4b_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/40000/AB8B94AE-0440-FA43-B72E-F2BEC60B7820.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/StealthSHH_2t4b_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/40000/ABB5E98A-CCBE-5F44-AD35-7B96CB3EBBAD.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/StealthSHH_2t4b_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/40000/B06EA6E2-6661-754E-9523-F02ACF5C2DED.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/StealthSHH_2t4b_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/40000/B0B81821-DEEF-2741-B612-04CB1C1C2526.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/StealthSHH_2t4b_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/40000/B1606521-360B-094A-BBB6-02CD18C312F2.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/StealthSHH_2t4b_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/40000/B72672B0-E81A-8449-BB1D-49320EC3C846.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/StealthSHH_2t4b_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/40000/B8B8441E-D3ED-A749-8EF7-D4E1AE96C9B0.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/StealthSHH_2t4b_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/40000/B91447F4-5202-6E49-86FC-23265B436E5C.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/StealthSHH_2t4b_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/40000/BB978205-8356-A44D-9113-51B390094873.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/StealthSHH_2t4b_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/40000/BE9B7BEB-5FAD-EF49-91DB-5DDE9AC2231D.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/StealthSHH_2t4b_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/40000/C0B4BB78-4725-9B42-8389-230ADABD33DB.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/StealthSHH_2t4b_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/40000/C460DFDA-A50A-1348-8CF5-74B6019EC9CF.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/StealthSHH_2t4b_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/40000/C48AB3A9-376D-1046-ADD3-995D8A7CF2DD.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/StealthSHH_2t4b_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/40000/C676BF5B-395E-3940-A2EC-A305EC40F37A.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/StealthSHH_2t4b_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/40000/D2E2CD35-2223-AD44-B5FF-40C22BB11AAD.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/StealthSHH_2t4b_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/40000/D328A5DD-850D-5641-99B3-26149EBD59D3.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/StealthSHH_2t4b_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/40000/E049A152-4EFE-1A43-9D2D-73065CF8B674.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/StealthSHH_2t4b_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/40000/E21DC03F-A5D6-D747-9A8D-671FEF11792B.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/StealthSHH_2t4b_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/40000/E6616495-31F3-634A-81FF-FCF6CAF0C010.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/StealthSHH_2t4b_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/40000/EC710A57-1C16-704B-853D-B0F2E5D846FE.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/StealthSHH_2t4b_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/40000/F1367A1E-D6A1-8047-AB6C-F28C29C4AC0A.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/StealthSHH_2t4b_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/40000/F27CE2E9-38EB-824D-9D1A-A3C9B28835C4.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/StealthSHH_2t4b_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/40000/F684A921-5082-9F41-8784-9B7742EBAD2F.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/StealthSHH_2t4b_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/40000/F80F1100-6C1C-304A-961E-CC3C43A26622.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/StealthSHH_2t4b_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/40000/FB5C931F-5373-A143-A871-A9BA40D8EEE2.root',
] )
