import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/user/lpcdarkqcd/boosted/signal_production_3Dscan/2018/MINIAOD/step_MINIAOD_s-channel_mMed-300_mDark-1_rinv-0.9_alpha-peak_MADPT300_13TeV-madgraphMLM-pythia8_n-3046/part-1.root',
       '/store/user/lpcdarkqcd/boosted/signal_production_3Dscan/2018/MINIAOD/step_MINIAOD_s-channel_mMed-300_mDark-1_rinv-0.9_alpha-peak_MADPT300_13TeV-madgraphMLM-pythia8_n-3046/part-2.root',
       '/store/user/lpcdarkqcd/boosted/signal_production_3Dscan/2018/MINIAOD/step_MINIAOD_s-channel_mMed-300_mDark-1_rinv-0.9_alpha-peak_MADPT300_13TeV-madgraphMLM-pythia8_n-3046/part-3.root',
       '/store/user/lpcdarkqcd/boosted/signal_production_3Dscan/2018/MINIAOD/step_MINIAOD_s-channel_mMed-300_mDark-1_rinv-0.9_alpha-peak_MADPT300_13TeV-madgraphMLM-pythia8_n-3046/part-4.root',
       '/store/user/lpcdarkqcd/boosted/signal_production_3Dscan/2018/MINIAOD/step_MINIAOD_s-channel_mMed-300_mDark-1_rinv-0.9_alpha-peak_MADPT300_13TeV-madgraphMLM-pythia8_n-3046/part-5.root',
       '/store/user/lpcdarkqcd/boosted/signal_production_3Dscan/2018/MINIAOD/step_MINIAOD_s-channel_mMed-300_mDark-1_rinv-0.9_alpha-peak_MADPT300_13TeV-madgraphMLM-pythia8_n-3046/part-6.root',
       '/store/user/lpcdarkqcd/boosted/signal_production_3Dscan/2018/MINIAOD/step_MINIAOD_s-channel_mMed-300_mDark-1_rinv-0.9_alpha-peak_MADPT300_13TeV-madgraphMLM-pythia8_n-3046/part-7.root',
       '/store/user/lpcdarkqcd/boosted/signal_production_3Dscan/2018/MINIAOD/step_MINIAOD_s-channel_mMed-300_mDark-1_rinv-0.9_alpha-peak_MADPT300_13TeV-madgraphMLM-pythia8_n-3046/part-8.root',
       '/store/user/lpcdarkqcd/boosted/signal_production_3Dscan/2018/MINIAOD/step_MINIAOD_s-channel_mMed-300_mDark-1_rinv-0.9_alpha-peak_MADPT300_13TeV-madgraphMLM-pythia8_n-3046/part-9.root',
       '/store/user/lpcdarkqcd/boosted/signal_production_3Dscan/2018/MINIAOD/step_MINIAOD_s-channel_mMed-300_mDark-1_rinv-0.9_alpha-peak_MADPT300_13TeV-madgraphMLM-pythia8_n-3046/part-10.root',
       '/store/user/lpcdarkqcd/boosted/signal_production_3Dscan/2018/MINIAOD/step_MINIAOD_s-channel_mMed-300_mDark-1_rinv-0.9_alpha-peak_MADPT300_13TeV-madgraphMLM-pythia8_n-3046/part-11.root',
       '/store/user/lpcdarkqcd/boosted/signal_production_3Dscan/2018/MINIAOD/step_MINIAOD_s-channel_mMed-300_mDark-1_rinv-0.9_alpha-peak_MADPT300_13TeV-madgraphMLM-pythia8_n-3046/part-12.root',
       '/store/user/lpcdarkqcd/boosted/signal_production_3Dscan/2018/MINIAOD/step_MINIAOD_s-channel_mMed-300_mDark-1_rinv-0.9_alpha-peak_MADPT300_13TeV-madgraphMLM-pythia8_n-3046/part-13.root',
       '/store/user/lpcdarkqcd/boosted/signal_production_3Dscan/2018/MINIAOD/step_MINIAOD_s-channel_mMed-300_mDark-1_rinv-0.9_alpha-peak_MADPT300_13TeV-madgraphMLM-pythia8_n-3046/part-14.root',
       '/store/user/lpcdarkqcd/boosted/signal_production_3Dscan/2018/MINIAOD/step_MINIAOD_s-channel_mMed-300_mDark-1_rinv-0.9_alpha-peak_MADPT300_13TeV-madgraphMLM-pythia8_n-3046/part-15.root',
       '/store/user/lpcdarkqcd/boosted/signal_production_3Dscan/2018/MINIAOD/step_MINIAOD_s-channel_mMed-300_mDark-1_rinv-0.9_alpha-peak_MADPT300_13TeV-madgraphMLM-pythia8_n-3046/part-16.root',
       '/store/user/lpcdarkqcd/boosted/signal_production_3Dscan/2018/MINIAOD/step_MINIAOD_s-channel_mMed-300_mDark-1_rinv-0.9_alpha-peak_MADPT300_13TeV-madgraphMLM-pythia8_n-3046/part-17.root',
       '/store/user/lpcdarkqcd/boosted/signal_production_3Dscan/2018/MINIAOD/step_MINIAOD_s-channel_mMed-300_mDark-1_rinv-0.9_alpha-peak_MADPT300_13TeV-madgraphMLM-pythia8_n-3046/part-18.root',
       '/store/user/lpcdarkqcd/boosted/signal_production_3Dscan/2018/MINIAOD/step_MINIAOD_s-channel_mMed-300_mDark-1_rinv-0.9_alpha-peak_MADPT300_13TeV-madgraphMLM-pythia8_n-3046/part-19.root',
       '/store/user/lpcdarkqcd/boosted/signal_production_3Dscan/2018/MINIAOD/step_MINIAOD_s-channel_mMed-300_mDark-1_rinv-0.9_alpha-peak_MADPT300_13TeV-madgraphMLM-pythia8_n-3046/part-20.root',
       '/store/user/lpcdarkqcd/boosted/signal_production_3Dscan/2018/MINIAOD/step_MINIAOD_s-channel_mMed-300_mDark-1_rinv-0.9_alpha-peak_MADPT300_13TeV-madgraphMLM-pythia8_n-3046/part-22.root',
       '/store/user/lpcdarkqcd/boosted/signal_production_3Dscan/2018/MINIAOD/step_MINIAOD_s-channel_mMed-300_mDark-1_rinv-0.9_alpha-peak_MADPT300_13TeV-madgraphMLM-pythia8_n-3046/part-23.root',
       '/store/user/lpcdarkqcd/boosted/signal_production_3Dscan/2018/MINIAOD/step_MINIAOD_s-channel_mMed-300_mDark-1_rinv-0.9_alpha-peak_MADPT300_13TeV-madgraphMLM-pythia8_n-3046/part-25.root',
       '/store/user/lpcdarkqcd/boosted/signal_production_3Dscan/2018/MINIAOD/step_MINIAOD_s-channel_mMed-300_mDark-1_rinv-0.9_alpha-peak_MADPT300_13TeV-madgraphMLM-pythia8_n-3046/part-26.root',
       '/store/user/lpcdarkqcd/boosted/signal_production_3Dscan/2018/MINIAOD/step_MINIAOD_s-channel_mMed-300_mDark-1_rinv-0.9_alpha-peak_MADPT300_13TeV-madgraphMLM-pythia8_n-3046/part-27.root',
       '/store/user/lpcdarkqcd/boosted/signal_production_3Dscan/2018/MINIAOD/step_MINIAOD_s-channel_mMed-300_mDark-1_rinv-0.9_alpha-peak_MADPT300_13TeV-madgraphMLM-pythia8_n-3046/part-28.root',
       '/store/user/lpcdarkqcd/boosted/signal_production_3Dscan/2018/MINIAOD/step_MINIAOD_s-channel_mMed-300_mDark-1_rinv-0.9_alpha-peak_MADPT300_13TeV-madgraphMLM-pythia8_n-3046/part-29.root',
       '/store/user/lpcdarkqcd/boosted/signal_production_3Dscan/2018/MINIAOD/step_MINIAOD_s-channel_mMed-300_mDark-1_rinv-0.9_alpha-peak_MADPT300_13TeV-madgraphMLM-pythia8_n-3046/part-30.root',
       '/store/user/lpcdarkqcd/boosted/signal_production_3Dscan/2018/MINIAOD/step_MINIAOD_s-channel_mMed-300_mDark-1_rinv-0.9_alpha-peak_MADPT300_13TeV-madgraphMLM-pythia8_n-3046/part-31.root',
       '/store/user/lpcdarkqcd/boosted/signal_production_3Dscan/2018/MINIAOD/step_MINIAOD_s-channel_mMed-300_mDark-1_rinv-0.9_alpha-peak_MADPT300_13TeV-madgraphMLM-pythia8_n-3046/part-32.root',
       '/store/user/lpcdarkqcd/boosted/signal_production_3Dscan/2018/MINIAOD/step_MINIAOD_s-channel_mMed-300_mDark-1_rinv-0.9_alpha-peak_MADPT300_13TeV-madgraphMLM-pythia8_n-3046/part-33.root',
       '/store/user/lpcdarkqcd/boosted/signal_production_3Dscan/2018/MINIAOD/step_MINIAOD_s-channel_mMed-300_mDark-1_rinv-0.9_alpha-peak_MADPT300_13TeV-madgraphMLM-pythia8_n-3046/part-34.root',
       '/store/user/lpcdarkqcd/boosted/signal_production_3Dscan/2018/MINIAOD/step_MINIAOD_s-channel_mMed-300_mDark-1_rinv-0.9_alpha-peak_MADPT300_13TeV-madgraphMLM-pythia8_n-3046/part-35.root',
       '/store/user/lpcdarkqcd/boosted/signal_production_3Dscan/2018/MINIAOD/step_MINIAOD_s-channel_mMed-300_mDark-1_rinv-0.9_alpha-peak_MADPT300_13TeV-madgraphMLM-pythia8_n-3046/part-36.root',
       '/store/user/lpcdarkqcd/boosted/signal_production_3Dscan/2018/MINIAOD/step_MINIAOD_s-channel_mMed-300_mDark-1_rinv-0.9_alpha-peak_MADPT300_13TeV-madgraphMLM-pythia8_n-3046/part-37.root',
       '/store/user/lpcdarkqcd/boosted/signal_production_3Dscan/2018/MINIAOD/step_MINIAOD_s-channel_mMed-300_mDark-1_rinv-0.9_alpha-peak_MADPT300_13TeV-madgraphMLM-pythia8_n-3046/part-38.root',
       '/store/user/lpcdarkqcd/boosted/signal_production_3Dscan/2018/MINIAOD/step_MINIAOD_s-channel_mMed-300_mDark-1_rinv-0.9_alpha-peak_MADPT300_13TeV-madgraphMLM-pythia8_n-3046/part-39.root',
       '/store/user/lpcdarkqcd/boosted/signal_production_3Dscan/2018/MINIAOD/step_MINIAOD_s-channel_mMed-300_mDark-1_rinv-0.9_alpha-peak_MADPT300_13TeV-madgraphMLM-pythia8_n-3046/part-40.root',
       '/store/user/lpcdarkqcd/boosted/signal_production_3Dscan/2018/MINIAOD/step_MINIAOD_s-channel_mMed-300_mDark-1_rinv-0.9_alpha-peak_MADPT300_13TeV-madgraphMLM-pythia8_n-3046/part-41.root',
       '/store/user/lpcdarkqcd/boosted/signal_production_3Dscan/2018/MINIAOD/step_MINIAOD_s-channel_mMed-300_mDark-1_rinv-0.9_alpha-peak_MADPT300_13TeV-madgraphMLM-pythia8_n-3046/part-42.root',
       '/store/user/lpcdarkqcd/boosted/signal_production_3Dscan/2018/MINIAOD/step_MINIAOD_s-channel_mMed-300_mDark-1_rinv-0.9_alpha-peak_MADPT300_13TeV-madgraphMLM-pythia8_n-3046/part-43.root',
       '/store/user/lpcdarkqcd/boosted/signal_production_3Dscan/2018/MINIAOD/step_MINIAOD_s-channel_mMed-300_mDark-1_rinv-0.9_alpha-peak_MADPT300_13TeV-madgraphMLM-pythia8_n-3046/part-44.root',
       '/store/user/lpcdarkqcd/boosted/signal_production_3Dscan/2018/MINIAOD/step_MINIAOD_s-channel_mMed-300_mDark-1_rinv-0.9_alpha-peak_MADPT300_13TeV-madgraphMLM-pythia8_n-3046/part-45.root',
       '/store/user/lpcdarkqcd/boosted/signal_production_3Dscan/2018/MINIAOD/step_MINIAOD_s-channel_mMed-300_mDark-1_rinv-0.9_alpha-peak_MADPT300_13TeV-madgraphMLM-pythia8_n-3046/part-46.root',
       '/store/user/lpcdarkqcd/boosted/signal_production_3Dscan/2018/MINIAOD/step_MINIAOD_s-channel_mMed-300_mDark-1_rinv-0.9_alpha-peak_MADPT300_13TeV-madgraphMLM-pythia8_n-3046/part-47.root',
       '/store/user/lpcdarkqcd/boosted/signal_production_3Dscan/2018/MINIAOD/step_MINIAOD_s-channel_mMed-300_mDark-1_rinv-0.9_alpha-peak_MADPT300_13TeV-madgraphMLM-pythia8_n-3046/part-48.root',
       '/store/user/lpcdarkqcd/boosted/signal_production_3Dscan/2018/MINIAOD/step_MINIAOD_s-channel_mMed-300_mDark-1_rinv-0.9_alpha-peak_MADPT300_13TeV-madgraphMLM-pythia8_n-3046/part-49.root',
       '/store/user/lpcdarkqcd/boosted/signal_production_3Dscan/2018/MINIAOD/step_MINIAOD_s-channel_mMed-300_mDark-1_rinv-0.9_alpha-peak_MADPT300_13TeV-madgraphMLM-pythia8_n-3046/part-50.root',
       '/store/user/lpcdarkqcd/boosted/signal_production_3Dscan/2018/MINIAOD/step_MINIAOD_s-channel_mMed-300_mDark-1_rinv-0.9_alpha-peak_MADPT300_13TeV-madgraphMLM-pythia8_n-3046/part-51.root',
       '/store/user/lpcdarkqcd/boosted/signal_production_3Dscan/2018/MINIAOD/step_MINIAOD_s-channel_mMed-300_mDark-1_rinv-0.9_alpha-peak_MADPT300_13TeV-madgraphMLM-pythia8_n-3046/part-52.root',
       '/store/user/lpcdarkqcd/boosted/signal_production_3Dscan/2018/MINIAOD/step_MINIAOD_s-channel_mMed-300_mDark-1_rinv-0.9_alpha-peak_MADPT300_13TeV-madgraphMLM-pythia8_n-3046/part-53.root',
       '/store/user/lpcdarkqcd/boosted/signal_production_3Dscan/2018/MINIAOD/step_MINIAOD_s-channel_mMed-300_mDark-1_rinv-0.9_alpha-peak_MADPT300_13TeV-madgraphMLM-pythia8_n-3046/part-54.root',
       '/store/user/lpcdarkqcd/boosted/signal_production_3Dscan/2018/MINIAOD/step_MINIAOD_s-channel_mMed-300_mDark-1_rinv-0.9_alpha-peak_MADPT300_13TeV-madgraphMLM-pythia8_n-3046/part-55.root',
       '/store/user/lpcdarkqcd/boosted/signal_production_3Dscan/2018/MINIAOD/step_MINIAOD_s-channel_mMed-300_mDark-1_rinv-0.9_alpha-peak_MADPT300_13TeV-madgraphMLM-pythia8_n-3046/part-56.root',
       '/store/user/lpcdarkqcd/boosted/signal_production_3Dscan/2018/MINIAOD/step_MINIAOD_s-channel_mMed-300_mDark-1_rinv-0.9_alpha-peak_MADPT300_13TeV-madgraphMLM-pythia8_n-3046/part-57.root',
       '/store/user/lpcdarkqcd/boosted/signal_production_3Dscan/2018/MINIAOD/step_MINIAOD_s-channel_mMed-300_mDark-1_rinv-0.9_alpha-peak_MADPT300_13TeV-madgraphMLM-pythia8_n-3046/part-58.root',
       '/store/user/lpcdarkqcd/boosted/signal_production_3Dscan/2018/MINIAOD/step_MINIAOD_s-channel_mMed-300_mDark-1_rinv-0.9_alpha-peak_MADPT300_13TeV-madgraphMLM-pythia8_n-3046/part-59.root',
       '/store/user/lpcdarkqcd/boosted/signal_production_3Dscan/2018/MINIAOD/step_MINIAOD_s-channel_mMed-300_mDark-1_rinv-0.9_alpha-peak_MADPT300_13TeV-madgraphMLM-pythia8_n-3046/part-60.root',
       '/store/user/lpcdarkqcd/boosted/signal_production_3Dscan/2018/MINIAOD/step_MINIAOD_s-channel_mMed-300_mDark-1_rinv-0.9_alpha-peak_MADPT300_13TeV-madgraphMLM-pythia8_n-3046/part-61.root',
       '/store/user/lpcdarkqcd/boosted/signal_production_3Dscan/2018/MINIAOD/step_MINIAOD_s-channel_mMed-300_mDark-1_rinv-0.9_alpha-peak_MADPT300_13TeV-madgraphMLM-pythia8_n-3046/part-62.root',
       '/store/user/lpcdarkqcd/boosted/signal_production_3Dscan/2018/MINIAOD/step_MINIAOD_s-channel_mMed-300_mDark-1_rinv-0.9_alpha-peak_MADPT300_13TeV-madgraphMLM-pythia8_n-3046/part-63.root',
       '/store/user/lpcdarkqcd/boosted/signal_production_3Dscan/2018/MINIAOD/step_MINIAOD_s-channel_mMed-300_mDark-1_rinv-0.9_alpha-peak_MADPT300_13TeV-madgraphMLM-pythia8_n-3046/part-64.root',
       '/store/user/lpcdarkqcd/boosted/signal_production_3Dscan/2018/MINIAOD/step_MINIAOD_s-channel_mMed-300_mDark-1_rinv-0.9_alpha-peak_MADPT300_13TeV-madgraphMLM-pythia8_n-3046/part-65.root',
       '/store/user/lpcdarkqcd/boosted/signal_production_3Dscan/2018/MINIAOD/step_MINIAOD_s-channel_mMed-300_mDark-1_rinv-0.9_alpha-peak_MADPT300_13TeV-madgraphMLM-pythia8_n-3046/part-66.root',
       '/store/user/lpcdarkqcd/boosted/signal_production_3Dscan/2018/MINIAOD/step_MINIAOD_s-channel_mMed-300_mDark-1_rinv-0.9_alpha-peak_MADPT300_13TeV-madgraphMLM-pythia8_n-3046/part-67.root',
       '/store/user/lpcdarkqcd/boosted/signal_production_3Dscan/2018/MINIAOD/step_MINIAOD_s-channel_mMed-300_mDark-1_rinv-0.9_alpha-peak_MADPT300_13TeV-madgraphMLM-pythia8_n-3046/part-68.root',
       '/store/user/lpcdarkqcd/boosted/signal_production_3Dscan/2018/MINIAOD/step_MINIAOD_s-channel_mMed-300_mDark-1_rinv-0.9_alpha-peak_MADPT300_13TeV-madgraphMLM-pythia8_n-3046/part-69.root',
       '/store/user/lpcdarkqcd/boosted/signal_production_3Dscan/2018/MINIAOD/step_MINIAOD_s-channel_mMed-300_mDark-1_rinv-0.9_alpha-peak_MADPT300_13TeV-madgraphMLM-pythia8_n-3046/part-70.root',
       '/store/user/lpcdarkqcd/boosted/signal_production_3Dscan/2018/MINIAOD/step_MINIAOD_s-channel_mMed-300_mDark-1_rinv-0.9_alpha-peak_MADPT300_13TeV-madgraphMLM-pythia8_n-3046/part-71.root',
       '/store/user/lpcdarkqcd/boosted/signal_production_3Dscan/2018/MINIAOD/step_MINIAOD_s-channel_mMed-300_mDark-1_rinv-0.9_alpha-peak_MADPT300_13TeV-madgraphMLM-pythia8_n-3046/part-72.root',
       '/store/user/lpcdarkqcd/boosted/signal_production_3Dscan/2018/MINIAOD/step_MINIAOD_s-channel_mMed-300_mDark-1_rinv-0.9_alpha-peak_MADPT300_13TeV-madgraphMLM-pythia8_n-3046/part-73.root',
       '/store/user/lpcdarkqcd/boosted/signal_production_3Dscan/2018/MINIAOD/step_MINIAOD_s-channel_mMed-300_mDark-1_rinv-0.9_alpha-peak_MADPT300_13TeV-madgraphMLM-pythia8_n-3046/part-74.root',
       '/store/user/lpcdarkqcd/boosted/signal_production_3Dscan/2018/MINIAOD/step_MINIAOD_s-channel_mMed-300_mDark-1_rinv-0.9_alpha-peak_MADPT300_13TeV-madgraphMLM-pythia8_n-3046/part-75.root',
] )
