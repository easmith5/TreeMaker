import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/user/lpcdarkqcd/boosted/signal_production_3Dscan/2016/MINIAOD/step_MINIAOD_s-channel_mMed-300_mDark-10_rinv-0.7_alpha-peak_MADPT300_13TeV-madgraphMLM-pythia8_n-2243/part-1.root',
       '/store/user/lpcdarkqcd/boosted/signal_production_3Dscan/2016/MINIAOD/step_MINIAOD_s-channel_mMed-300_mDark-10_rinv-0.7_alpha-peak_MADPT300_13TeV-madgraphMLM-pythia8_n-2243/part-2.root',
       '/store/user/lpcdarkqcd/boosted/signal_production_3Dscan/2016/MINIAOD/step_MINIAOD_s-channel_mMed-300_mDark-10_rinv-0.7_alpha-peak_MADPT300_13TeV-madgraphMLM-pythia8_n-2243/part-3.root',
       '/store/user/lpcdarkqcd/boosted/signal_production_3Dscan/2016/MINIAOD/step_MINIAOD_s-channel_mMed-300_mDark-10_rinv-0.7_alpha-peak_MADPT300_13TeV-madgraphMLM-pythia8_n-2243/part-4.root',
       '/store/user/lpcdarkqcd/boosted/signal_production_3Dscan/2016/MINIAOD/step_MINIAOD_s-channel_mMed-300_mDark-10_rinv-0.7_alpha-peak_MADPT300_13TeV-madgraphMLM-pythia8_n-2243/part-5.root',
       '/store/user/lpcdarkqcd/boosted/signal_production_3Dscan/2016/MINIAOD/step_MINIAOD_s-channel_mMed-300_mDark-10_rinv-0.7_alpha-peak_MADPT300_13TeV-madgraphMLM-pythia8_n-2243/part-6.root',
       '/store/user/lpcdarkqcd/boosted/signal_production_3Dscan/2016/MINIAOD/step_MINIAOD_s-channel_mMed-300_mDark-10_rinv-0.7_alpha-peak_MADPT300_13TeV-madgraphMLM-pythia8_n-2243/part-7.root',
       '/store/user/lpcdarkqcd/boosted/signal_production_3Dscan/2016/MINIAOD/step_MINIAOD_s-channel_mMed-300_mDark-10_rinv-0.7_alpha-peak_MADPT300_13TeV-madgraphMLM-pythia8_n-2243/part-8.root',
       '/store/user/lpcdarkqcd/boosted/signal_production_3Dscan/2016/MINIAOD/step_MINIAOD_s-channel_mMed-300_mDark-10_rinv-0.7_alpha-peak_MADPT300_13TeV-madgraphMLM-pythia8_n-2243/part-9.root',
       '/store/user/lpcdarkqcd/boosted/signal_production_3Dscan/2016/MINIAOD/step_MINIAOD_s-channel_mMed-300_mDark-10_rinv-0.7_alpha-peak_MADPT300_13TeV-madgraphMLM-pythia8_n-2243/part-10.root',
       '/store/user/lpcdarkqcd/boosted/signal_production_3Dscan/2016/MINIAOD/step_MINIAOD_s-channel_mMed-300_mDark-10_rinv-0.7_alpha-peak_MADPT300_13TeV-madgraphMLM-pythia8_n-2243/part-11.root',
       '/store/user/lpcdarkqcd/boosted/signal_production_3Dscan/2016/MINIAOD/step_MINIAOD_s-channel_mMed-300_mDark-10_rinv-0.7_alpha-peak_MADPT300_13TeV-madgraphMLM-pythia8_n-2243/part-12.root',
       '/store/user/lpcdarkqcd/boosted/signal_production_3Dscan/2016/MINIAOD/step_MINIAOD_s-channel_mMed-300_mDark-10_rinv-0.7_alpha-peak_MADPT300_13TeV-madgraphMLM-pythia8_n-2243/part-13.root',
       '/store/user/lpcdarkqcd/boosted/signal_production_3Dscan/2016/MINIAOD/step_MINIAOD_s-channel_mMed-300_mDark-10_rinv-0.7_alpha-peak_MADPT300_13TeV-madgraphMLM-pythia8_n-2243/part-14.root',
       '/store/user/lpcdarkqcd/boosted/signal_production_3Dscan/2016/MINIAOD/step_MINIAOD_s-channel_mMed-300_mDark-10_rinv-0.7_alpha-peak_MADPT300_13TeV-madgraphMLM-pythia8_n-2243/part-15.root',
       '/store/user/lpcdarkqcd/boosted/signal_production_3Dscan/2016/MINIAOD/step_MINIAOD_s-channel_mMed-300_mDark-10_rinv-0.7_alpha-peak_MADPT300_13TeV-madgraphMLM-pythia8_n-2243/part-16.root',
       '/store/user/lpcdarkqcd/boosted/signal_production_3Dscan/2016/MINIAOD/step_MINIAOD_s-channel_mMed-300_mDark-10_rinv-0.7_alpha-peak_MADPT300_13TeV-madgraphMLM-pythia8_n-2243/part-17.root',
       '/store/user/lpcdarkqcd/boosted/signal_production_3Dscan/2016/MINIAOD/step_MINIAOD_s-channel_mMed-300_mDark-10_rinv-0.7_alpha-peak_MADPT300_13TeV-madgraphMLM-pythia8_n-2243/part-18.root',
       '/store/user/lpcdarkqcd/boosted/signal_production_3Dscan/2016/MINIAOD/step_MINIAOD_s-channel_mMed-300_mDark-10_rinv-0.7_alpha-peak_MADPT300_13TeV-madgraphMLM-pythia8_n-2243/part-19.root',
       '/store/user/lpcdarkqcd/boosted/signal_production_3Dscan/2016/MINIAOD/step_MINIAOD_s-channel_mMed-300_mDark-10_rinv-0.7_alpha-peak_MADPT300_13TeV-madgraphMLM-pythia8_n-2243/part-20.root',
       '/store/user/lpcdarkqcd/boosted/signal_production_3Dscan/2016/MINIAOD/step_MINIAOD_s-channel_mMed-300_mDark-10_rinv-0.7_alpha-peak_MADPT300_13TeV-madgraphMLM-pythia8_n-2243/part-21.root',
       '/store/user/lpcdarkqcd/boosted/signal_production_3Dscan/2016/MINIAOD/step_MINIAOD_s-channel_mMed-300_mDark-10_rinv-0.7_alpha-peak_MADPT300_13TeV-madgraphMLM-pythia8_n-2243/part-22.root',
       '/store/user/lpcdarkqcd/boosted/signal_production_3Dscan/2016/MINIAOD/step_MINIAOD_s-channel_mMed-300_mDark-10_rinv-0.7_alpha-peak_MADPT300_13TeV-madgraphMLM-pythia8_n-2243/part-23.root',
       '/store/user/lpcdarkqcd/boosted/signal_production_3Dscan/2016/MINIAOD/step_MINIAOD_s-channel_mMed-300_mDark-10_rinv-0.7_alpha-peak_MADPT300_13TeV-madgraphMLM-pythia8_n-2243/part-24.root',
       '/store/user/lpcdarkqcd/boosted/signal_production_3Dscan/2016/MINIAOD/step_MINIAOD_s-channel_mMed-300_mDark-10_rinv-0.7_alpha-peak_MADPT300_13TeV-madgraphMLM-pythia8_n-2243/part-25.root',
       '/store/user/lpcdarkqcd/boosted/signal_production_3Dscan/2016/MINIAOD/step_MINIAOD_s-channel_mMed-300_mDark-10_rinv-0.7_alpha-peak_MADPT300_13TeV-madgraphMLM-pythia8_n-2243/part-26.root',
       '/store/user/lpcdarkqcd/boosted/signal_production_3Dscan/2016/MINIAOD/step_MINIAOD_s-channel_mMed-300_mDark-10_rinv-0.7_alpha-peak_MADPT300_13TeV-madgraphMLM-pythia8_n-2243/part-27.root',
       '/store/user/lpcdarkqcd/boosted/signal_production_3Dscan/2016/MINIAOD/step_MINIAOD_s-channel_mMed-300_mDark-10_rinv-0.7_alpha-peak_MADPT300_13TeV-madgraphMLM-pythia8_n-2243/part-28.root',
       '/store/user/lpcdarkqcd/boosted/signal_production_3Dscan/2016/MINIAOD/step_MINIAOD_s-channel_mMed-300_mDark-10_rinv-0.7_alpha-peak_MADPT300_13TeV-madgraphMLM-pythia8_n-2243/part-29.root',
       '/store/user/lpcdarkqcd/boosted/signal_production_3Dscan/2016/MINIAOD/step_MINIAOD_s-channel_mMed-300_mDark-10_rinv-0.7_alpha-peak_MADPT300_13TeV-madgraphMLM-pythia8_n-2243/part-30.root',
       '/store/user/lpcdarkqcd/boosted/signal_production_3Dscan/2016/MINIAOD/step_MINIAOD_s-channel_mMed-300_mDark-10_rinv-0.7_alpha-peak_MADPT300_13TeV-madgraphMLM-pythia8_n-2243/part-31.root',
       '/store/user/lpcdarkqcd/boosted/signal_production_3Dscan/2016/MINIAOD/step_MINIAOD_s-channel_mMed-300_mDark-10_rinv-0.7_alpha-peak_MADPT300_13TeV-madgraphMLM-pythia8_n-2243/part-32.root',
       '/store/user/lpcdarkqcd/boosted/signal_production_3Dscan/2016/MINIAOD/step_MINIAOD_s-channel_mMed-300_mDark-10_rinv-0.7_alpha-peak_MADPT300_13TeV-madgraphMLM-pythia8_n-2243/part-33.root',
       '/store/user/lpcdarkqcd/boosted/signal_production_3Dscan/2016/MINIAOD/step_MINIAOD_s-channel_mMed-300_mDark-10_rinv-0.7_alpha-peak_MADPT300_13TeV-madgraphMLM-pythia8_n-2243/part-34.root',
       '/store/user/lpcdarkqcd/boosted/signal_production_3Dscan/2016/MINIAOD/step_MINIAOD_s-channel_mMed-300_mDark-10_rinv-0.7_alpha-peak_MADPT300_13TeV-madgraphMLM-pythia8_n-2243/part-35.root',
       '/store/user/lpcdarkqcd/boosted/signal_production_3Dscan/2016/MINIAOD/step_MINIAOD_s-channel_mMed-300_mDark-10_rinv-0.7_alpha-peak_MADPT300_13TeV-madgraphMLM-pythia8_n-2243/part-36.root',
       '/store/user/lpcdarkqcd/boosted/signal_production_3Dscan/2016/MINIAOD/step_MINIAOD_s-channel_mMed-300_mDark-10_rinv-0.7_alpha-peak_MADPT300_13TeV-madgraphMLM-pythia8_n-2243/part-37.root',
       '/store/user/lpcdarkqcd/boosted/signal_production_3Dscan/2016/MINIAOD/step_MINIAOD_s-channel_mMed-300_mDark-10_rinv-0.7_alpha-peak_MADPT300_13TeV-madgraphMLM-pythia8_n-2243/part-38.root',
       '/store/user/lpcdarkqcd/boosted/signal_production_3Dscan/2016/MINIAOD/step_MINIAOD_s-channel_mMed-300_mDark-10_rinv-0.7_alpha-peak_MADPT300_13TeV-madgraphMLM-pythia8_n-2243/part-39.root',
       '/store/user/lpcdarkqcd/boosted/signal_production_3Dscan/2016/MINIAOD/step_MINIAOD_s-channel_mMed-300_mDark-10_rinv-0.7_alpha-peak_MADPT300_13TeV-madgraphMLM-pythia8_n-2243/part-40.root',
       '/store/user/lpcdarkqcd/boosted/signal_production_3Dscan/2016/MINIAOD/step_MINIAOD_s-channel_mMed-300_mDark-10_rinv-0.7_alpha-peak_MADPT300_13TeV-madgraphMLM-pythia8_n-2243/part-41.root',
       '/store/user/lpcdarkqcd/boosted/signal_production_3Dscan/2016/MINIAOD/step_MINIAOD_s-channel_mMed-300_mDark-10_rinv-0.7_alpha-peak_MADPT300_13TeV-madgraphMLM-pythia8_n-2243/part-42.root',
       '/store/user/lpcdarkqcd/boosted/signal_production_3Dscan/2016/MINIAOD/step_MINIAOD_s-channel_mMed-300_mDark-10_rinv-0.7_alpha-peak_MADPT300_13TeV-madgraphMLM-pythia8_n-2243/part-43.root',
       '/store/user/lpcdarkqcd/boosted/signal_production_3Dscan/2016/MINIAOD/step_MINIAOD_s-channel_mMed-300_mDark-10_rinv-0.7_alpha-peak_MADPT300_13TeV-madgraphMLM-pythia8_n-2243/part-44.root',
       '/store/user/lpcdarkqcd/boosted/signal_production_3Dscan/2016/MINIAOD/step_MINIAOD_s-channel_mMed-300_mDark-10_rinv-0.7_alpha-peak_MADPT300_13TeV-madgraphMLM-pythia8_n-2243/part-45.root',
       '/store/user/lpcdarkqcd/boosted/signal_production_3Dscan/2016/MINIAOD/step_MINIAOD_s-channel_mMed-300_mDark-10_rinv-0.7_alpha-peak_MADPT300_13TeV-madgraphMLM-pythia8_n-2243/part-46.root',
] )