sampleDataSet = '/QCD_Pt-20to30_MuEnrichedPt5_TuneZ2star_8TeV_pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM'  

sampleCMSEnergy = 8000

sampleRelease = "CMSSW_5_3_2_patch4" # original (i.e. RECO file) release, not the one we plan to process them with
sampleProcessRelease = "CMSSW_5_3_8" # release used to create new files with

sampleNumEvents = 8486904

sampleXSec = 2.87E8 * 0.0065 # pb

# global tag can be extracted from file using edmProvDump filename|grep globaltag
# note however that this is the tag for *further* processing, not the original tag
sampleGlobalTag = 'START53_V7G::All'

sampleDuplicateCheckMode = 'checkAllFilesOpened'

sampleType = "BKGMC"

samplePatDBSName=""

sampleBaseDir="dcap://dcap.pp.rl.ac.uk///pnfs/pp.rl.ac.uk/data/cms/store/user/ejclemen//QCD_Pt-20to30_MuEnrichedPt5_TuneZ2star_8TeV_pythia6/QCDMu20Pt5_pat_20131129/10b5286681675c887ef3085adebe4aeb/"
samplePatFiles = [
sampleBaseDir+"PATtuple_126_7_8YP.root",
sampleBaseDir+"PATtuple_13_6_MDi.root",
sampleBaseDir+"PATtuple_16_6_utS.root",
sampleBaseDir+"PATtuple_115_6_LUJ.root",
sampleBaseDir+"PATtuple_157_5_0su.root",
sampleBaseDir+"PATtuple_149_5_fDQ.root",
sampleBaseDir+"PATtuple_129_7_NOf.root",
sampleBaseDir+"PATtuple_2_6_g7p.root",
sampleBaseDir+"PATtuple_1_6_VPP.root",
sampleBaseDir+"PATtuple_15_2_X6U.root",
sampleBaseDir+"PATtuple_144_3_9pV.root",
sampleBaseDir+"PATtuple_112_3_KSU.root",
sampleBaseDir+"PATtuple_139_3_ELA.root",
sampleBaseDir+"PATtuple_158_2_h9U.root",
sampleBaseDir+"PATtuple_155_2_xLB.root",
sampleBaseDir+"PATtuple_159_2_RhN.root",
sampleBaseDir+"PATtuple_50_2_fXS.root",
sampleBaseDir+"PATtuple_162_2_oTA.root",
sampleBaseDir+"PATtuple_37_2_cBb.root",
sampleBaseDir+"PATtuple_166_2_zv9.root",
sampleBaseDir+"PATtuple_42_2_C5Z.root",
sampleBaseDir+"PATtuple_97_2_G6Z.root",
sampleBaseDir+"PATtuple_55_2_46B.root",
sampleBaseDir+"PATtuple_103_2_ROz.root",
sampleBaseDir+"PATtuple_152_2_WzC.root",
sampleBaseDir+"PATtuple_68_2_0ES.root",
sampleBaseDir+"PATtuple_62_2_wVQ.root",
sampleBaseDir+"PATtuple_45_2_Y6t.root",
sampleBaseDir+"PATtuple_57_2_78W.root",
sampleBaseDir+"PATtuple_41_2_uJ6.root",
sampleBaseDir+"PATtuple_83_2_tLN.root",
sampleBaseDir+"PATtuple_33_2_S6D.root",
sampleBaseDir+"PATtuple_154_2_D8y.root",
sampleBaseDir+"PATtuple_51_2_zjb.root",
sampleBaseDir+"PATtuple_90_2_n2L.root",
sampleBaseDir+"PATtuple_72_2_QuK.root",
sampleBaseDir+"PATtuple_170_2_tJ9.root",
sampleBaseDir+"PATtuple_108_2_3ur.root",
sampleBaseDir+"PATtuple_94_2_cVh.root",
sampleBaseDir+"PATtuple_52_2_MB7.root",
sampleBaseDir+"PATtuple_8_2_eze.root",
sampleBaseDir+"PATtuple_47_2_kpu.root",
sampleBaseDir+"PATtuple_30_2_qPS.root",
sampleBaseDir+"PATtuple_107_2_yVH.root",
sampleBaseDir+"PATtuple_74_2_Y9c.root",
sampleBaseDir+"PATtuple_49_2_7vN.root",
sampleBaseDir+"PATtuple_120_2_yDm.root",
sampleBaseDir+"PATtuple_65_2_nZz.root",
sampleBaseDir+"PATtuple_169_2_98t.root",
sampleBaseDir+"PATtuple_63_2_l4S.root",
sampleBaseDir+"PATtuple_43_2_trf.root",
sampleBaseDir+"PATtuple_79_2_w6F.root",
sampleBaseDir+"PATtuple_67_2_ymO.root",
sampleBaseDir+"PATtuple_84_2_Abp.root",
sampleBaseDir+"PATtuple_164_2_h4W.root",
sampleBaseDir+"PATtuple_71_2_TeL.root",
sampleBaseDir+"PATtuple_100_2_lmC.root",
sampleBaseDir+"PATtuple_77_2_wWv.root",
sampleBaseDir+"PATtuple_106_2_rpH.root",
sampleBaseDir+"PATtuple_69_2_I0B.root",
sampleBaseDir+"PATtuple_101_2_Dfv.root",
sampleBaseDir+"PATtuple_66_2_R8m.root",
sampleBaseDir+"PATtuple_109_2_zy7.root",
sampleBaseDir+"PATtuple_39_2_G3A.root",
sampleBaseDir+"PATtuple_92_2_9vw.root",
sampleBaseDir+"PATtuple_64_2_Of7.root",
sampleBaseDir+"PATtuple_48_2_ZQJ.root",
sampleBaseDir+"PATtuple_171_2_kjg.root",
sampleBaseDir+"PATtuple_76_2_vPV.root",
sampleBaseDir+"PATtuple_140_2_WhO.root",
sampleBaseDir+"PATtuple_136_2_7WK.root",
sampleBaseDir+"PATtuple_127_2_9Fa.root",
sampleBaseDir+"PATtuple_122_2_96T.root",
sampleBaseDir+"PATtuple_132_2_ySF.root",
sampleBaseDir+"PATtuple_167_2_1lv.root",
sampleBaseDir+"PATtuple_99_2_ZmJ.root",
sampleBaseDir+"PATtuple_36_2_0b7.root",
sampleBaseDir+"PATtuple_116_2_VYP.root",
sampleBaseDir+"PATtuple_117_2_a47.root",
sampleBaseDir+"PATtuple_119_2_PGR.root",
sampleBaseDir+"PATtuple_131_2_qub.root",
sampleBaseDir+"PATtuple_137_2_9Ds.root",
sampleBaseDir+"PATtuple_124_2_PCG.root",
sampleBaseDir+"PATtuple_123_2_T9L.root",
sampleBaseDir+"PATtuple_168_2_f3i.root",
sampleBaseDir+"PATtuple_135_2_5f1.root",
sampleBaseDir+"PATtuple_125_2_mZ0.root",
sampleBaseDir+"PATtuple_88_2_l1t.root",
sampleBaseDir+"PATtuple_89_2_0LA.root",
sampleBaseDir+"PATtuple_163_1_FO4.root",
sampleBaseDir+"PATtuple_156_1_YQE.root",
sampleBaseDir+"PATtuple_110_1_kRB.root",
sampleBaseDir+"PATtuple_165_1_G46.root",
sampleBaseDir+"PATtuple_160_1_Q9L.root",
sampleBaseDir+"PATtuple_146_1_KnS.root",
sampleBaseDir+"PATtuple_153_1_5M8.root",
sampleBaseDir+"PATtuple_133_1_kJi.root",
sampleBaseDir+"PATtuple_142_1_4Mb.root",
sampleBaseDir+"PATtuple_134_1_GW8.root",
sampleBaseDir+"PATtuple_141_1_vaG.root",
sampleBaseDir+"PATtuple_20_1_wYD.root",
sampleBaseDir+"PATtuple_54_1_LmK.root",
sampleBaseDir+"PATtuple_102_1_0Yb.root",
sampleBaseDir+"PATtuple_56_1_iSB.root",
sampleBaseDir+"PATtuple_58_1_3A4.root",
sampleBaseDir+"PATtuple_93_1_04l.root",
sampleBaseDir+"PATtuple_87_1_UVp.root",
sampleBaseDir+"PATtuple_73_1_mCt.root",
sampleBaseDir+"PATtuple_82_1_Krx.root",
sampleBaseDir+"PATtuple_113_1_Tac.root",
sampleBaseDir+"PATtuple_53_1_Rh5.root",
sampleBaseDir+"PATtuple_105_1_uMk.root",
sampleBaseDir+"PATtuple_86_1_TDA.root",
sampleBaseDir+"PATtuple_61_1_QQv.root",
sampleBaseDir+"PATtuple_95_1_BnE.root",
sampleBaseDir+"PATtuple_80_1_s1d.root",
sampleBaseDir+"PATtuple_60_1_bgq.root",
sampleBaseDir+"PATtuple_91_1_Yr8.root",
sampleBaseDir+"PATtuple_44_1_9oo.root",
sampleBaseDir+"PATtuple_26_1_pHa.root",
sampleBaseDir+"PATtuple_130_3_JHm.root",
sampleBaseDir+"PATtuple_70_3_sDU.root",
sampleBaseDir+"PATtuple_96_3_Kvk.root",
sampleBaseDir+"PATtuple_151_3_137.root",
sampleBaseDir+"PATtuple_40_3_et8.root",
sampleBaseDir+"PATtuple_19_3_gKe.root",
sampleBaseDir+"PATtuple_118_3_utS.root",
sampleBaseDir+"PATtuple_143_3_ZS3.root",
sampleBaseDir+"PATtuple_85_3_oOH.root",
sampleBaseDir+"PATtuple_46_3_pj0.root",
sampleBaseDir+"PATtuple_147_3_DBW.root",
sampleBaseDir+"PATtuple_18_2_zSv.root",
sampleBaseDir+"PATtuple_17_2_ife.root",
sampleBaseDir+"PATtuple_145_3_OR3.root",
sampleBaseDir+"PATtuple_150_3_D26.root",
sampleBaseDir+"PATtuple_148_3_dfy.root",
sampleBaseDir+"PATtuple_111_3_750.root",
sampleBaseDir+"PATtuple_104_3_Xtc.root",
sampleBaseDir+"PATtuple_128_3_DzJ.root",
sampleBaseDir+"PATtuple_22_2_Dxp.root",
sampleBaseDir+"PATtuple_121_3_byE.root",
sampleBaseDir+"PATtuple_138_3_QAK.root",
sampleBaseDir+"PATtuple_161_3_wcg.root",
sampleBaseDir+"PATtuple_78_1_30O.root",
sampleBaseDir+"PATtuple_98_2_VvF.root",
sampleBaseDir+"PATtuple_59_1_GQJ.root",
sampleBaseDir+"PATtuple_21_1_1rz.root",
sampleBaseDir+"PATtuple_75_2_UYq.root",
sampleBaseDir+"PATtuple_81_1_X2c.root",
sampleBaseDir+"PATtuple_114_2_toR.root",
sampleBaseDir+"PATtuple_35_1_xyl.root",
sampleBaseDir+"PATtuple_25_1_Qm7.root",
sampleBaseDir+"PATtuple_38_1_htY.root",
sampleBaseDir+"PATtuple_31_1_Lfl.root",
sampleBaseDir+"PATtuple_9_1_vHJ.root",
sampleBaseDir+"PATtuple_27_1_aN8.root",
sampleBaseDir+"PATtuple_23_1_Qed.root",
sampleBaseDir+"PATtuple_29_1_C4V.root",
sampleBaseDir+"PATtuple_24_1_D0L.root",
sampleBaseDir+"PATtuple_11_1_Ai7.root",
sampleBaseDir+"PATtuple_28_1_WDr.root",
sampleBaseDir+"PATtuple_10_1_2Gt.root",
sampleBaseDir+"PATtuple_34_1_UmN.root",
sampleBaseDir+"PATtuple_32_1_6r5.root",
sampleBaseDir+"PATtuple_14_1_5ZI.root",
sampleBaseDir+"PATtuple_12_1_DrA.root",
sampleBaseDir+"PATtuple_7_1_L5P.root",
sampleBaseDir+"PATtuple_5_1_F1J.root",
sampleBaseDir+"PATtuple_4_1_KXu.root",
sampleBaseDir+"PATtuple_6_1_PdS.root",
sampleBaseDir+"PATtuple_3_1_KwG.root",
]
