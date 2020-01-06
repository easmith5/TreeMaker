import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5up_PSweights_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/70000/0076728C-288C-E811-8D5E-0CC47AA47824.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5up_PSweights_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/70000/02850BC1-CB8C-E811-9AE1-0CC47A57CD56.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5up_PSweights_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/70000/061009A4-C087-E811-83F1-0025907D24F0.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5up_PSweights_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/70000/0AFC9C09-1C89-E811-9543-002590D9D9BC.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5up_PSweights_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/70000/10EFD19D-D58A-E811-A1D3-0CC47A57CCF4.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5up_PSweights_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/70000/142B3058-498C-E811-A527-0CC47AA53DBE.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5up_PSweights_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/70000/14459F95-288C-E811-854A-0CC47A57CCE8.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5up_PSweights_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/70000/147BB76C-498C-E811-A5F4-003048C8F3A2.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5up_PSweights_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/70000/1653BD64-498C-E811-AD26-00259019A43E.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5up_PSweights_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/70000/16A37CB1-D58A-E811-A73C-0025901AEDA4.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5up_PSweights_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/70000/188CDD15-4E8A-E811-9816-0CC47A57D066.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5up_PSweights_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/70000/18CD809E-2A8C-E811-AF7B-0CC47A57CD56.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5up_PSweights_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/70000/1A2C7C15-BC8B-E811-A8B1-0CC47AB0BDDE.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5up_PSweights_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/70000/1AB27D24-4788-E811-BC99-00259075D702.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5up_PSweights_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/70000/1C2B300F-958B-E811-9607-00259048A8F0.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5up_PSweights_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/70000/2211A210-088C-E811-B7CC-002590FD5A48.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5up_PSweights_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/70000/2239B066-498C-E811-AA03-002590D9D966.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5up_PSweights_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/70000/22BCB49E-2A8C-E811-AA46-0CC47AA53D6E.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5up_PSweights_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/70000/245B5D98-288C-E811-A0A0-0025901AC3DE.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5up_PSweights_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/70000/248EC89D-2A8C-E811-A8FE-00259029E66E.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5up_PSweights_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/70000/281988F9-CD89-E811-96A0-0CC47A0AD742.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5up_PSweights_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/70000/284B86C4-E98B-E811-A23B-003048CBA444.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5up_PSweights_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/70000/2A5BABBF-2A8C-E811-B329-00259029E66E.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5up_PSweights_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/70000/2E4B7A8E-2A8C-E811-AC34-0CC47A57CCEA.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5up_PSweights_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/70000/2EB04AA4-2A8C-E811-A674-0025907859C4.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5up_PSweights_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/70000/32B1FF6B-498C-E811-BE23-002590D9D8B8.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5up_PSweights_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/70000/36BCCDA3-2A8C-E811-B579-0CC47A0AD6E0.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5up_PSweights_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/70000/4206E259-008C-E811-816A-0025907DE278.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5up_PSweights_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/70000/42251722-D58B-E811-BE91-002590D9D896.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5up_PSweights_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/70000/429A8C91-2A8C-E811-8BE0-0CC47AA53D60.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5up_PSweights_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/70000/42BA01AC-2A8C-E811-AD55-002590FD5A78.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5up_PSweights_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/70000/46059E4C-EA8B-E811-BB8E-0CC47AD24D28.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5up_PSweights_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/70000/4A9784D0-2A8C-E811-8896-0CC47A0AD742.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5up_PSweights_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/70000/50A07F16-088C-E811-96F3-0CC47A57D168.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5up_PSweights_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/70000/528452A1-288C-E811-B536-003048CB8572.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5up_PSweights_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/70000/529A44FB-E98B-E811-8886-00259075D708.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5up_PSweights_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/70000/541D8590-2A8C-E811-8532-0CC47AA53D98.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5up_PSweights_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/70000/56FF5892-2A8C-E811-B4D5-0CC47AA53D68.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5up_PSweights_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/70000/58C44560-498C-E811-99A8-002590D9D8B6.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5up_PSweights_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/70000/5AC93281-488C-E811-B16A-0CC47A0AD6F8.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5up_PSweights_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/70000/5C582C8A-288C-E811-92AA-F452141014E0.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5up_PSweights_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/70000/66B9E571-498C-E811-9B07-0CC47A57CCEA.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5up_PSweights_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/70000/6808525A-498C-E811-90F6-0CC47AD24D32.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5up_PSweights_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/70000/6A0D42D3-FB87-E811-A96B-0CC47AB0BB0A.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5up_PSweights_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/70000/6A59BFC2-E98B-E811-90FA-00259029E87C.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5up_PSweights_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/70000/6AD27191-498C-E811-ABF1-0025902BD8CE.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5up_PSweights_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/70000/6E14E35C-958B-E811-BE55-0CC47AA47824.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5up_PSweights_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/70000/70F7AAA6-2A8C-E811-9F6A-0CC47A0AD742.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5up_PSweights_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/70000/78093BB7-078B-E811-B43F-0CC47AB0B828.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5up_PSweights_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/70000/786B9A9C-288C-E811-8472-003048C8F3A2.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5up_PSweights_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/70000/78D17B7A-498C-E811-BF58-00259029ED64.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5up_PSweights_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/70000/7C2FE192-288C-E811-825D-00259029E7FC.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5up_PSweights_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/70000/7CD2B22A-2B8C-E811-9493-0CC47A0AD6E0.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5up_PSweights_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/70000/84886C59-588B-E811-8CCD-0025907D244A.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5up_PSweights_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/70000/885208B4-D58A-E811-BEF6-00259029E71C.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5up_PSweights_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/70000/8A017F8D-288C-E811-84D0-0CC47AA47914.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5up_PSweights_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/70000/8CB6449B-2A8C-E811-88BA-0CC47A57D168.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5up_PSweights_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/70000/968D7192-2A8C-E811-AD0C-0CC47A0AD74E.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5up_PSweights_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/70000/98988E1C-958B-E811-9AF6-00259029E920.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5up_PSweights_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/70000/9AAC7B99-418C-E811-8D35-0025907DE278.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5up_PSweights_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/70000/9C93D28E-2A8C-E811-8B2D-0CC47AB0B828.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5up_PSweights_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/70000/9E4461D5-FB87-E811-9014-0CC47A57CB62.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5up_PSweights_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/70000/A660B29C-D58A-E811-B977-0CC47AA53D68.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5up_PSweights_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/70000/A882EA57-498C-E811-8E1A-0007432CAA50.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5up_PSweights_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/70000/AE0C9B9C-288C-E811-AA24-0CC47AA53D68.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5up_PSweights_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/70000/AE51338B-2A8C-E811-92E0-F452141014E0.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5up_PSweights_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/70000/AE773199-2A8C-E811-8B1B-0CC47AA53D8A.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5up_PSweights_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/70000/AEE88049-CE8B-E811-914B-0CC47A57CD6A.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5up_PSweights_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/70000/B62D4ECD-2A8C-E811-90FD-0CC47AA53D8A.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5up_PSweights_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/70000/BA468B91-2A8C-E811-911B-0CC47A57D036.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5up_PSweights_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/70000/BAE8739D-2A8C-E811-A329-0CC47A57CCE8.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5up_PSweights_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/70000/BC44D28B-2A8C-E811-ACA0-0CC47AA53DBE.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5up_PSweights_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/70000/BECC6CD5-E98B-E811-B8FB-0CC47AA53D64.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5up_PSweights_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/70000/C09FC386-2A8C-E811-832A-0025907D1D6C.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5up_PSweights_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/70000/C2A928F7-2A8C-E811-93B1-0CC47AA53D6E.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5up_PSweights_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/70000/C43321A0-2A8C-E811-83B2-003048CB7DA2.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5up_PSweights_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/70000/C8873AB7-078B-E811-8EB3-0CC47AB0B828.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5up_PSweights_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/70000/CE9F9594-288C-E811-BCAD-0CC47AA53D8A.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5up_PSweights_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/70000/D01AF3AF-9489-E811-9ED9-002590D9D8AC.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5up_PSweights_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/70000/D2003494-2A8C-E811-87B3-0025907D2212.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5up_PSweights_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/70000/D4103F97-288C-E811-9A4D-0CC47A57CBCC.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5up_PSweights_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/70000/E0DF5792-2A8C-E811-AA01-0CC47AA53D68.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5up_PSweights_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/70000/E212E48F-2A8C-E811-824A-0CC47AA53D6A.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5up_PSweights_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/70000/E24A3296-2A8C-E811-9800-0CC47AD24D28.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5up_PSweights_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/70000/E25A4B5D-498C-E811-83F6-0CC47AA53D82.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5up_PSweights_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/70000/E8B2AA8C-2A8C-E811-B7C4-0CC47AA53D60.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5up_PSweights_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/70000/F23A83B8-2A8C-E811-A19B-002590D9D8BA.root',
] )