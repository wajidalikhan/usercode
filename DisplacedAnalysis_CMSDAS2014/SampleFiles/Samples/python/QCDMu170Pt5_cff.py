sampleDataSet = '/QCD_Pt-170to300_MuEnrichedPt5_TuneZ2star_8TeV_pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM'  

sampleCMSEnergy = 8000

sampleRelease = "CMSSW_5_3_2_patch4" # original (i.e. RECO file) release, not the one we plan to process them with
sampleProcessRelease = "CMSSW_5_3_8" # release used to create new files with

sampleNumEvents = 7669947

sampleXSec = 34020.0 * 0.0676 # pb

# global tag can be extracted from file using edmProvDump filename|grep globaltag
# note however that this is the tag for *further* processing, not the original tag
sampleGlobalTag = 'START53_V7G::All'

sampleDuplicateCheckMode = 'checkAllFilesOpened'

sampleType = "BKGMC"
samplePatDBSName=""

sampleBaseDir="dcap://dcap.pp.rl.ac.uk///pnfs/pp.rl.ac.uk/data/cms/store/user/ejclemen//QCD_Pt-170to300_MuEnrichedPt5_TuneZ2star_8TeV_pythia6/QCDMu170Pt5_pat_20131129/10b5286681675c887ef3085adebe4aeb/"
samplePatFiles = [
sampleBaseDir+"PATtuple_18_2_lZE.root",
sampleBaseDir+"PATtuple_151_2_eLy.root",
sampleBaseDir+"PATtuple_12_2_pRT.root",
sampleBaseDir+"PATtuple_17_2_UJk.root",
sampleBaseDir+"PATtuple_139_2_qsd.root",
sampleBaseDir+"PATtuple_5_2_X6c.root",
sampleBaseDir+"PATtuple_66_2_nLg.root",
sampleBaseDir+"PATtuple_2_2_P1Z.root",
sampleBaseDir+"PATtuple_70_2_1da.root",
sampleBaseDir+"PATtuple_53_2_daG.root",
sampleBaseDir+"PATtuple_8_2_Tbg.root",
sampleBaseDir+"PATtuple_68_2_rxi.root",
sampleBaseDir+"PATtuple_150_2_ND2.root",
sampleBaseDir+"PATtuple_92_2_UoP.root",
sampleBaseDir+"PATtuple_96_2_qQO.root",
sampleBaseDir+"PATtuple_77_2_vUJ.root",
sampleBaseDir+"PATtuple_82_2_sv4.root",
sampleBaseDir+"PATtuple_145_2_H7P.root",
sampleBaseDir+"PATtuple_76_2_iE7.root",
sampleBaseDir+"PATtuple_16_2_nVA.root",
sampleBaseDir+"PATtuple_110_2_xHI.root",
sampleBaseDir+"PATtuple_137_2_f5z.root",
sampleBaseDir+"PATtuple_49_2_ztY.root",
sampleBaseDir+"PATtuple_59_2_MLm.root",
sampleBaseDir+"PATtuple_113_2_AV8.root",
sampleBaseDir+"PATtuple_21_2_sUa.root",
sampleBaseDir+"PATtuple_116_2_4go.root",
sampleBaseDir+"PATtuple_114_2_AKc.root",
sampleBaseDir+"PATtuple_95_2_inj.root",
sampleBaseDir+"PATtuple_84_2_X0p.root",
sampleBaseDir+"PATtuple_98_2_xPn.root",
sampleBaseDir+"PATtuple_100_2_MWU.root",
sampleBaseDir+"PATtuple_85_1_puq.root",
sampleBaseDir+"PATtuple_47_1_RZF.root",
sampleBaseDir+"PATtuple_13_1_X0z.root",
sampleBaseDir+"PATtuple_147_1_JGZ.root",
sampleBaseDir+"PATtuple_35_1_tmk.root",
sampleBaseDir+"PATtuple_72_1_U58.root",
sampleBaseDir+"PATtuple_52_1_gkn.root",
sampleBaseDir+"PATtuple_91_1_WjF.root",
sampleBaseDir+"PATtuple_43_1_rRJ.root",
sampleBaseDir+"PATtuple_112_1_eox.root",
sampleBaseDir+"PATtuple_69_1_meW.root",
sampleBaseDir+"PATtuple_148_1_8RE.root",
sampleBaseDir+"PATtuple_11_1_iso.root",
sampleBaseDir+"PATtuple_62_1_ya1.root",
sampleBaseDir+"PATtuple_125_1_nYM.root",
sampleBaseDir+"PATtuple_130_1_TYz.root",
sampleBaseDir+"PATtuple_44_1_pRd.root",
sampleBaseDir+"PATtuple_63_1_sqB.root",
sampleBaseDir+"PATtuple_115_1_FKd.root",
sampleBaseDir+"PATtuple_135_1_VWE.root",
sampleBaseDir+"PATtuple_42_1_7EG.root",
sampleBaseDir+"PATtuple_105_1_jbG.root",
sampleBaseDir+"PATtuple_127_1_pFY.root",
sampleBaseDir+"PATtuple_120_1_tEk.root",
sampleBaseDir+"PATtuple_134_1_GfC.root",
sampleBaseDir+"PATtuple_124_1_C3L.root",
sampleBaseDir+"PATtuple_78_1_Y5b.root",
sampleBaseDir+"PATtuple_36_1_yNK.root",
sampleBaseDir+"PATtuple_23_1_DZ3.root",
sampleBaseDir+"PATtuple_141_1_zQs.root",
sampleBaseDir+"PATtuple_132_1_zEs.root",
sampleBaseDir+"PATtuple_39_1_BTT.root",
sampleBaseDir+"PATtuple_93_1_A24.root",
sampleBaseDir+"PATtuple_67_1_chu.root",
sampleBaseDir+"PATtuple_33_1_JTI.root",
sampleBaseDir+"PATtuple_29_1_0nl.root",
sampleBaseDir+"PATtuple_30_1_w6W.root",
sampleBaseDir+"PATtuple_101_1_xIu.root",
sampleBaseDir+"PATtuple_71_1_KDu.root",
sampleBaseDir+"PATtuple_31_1_eI3.root",
sampleBaseDir+"PATtuple_140_1_zX5.root",
sampleBaseDir+"PATtuple_25_1_yE6.root",
sampleBaseDir+"PATtuple_106_1_C8L.root",
sampleBaseDir+"PATtuple_142_1_p9r.root",
sampleBaseDir+"PATtuple_15_1_FD4.root",
sampleBaseDir+"PATtuple_154_1_Jwf.root",
sampleBaseDir+"PATtuple_136_1_NdI.root",
sampleBaseDir+"PATtuple_152_1_76e.root",
sampleBaseDir+"PATtuple_104_1_KLA.root",
sampleBaseDir+"PATtuple_103_1_34v.root",
sampleBaseDir+"PATtuple_122_1_dzS.root",
sampleBaseDir+"PATtuple_107_1_RPH.root",
sampleBaseDir+"PATtuple_111_1_fdj.root",
sampleBaseDir+"PATtuple_58_1_biT.root",
sampleBaseDir+"PATtuple_129_1_KTR.root",
sampleBaseDir+"PATtuple_133_1_q4H.root",
sampleBaseDir+"PATtuple_124_1_Q06.root",
sampleBaseDir+"PATtuple_135_1_766.root",
sampleBaseDir+"PATtuple_121_1_gvh.root",
sampleBaseDir+"PATtuple_10_1_XZV.root",
sampleBaseDir+"PATtuple_55_1_UF3.root",
sampleBaseDir+"PATtuple_41_1_i6g.root",
sampleBaseDir+"PATtuple_155_1_3lD.root",
sampleBaseDir+"PATtuple_19_1_K7d.root",
sampleBaseDir+"PATtuple_75_1_Ayr.root",
sampleBaseDir+"PATtuple_108_1_A4j.root",
sampleBaseDir+"PATtuple_57_6_kOL.root",
sampleBaseDir+"PATtuple_81_6_6pg.root",
sampleBaseDir+"PATtuple_32_5_N0h.root",
sampleBaseDir+"PATtuple_73_6_Ezn.root",
sampleBaseDir+"PATtuple_48_5_Hir.root",
sampleBaseDir+"PATtuple_80_5_vD8.root",
sampleBaseDir+"PATtuple_89_6_9Hl.root",
sampleBaseDir+"PATtuple_50_5_y0m.root",
sampleBaseDir+"PATtuple_83_5_SpA.root",
sampleBaseDir+"PATtuple_27_6_kKq.root",
sampleBaseDir+"PATtuple_60_6_HvB.root",
sampleBaseDir+"PATtuple_28_6_LvM.root",
sampleBaseDir+"PATtuple_26_6_sj4.root",
sampleBaseDir+"PATtuple_121_6_lFn.root",
sampleBaseDir+"PATtuple_9_5_4wA.root",
sampleBaseDir+"PATtuple_6_5_1MU.root",
sampleBaseDir+"PATtuple_3_5_rfc.root",
sampleBaseDir+"PATtuple_126_2_kP9.root",
sampleBaseDir+"PATtuple_56_2_zPj.root",
sampleBaseDir+"PATtuple_128_2_0qh.root",
sampleBaseDir+"PATtuple_86_2_MRL.root",
sampleBaseDir+"PATtuple_38_2_ueb.root",
sampleBaseDir+"PATtuple_123_2_RWO.root",
sampleBaseDir+"PATtuple_143_2_4GG.root",
sampleBaseDir+"PATtuple_146_2_KFs.root",
sampleBaseDir+"PATtuple_144_2_xNC.root",
sampleBaseDir+"PATtuple_20_2_beI.root",
sampleBaseDir+"PATtuple_149_2_Wty.root",
sampleBaseDir+"PATtuple_14_2_83O.root",
sampleBaseDir+"PATtuple_118_1_mDG.root",
sampleBaseDir+"PATtuple_109_1_SXg.root",
sampleBaseDir+"PATtuple_117_1_Fl8.root",
sampleBaseDir+"PATtuple_119_1_WeE.root",
sampleBaseDir+"PATtuple_40_1_KSL.root",
sampleBaseDir+"PATtuple_153_1_Sp8.root",
sampleBaseDir+"PATtuple_97_1_iaV.root",
sampleBaseDir+"PATtuple_54_1_V5W.root",
sampleBaseDir+"PATtuple_88_1_NSG.root",
sampleBaseDir+"PATtuple_37_1_a0n.root",
sampleBaseDir+"PATtuple_51_1_zt4.root",
sampleBaseDir+"PATtuple_45_1_Zlk.root",
sampleBaseDir+"PATtuple_138_1_ZHq.root",
sampleBaseDir+"PATtuple_87_1_hjk.root",
sampleBaseDir+"PATtuple_94_1_zJZ.root",
sampleBaseDir+"PATtuple_90_1_APB.root",
sampleBaseDir+"PATtuple_79_1_peF.root",
sampleBaseDir+"PATtuple_46_1_yJV.root",
sampleBaseDir+"PATtuple_22_1_k7s.root",
sampleBaseDir+"PATtuple_34_1_moq.root",
sampleBaseDir+"PATtuple_24_1_8cl.root",
sampleBaseDir+"PATtuple_4_1_89A.root",
sampleBaseDir+"PATtuple_7_1_YGA.root",
sampleBaseDir+"PATtuple_61_1_hTa.root",
sampleBaseDir+"PATtuple_1_1_RWK.root",
]