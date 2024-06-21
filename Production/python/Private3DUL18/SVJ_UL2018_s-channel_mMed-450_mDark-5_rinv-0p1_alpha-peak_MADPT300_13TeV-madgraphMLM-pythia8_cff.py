import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/user/lpcdarkqcd/boosted/signal_production_3Dscan/2018/MINIAOD/step_MINIAOD_s-channel_mMed-450_mDark-5_rinv-0.1_alpha-peak_MADPT300_13TeV-madgraphMLM-pythia8_n-3349/part-1.root',
       '/store/user/lpcdarkqcd/boosted/signal_production_3Dscan/2018/MINIAOD/step_MINIAOD_s-channel_mMed-450_mDark-5_rinv-0.1_alpha-peak_MADPT300_13TeV-madgraphMLM-pythia8_n-3349/part-2.root',
       '/store/user/lpcdarkqcd/boosted/signal_production_3Dscan/2018/MINIAOD/step_MINIAOD_s-channel_mMed-450_mDark-5_rinv-0.1_alpha-peak_MADPT300_13TeV-madgraphMLM-pythia8_n-3349/part-3.root',
       '/store/user/lpcdarkqcd/boosted/signal_production_3Dscan/2018/MINIAOD/step_MINIAOD_s-channel_mMed-450_mDark-5_rinv-0.1_alpha-peak_MADPT300_13TeV-madgraphMLM-pythia8_n-3349/part-4.root',
       '/store/user/lpcdarkqcd/boosted/signal_production_3Dscan/2018/MINIAOD/step_MINIAOD_s-channel_mMed-450_mDark-5_rinv-0.1_alpha-peak_MADPT300_13TeV-madgraphMLM-pythia8_n-3349/part-5.root',
       '/store/user/lpcdarkqcd/boosted/signal_production_3Dscan/2018/MINIAOD/step_MINIAOD_s-channel_mMed-450_mDark-5_rinv-0.1_alpha-peak_MADPT300_13TeV-madgraphMLM-pythia8_n-3349/part-6.root',
       '/store/user/lpcdarkqcd/boosted/signal_production_3Dscan/2018/MINIAOD/step_MINIAOD_s-channel_mMed-450_mDark-5_rinv-0.1_alpha-peak_MADPT300_13TeV-madgraphMLM-pythia8_n-3349/part-7.root',
       '/store/user/lpcdarkqcd/boosted/signal_production_3Dscan/2018/MINIAOD/step_MINIAOD_s-channel_mMed-450_mDark-5_rinv-0.1_alpha-peak_MADPT300_13TeV-madgraphMLM-pythia8_n-3349/part-8.root',
       '/store/user/lpcdarkqcd/boosted/signal_production_3Dscan/2018/MINIAOD/step_MINIAOD_s-channel_mMed-450_mDark-5_rinv-0.1_alpha-peak_MADPT300_13TeV-madgraphMLM-pythia8_n-3349/part-9.root',
       '/store/user/lpcdarkqcd/boosted/signal_production_3Dscan/2018/MINIAOD/step_MINIAOD_s-channel_mMed-450_mDark-5_rinv-0.1_alpha-peak_MADPT300_13TeV-madgraphMLM-pythia8_n-3349/part-11.root',
       '/store/user/lpcdarkqcd/boosted/signal_production_3Dscan/2018/MINIAOD/step_MINIAOD_s-channel_mMed-450_mDark-5_rinv-0.1_alpha-peak_MADPT300_13TeV-madgraphMLM-pythia8_n-3349/part-12.root',
       '/store/user/lpcdarkqcd/boosted/signal_production_3Dscan/2018/MINIAOD/step_MINIAOD_s-channel_mMed-450_mDark-5_rinv-0.1_alpha-peak_MADPT300_13TeV-madgraphMLM-pythia8_n-3349/part-13.root',
       '/store/user/lpcdarkqcd/boosted/signal_production_3Dscan/2018/MINIAOD/step_MINIAOD_s-channel_mMed-450_mDark-5_rinv-0.1_alpha-peak_MADPT300_13TeV-madgraphMLM-pythia8_n-3349/part-14.root',
       '/store/user/lpcdarkqcd/boosted/signal_production_3Dscan/2018/MINIAOD/step_MINIAOD_s-channel_mMed-450_mDark-5_rinv-0.1_alpha-peak_MADPT300_13TeV-madgraphMLM-pythia8_n-3349/part-15.root',
       '/store/user/lpcdarkqcd/boosted/signal_production_3Dscan/2018/MINIAOD/step_MINIAOD_s-channel_mMed-450_mDark-5_rinv-0.1_alpha-peak_MADPT300_13TeV-madgraphMLM-pythia8_n-3349/part-16.root',
       '/store/user/lpcdarkqcd/boosted/signal_production_3Dscan/2018/MINIAOD/step_MINIAOD_s-channel_mMed-450_mDark-5_rinv-0.1_alpha-peak_MADPT300_13TeV-madgraphMLM-pythia8_n-3349/part-17.root',
       '/store/user/lpcdarkqcd/boosted/signal_production_3Dscan/2018/MINIAOD/step_MINIAOD_s-channel_mMed-450_mDark-5_rinv-0.1_alpha-peak_MADPT300_13TeV-madgraphMLM-pythia8_n-3349/part-18.root',
       '/store/user/lpcdarkqcd/boosted/signal_production_3Dscan/2018/MINIAOD/step_MINIAOD_s-channel_mMed-450_mDark-5_rinv-0.1_alpha-peak_MADPT300_13TeV-madgraphMLM-pythia8_n-3349/part-19.root',
       '/store/user/lpcdarkqcd/boosted/signal_production_3Dscan/2018/MINIAOD/step_MINIAOD_s-channel_mMed-450_mDark-5_rinv-0.1_alpha-peak_MADPT300_13TeV-madgraphMLM-pythia8_n-3349/part-20.root',
       '/store/user/lpcdarkqcd/boosted/signal_production_3Dscan/2018/MINIAOD/step_MINIAOD_s-channel_mMed-450_mDark-5_rinv-0.1_alpha-peak_MADPT300_13TeV-madgraphMLM-pythia8_n-3349/part-21.root',
       '/store/user/lpcdarkqcd/boosted/signal_production_3Dscan/2018/MINIAOD/step_MINIAOD_s-channel_mMed-450_mDark-5_rinv-0.1_alpha-peak_MADPT300_13TeV-madgraphMLM-pythia8_n-3349/part-22.root',
       '/store/user/lpcdarkqcd/boosted/signal_production_3Dscan/2018/MINIAOD/step_MINIAOD_s-channel_mMed-450_mDark-5_rinv-0.1_alpha-peak_MADPT300_13TeV-madgraphMLM-pythia8_n-3349/part-23.root',
       '/store/user/lpcdarkqcd/boosted/signal_production_3Dscan/2018/MINIAOD/step_MINIAOD_s-channel_mMed-450_mDark-5_rinv-0.1_alpha-peak_MADPT300_13TeV-madgraphMLM-pythia8_n-3349/part-24.root',
       '/store/user/lpcdarkqcd/boosted/signal_production_3Dscan/2018/MINIAOD/step_MINIAOD_s-channel_mMed-450_mDark-5_rinv-0.1_alpha-peak_MADPT300_13TeV-madgraphMLM-pythia8_n-3349/part-25.root',
       '/store/user/lpcdarkqcd/boosted/signal_production_3Dscan/2018/MINIAOD/step_MINIAOD_s-channel_mMed-450_mDark-5_rinv-0.1_alpha-peak_MADPT300_13TeV-madgraphMLM-pythia8_n-3349/part-26.root',
       '/store/user/lpcdarkqcd/boosted/signal_production_3Dscan/2018/MINIAOD/step_MINIAOD_s-channel_mMed-450_mDark-5_rinv-0.1_alpha-peak_MADPT300_13TeV-madgraphMLM-pythia8_n-3349/part-27.root',
       '/store/user/lpcdarkqcd/boosted/signal_production_3Dscan/2018/MINIAOD/step_MINIAOD_s-channel_mMed-450_mDark-5_rinv-0.1_alpha-peak_MADPT300_13TeV-madgraphMLM-pythia8_n-3349/part-28.root',
       '/store/user/lpcdarkqcd/boosted/signal_production_3Dscan/2018/MINIAOD/step_MINIAOD_s-channel_mMed-450_mDark-5_rinv-0.1_alpha-peak_MADPT300_13TeV-madgraphMLM-pythia8_n-3349/part-29.root',
       '/store/user/lpcdarkqcd/boosted/signal_production_3Dscan/2018/MINIAOD/step_MINIAOD_s-channel_mMed-450_mDark-5_rinv-0.1_alpha-peak_MADPT300_13TeV-madgraphMLM-pythia8_n-3349/part-30.root',
       '/store/user/lpcdarkqcd/boosted/signal_production_3Dscan/2018/MINIAOD/step_MINIAOD_s-channel_mMed-450_mDark-5_rinv-0.1_alpha-peak_MADPT300_13TeV-madgraphMLM-pythia8_n-3349/part-31.root',
       '/store/user/lpcdarkqcd/boosted/signal_production_3Dscan/2018/MINIAOD/step_MINIAOD_s-channel_mMed-450_mDark-5_rinv-0.1_alpha-peak_MADPT300_13TeV-madgraphMLM-pythia8_n-3349/part-32.root',
       '/store/user/lpcdarkqcd/boosted/signal_production_3Dscan/2018/MINIAOD/step_MINIAOD_s-channel_mMed-450_mDark-5_rinv-0.1_alpha-peak_MADPT300_13TeV-madgraphMLM-pythia8_n-3349/part-34.root',
       '/store/user/lpcdarkqcd/boosted/signal_production_3Dscan/2018/MINIAOD/step_MINIAOD_s-channel_mMed-450_mDark-5_rinv-0.1_alpha-peak_MADPT300_13TeV-madgraphMLM-pythia8_n-3349/part-35.root',
       '/store/user/lpcdarkqcd/boosted/signal_production_3Dscan/2018/MINIAOD/step_MINIAOD_s-channel_mMed-450_mDark-5_rinv-0.1_alpha-peak_MADPT300_13TeV-madgraphMLM-pythia8_n-3349/part-36.root',
       '/store/user/lpcdarkqcd/boosted/signal_production_3Dscan/2018/MINIAOD/step_MINIAOD_s-channel_mMed-450_mDark-5_rinv-0.1_alpha-peak_MADPT300_13TeV-madgraphMLM-pythia8_n-3349/part-37.root',
       '/store/user/lpcdarkqcd/boosted/signal_production_3Dscan/2018/MINIAOD/step_MINIAOD_s-channel_mMed-450_mDark-5_rinv-0.1_alpha-peak_MADPT300_13TeV-madgraphMLM-pythia8_n-3349/part-38.root',
       '/store/user/lpcdarkqcd/boosted/signal_production_3Dscan/2018/MINIAOD/step_MINIAOD_s-channel_mMed-450_mDark-5_rinv-0.1_alpha-peak_MADPT300_13TeV-madgraphMLM-pythia8_n-3349/part-39.root',
       '/store/user/lpcdarkqcd/boosted/signal_production_3Dscan/2018/MINIAOD/step_MINIAOD_s-channel_mMed-450_mDark-5_rinv-0.1_alpha-peak_MADPT300_13TeV-madgraphMLM-pythia8_n-3349/part-40.root',
       '/store/user/lpcdarkqcd/boosted/signal_production_3Dscan/2018/MINIAOD/step_MINIAOD_s-channel_mMed-450_mDark-5_rinv-0.1_alpha-peak_MADPT300_13TeV-madgraphMLM-pythia8_n-3349/part-41.root',
       '/store/user/lpcdarkqcd/boosted/signal_production_3Dscan/2018/MINIAOD/step_MINIAOD_s-channel_mMed-450_mDark-5_rinv-0.1_alpha-peak_MADPT300_13TeV-madgraphMLM-pythia8_n-3349/part-42.root',
       '/store/user/lpcdarkqcd/boosted/signal_production_3Dscan/2018/MINIAOD/step_MINIAOD_s-channel_mMed-450_mDark-5_rinv-0.1_alpha-peak_MADPT300_13TeV-madgraphMLM-pythia8_n-3349/part-43.root',
       '/store/user/lpcdarkqcd/boosted/signal_production_3Dscan/2018/MINIAOD/step_MINIAOD_s-channel_mMed-450_mDark-5_rinv-0.1_alpha-peak_MADPT300_13TeV-madgraphMLM-pythia8_n-3349/part-44.root',
       '/store/user/lpcdarkqcd/boosted/signal_production_3Dscan/2018/MINIAOD/step_MINIAOD_s-channel_mMed-450_mDark-5_rinv-0.1_alpha-peak_MADPT300_13TeV-madgraphMLM-pythia8_n-3349/part-45.root',
       '/store/user/lpcdarkqcd/boosted/signal_production_3Dscan/2018/MINIAOD/step_MINIAOD_s-channel_mMed-450_mDark-5_rinv-0.1_alpha-peak_MADPT300_13TeV-madgraphMLM-pythia8_n-3349/part-46.root',
       '/store/user/lpcdarkqcd/boosted/signal_production_3Dscan/2018/MINIAOD/step_MINIAOD_s-channel_mMed-450_mDark-5_rinv-0.1_alpha-peak_MADPT300_13TeV-madgraphMLM-pythia8_n-3349/part-47.root',
       '/store/user/lpcdarkqcd/boosted/signal_production_3Dscan/2018/MINIAOD/step_MINIAOD_s-channel_mMed-450_mDark-5_rinv-0.1_alpha-peak_MADPT300_13TeV-madgraphMLM-pythia8_n-3349/part-48.root',
       '/store/user/lpcdarkqcd/boosted/signal_production_3Dscan/2018/MINIAOD/step_MINIAOD_s-channel_mMed-450_mDark-5_rinv-0.1_alpha-peak_MADPT300_13TeV-madgraphMLM-pythia8_n-3349/part-49.root',
       '/store/user/lpcdarkqcd/boosted/signal_production_3Dscan/2018/MINIAOD/step_MINIAOD_s-channel_mMed-450_mDark-5_rinv-0.1_alpha-peak_MADPT300_13TeV-madgraphMLM-pythia8_n-3349/part-50.root',
       '/store/user/lpcdarkqcd/boosted/signal_production_3Dscan/2018/MINIAOD/step_MINIAOD_s-channel_mMed-450_mDark-5_rinv-0.1_alpha-peak_MADPT300_13TeV-madgraphMLM-pythia8_n-3349/part-51.root',
       '/store/user/lpcdarkqcd/boosted/signal_production_3Dscan/2018/MINIAOD/step_MINIAOD_s-channel_mMed-450_mDark-5_rinv-0.1_alpha-peak_MADPT300_13TeV-madgraphMLM-pythia8_n-3349/part-52.root',
       '/store/user/lpcdarkqcd/boosted/signal_production_3Dscan/2018/MINIAOD/step_MINIAOD_s-channel_mMed-450_mDark-5_rinv-0.1_alpha-peak_MADPT300_13TeV-madgraphMLM-pythia8_n-3349/part-53.root',
       '/store/user/lpcdarkqcd/boosted/signal_production_3Dscan/2018/MINIAOD/step_MINIAOD_s-channel_mMed-450_mDark-5_rinv-0.1_alpha-peak_MADPT300_13TeV-madgraphMLM-pythia8_n-3349/part-54.root',
       '/store/user/lpcdarkqcd/boosted/signal_production_3Dscan/2018/MINIAOD/step_MINIAOD_s-channel_mMed-450_mDark-5_rinv-0.1_alpha-peak_MADPT300_13TeV-madgraphMLM-pythia8_n-3349/part-55.root',
       '/store/user/lpcdarkqcd/boosted/signal_production_3Dscan/2018/MINIAOD/step_MINIAOD_s-channel_mMed-450_mDark-5_rinv-0.1_alpha-peak_MADPT300_13TeV-madgraphMLM-pythia8_n-3349/part-56.root',
       '/store/user/lpcdarkqcd/boosted/signal_production_3Dscan/2018/MINIAOD/step_MINIAOD_s-channel_mMed-450_mDark-5_rinv-0.1_alpha-peak_MADPT300_13TeV-madgraphMLM-pythia8_n-3349/part-57.root',
       '/store/user/lpcdarkqcd/boosted/signal_production_3Dscan/2018/MINIAOD/step_MINIAOD_s-channel_mMed-450_mDark-5_rinv-0.1_alpha-peak_MADPT300_13TeV-madgraphMLM-pythia8_n-3349/part-58.root',
       '/store/user/lpcdarkqcd/boosted/signal_production_3Dscan/2018/MINIAOD/step_MINIAOD_s-channel_mMed-450_mDark-5_rinv-0.1_alpha-peak_MADPT300_13TeV-madgraphMLM-pythia8_n-3349/part-59.root',
       '/store/user/lpcdarkqcd/boosted/signal_production_3Dscan/2018/MINIAOD/step_MINIAOD_s-channel_mMed-450_mDark-5_rinv-0.1_alpha-peak_MADPT300_13TeV-madgraphMLM-pythia8_n-3349/part-60.root',
       '/store/user/lpcdarkqcd/boosted/signal_production_3Dscan/2018/MINIAOD/step_MINIAOD_s-channel_mMed-450_mDark-5_rinv-0.1_alpha-peak_MADPT300_13TeV-madgraphMLM-pythia8_n-3349/part-61.root',
       '/store/user/lpcdarkqcd/boosted/signal_production_3Dscan/2018/MINIAOD/step_MINIAOD_s-channel_mMed-450_mDark-5_rinv-0.1_alpha-peak_MADPT300_13TeV-madgraphMLM-pythia8_n-3349/part-62.root',
       '/store/user/lpcdarkqcd/boosted/signal_production_3Dscan/2018/MINIAOD/step_MINIAOD_s-channel_mMed-450_mDark-5_rinv-0.1_alpha-peak_MADPT300_13TeV-madgraphMLM-pythia8_n-3349/part-63.root',
       '/store/user/lpcdarkqcd/boosted/signal_production_3Dscan/2018/MINIAOD/step_MINIAOD_s-channel_mMed-450_mDark-5_rinv-0.1_alpha-peak_MADPT300_13TeV-madgraphMLM-pythia8_n-3349/part-64.root',
       '/store/user/lpcdarkqcd/boosted/signal_production_3Dscan/2018/MINIAOD/step_MINIAOD_s-channel_mMed-450_mDark-5_rinv-0.1_alpha-peak_MADPT300_13TeV-madgraphMLM-pythia8_n-3349/part-65.root',
       '/store/user/lpcdarkqcd/boosted/signal_production_3Dscan/2018/MINIAOD/step_MINIAOD_s-channel_mMed-450_mDark-5_rinv-0.1_alpha-peak_MADPT300_13TeV-madgraphMLM-pythia8_n-3349/part-66.root',
       '/store/user/lpcdarkqcd/boosted/signal_production_3Dscan/2018/MINIAOD/step_MINIAOD_s-channel_mMed-450_mDark-5_rinv-0.1_alpha-peak_MADPT300_13TeV-madgraphMLM-pythia8_n-3349/part-67.root',
       '/store/user/lpcdarkqcd/boosted/signal_production_3Dscan/2018/MINIAOD/step_MINIAOD_s-channel_mMed-450_mDark-5_rinv-0.1_alpha-peak_MADPT300_13TeV-madgraphMLM-pythia8_n-3349/part-68.root',
       '/store/user/lpcdarkqcd/boosted/signal_production_3Dscan/2018/MINIAOD/step_MINIAOD_s-channel_mMed-450_mDark-5_rinv-0.1_alpha-peak_MADPT300_13TeV-madgraphMLM-pythia8_n-3349/part-69.root',
       '/store/user/lpcdarkqcd/boosted/signal_production_3Dscan/2018/MINIAOD/step_MINIAOD_s-channel_mMed-450_mDark-5_rinv-0.1_alpha-peak_MADPT300_13TeV-madgraphMLM-pythia8_n-3349/part-70.root',
       '/store/user/lpcdarkqcd/boosted/signal_production_3Dscan/2018/MINIAOD/step_MINIAOD_s-channel_mMed-450_mDark-5_rinv-0.1_alpha-peak_MADPT300_13TeV-madgraphMLM-pythia8_n-3349/part-71.root',
       '/store/user/lpcdarkqcd/boosted/signal_production_3Dscan/2018/MINIAOD/step_MINIAOD_s-channel_mMed-450_mDark-5_rinv-0.1_alpha-peak_MADPT300_13TeV-madgraphMLM-pythia8_n-3349/part-72.root',
       '/store/user/lpcdarkqcd/boosted/signal_production_3Dscan/2018/MINIAOD/step_MINIAOD_s-channel_mMed-450_mDark-5_rinv-0.1_alpha-peak_MADPT300_13TeV-madgraphMLM-pythia8_n-3349/part-73.root',
       '/store/user/lpcdarkqcd/boosted/signal_production_3Dscan/2018/MINIAOD/step_MINIAOD_s-channel_mMed-450_mDark-5_rinv-0.1_alpha-peak_MADPT300_13TeV-madgraphMLM-pythia8_n-3349/part-74.root',
       '/store/user/lpcdarkqcd/boosted/signal_production_3Dscan/2018/MINIAOD/step_MINIAOD_s-channel_mMed-450_mDark-5_rinv-0.1_alpha-peak_MADPT300_13TeV-madgraphMLM-pythia8_n-3349/part-75.root',
] )
