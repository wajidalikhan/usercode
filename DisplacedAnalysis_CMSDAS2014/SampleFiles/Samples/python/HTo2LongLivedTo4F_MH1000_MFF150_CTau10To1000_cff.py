sampleDataSet = '/HTo2LongLivedTo4F_MH-1000_MFF-150_CTau10To1000_8TeV-pythia6/Summer12_DR53X-DEBUG_PU_S10_START53_V7A-v2/AODSIM'  

sampleCMSEnergy = 8000

sampleRelease = "CMSSW_5_3_2_patch4" # original (i.e. RECO file) release, not the one we plan to process them with
sampleProcessRelease = "CMSSW_5_3_5" # release used to create new files with

sampleNumEvents = 99016

sampleXSec = 1 # pb

# global tag can be extracted from file using edmProvDump filename|grep globaltag
# note however that this is the tag for *further* processing, not the original tag
sampleGlobalTag = 'START53_V7A::All'

sampleDuplicateCheckMode = 'checkAllFilesOpened'

sampleType = "SIGNALMC"








samplePatDBSName=""

sampleBaseDir="dcap://dcap.pp.rl.ac.uk///pnfs/pp.rl.ac.uk/data/cms/store/user/ejclemen//HTo2LongLivedTo4F_MH-1000_MFF-150_CTau10To1000_8TeV-pythia6/HTo2LongLivedTo4F_MH1000_MFF150_CTau10To1000_pat_20130123/6116ed9d2ff4828f95fa33fe25241a8f/"
samplePatFiles = [
sampleBaseDir+"PATtuple_33_1_Rae.root",
sampleBaseDir+"PATtuple_34_1_VVN.root",
sampleBaseDir+"PATtuple_19_1_tU4.root",
sampleBaseDir+"PATtuple_25_1_KHM.root",
sampleBaseDir+"PATtuple_2_1_1xz.root",
sampleBaseDir+"PATtuple_10_1_zbD.root",
sampleBaseDir+"PATtuple_28_1_HpP.root",
sampleBaseDir+"PATtuple_12_1_doZ.root",
sampleBaseDir+"PATtuple_23_1_pQN.root",
sampleBaseDir+"PATtuple_22_1_3Vh.root",
sampleBaseDir+"PATtuple_26_1_jWm.root",
sampleBaseDir+"PATtuple_30_1_wgX.root",
sampleBaseDir+"PATtuple_46_1_zMJ.root",
sampleBaseDir+"PATtuple_36_1_T5h.root",
sampleBaseDir+"PATtuple_40_1_C0L.root",
sampleBaseDir+"PATtuple_41_1_tHu.root",
sampleBaseDir+"PATtuple_18_1_kmO.root",
sampleBaseDir+"PATtuple_16_1_wzK.root",
sampleBaseDir+"PATtuple_31_1_zdx.root",
sampleBaseDir+"PATtuple_7_1_R6H.root",
sampleBaseDir+"PATtuple_3_1_81F.root",
sampleBaseDir+"PATtuple_27_1_WLb.root",
sampleBaseDir+"PATtuple_29_1_PDW.root",
sampleBaseDir+"PATtuple_1_1_Fxj.root",
sampleBaseDir+"PATtuple_24_1_1Tf.root",
sampleBaseDir+"PATtuple_11_1_VrO.root",
sampleBaseDir+"PATtuple_13_1_jL4.root",
sampleBaseDir+"PATtuple_49_1_B96.root",
sampleBaseDir+"PATtuple_48_1_N2n.root",
sampleBaseDir+"PATtuple_43_1_9Ak.root",
sampleBaseDir+"PATtuple_47_1_1B4.root",
sampleBaseDir+"PATtuple_35_1_pdh.root",
sampleBaseDir+"PATtuple_44_1_c5t.root",
sampleBaseDir+"PATtuple_21_1_5ob.root",
sampleBaseDir+"PATtuple_20_1_rU1.root",
sampleBaseDir+"PATtuple_17_1_p4F.root",
sampleBaseDir+"PATtuple_37_1_jCm.root",
sampleBaseDir+"PATtuple_15_1_jKR.root",
sampleBaseDir+"PATtuple_42_1_Zxf.root",
sampleBaseDir+"PATtuple_14_1_C4W.root",
sampleBaseDir+"PATtuple_32_1_CJq.root",
sampleBaseDir+"PATtuple_6_1_yqT.root",
sampleBaseDir+"PATtuple_39_1_E76.root",
sampleBaseDir+"PATtuple_45_1_KWk.root",
sampleBaseDir+"PATtuple_38_1_HEJ.root",
sampleBaseDir+"PATtuple_8_1_K4C.root",
sampleBaseDir+"PATtuple_9_1_Xhh.root",
sampleBaseDir+"PATtuple_4_1_ORR.root",
sampleBaseDir+"PATtuple_5_1_tZH.root",
sampleBaseDir+"PATtuple_50_1_9Wy.root",
]
