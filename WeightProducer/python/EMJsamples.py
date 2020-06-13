import FWCore.ParameterSet.Config as cms
from TreeMaker.WeightProducer.MCSample import MCSample
EMJsamples = [
MCSample("step4_MINIAOD_mMed-1000_mDark-20_kappa-1_aligned-down", "ProductionV1", "", "Constant", 5000),
MCSample("step4_MINIAOD_mMed-1000_mDark-20_kappa-0p56_aligned-down", "ProductionV1", "", "Constant", 5000),
MCSample("step4_MINIAOD_mMed-1000_mDark-20_kappa-0p37_aligned-down", "ProductionV1", "", "Constant", 5000),
MCSample("step4_MINIAOD_mMed-1000_mDark-20_kappa-0p25_aligned-down", "ProductionV1", "", "Constant", 5000),
MCSample("step4_MINIAOD_mMed-1000_mDark-20_kappa-0p21_aligned-down", "ProductionV1", "", "Constant", 5000),
MCSample("step4_MINIAOD_mMed-1000_mDark-20_kappa-0p18_aligned-down", "ProductionV1", "", "Constant", 5000),
MCSample("step4_MINIAOD_mMed-1000_mDark-20_kappa-0p12_aligned-down", "ProductionV1", "", "Constant", 5000),
MCSample("step4_MINIAOD_mMed-1200_mDark-20_kappa-1_aligned-down", "ProductionV1", "", "Constant", 5000),
MCSample("step4_MINIAOD_mMed-1200_mDark-20_kappa-0p45_aligned-down", "ProductionV1", "", "Constant", 5000),
MCSample("step4_MINIAOD_mMed-1200_mDark-20_kappa-0p3_aligned-down", "ProductionV1", "", "Constant", 5000),
MCSample("step4_MINIAOD_mMed-1200_mDark-20_kappa-0p26_aligned-down", "ProductionV1", "", "Constant", 5000),
MCSample("step4_MINIAOD_mMed-1200_mDark-20_kappa-0p21_aligned-down", "ProductionV1", "", "Constant", 5000),
MCSample("step4_MINIAOD_mMed-1200_mDark-20_kappa-0p14_aligned-down", "ProductionV1", "", "Constant", 5000),
MCSample("step4_MINIAOD_mMed-1600_mDark-20_kappa-1_aligned-down", "ProductionV1", "", "Constant", 5000),
MCSample("step4_MINIAOD_mMed-1600_mDark-20_kappa-0p59_aligned-down", "ProductionV1", "", "Constant", 5000),
MCSample("step4_MINIAOD_mMed-1600_mDark-20_kappa-0p4_aligned-down", "ProductionV1", "", "Constant", 5000),
MCSample("step4_MINIAOD_mMed-1600_mDark-20_kappa-0p34_aligned-down", "ProductionV1", "", "Constant", 5000),
MCSample("step4_MINIAOD_mMed-1600_mDark-20_kappa-0p28_aligned-down", "ProductionV1", "", "Constant", 5000),
MCSample("step4_MINIAOD_mMed-1600_mDark-20_kappa-0p19_aligned-down", "ProductionV1", "", "Constant", 5000),
MCSample("step4_MINIAOD_mMed-1400_mDark-20_kappa-1_aligned-down", "ProductionV1", "", "Constant", 5000),
MCSample("step4_MINIAOD_mMed-1400_mDark-20_kappa-0p52_aligned-down", "ProductionV1", "", "Constant", 5000),
MCSample("step4_MINIAOD_mMed-1400_mDark-20_kappa-0p35_aligned-down", "ProductionV1", "", "Constant", 5000),
MCSample("step4_MINIAOD_mMed-1400_mDark-20_kappa-0p3_aligned-down", "ProductionV1", "", "Constant", 5000),
MCSample("step4_MINIAOD_mMed-1400_mDark-20_kappa-0p25_aligned-down", "ProductionV1", "", "Constant", 5000),
MCSample("step4_MINIAOD_mMed-1400_mDark-20_kappa-0p16_aligned-down", "ProductionV1", "", "Constant", 5000),
MCSample("step4_MINIAOD_mMed-1500_mDark-4_kappa-1_aligned-up", "ProductionV1", "", "Constant", 5000),
MCSample("step4_MINIAOD_mMed-1000_mDark-10_ctau-0p1_unflavored-down", "ProductionV1", "", "Constant", 5000),
MCSample("step4_MINIAOD_mMed-1000_mDark-10_ctau-1_unflavored-down", "ProductionV1", "", "Constant", 5000),
MCSample("step4_MINIAOD_mMed-1000_mDark-10_ctau-2_unflavored-down", "ProductionV1", "", "Constant", 5000),
MCSample("step4_MINIAOD_mMed-1000_mDark-10_ctau-5_unflavored-down", "ProductionV1", "", "Constant", 5000),
MCSample("step4_MINIAOD_mMed-1000_mDark-10_ctau-25_unflavored-down", "ProductionV1", "", "Constant", 5000),
MCSample("step4_MINIAOD_mMed-1000_mDark-10_ctau-45_unflavored-down", "ProductionV1", "", "Constant", 5000),
MCSample("step4_MINIAOD_mMed-1000_mDark-10_ctau-60_unflavored-down", "ProductionV1", "", "Constant", 5000),
MCSample("step4_MINIAOD_mMed-1000_mDark-10_ctau-100_unflavored-down", "ProductionV1", "", "Constant", 5000),
MCSample("step4_MINIAOD_mMed-1000_mDark-10_ctau-150_unflavored-down", "ProductionV1", "", "Constant", 5000),
MCSample("step4_MINIAOD_mMed-1000_mDark-10_ctau-225_unflavored-down", "ProductionV1", "", "Constant", 5000),
MCSample("step4_MINIAOD_mMed-1000_mDark-10_ctau-300_unflavored-down", "ProductionV1", "", "Constant", 5000),
MCSample("step4_MINIAOD_mMed-1000_mDark-10_ctau-500_unflavored-down", "ProductionV1", "", "Constant", 5000),
MCSample("step4_MINIAOD_mMed-1000_mDark-10_ctau-1000_unflavored-down", "ProductionV1", "", "Constant", 5000),
MCSample("step4_MINIAOD_mMed-1000_mDark-20_ctau-0p1_unflavored-down", "ProductionV1", "", "Constant", 5000),
MCSample("step4_MINIAOD_mMed-1000_mDark-20_ctau-1_unflavored-down", "ProductionV1", "", "Constant", 5000),
MCSample("step4_MINIAOD_mMed-1000_mDark-20_ctau-2_unflavored-down", "ProductionV1", "", "Constant", 5000),
MCSample("step4_MINIAOD_mMed-1000_mDark-20_ctau-5_unflavored-down", "ProductionV1", "", "Constant", 5000),
MCSample("step4_MINIAOD_mMed-1000_mDark-20_ctau-25_unflavored-down", "ProductionV1", "", "Constant", 5000),
MCSample("step4_MINIAOD_mMed-1000_mDark-20_ctau-45_unflavored-down", "ProductionV1", "", "Constant", 5000),
MCSample("step4_MINIAOD_mMed-1000_mDark-20_ctau-60_unflavored-down", "ProductionV1", "", "Constant", 5000),
MCSample("step4_MINIAOD_mMed-1000_mDark-20_ctau-100_unflavored-down", "ProductionV1", "", "Constant", 5000),
MCSample("step4_MINIAOD_mMed-1000_mDark-20_ctau-150_unflavored-down", "ProductionV1", "", "Constant", 5000),
MCSample("step4_MINIAOD_mMed-1000_mDark-20_ctau-225_unflavored-down", "ProductionV1", "", "Constant", 5000),
MCSample("step4_MINIAOD_mMed-1000_mDark-20_ctau-300_unflavored-down", "ProductionV1", "", "Constant", 5000),
MCSample("step4_MINIAOD_mMed-1000_mDark-20_ctau-500_unflavored-down", "ProductionV1", "", "Constant", 5000),
MCSample("step4_MINIAOD_mMed-1000_mDark-20_ctau-1000_unflavored-down", "ProductionV1", "", "Constant", 5000),
MCSample("step4_MINIAOD_mMed-1200_mDark-10_ctau-0p1_unflavored-down", "ProductionV1", "", "Constant", 5000),
MCSample("step4_MINIAOD_mMed-1200_mDark-10_ctau-1_unflavored-down", "ProductionV1", "", "Constant", 5000),
MCSample("step4_MINIAOD_mMed-1200_mDark-10_ctau-2_unflavored-down", "ProductionV1", "", "Constant", 5000),
MCSample("step4_MINIAOD_mMed-1200_mDark-10_ctau-5_unflavored-down", "ProductionV1", "", "Constant", 5000),
MCSample("step4_MINIAOD_mMed-1200_mDark-10_ctau-25_unflavored-down", "ProductionV1", "", "Constant", 5000),
MCSample("step4_MINIAOD_mMed-1200_mDark-10_ctau-45_unflavored-down", "ProductionV1", "", "Constant", 5000),
MCSample("step4_MINIAOD_mMed-1200_mDark-10_ctau-60_unflavored-down", "ProductionV1", "", "Constant", 5000),
MCSample("step4_MINIAOD_mMed-1200_mDark-10_ctau-100_unflavored-down", "ProductionV1", "", "Constant", 5000),
MCSample("step4_MINIAOD_mMed-1200_mDark-10_ctau-150_unflavored-down", "ProductionV1", "", "Constant", 5000),
MCSample("step4_MINIAOD_mMed-1200_mDark-10_ctau-225_unflavored-down", "ProductionV1", "", "Constant", 5000),
MCSample("step4_MINIAOD_mMed-1200_mDark-10_ctau-300_unflavored-down", "ProductionV1", "", "Constant", 5000),
MCSample("step4_MINIAOD_mMed-1200_mDark-10_ctau-500_unflavored-down", "ProductionV1", "", "Constant", 5000),
MCSample("step4_MINIAOD_mMed-1200_mDark-10_ctau-1000_unflavored-down", "ProductionV1", "", "Constant", 5000),
MCSample("step4_MINIAOD_mMed-1200_mDark-20_ctau-0p1_unflavored-down", "ProductionV1", "", "Constant", 5000),
MCSample("step4_MINIAOD_mMed-1200_mDark-20_ctau-1_unflavored-down", "ProductionV1", "", "Constant", 5000),
MCSample("step4_MINIAOD_mMed-1200_mDark-20_ctau-2_unflavored-down", "ProductionV1", "", "Constant", 5000),
MCSample("step4_MINIAOD_mMed-1200_mDark-20_ctau-5_unflavored-down", "ProductionV1", "", "Constant", 5000),
MCSample("step4_MINIAOD_mMed-1200_mDark-20_ctau-25_unflavored-down", "ProductionV1", "", "Constant", 5000),
MCSample("step4_MINIAOD_mMed-1200_mDark-20_ctau-45_unflavored-down", "ProductionV1", "", "Constant", 5000),
MCSample("step4_MINIAOD_mMed-1200_mDark-20_ctau-60_unflavored-down", "ProductionV1", "", "Constant", 5000),
MCSample("step4_MINIAOD_mMed-1200_mDark-20_ctau-100_unflavored-down", "ProductionV1", "", "Constant", 5000),
MCSample("step4_MINIAOD_mMed-1200_mDark-20_ctau-150_unflavored-down", "ProductionV1", "", "Constant", 5000),
MCSample("step4_MINIAOD_mMed-1200_mDark-20_ctau-225_unflavored-down", "ProductionV1", "", "Constant", 5000),
MCSample("step4_MINIAOD_mMed-1200_mDark-20_ctau-300_unflavored-down", "ProductionV1", "", "Constant", 5000),
MCSample("step4_MINIAOD_mMed-1200_mDark-20_ctau-500_unflavored-down", "ProductionV1", "", "Constant", 5000),
MCSample("step4_MINIAOD_mMed-1200_mDark-20_ctau-1000_unflavored-down", "ProductionV1", "", "Constant", 5000),
MCSample("step4_MINIAOD_mMed-1400_mDark-10_ctau-0p1_unflavored-down", "ProductionV1", "", "Constant", 5000),
MCSample("step4_MINIAOD_mMed-1400_mDark-10_ctau-1_unflavored-down", "ProductionV1", "", "Constant", 5000),
MCSample("step4_MINIAOD_mMed-1400_mDark-10_ctau-2_unflavored-down", "ProductionV1", "", "Constant", 5000),
MCSample("step4_MINIAOD_mMed-1400_mDark-10_ctau-5_unflavored-down", "ProductionV1", "", "Constant", 5000),
MCSample("step4_MINIAOD_mMed-1400_mDark-10_ctau-25_unflavored-down", "ProductionV1", "", "Constant", 5000),
MCSample("step4_MINIAOD_mMed-1400_mDark-10_ctau-45_unflavored-down", "ProductionV1", "", "Constant", 5000),
MCSample("step4_MINIAOD_mMed-1400_mDark-10_ctau-60_unflavored-down", "ProductionV1", "", "Constant", 5000),
MCSample("step4_MINIAOD_mMed-1400_mDark-10_ctau-100_unflavored-down", "ProductionV1", "", "Constant", 5000),
MCSample("step4_MINIAOD_mMed-1400_mDark-10_ctau-150_unflavored-down", "ProductionV1", "", "Constant", 5000),
MCSample("step4_MINIAOD_mMed-1400_mDark-10_ctau-225_unflavored-down", "ProductionV1", "", "Constant", 5000),
MCSample("step4_MINIAOD_mMed-1400_mDark-10_ctau-300_unflavored-down", "ProductionV1", "", "Constant", 5000),
MCSample("step4_MINIAOD_mMed-1400_mDark-10_ctau-500_unflavored-down", "ProductionV1", "", "Constant", 5000),
MCSample("step4_MINIAOD_mMed-1400_mDark-10_ctau-1000_unflavored-down", "ProductionV1", "", "Constant", 5000),
MCSample("step4_MINIAOD_mMed-1400_mDark-20_ctau-0p1_unflavored-down", "ProductionV1", "", "Constant", 5000),
MCSample("step4_MINIAOD_mMed-1400_mDark-20_ctau-1_unflavored-down", "ProductionV1", "", "Constant", 5000),
MCSample("step4_MINIAOD_mMed-1400_mDark-20_ctau-2_unflavored-down", "ProductionV1", "", "Constant", 5000),
MCSample("step4_MINIAOD_mMed-1400_mDark-20_ctau-5_unflavored-down", "ProductionV1", "", "Constant", 5000),
MCSample("step4_MINIAOD_mMed-1400_mDark-20_ctau-25_unflavored-down", "ProductionV1", "", "Constant", 5000),
MCSample("step4_MINIAOD_mMed-1400_mDark-20_ctau-45_unflavored-down", "ProductionV1", "", "Constant", 5000),
MCSample("step4_MINIAOD_mMed-1400_mDark-20_ctau-60_unflavored-down", "ProductionV1", "", "Constant", 5000),
MCSample("step4_MINIAOD_mMed-1400_mDark-20_ctau-100_unflavored-down", "ProductionV1", "", "Constant", 5000),
MCSample("step4_MINIAOD_mMed-1400_mDark-20_ctau-150_unflavored-down", "ProductionV1", "", "Constant", 5000),
MCSample("step4_MINIAOD_mMed-1400_mDark-20_ctau-225_unflavored-down", "ProductionV1", "", "Constant", 5000),
MCSample("step4_MINIAOD_mMed-1400_mDark-20_ctau-300_unflavored-down", "ProductionV1", "", "Constant", 5000),
MCSample("step4_MINIAOD_mMed-1400_mDark-20_ctau-500_unflavored-down", "ProductionV1", "", "Constant", 5000),
MCSample("step4_MINIAOD_mMed-1400_mDark-20_ctau-1000_unflavored-down", "ProductionV1", "", "Constant", 5000),
MCSample("step4_MINIAOD_mMed-1500_mDark-10_ctau-0p1_unflavored-down", "ProductionV1", "", "Constant", 5000),
MCSample("step4_MINIAOD_mMed-1500_mDark-10_ctau-1_unflavored-down", "ProductionV1", "", "Constant", 5000),
MCSample("step4_MINIAOD_mMed-1500_mDark-10_ctau-2_unflavored-down", "ProductionV1", "", "Constant", 5000),
MCSample("step4_MINIAOD_mMed-1500_mDark-10_ctau-5_unflavored-down", "ProductionV1", "", "Constant", 5000),
MCSample("step4_MINIAOD_mMed-1500_mDark-10_ctau-25_unflavored-down", "ProductionV1", "", "Constant", 5000),
MCSample("step4_MINIAOD_mMed-1500_mDark-10_ctau-45_unflavored-down", "ProductionV1", "", "Constant", 5000),
MCSample("step4_MINIAOD_mMed-1500_mDark-10_ctau-60_unflavored-down", "ProductionV1", "", "Constant", 5000),
MCSample("step4_MINIAOD_mMed-1500_mDark-10_ctau-100_unflavored-down", "ProductionV1", "", "Constant", 5000),
MCSample("step4_MINIAOD_mMed-1500_mDark-10_ctau-150_unflavored-down", "ProductionV1", "", "Constant", 5000),
MCSample("step4_MINIAOD_mMed-1500_mDark-10_ctau-225_unflavored-down", "ProductionV1", "", "Constant", 5000),
MCSample("step4_MINIAOD_mMed-1500_mDark-10_ctau-300_unflavored-down", "ProductionV1", "", "Constant", 5000),
MCSample("step4_MINIAOD_mMed-1500_mDark-10_ctau-500_unflavored-down", "ProductionV1", "", "Constant", 5000),
MCSample("step4_MINIAOD_mMed-1500_mDark-10_ctau-1000_unflavored-down", "ProductionV1", "", "Constant", 5000),
MCSample("step4_MINIAOD_mMed-1500_mDark-20_ctau-0p1_unflavored-down", "ProductionV1", "", "Constant", 5000),
MCSample("step4_MINIAOD_mMed-1500_mDark-20_ctau-1_unflavored-down", "ProductionV1", "", "Constant", 5000),
MCSample("step4_MINIAOD_mMed-1500_mDark-20_ctau-2_unflavored-down", "ProductionV1", "", "Constant", 5000),
MCSample("step4_MINIAOD_mMed-1500_mDark-20_ctau-5_unflavored-down", "ProductionV1", "", "Constant", 5000),
MCSample("step4_MINIAOD_mMed-1500_mDark-20_ctau-25_unflavored-down", "ProductionV1", "", "Constant", 5000),
MCSample("step4_MINIAOD_mMed-1500_mDark-20_ctau-45_unflavored-down", "ProductionV1", "", "Constant", 5000),
MCSample("step4_MINIAOD_mMed-1500_mDark-20_ctau-60_unflavored-down", "ProductionV1", "", "Constant", 5000),
MCSample("step4_MINIAOD_mMed-1500_mDark-20_ctau-100_unflavored-down", "ProductionV1", "", "Constant", 5000),
MCSample("step4_MINIAOD_mMed-1500_mDark-20_ctau-150_unflavored-down", "ProductionV1", "", "Constant", 5000),
MCSample("step4_MINIAOD_mMed-1500_mDark-20_ctau-225_unflavored-down", "ProductionV1", "", "Constant", 5000),
MCSample("step4_MINIAOD_mMed-1500_mDark-20_ctau-300_unflavored-down", "ProductionV1", "", "Constant", 5000),
MCSample("step4_MINIAOD_mMed-1500_mDark-20_ctau-500_unflavored-down", "ProductionV1", "", "Constant", 5000),
MCSample("step4_MINIAOD_mMed-1500_mDark-20_ctau-1000_unflavored-down", "ProductionV1", "", "Constant", 5000),
MCSample("step4_MINIAOD_mMed-1600_mDark-10_ctau-0p1_unflavored-down", "ProductionV1", "", "Constant", 5000),
MCSample("step4_MINIAOD_mMed-1600_mDark-10_ctau-1_unflavored-down", "ProductionV1", "", "Constant", 5000),
MCSample("step4_MINIAOD_mMed-1600_mDark-10_ctau-2_unflavored-down", "ProductionV1", "", "Constant", 5000),
MCSample("step4_MINIAOD_mMed-1600_mDark-10_ctau-5_unflavored-down", "ProductionV1", "", "Constant", 5000),
MCSample("step4_MINIAOD_mMed-1600_mDark-10_ctau-25_unflavored-down", "ProductionV1", "", "Constant", 5000),
MCSample("step4_MINIAOD_mMed-1600_mDark-10_ctau-45_unflavored-down", "ProductionV1", "", "Constant", 5000),
MCSample("step4_MINIAOD_mMed-1600_mDark-10_ctau-60_unflavored-down", "ProductionV1", "", "Constant", 5000),
MCSample("step4_MINIAOD_mMed-1600_mDark-10_ctau-100_unflavored-down", "ProductionV1", "", "Constant", 5000),
MCSample("step4_MINIAOD_mMed-1600_mDark-10_ctau-150_unflavored-down", "ProductionV1", "", "Constant", 5000),
MCSample("step4_MINIAOD_mMed-1600_mDark-10_ctau-225_unflavored-down", "ProductionV1", "", "Constant", 5000),
MCSample("step4_MINIAOD_mMed-1600_mDark-10_ctau-300_unflavored-down", "ProductionV1", "", "Constant", 5000),
MCSample("step4_MINIAOD_mMed-1600_mDark-10_ctau-500_unflavored-down", "ProductionV1", "", "Constant", 5000),
MCSample("step4_MINIAOD_mMed-1600_mDark-10_ctau-1000_unflavored-down", "ProductionV1", "", "Constant", 5000),
MCSample("step4_MINIAOD_mMed-1600_mDark-20_ctau-0p1_unflavored-down", "ProductionV1", "", "Constant", 5000),
MCSample("step4_MINIAOD_mMed-1600_mDark-20_ctau-1_unflavored-down", "ProductionV1", "", "Constant", 5000),
MCSample("step4_MINIAOD_mMed-1600_mDark-20_ctau-2_unflavored-down", "ProductionV1", "", "Constant", 5000),
MCSample("step4_MINIAOD_mMed-1600_mDark-20_ctau-5_unflavored-down", "ProductionV1", "", "Constant", 5000),
MCSample("step4_MINIAOD_mMed-1600_mDark-20_ctau-25_unflavored-down", "ProductionV1", "", "Constant", 5000),
MCSample("step4_MINIAOD_mMed-1600_mDark-20_ctau-45_unflavored-down", "ProductionV1", "", "Constant", 5000),
MCSample("step4_MINIAOD_mMed-1600_mDark-20_ctau-60_unflavored-down", "ProductionV1", "", "Constant", 5000),
MCSample("step4_MINIAOD_mMed-1600_mDark-20_ctau-100_unflavored-down", "ProductionV1", "", "Constant", 5000),
MCSample("step4_MINIAOD_mMed-1600_mDark-20_ctau-150_unflavored-down", "ProductionV1", "", "Constant", 5000),
MCSample("step4_MINIAOD_mMed-1600_mDark-20_ctau-225_unflavored-down", "ProductionV1", "", "Constant", 5000),
MCSample("step4_MINIAOD_mMed-1600_mDark-20_ctau-300_unflavored-down", "ProductionV1", "", "Constant", 5000),
MCSample("step4_MINIAOD_mMed-1600_mDark-20_ctau-500_unflavored-down", "ProductionV1", "", "Constant", 5000),
MCSample("step4_MINIAOD_mMed-1600_mDark-20_ctau-1000_unflavored-down", "ProductionV1", "", "Constant", 5000)
]