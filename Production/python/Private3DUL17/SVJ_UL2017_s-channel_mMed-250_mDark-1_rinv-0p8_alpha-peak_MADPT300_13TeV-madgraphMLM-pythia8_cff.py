import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/user/lpcdarkqcd/boosted/signal_production_3Dscan/2017/MINIAOD/step_MINIAOD_s-channel_mMed-250_mDark-1_rinv-0.8_alpha-peak_MADPT300_13TeV-madgraphMLM-pythia8_n-2591/part-1.root',
       '/store/user/lpcdarkqcd/boosted/signal_production_3Dscan/2017/MINIAOD/step_MINIAOD_s-channel_mMed-250_mDark-1_rinv-0.8_alpha-peak_MADPT300_13TeV-madgraphMLM-pythia8_n-2591/part-2.root',
       '/store/user/lpcdarkqcd/boosted/signal_production_3Dscan/2017/MINIAOD/step_MINIAOD_s-channel_mMed-250_mDark-1_rinv-0.8_alpha-peak_MADPT300_13TeV-madgraphMLM-pythia8_n-2591/part-3.root',
       '/store/user/lpcdarkqcd/boosted/signal_production_3Dscan/2017/MINIAOD/step_MINIAOD_s-channel_mMed-250_mDark-1_rinv-0.8_alpha-peak_MADPT300_13TeV-madgraphMLM-pythia8_n-2591/part-4.root',
       '/store/user/lpcdarkqcd/boosted/signal_production_3Dscan/2017/MINIAOD/step_MINIAOD_s-channel_mMed-250_mDark-1_rinv-0.8_alpha-peak_MADPT300_13TeV-madgraphMLM-pythia8_n-2591/part-5.root',
       '/store/user/lpcdarkqcd/boosted/signal_production_3Dscan/2017/MINIAOD/step_MINIAOD_s-channel_mMed-250_mDark-1_rinv-0.8_alpha-peak_MADPT300_13TeV-madgraphMLM-pythia8_n-2591/part-6.root',
       '/store/user/lpcdarkqcd/boosted/signal_production_3Dscan/2017/MINIAOD/step_MINIAOD_s-channel_mMed-250_mDark-1_rinv-0.8_alpha-peak_MADPT300_13TeV-madgraphMLM-pythia8_n-2591/part-7.root',
       '/store/user/lpcdarkqcd/boosted/signal_production_3Dscan/2017/MINIAOD/step_MINIAOD_s-channel_mMed-250_mDark-1_rinv-0.8_alpha-peak_MADPT300_13TeV-madgraphMLM-pythia8_n-2591/part-8.root',
       '/store/user/lpcdarkqcd/boosted/signal_production_3Dscan/2017/MINIAOD/step_MINIAOD_s-channel_mMed-250_mDark-1_rinv-0.8_alpha-peak_MADPT300_13TeV-madgraphMLM-pythia8_n-2591/part-9.root',
       '/store/user/lpcdarkqcd/boosted/signal_production_3Dscan/2017/MINIAOD/step_MINIAOD_s-channel_mMed-250_mDark-1_rinv-0.8_alpha-peak_MADPT300_13TeV-madgraphMLM-pythia8_n-2591/part-10.root',
       '/store/user/lpcdarkqcd/boosted/signal_production_3Dscan/2017/MINIAOD/step_MINIAOD_s-channel_mMed-250_mDark-1_rinv-0.8_alpha-peak_MADPT300_13TeV-madgraphMLM-pythia8_n-2591/part-11.root',
       '/store/user/lpcdarkqcd/boosted/signal_production_3Dscan/2017/MINIAOD/step_MINIAOD_s-channel_mMed-250_mDark-1_rinv-0.8_alpha-peak_MADPT300_13TeV-madgraphMLM-pythia8_n-2591/part-12.root',
       '/store/user/lpcdarkqcd/boosted/signal_production_3Dscan/2017/MINIAOD/step_MINIAOD_s-channel_mMed-250_mDark-1_rinv-0.8_alpha-peak_MADPT300_13TeV-madgraphMLM-pythia8_n-2591/part-13.root',
       '/store/user/lpcdarkqcd/boosted/signal_production_3Dscan/2017/MINIAOD/step_MINIAOD_s-channel_mMed-250_mDark-1_rinv-0.8_alpha-peak_MADPT300_13TeV-madgraphMLM-pythia8_n-2591/part-14.root',
       '/store/user/lpcdarkqcd/boosted/signal_production_3Dscan/2017/MINIAOD/step_MINIAOD_s-channel_mMed-250_mDark-1_rinv-0.8_alpha-peak_MADPT300_13TeV-madgraphMLM-pythia8_n-2591/part-15.root',
       '/store/user/lpcdarkqcd/boosted/signal_production_3Dscan/2017/MINIAOD/step_MINIAOD_s-channel_mMed-250_mDark-1_rinv-0.8_alpha-peak_MADPT300_13TeV-madgraphMLM-pythia8_n-2591/part-16.root',
       '/store/user/lpcdarkqcd/boosted/signal_production_3Dscan/2017/MINIAOD/step_MINIAOD_s-channel_mMed-250_mDark-1_rinv-0.8_alpha-peak_MADPT300_13TeV-madgraphMLM-pythia8_n-2591/part-17.root',
       '/store/user/lpcdarkqcd/boosted/signal_production_3Dscan/2017/MINIAOD/step_MINIAOD_s-channel_mMed-250_mDark-1_rinv-0.8_alpha-peak_MADPT300_13TeV-madgraphMLM-pythia8_n-2591/part-18.root',
       '/store/user/lpcdarkqcd/boosted/signal_production_3Dscan/2017/MINIAOD/step_MINIAOD_s-channel_mMed-250_mDark-1_rinv-0.8_alpha-peak_MADPT300_13TeV-madgraphMLM-pythia8_n-2591/part-19.root',
       '/store/user/lpcdarkqcd/boosted/signal_production_3Dscan/2017/MINIAOD/step_MINIAOD_s-channel_mMed-250_mDark-1_rinv-0.8_alpha-peak_MADPT300_13TeV-madgraphMLM-pythia8_n-2591/part-20.root',
       '/store/user/lpcdarkqcd/boosted/signal_production_3Dscan/2017/MINIAOD/step_MINIAOD_s-channel_mMed-250_mDark-1_rinv-0.8_alpha-peak_MADPT300_13TeV-madgraphMLM-pythia8_n-2591/part-21.root',
       '/store/user/lpcdarkqcd/boosted/signal_production_3Dscan/2017/MINIAOD/step_MINIAOD_s-channel_mMed-250_mDark-1_rinv-0.8_alpha-peak_MADPT300_13TeV-madgraphMLM-pythia8_n-2591/part-22.root',
       '/store/user/lpcdarkqcd/boosted/signal_production_3Dscan/2017/MINIAOD/step_MINIAOD_s-channel_mMed-250_mDark-1_rinv-0.8_alpha-peak_MADPT300_13TeV-madgraphMLM-pythia8_n-2591/part-23.root',
       '/store/user/lpcdarkqcd/boosted/signal_production_3Dscan/2017/MINIAOD/step_MINIAOD_s-channel_mMed-250_mDark-1_rinv-0.8_alpha-peak_MADPT300_13TeV-madgraphMLM-pythia8_n-2591/part-24.root',
       '/store/user/lpcdarkqcd/boosted/signal_production_3Dscan/2017/MINIAOD/step_MINIAOD_s-channel_mMed-250_mDark-1_rinv-0.8_alpha-peak_MADPT300_13TeV-madgraphMLM-pythia8_n-2591/part-25.root',
       '/store/user/lpcdarkqcd/boosted/signal_production_3Dscan/2017/MINIAOD/step_MINIAOD_s-channel_mMed-250_mDark-1_rinv-0.8_alpha-peak_MADPT300_13TeV-madgraphMLM-pythia8_n-2591/part-26.root',
       '/store/user/lpcdarkqcd/boosted/signal_production_3Dscan/2017/MINIAOD/step_MINIAOD_s-channel_mMed-250_mDark-1_rinv-0.8_alpha-peak_MADPT300_13TeV-madgraphMLM-pythia8_n-2591/part-27.root',
       '/store/user/lpcdarkqcd/boosted/signal_production_3Dscan/2017/MINIAOD/step_MINIAOD_s-channel_mMed-250_mDark-1_rinv-0.8_alpha-peak_MADPT300_13TeV-madgraphMLM-pythia8_n-2591/part-28.root',
       '/store/user/lpcdarkqcd/boosted/signal_production_3Dscan/2017/MINIAOD/step_MINIAOD_s-channel_mMed-250_mDark-1_rinv-0.8_alpha-peak_MADPT300_13TeV-madgraphMLM-pythia8_n-2591/part-29.root',
       '/store/user/lpcdarkqcd/boosted/signal_production_3Dscan/2017/MINIAOD/step_MINIAOD_s-channel_mMed-250_mDark-1_rinv-0.8_alpha-peak_MADPT300_13TeV-madgraphMLM-pythia8_n-2591/part-30.root',
       '/store/user/lpcdarkqcd/boosted/signal_production_3Dscan/2017/MINIAOD/step_MINIAOD_s-channel_mMed-250_mDark-1_rinv-0.8_alpha-peak_MADPT300_13TeV-madgraphMLM-pythia8_n-2591/part-31.root',
       '/store/user/lpcdarkqcd/boosted/signal_production_3Dscan/2017/MINIAOD/step_MINIAOD_s-channel_mMed-250_mDark-1_rinv-0.8_alpha-peak_MADPT300_13TeV-madgraphMLM-pythia8_n-2591/part-32.root',
       '/store/user/lpcdarkqcd/boosted/signal_production_3Dscan/2017/MINIAOD/step_MINIAOD_s-channel_mMed-250_mDark-1_rinv-0.8_alpha-peak_MADPT300_13TeV-madgraphMLM-pythia8_n-2591/part-33.root',
       '/store/user/lpcdarkqcd/boosted/signal_production_3Dscan/2017/MINIAOD/step_MINIAOD_s-channel_mMed-250_mDark-1_rinv-0.8_alpha-peak_MADPT300_13TeV-madgraphMLM-pythia8_n-2591/part-34.root',
       '/store/user/lpcdarkqcd/boosted/signal_production_3Dscan/2017/MINIAOD/step_MINIAOD_s-channel_mMed-250_mDark-1_rinv-0.8_alpha-peak_MADPT300_13TeV-madgraphMLM-pythia8_n-2591/part-35.root',
       '/store/user/lpcdarkqcd/boosted/signal_production_3Dscan/2017/MINIAOD/step_MINIAOD_s-channel_mMed-250_mDark-1_rinv-0.8_alpha-peak_MADPT300_13TeV-madgraphMLM-pythia8_n-2591/part-36.root',
       '/store/user/lpcdarkqcd/boosted/signal_production_3Dscan/2017/MINIAOD/step_MINIAOD_s-channel_mMed-250_mDark-1_rinv-0.8_alpha-peak_MADPT300_13TeV-madgraphMLM-pythia8_n-2591/part-37.root',
       '/store/user/lpcdarkqcd/boosted/signal_production_3Dscan/2017/MINIAOD/step_MINIAOD_s-channel_mMed-250_mDark-1_rinv-0.8_alpha-peak_MADPT300_13TeV-madgraphMLM-pythia8_n-2591/part-38.root',
       '/store/user/lpcdarkqcd/boosted/signal_production_3Dscan/2017/MINIAOD/step_MINIAOD_s-channel_mMed-250_mDark-1_rinv-0.8_alpha-peak_MADPT300_13TeV-madgraphMLM-pythia8_n-2591/part-39.root',
       '/store/user/lpcdarkqcd/boosted/signal_production_3Dscan/2017/MINIAOD/step_MINIAOD_s-channel_mMed-250_mDark-1_rinv-0.8_alpha-peak_MADPT300_13TeV-madgraphMLM-pythia8_n-2591/part-40.root',
       '/store/user/lpcdarkqcd/boosted/signal_production_3Dscan/2017/MINIAOD/step_MINIAOD_s-channel_mMed-250_mDark-1_rinv-0.8_alpha-peak_MADPT300_13TeV-madgraphMLM-pythia8_n-2591/part-41.root',
       '/store/user/lpcdarkqcd/boosted/signal_production_3Dscan/2017/MINIAOD/step_MINIAOD_s-channel_mMed-250_mDark-1_rinv-0.8_alpha-peak_MADPT300_13TeV-madgraphMLM-pythia8_n-2591/part-42.root',
       '/store/user/lpcdarkqcd/boosted/signal_production_3Dscan/2017/MINIAOD/step_MINIAOD_s-channel_mMed-250_mDark-1_rinv-0.8_alpha-peak_MADPT300_13TeV-madgraphMLM-pythia8_n-2591/part-43.root',
       '/store/user/lpcdarkqcd/boosted/signal_production_3Dscan/2017/MINIAOD/step_MINIAOD_s-channel_mMed-250_mDark-1_rinv-0.8_alpha-peak_MADPT300_13TeV-madgraphMLM-pythia8_n-2591/part-44.root',
       '/store/user/lpcdarkqcd/boosted/signal_production_3Dscan/2017/MINIAOD/step_MINIAOD_s-channel_mMed-250_mDark-1_rinv-0.8_alpha-peak_MADPT300_13TeV-madgraphMLM-pythia8_n-2591/part-45.root',
       '/store/user/lpcdarkqcd/boosted/signal_production_3Dscan/2017/MINIAOD/step_MINIAOD_s-channel_mMed-250_mDark-1_rinv-0.8_alpha-peak_MADPT300_13TeV-madgraphMLM-pythia8_n-2591/part-46.root',
       '/store/user/lpcdarkqcd/boosted/signal_production_3Dscan/2017/MINIAOD/step_MINIAOD_s-channel_mMed-250_mDark-1_rinv-0.8_alpha-peak_MADPT300_13TeV-madgraphMLM-pythia8_n-2591/part-47.root',
       '/store/user/lpcdarkqcd/boosted/signal_production_3Dscan/2017/MINIAOD/step_MINIAOD_s-channel_mMed-250_mDark-1_rinv-0.8_alpha-peak_MADPT300_13TeV-madgraphMLM-pythia8_n-2591/part-48.root',
       '/store/user/lpcdarkqcd/boosted/signal_production_3Dscan/2017/MINIAOD/step_MINIAOD_s-channel_mMed-250_mDark-1_rinv-0.8_alpha-peak_MADPT300_13TeV-madgraphMLM-pythia8_n-2591/part-49.root',
       '/store/user/lpcdarkqcd/boosted/signal_production_3Dscan/2017/MINIAOD/step_MINIAOD_s-channel_mMed-250_mDark-1_rinv-0.8_alpha-peak_MADPT300_13TeV-madgraphMLM-pythia8_n-2591/part-50.root',
       '/store/user/lpcdarkqcd/boosted/signal_production_3Dscan/2017/MINIAOD/step_MINIAOD_s-channel_mMed-250_mDark-1_rinv-0.8_alpha-peak_MADPT300_13TeV-madgraphMLM-pythia8_n-2591/part-51.root',
       '/store/user/lpcdarkqcd/boosted/signal_production_3Dscan/2017/MINIAOD/step_MINIAOD_s-channel_mMed-250_mDark-1_rinv-0.8_alpha-peak_MADPT300_13TeV-madgraphMLM-pythia8_n-2591/part-52.root',
] )
