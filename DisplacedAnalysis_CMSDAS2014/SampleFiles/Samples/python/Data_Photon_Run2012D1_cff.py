#sampleDataSet = '/DoublePhotonHighPt/Run2012D-PromptReco-v1/AOD'
sampleDataSet = '/DoublePhoton/Run2012D-PromptReco-v1/AOD'

# original (i.e. RECO file) release,
# not the one we plan to process them with
sampleRelease = "CMSSW_5_3_4" 
# release used to create new files with
sampleProcessRelease = "CMSSW_5_3_5" 

#sampleNumEvents = 20060017 # according to DBS, as of 25 January 2013
sampleNumEvents = 50623490

# global tag needs to be chosen to match release, trigger menu and alignment conditions.
# see https://twiki.cern.ch/twiki/bin/view/CMS/SWGuideFrontierConditions
sampleGlobalTag = 'GR_P_V42_AN3::All'

# data quality run/lumi section selection
sampleJSON = "https://cms-service-dqm.web.cern.ch/cms-service-dqm/CAF/certification/Collisions12/8TeV/Prompt/Cert_190456-208686_8TeV_PromptReco_Collisions12_JSON.txt"

# restrict run range (mainly to get a sample with consistent trigger configuration)

# use checkAllFilesOpened whenever possible, and noDuplicateCheck when necessary
sampleDuplicateCheckMode = "checkAllFilesOpened"

# "DATA" or "MC"
sampleType = "DATA"







samplePatDBSName=""

sampleBaseDir="dcap://dcap.pp.rl.ac.uk///pnfs/pp.rl.ac.uk/data/cms/store/user/ejclemen//DoublePhoton/Data_Photon_Run2012D1_pat_20130131_1/305c779411eb21e3b1baec97cb367d9a/"
samplePatFiles = [
sampleBaseDir+"PATtuple_226_9_3hk.root",
sampleBaseDir+"PATtuple_328_6_upD.root",
sampleBaseDir+"PATtuple_502_6_F9v.root",
sampleBaseDir+"PATtuple_9_4_oRu.root",
sampleBaseDir+"PATtuple_2_6_AGl.root",
sampleBaseDir+"PATtuple_436_6_it2.root",
sampleBaseDir+"PATtuple_555_6_M0J.root",
sampleBaseDir+"PATtuple_356_6_X8w.root",
sampleBaseDir+"PATtuple_137_6_RUx.root",
sampleBaseDir+"PATtuple_453_5_GsM.root",
sampleBaseDir+"PATtuple_405_6_cKm.root",
sampleBaseDir+"PATtuple_404_5_J9m.root",
sampleBaseDir+"PATtuple_672_6_CY1.root",
sampleBaseDir+"PATtuple_131_6_0Xt.root",
sampleBaseDir+"PATtuple_369_5_tCg.root",
sampleBaseDir+"PATtuple_177_7_cQ9.root",
sampleBaseDir+"PATtuple_553_6_pGT.root",
sampleBaseDir+"PATtuple_387_6_VBA.root",
sampleBaseDir+"PATtuple_186_6_NVf.root",
sampleBaseDir+"PATtuple_194_7_bRA.root",
sampleBaseDir+"PATtuple_616_5_SJE.root",
sampleBaseDir+"PATtuple_136_6_eA6.root",
sampleBaseDir+"PATtuple_223_6_4N8.root",
sampleBaseDir+"PATtuple_607_5_wgb.root",
sampleBaseDir+"PATtuple_193_6_jrM.root",
sampleBaseDir+"PATtuple_222_6_Z5e.root",
sampleBaseDir+"PATtuple_228_6_3te.root",
sampleBaseDir+"PATtuple_143_7_Zbl.root",
sampleBaseDir+"PATtuple_438_6_tGq.root",
sampleBaseDir+"PATtuple_253_6_tHg.root",
sampleBaseDir+"PATtuple_643_5_zA1.root",
sampleBaseDir+"PATtuple_494_6_n9U.root",
sampleBaseDir+"PATtuple_568_6_JNH.root",
sampleBaseDir+"PATtuple_572_5_Pks.root",
sampleBaseDir+"PATtuple_584_5_btA.root",
sampleBaseDir+"PATtuple_138_7_GIl.root",
sampleBaseDir+"PATtuple_573_5_mXa.root",
sampleBaseDir+"PATtuple_156_2_xqc.root",
sampleBaseDir+"PATtuple_115_2_qgu.root",
sampleBaseDir+"PATtuple_155_2_4qZ.root",
sampleBaseDir+"PATtuple_549_2_SwP.root",
sampleBaseDir+"PATtuple_101_2_7bL.root",
sampleBaseDir+"PATtuple_385_2_KEl.root",
sampleBaseDir+"PATtuple_329_2_bkD.root",
sampleBaseDir+"PATtuple_358_2_awV.root",
sampleBaseDir+"PATtuple_428_2_0RB.root",
sampleBaseDir+"PATtuple_184_3_ClQ.root",
sampleBaseDir+"PATtuple_135_3_wwp.root",
sampleBaseDir+"PATtuple_159_2_wIK.root",
sampleBaseDir+"PATtuple_394_2_NpC.root",
sampleBaseDir+"PATtuple_30_2_VZz.root",
sampleBaseDir+"PATtuple_468_2_csd.root",
sampleBaseDir+"PATtuple_427_2_tlD.root",
sampleBaseDir+"PATtuple_390_2_PAa.root",
sampleBaseDir+"PATtuple_425_2_lij.root",
sampleBaseDir+"PATtuple_342_2_Hf6.root",
sampleBaseDir+"PATtuple_240_2_duf.root",
sampleBaseDir+"PATtuple_17_2_SYI.root",
sampleBaseDir+"PATtuple_437_2_6yR.root",
sampleBaseDir+"PATtuple_132_3_ol2.root",
sampleBaseDir+"PATtuple_552_2_v8g.root",
sampleBaseDir+"PATtuple_62_3_DIG.root",
sampleBaseDir+"PATtuple_481_2_JQJ.root",
sampleBaseDir+"PATtuple_409_2_so7.root",
sampleBaseDir+"PATtuple_330_2_L9z.root",
sampleBaseDir+"PATtuple_142_2_hXD.root",
sampleBaseDir+"PATtuple_195_2_kWY.root",
sampleBaseDir+"PATtuple_317_2_rpc.root",
sampleBaseDir+"PATtuple_344_2_kur.root",
sampleBaseDir+"PATtuple_212_2_4S2.root",
sampleBaseDir+"PATtuple_343_2_de8.root",
sampleBaseDir+"PATtuple_410_3_gyu.root",
sampleBaseDir+"PATtuple_251_2_IMZ.root",
sampleBaseDir+"PATtuple_471_2_j4S.root",
sampleBaseDir+"PATtuple_189_3_wOm.root",
sampleBaseDir+"PATtuple_290_2_R6b.root",
sampleBaseDir+"PATtuple_243_2_HWd.root",
sampleBaseDir+"PATtuple_294_2_4y0.root",
sampleBaseDir+"PATtuple_514_2_TEU.root",
sampleBaseDir+"PATtuple_430_2_3L8.root",
sampleBaseDir+"PATtuple_42_3_ltv.root",
sampleBaseDir+"PATtuple_503_2_Zbo.root",
sampleBaseDir+"PATtuple_191_2_qzV.root",
sampleBaseDir+"PATtuple_429_2_B14.root",
sampleBaseDir+"PATtuple_59_2_nO8.root",
sampleBaseDir+"PATtuple_106_3_AJ2.root",
sampleBaseDir+"PATtuple_331_2_n0I.root",
sampleBaseDir+"PATtuple_615_2_9r0.root",
sampleBaseDir+"PATtuple_3_2_Atx.root",
sampleBaseDir+"PATtuple_546_2_KOc.root",
sampleBaseDir+"PATtuple_659_2_1JV.root",
sampleBaseDir+"PATtuple_495_2_Pgl.root",
sampleBaseDir+"PATtuple_190_3_eRc.root",
sampleBaseDir+"PATtuple_109_2_ai0.root",
sampleBaseDir+"PATtuple_357_2_8r1.root",
sampleBaseDir+"PATtuple_93_7_DfH.root",
sampleBaseDir+"PATtuple_133_6_7P1.root",
sampleBaseDir+"PATtuple_211_5_ivX.root",
sampleBaseDir+"PATtuple_452_5_HGd.root",
sampleBaseDir+"PATtuple_388_5_CPO.root",
sampleBaseDir+"PATtuple_227_5_We9.root",
sampleBaseDir+"PATtuple_657_5_uoj.root",
sampleBaseDir+"PATtuple_218_5_flm.root",
sampleBaseDir+"PATtuple_614_5_QkC.root",
sampleBaseDir+"PATtuple_176_5_1c9.root",
sampleBaseDir+"PATtuple_121_5_f3R.root",
sampleBaseDir+"PATtuple_450_5_lCT.root",
sampleBaseDir+"PATtuple_123_6_3ZR.root",
sampleBaseDir+"PATtuple_183_5_xbK.root",
sampleBaseDir+"PATtuple_117_6_2K0.root",
sampleBaseDir+"PATtuple_558_4_MFq.root",
sampleBaseDir+"PATtuple_104_6_e6z.root",
sampleBaseDir+"PATtuple_600_4_Xu7.root",
sampleBaseDir+"PATtuple_370_4_nt0.root",
sampleBaseDir+"PATtuple_113_4_oNZ.root",
sampleBaseDir+"PATtuple_493_4_94L.root",
sampleBaseDir+"PATtuple_269_4_iMJ.root",
sampleBaseDir+"PATtuple_100_4_4ok.root",
sampleBaseDir+"PATtuple_551_4_BGh.root",
sampleBaseDir+"PATtuple_252_5_ifp.root",
sampleBaseDir+"PATtuple_306_4_7bC.root",
sampleBaseDir+"PATtuple_308_4_GrP.root",
sampleBaseDir+"PATtuple_268_4_eVB.root",
sampleBaseDir+"PATtuple_60_4_fY1.root",
sampleBaseDir+"PATtuple_7_4_f7C.root",
sampleBaseDir+"PATtuple_319_4_8ov.root",
sampleBaseDir+"PATtuple_108_5_XSK.root",
sampleBaseDir+"PATtuple_102_4_Juw.root",
sampleBaseDir+"PATtuple_613_4_XP9.root",
sampleBaseDir+"PATtuple_103_4_1Uy.root",
sampleBaseDir+"PATtuple_323_4_ySz.root",
sampleBaseDir+"PATtuple_660_4_Xxy.root",
sampleBaseDir+"PATtuple_571_5_lBL.root",
sampleBaseDir+"PATtuple_80_4_P0B.root",
sampleBaseDir+"PATtuple_246_5_v0n.root",
sampleBaseDir+"PATtuple_578_4_lRx.root",
sampleBaseDir+"PATtuple_188_3_CeN.root",
sampleBaseDir+"PATtuple_85_5_6IP.root",
sampleBaseDir+"PATtuple_583_4_Mb2.root",
sampleBaseDir+"PATtuple_598_3_2R0.root",
sampleBaseDir+"PATtuple_593_4_8Zx.root",
sampleBaseDir+"PATtuple_442_4_2Ok.root",
sampleBaseDir+"PATtuple_87_4_i4W.root",
sampleBaseDir+"PATtuple_580_4_RGe.root",
sampleBaseDir+"PATtuple_581_4_vYn.root",
sampleBaseDir+"PATtuple_77_3_qLO.root",
sampleBaseDir+"PATtuple_564_4_Ady.root",
sampleBaseDir+"PATtuple_597_3_Q7O.root",
sampleBaseDir+"PATtuple_565_4_4P0.root",
sampleBaseDir+"PATtuple_599_3_S6l.root",
sampleBaseDir+"PATtuple_521_3_6DG.root",
sampleBaseDir+"PATtuple_407_3_Tau.root",
sampleBaseDir+"PATtuple_426_3_X33.root",
sampleBaseDir+"PATtuple_28_4_Sgd.root",
sampleBaseDir+"PATtuple_513_3_9cT.root",
sampleBaseDir+"PATtuple_289_3_ub0.root",
sampleBaseDir+"PATtuple_606_3_NNm.root",
sampleBaseDir+"PATtuple_570_3_VNs.root",
sampleBaseDir+"PATtuple_318_3_ML3.root",
sampleBaseDir+"PATtuple_129_3_IGQ.root",
sampleBaseDir+"PATtuple_569_3_GK0.root",
sampleBaseDir+"PATtuple_544_3_nYf.root",
sampleBaseDir+"PATtuple_596_3_6WZ.root",
sampleBaseDir+"PATtuple_454_3_xhU.root",
sampleBaseDir+"PATtuple_522_3_kNU.root",
sampleBaseDir+"PATtuple_182_4_W94.root",
sampleBaseDir+"PATtuple_116_3_Nq3.root",
sampleBaseDir+"PATtuple_627_3_dJq.root",
sampleBaseDir+"PATtuple_157_3_ZHj.root",
sampleBaseDir+"PATtuple_76_4_kXO.root",
sampleBaseDir+"PATtuple_574_3_Tgg.root",
sampleBaseDir+"PATtuple_128_6_XaG.root",
sampleBaseDir+"PATtuple_467_5_fQl.root",
sampleBaseDir+"PATtuple_504_5_zrK.root",
sampleBaseDir+"PATtuple_18_6_t2w.root",
sampleBaseDir+"PATtuple_242_7_Tb6.root",
sampleBaseDir+"PATtuple_44_5_34a.root",
sampleBaseDir+"PATtuple_8_5_32E.root",
sampleBaseDir+"PATtuple_119_5_8ZL.root",
sampleBaseDir+"PATtuple_654_7_qrB.root",
sampleBaseDir+"PATtuple_457_5_41d.root",
sampleBaseDir+"PATtuple_267_4_Ndx.root",
sampleBaseDir+"PATtuple_248_5_NiG.root",
sampleBaseDir+"PATtuple_469_3_bf2.root",
sampleBaseDir+"PATtuple_523_3_Vr2.root",
sampleBaseDir+"PATtuple_603_3_uwC.root",
sampleBaseDir+"PATtuple_179_4_pdk.root",
sampleBaseDir+"PATtuple_392_3_8bJ.root",
sampleBaseDir+"PATtuple_560_3_Cmp.root",
sampleBaseDir+"PATtuple_588_3_7HZ.root",
sampleBaseDir+"PATtuple_180_3_0Hn.root",
sampleBaseDir+"PATtuple_612_3_gjE.root",
sampleBaseDir+"PATtuple_31_3_WgG.root",
sampleBaseDir+"PATtuple_45_3_Jaq.root",
sampleBaseDir+"PATtuple_592_3_gYZ.root",
sampleBaseDir+"PATtuple_632_3_J2p.root",
sampleBaseDir+"PATtuple_575_3_Qo1.root",
sampleBaseDir+"PATtuple_610_3_SJq.root",
sampleBaseDir+"PATtuple_559_3_LYl.root",
sampleBaseDir+"PATtuple_376_3_CCb.root",
sampleBaseDir+"PATtuple_633_3_UfH.root",
sampleBaseDir+"PATtuple_364_3_XAt.root",
sampleBaseDir+"PATtuple_586_3_2Vf.root",
sampleBaseDir+"PATtuple_147_4_RnF.root",
sampleBaseDir+"PATtuple_611_3_15C.root",
sampleBaseDir+"PATtuple_604_3_xix.root",
sampleBaseDir+"PATtuple_562_3_BQk.root",
sampleBaseDir+"PATtuple_591_3_Ly4.root",
sampleBaseDir+"PATtuple_590_3_wlC.root",
sampleBaseDir+"PATtuple_563_3_1M5.root",
sampleBaseDir+"PATtuple_561_3_57r.root",
sampleBaseDir+"PATtuple_15_4_cAj.root",
sampleBaseDir+"PATtuple_465_3_BAk.root",
sampleBaseDir+"PATtuple_577_3_Bnr.root",
sampleBaseDir+"PATtuple_655_3_iZC.root",
sampleBaseDir+"PATtuple_37_3_M3O.root",
sampleBaseDir+"PATtuple_594_3_kih.root",
sampleBaseDir+"PATtuple_576_3_pVy.root",
sampleBaseDir+"PATtuple_579_3_RxQ.root",
sampleBaseDir+"PATtuple_566_3_0ww.root",
sampleBaseDir+"PATtuple_595_3_RrE.root",
sampleBaseDir+"PATtuple_641_3_9qT.root",
sampleBaseDir+"PATtuple_582_3_hRR.root",
sampleBaseDir+"PATtuple_567_3_eQD.root",
sampleBaseDir+"PATtuple_554_2_FEs.root",
sampleBaseDir+"PATtuple_543_2_sF4.root",
sampleBaseDir+"PATtuple_250_2_vfI.root",
sampleBaseDir+"PATtuple_43_3_srR.root",
sampleBaseDir+"PATtuple_537_2_oDA.root",
sampleBaseDir+"PATtuple_221_2_We3.root",
sampleBaseDir+"PATtuple_241_3_eT9.root",
sampleBaseDir+"PATtuple_134_2_0CU.root",
sampleBaseDir+"PATtuple_548_2_aRS.root",
sampleBaseDir+"PATtuple_349_4_G3l.root",
sampleBaseDir+"PATtuple_145_2_Ul8.root",
sampleBaseDir+"PATtuple_320_2_0XB.root",
sampleBaseDir+"PATtuple_386_2_Spr.root",
sampleBaseDir+"PATtuple_158_3_Ftz.root",
sampleBaseDir+"PATtuple_229_2_kdb.root",
sampleBaseDir+"PATtuple_192_2_hoV.root",
sampleBaseDir+"PATtuple_321_2_iqq.root",
sampleBaseDir+"PATtuple_75_3_mtc.root",
sampleBaseDir+"PATtuple_219_2_5n3.root",
sampleBaseDir+"PATtuple_539_2_yo7.root",
sampleBaseDir+"PATtuple_550_2_oe3.root",
sampleBaseDir+"PATtuple_396_3_Jd1.root",
sampleBaseDir+"PATtuple_389_2_b78.root",
sampleBaseDir+"PATtuple_629_2_W2X.root",
sampleBaseDir+"PATtuple_27_2_mI5.root",
sampleBaseDir+"PATtuple_130_2_yvc.root",
sampleBaseDir+"PATtuple_295_2_Psi.root",
sampleBaseDir+"PATtuple_381_2_YFA.root",
sampleBaseDir+"PATtuple_368_2_CA9.root",
sampleBaseDir+"PATtuple_144_3_cuG.root",
sampleBaseDir+"PATtuple_480_2_6VT.root",
sampleBaseDir+"PATtuple_256_2_JbA.root",
sampleBaseDir+"PATtuple_185_3_ZaR.root",
sampleBaseDir+"PATtuple_375_2_jfl.root",
sampleBaseDir+"PATtuple_78_2_W68.root",
sampleBaseDir+"PATtuple_408_2_STx.root",
sampleBaseDir+"PATtuple_411_2_6pr.root",
sampleBaseDir+"PATtuple_187_2_ru6.root",
sampleBaseDir+"PATtuple_292_2_JlY.root",
sampleBaseDir+"PATtuple_63_3_KGl.root",
sampleBaseDir+"PATtuple_440_2_Jvw.root",
sampleBaseDir+"PATtuple_506_2_uqP.root",
sampleBaseDir+"PATtuple_393_2_nS7.root",
sampleBaseDir+"PATtuple_406_2_ZEt.root",
sampleBaseDir+"PATtuple_19_2_Uf4.root",
sampleBaseDir+"PATtuple_271_2_9zt.root",
sampleBaseDir+"PATtuple_644_2_KAy.root",
sampleBaseDir+"PATtuple_519_2_4xO.root",
sampleBaseDir+"PATtuple_432_2_XZp.root",
sampleBaseDir+"PATtuple_472_2_FB8.root",
sampleBaseDir+"PATtuple_198_3_QTh.root",
sampleBaseDir+"PATtuple_382_2_tQI.root",
sampleBaseDir+"PATtuple_505_2_vm6.root",
sampleBaseDir+"PATtuple_332_2_dOq.root",
sampleBaseDir+"PATtuple_249_2_SdW.root",
sampleBaseDir+"PATtuple_451_2_6vN.root",
sampleBaseDir+"PATtuple_225_2_VeH.root",
sampleBaseDir+"PATtuple_224_2_cgt.root",
sampleBaseDir+"PATtuple_146_3_Yy5.root",
sampleBaseDir+"PATtuple_160_2_8da.root",
sampleBaseDir+"PATtuple_529_2_SLH.root",
sampleBaseDir+"PATtuple_12_2_AsU.root",
sampleBaseDir+"PATtuple_305_2_zK1.root",
sampleBaseDir+"PATtuple_516_2_Z1N.root",
sampleBaseDir+"PATtuple_341_2_50M.root",
sampleBaseDir+"PATtuple_540_2_ffq.root",
sampleBaseDir+"PATtuple_487_2_fst.root",
sampleBaseDir+"PATtuple_140_3_s97.root",
sampleBaseDir+"PATtuple_112_4_CcO.root",
sampleBaseDir+"PATtuple_333_3_fJZ.root",
sampleBaseDir+"PATtuple_545_3_0vp.root",
sampleBaseDir+"PATtuple_617_3_V6T.root",
sampleBaseDir+"PATtuple_589_3_qrX.root",
sampleBaseDir+"PATtuple_303_3_ThZ.root",
sampleBaseDir+"PATtuple_515_3_Ufc.root",
sampleBaseDir+"PATtuple_456_3_hWI.root",
sampleBaseDir+"PATtuple_601_3_a9I.root",
sampleBaseDir+"PATtuple_114_3_kDO.root",
sampleBaseDir+"PATtuple_111_3_oGw.root",
sampleBaseDir+"PATtuple_29_4_OTA.root",
sampleBaseDir+"PATtuple_26_3_sz7.root",
sampleBaseDir+"PATtuple_11_4_D8s.root",
sampleBaseDir+"PATtuple_585_3_Qiq.root",
sampleBaseDir+"PATtuple_557_3_mQN.root",
sampleBaseDir+"PATtuple_609_3_z8R.root",
sampleBaseDir+"PATtuple_139_3_hk5.root",
sampleBaseDir+"PATtuple_107_3_nIT.root",
sampleBaseDir+"PATtuple_118_4_JX0.root",
sampleBaseDir+"PATtuple_602_3_QvW.root",
sampleBaseDir+"PATtuple_605_3_xqN.root",
sampleBaseDir+"PATtuple_272_3_NWR.root",
sampleBaseDir+"PATtuple_110_3_pTo.root",
sampleBaseDir+"PATtuple_91_2_C1j.root",
sampleBaseDir+"PATtuple_213_2_fOe.root",
sampleBaseDir+"PATtuple_524_2_SwV.root",
sampleBaseDir+"PATtuple_90_3_P9P.root",
sampleBaseDir+"PATtuple_486_2_xRa.root",
sampleBaseDir+"PATtuple_309_2_ios.root",
sampleBaseDir+"PATtuple_473_2_TNe.root",
sampleBaseDir+"PATtuple_270_2_Ey5.root",
sampleBaseDir+"PATtuple_484_2_4N5.root",
sampleBaseDir+"PATtuple_336_2_lfN.root",
sampleBaseDir+"PATtuple_415_2_gF7.root",
sampleBaseDir+"PATtuple_288_2_scb.root",
sampleBaseDir+"PATtuple_1_2_ZIg.root",
sampleBaseDir+"PATtuple_125_2_3Yg.root",
sampleBaseDir+"PATtuple_154_2_jj5.root",
sampleBaseDir+"PATtuple_10_2_siJ.root",
sampleBaseDir+"PATtuple_538_2_hKd.root",
sampleBaseDir+"PATtuple_431_2_57I.root",
sampleBaseDir+"PATtuple_517_2_KsY.root",
sampleBaseDir+"PATtuple_496_2_qEk.root",
sampleBaseDir+"PATtuple_124_2_z1M.root",
sampleBaseDir+"PATtuple_345_2_wDx.root",
sampleBaseDir+"PATtuple_383_2_nY6.root",
sampleBaseDir+"PATtuple_347_2_LCK.root",
sampleBaseDir+"PATtuple_151_3_lCR.root",
sampleBaseDir+"PATtuple_492_2_mAY.root",
sampleBaseDir+"PATtuple_214_3_jRG.root",
sampleBaseDir+"PATtuple_518_2_ICu.root",
sampleBaseDir+"PATtuple_322_2_8hq.root",
sampleBaseDir+"PATtuple_547_2_nxu.root",
sampleBaseDir+"PATtuple_631_2_C0d.root",
sampleBaseDir+"PATtuple_488_2_9RA.root",
sampleBaseDir+"PATtuple_202_3_vVY.root",
sampleBaseDir+"PATtuple_443_2_Aed.root",
sampleBaseDir+"PATtuple_164_2_T1h.root",
sampleBaseDir+"PATtuple_299_2_rLu.root",
sampleBaseDir+"PATtuple_201_2_3Gn.root",
sampleBaseDir+"PATtuple_166_2_MX2.root",
sampleBaseDir+"PATtuple_13_2_1cU.root",
sampleBaseDir+"PATtuple_94_2_KKU.root",
sampleBaseDir+"PATtuple_463_2_aW1.root",
sampleBaseDir+"PATtuple_464_2_dYG.root",
sampleBaseDir+"PATtuple_398_2_Pb1.root",
sampleBaseDir+"PATtuple_670_2_eMr.root",
sampleBaseDir+"PATtuple_354_2_fKQ.root",
sampleBaseDir+"PATtuple_477_2_AOC.root",
sampleBaseDir+"PATtuple_89_3_y7S.root",
sampleBaseDir+"PATtuple_81_2_2JQ.root",
sampleBaseDir+"PATtuple_263_2_5Ju.root",
sampleBaseDir+"PATtuple_70_2_cN7.root",
sampleBaseDir+"PATtuple_401_2_b3f.root",
sampleBaseDir+"PATtuple_534_2_UZE.root",
sampleBaseDir+"PATtuple_300_2_hgj.root",
sampleBaseDir+"PATtuple_625_2_DeA.root",
sampleBaseDir+"PATtuple_208_2_wVF.root",
sampleBaseDir+"PATtuple_673_2_boF.root",
sampleBaseDir+"PATtuple_444_2_Y27.root",
sampleBaseDir+"PATtuple_620_2_JAV.root",
sampleBaseDir+"PATtuple_167_2_lEE.root",
sampleBaseDir+"PATtuple_400_2_dpc.root",
sampleBaseDir+"PATtuple_169_2_Wm2.root",
sampleBaseDir+"PATtuple_206_2_HKQ.root",
sampleBaseDir+"PATtuple_203_2_zH3.root",
sampleBaseDir+"PATtuple_168_2_qMV.root",
sampleBaseDir+"PATtuple_281_2_lp6.root",
sampleBaseDir+"PATtuple_215_2_yXR.root",
sampleBaseDir+"PATtuple_665_2_Npo.root",
sampleBaseDir+"PATtuple_285_2_jsw.root",
sampleBaseDir+"PATtuple_422_2_9G1.root",
sampleBaseDir+"PATtuple_479_2_Ew9.root",
sampleBaseDir+"PATtuple_623_2_jfe.root",
sampleBaseDir+"PATtuple_266_3_NPh.root",
sampleBaseDir+"PATtuple_283_2_pug.root",
sampleBaseDir+"PATtuple_621_2_l6i.root",
sampleBaseDir+"PATtuple_533_2_dqj.root",
sampleBaseDir+"PATtuple_284_2_2HQ.root",
sampleBaseDir+"PATtuple_97_2_MPN.root",
sampleBaseDir+"PATtuple_302_2_bAm.root",
sampleBaseDir+"PATtuple_535_2_uaw.root",
sampleBaseDir+"PATtuple_661_2_Fnq.root",
sampleBaseDir+"PATtuple_622_2_ZyP.root",
sampleBaseDir+"PATtuple_282_2_FbM.root",
sampleBaseDir+"PATtuple_624_2_pgL.root",
sampleBaseDir+"PATtuple_65_2_Vvs.root",
sampleBaseDir+"PATtuple_466_2_Adb.root",
sampleBaseDir+"PATtuple_423_2_g9s.root",
sampleBaseDir+"PATtuple_173_2_Rsv.root",
sampleBaseDir+"PATtuple_71_2_R7s.root",
sampleBaseDir+"PATtuple_68_2_pwT.root",
sampleBaseDir+"PATtuple_262_2_IZn.root",
sampleBaseDir+"PATtuple_378_2_WjH.root",
sampleBaseDir+"PATtuple_339_2_R1Q.root",
sampleBaseDir+"PATtuple_170_2_Nwq.root",
sampleBaseDir+"PATtuple_264_2_z8a.root",
sampleBaseDir+"PATtuple_98_2_BEH.root",
sampleBaseDir+"PATtuple_626_2_7aE.root",
sampleBaseDir+"PATtuple_265_2_knA.root",
sampleBaseDir+"PATtuple_95_2_29b.root",
sampleBaseDir+"PATtuple_88_3_qSY.root",
sampleBaseDir+"PATtuple_55_2_o8y.root",
sampleBaseDir+"PATtuple_58_2_2Xq.root",
sampleBaseDir+"PATtuple_662_2_pux.root",
sampleBaseDir+"PATtuple_66_2_JPF.root",
sampleBaseDir+"PATtuple_639_2_v2w.root",
sampleBaseDir+"PATtuple_175_2_fUb.root",
sampleBaseDir+"PATtuple_656_2_cYY.root",
sampleBaseDir+"PATtuple_650_2_bft.root",
sampleBaseDir+"PATtuple_72_2_AKB.root",
sampleBaseDir+"PATtuple_14_2_FQT.root",
sampleBaseDir+"PATtuple_286_2_C7S.root",
sampleBaseDir+"PATtuple_637_3_6Na.root",
sampleBaseDir+"PATtuple_635_2_f1e.root",
sampleBaseDir+"PATtuple_663_2_lsr.root",
sampleBaseDir+"PATtuple_664_2_ppT.root",
sampleBaseDir+"PATtuple_56_2_B6x.root",
sampleBaseDir+"PATtuple_16_2_a99.root",
sampleBaseDir+"PATtuple_652_2_PeR.root",
sampleBaseDir+"PATtuple_636_2_PNu.root",
sampleBaseDir+"PATtuple_587_2_Js0.root",
sampleBaseDir+"PATtuple_48_2_B1h.root",
sampleBaseDir+"PATtuple_634_2_0Xo.root",
sampleBaseDir+"PATtuple_653_2_xdp.root",
sampleBaseDir+"PATtuple_24_3_Upc.root",
sampleBaseDir+"PATtuple_38_2_9IE.root",
sampleBaseDir+"PATtuple_638_2_InM.root",
sampleBaseDir+"PATtuple_447_2_4mo.root",
sampleBaseDir+"PATtuple_642_2_tQC.root",
sampleBaseDir+"PATtuple_619_2_3uv.root",
sampleBaseDir+"PATtuple_304_1_iRI.root",
sampleBaseDir+"PATtuple_127_2_EvH.root",
sampleBaseDir+"PATtuple_220_2_96F.root",
sampleBaseDir+"PATtuple_455_2_b4i.root",
sampleBaseDir+"PATtuple_278_2_240.root",
sampleBaseDir+"PATtuple_310_2_ROU.root",
sampleBaseDir+"PATtuple_439_2_l4O.root",
sampleBaseDir+"PATtuple_216_2_JHJ.root",
sampleBaseDir+"PATtuple_335_2_D2h.root",
sampleBaseDir+"PATtuple_360_2_vQn.root",
sampleBaseDir+"PATtuple_5_3_wtY.root",
sampleBaseDir+"PATtuple_247_2_GGI.root",
sampleBaseDir+"PATtuple_22_2_kGy.root",
sampleBaseDir+"PATtuple_47_2_c6X.root",
sampleBaseDir+"PATtuple_46_2_v6S.root",
sampleBaseDir+"PATtuple_334_2_MUt.root",
sampleBaseDir+"PATtuple_526_2_hKo.root",
sampleBaseDir+"PATtuple_293_2_8to.root",
sampleBaseDir+"PATtuple_527_2_Rq3.root",
sampleBaseDir+"PATtuple_261_2_qje.root",
sampleBaseDir+"PATtuple_152_3_dEX.root",
sampleBaseDir+"PATtuple_245_2_dAx.root",
sampleBaseDir+"PATtuple_371_2_3w5.root",
sampleBaseDir+"PATtuple_384_2_2X1.root",
sampleBaseDir+"PATtuple_417_2_ZdE.root",
sampleBaseDir+"PATtuple_474_2_Qmp.root",
sampleBaseDir+"PATtuple_326_2_aXU.root",
sampleBaseDir+"PATtuple_671_2_GRR.root",
sampleBaseDir+"PATtuple_512_2_12S.root",
sampleBaseDir+"PATtuple_485_2_2E3.root",
sampleBaseDir+"PATtuple_237_2_dvy.root",
sampleBaseDir+"PATtuple_500_2_JXB.root",
sampleBaseDir+"PATtuple_20_2_69M.root",
sampleBaseDir+"PATtuple_646_2_5QM.root",
sampleBaseDir+"PATtuple_424_2_8m0.root",
sampleBaseDir+"PATtuple_441_2_E7j.root",
sampleBaseDir+"PATtuple_470_2_Cu4.root",
sampleBaseDir+"PATtuple_161_3_LCX.root",
sampleBaseDir+"PATtuple_433_2_HMO.root",
sampleBaseDir+"PATtuple_316_2_uFU.root",
sampleBaseDir+"PATtuple_367_2_qts.root",
sampleBaseDir+"PATtuple_298_2_JW6.root",
sampleBaseDir+"PATtuple_351_2_epC.root",
sampleBaseDir+"PATtuple_325_2_ysX.root",
sampleBaseDir+"PATtuple_273_2_LxJ.root",
sampleBaseDir+"PATtuple_434_2_B5m.root",
sampleBaseDir+"PATtuple_489_2_qsR.root",
sampleBaseDir+"PATtuple_352_2_M2f.root",
sampleBaseDir+"PATtuple_148_3_6C7.root",
sampleBaseDir+"PATtuple_153_3_zTO.root",
sampleBaseDir+"PATtuple_475_2_uWs.root",
sampleBaseDir+"PATtuple_231_2_YaR.root",
sampleBaseDir+"PATtuple_69_2_OT2.root",
sampleBaseDir+"PATtuple_236_2_7UC.root",
sampleBaseDir+"PATtuple_460_2_aSV.root",
sampleBaseDir+"PATtuple_651_2_mWV.root",
sampleBaseDir+"PATtuple_296_2_7bH.root",
sampleBaseDir+"PATtuple_363_2_tvB.root",
sampleBaseDir+"PATtuple_377_2_5Ob.root",
sampleBaseDir+"PATtuple_649_2_2GH.root",
sampleBaseDir+"PATtuple_105_2_fj6.root",
sampleBaseDir+"PATtuple_499_2_AJS.root",
sampleBaseDir+"PATtuple_39_3_WfR.root",
sampleBaseDir+"PATtuple_327_2_91S.root",
sampleBaseDir+"PATtuple_6_2_rh3.root",
sampleBaseDir+"PATtuple_348_2_0Tj.root",
sampleBaseDir+"PATtuple_165_3_f28.root",
sampleBaseDir+"PATtuple_163_2_Yzi.root",
sampleBaseDir+"PATtuple_416_2_veP.root",
sampleBaseDir+"PATtuple_313_2_srZ.root",
sampleBaseDir+"PATtuple_235_2_Fn6.root",
sampleBaseDir+"PATtuple_258_2_wMe.root",
sampleBaseDir+"PATtuple_239_2_iQi.root",
sampleBaseDir+"PATtuple_483_2_2Ce.root",
sampleBaseDir+"PATtuple_79_2_wQf.root",
sampleBaseDir+"PATtuple_402_2_LD9.root",
sampleBaseDir+"PATtuple_311_2_vuf.root",
sampleBaseDir+"PATtuple_510_2_MqL.root",
sampleBaseDir+"PATtuple_501_2_8cc.root",
sampleBaseDir+"PATtuple_608_2_gwI.root",
sampleBaseDir+"PATtuple_446_2_M6c.root",
sampleBaseDir+"PATtuple_658_2_iSn.root",
sampleBaseDir+"PATtuple_122_2_3e3.root",
sampleBaseDir+"PATtuple_511_2_622.root",
sampleBaseDir+"PATtuple_478_2_0P2.root",
sampleBaseDir+"PATtuple_312_2_M4H.root",
sampleBaseDir+"PATtuple_532_2_ZzX.root",
sampleBaseDir+"PATtuple_82_2_g3v.root",
sampleBaseDir+"PATtuple_337_2_GpE.root",
sampleBaseDir+"PATtuple_647_2_lE8.root",
sampleBaseDir+"PATtuple_99_2_pvy.root",
sampleBaseDir+"PATtuple_462_2_qyP.root",
sampleBaseDir+"PATtuple_448_2_dZq.root",
sampleBaseDir+"PATtuple_149_2_WvK.root",
sampleBaseDir+"PATtuple_314_2_9Ra.root",
sampleBaseDir+"PATtuple_61_3_AtM.root",
sampleBaseDir+"PATtuple_530_2_XT7.root",
sampleBaseDir+"PATtuple_628_2_ruk.root",
sampleBaseDir+"PATtuple_238_3_0RW.root",
sampleBaseDir+"PATtuple_338_2_OWX.root",
sampleBaseDir+"PATtuple_630_2_eYd.root",
sampleBaseDir+"PATtuple_353_2_Yin.root",
sampleBaseDir+"PATtuple_531_2_qyB.root",
sampleBaseDir+"PATtuple_640_2_x3V.root",
sampleBaseDir+"PATtuple_260_2_mKm.root",
sampleBaseDir+"PATtuple_420_2_5n0.root",
sampleBaseDir+"PATtuple_490_2_6Tq.root",
sampleBaseDir+"PATtuple_399_2_JXX.root",
sampleBaseDir+"PATtuple_96_2_jaq.root",
sampleBaseDir+"PATtuple_397_2_akh.root",
sampleBaseDir+"PATtuple_365_2_3CG.root",
sampleBaseDir+"PATtuple_366_2_JKB.root",
sampleBaseDir+"PATtuple_421_2_Rr2.root",
sampleBaseDir+"PATtuple_374_2_uuV.root",
sampleBaseDir+"PATtuple_666_2_vov.root",
sampleBaseDir+"PATtuple_315_2_8y2.root",
sampleBaseDir+"PATtuple_204_2_QV2.root",
sampleBaseDir+"PATtuple_340_2_1hH.root",
sampleBaseDir+"PATtuple_259_2_QA6.root",
sampleBaseDir+"PATtuple_403_2_86J.root",
sampleBaseDir+"PATtuple_301_2_2pV.root",
sampleBaseDir+"PATtuple_244_2_ROd.root",
sampleBaseDir+"PATtuple_346_2_OHy.root",
sampleBaseDir+"PATtuple_497_1_hbb.root",
sampleBaseDir+"PATtuple_200_2_cHE.root",
sampleBaseDir+"PATtuple_25_2_Ieq.root",
sampleBaseDir+"PATtuple_274_2_VlO.root",
sampleBaseDir+"PATtuple_199_2_CZW.root",
sampleBaseDir+"PATtuple_126_2_4Xx.root",
sampleBaseDir+"PATtuple_150_2_EMZ.root",
sampleBaseDir+"PATtuple_279_2_vnS.root",
sampleBaseDir+"PATtuple_205_2_8l5.root",
sampleBaseDir+"PATtuple_528_1_d6F.root",
sampleBaseDir+"PATtuple_520_1_LI8.root",
sampleBaseDir+"PATtuple_297_1_pSo.root",
sampleBaseDir+"PATtuple_542_1_JHq.root",
sampleBaseDir+"PATtuple_280_1_kGc.root",
sampleBaseDir+"PATtuple_509_2_fZn.root",
sampleBaseDir+"PATtuple_350_2_hMO.root",
sampleBaseDir+"PATtuple_648_2_NDA.root",
sampleBaseDir+"PATtuple_307_2_74g.root",
sampleBaseDir+"PATtuple_373_2_mI2.root",
sampleBaseDir+"PATtuple_162_2_D5r.root",
sampleBaseDir+"PATtuple_525_2_UV1.root",
sampleBaseDir+"PATtuple_74_2_DMJ.root",
sampleBaseDir+"PATtuple_359_2_mMU.root",
sampleBaseDir+"PATtuple_217_2_9cE.root",
sampleBaseDir+"PATtuple_362_2_iyd.root",
sampleBaseDir+"PATtuple_324_2_CUA.root",
sampleBaseDir+"PATtuple_181_2_aq2.root",
sampleBaseDir+"PATtuple_254_3_l5G.root",
sampleBaseDir+"PATtuple_372_2_4f4.root",
sampleBaseDir+"PATtuple_508_2_9t2.root",
sampleBaseDir+"PATtuple_507_2_seC.root",
sampleBaseDir+"PATtuple_618_2_6Zw.root",
sampleBaseDir+"PATtuple_498_2_yvz.root",
sampleBaseDir+"PATtuple_414_2_HEH.root",
sampleBaseDir+"PATtuple_355_2_QvQ.root",
sampleBaseDir+"PATtuple_461_2_WOF.root",
sampleBaseDir+"PATtuple_120_2_LlQ.root",
sampleBaseDir+"PATtuple_291_1_YYt.root",
sampleBaseDir+"PATtuple_197_2_DPV.root",
sampleBaseDir+"PATtuple_380_1_Q7L.root",
sampleBaseDir+"PATtuple_287_2_Qyn.root",
sampleBaseDir+"PATtuple_141_2_8z4.root",
sampleBaseDir+"PATtuple_413_1_w5s.root",
sampleBaseDir+"PATtuple_178_2_PmM.root",
sampleBaseDir+"PATtuple_458_1_R2O.root",
sampleBaseDir+"PATtuple_449_2_B4z.root",
sampleBaseDir+"PATtuple_196_2_JwI.root",
sampleBaseDir+"PATtuple_379_1_MiW.root",
sampleBaseDir+"PATtuple_234_2_bZq.root",
sampleBaseDir+"PATtuple_64_2_OCT.root",
sampleBaseDir+"PATtuple_445_1_BjR.root",
sampleBaseDir+"PATtuple_255_1_qfp.root",
sampleBaseDir+"PATtuple_86_2_pJy.root",
sampleBaseDir+"PATtuple_276_1_qJz.root",
sampleBaseDir+"PATtuple_257_1_QiH.root",
sampleBaseDir+"PATtuple_209_2_v8D.root",
sampleBaseDir+"PATtuple_275_1_Z3H.root",
sampleBaseDir+"PATtuple_92_1_vUW.root",
sampleBaseDir+"PATtuple_476_1_f1T.root",
sampleBaseDir+"PATtuple_412_1_9D2.root",
sampleBaseDir+"PATtuple_645_1_82J.root",
sampleBaseDir+"PATtuple_482_1_6To.root",
sampleBaseDir+"PATtuple_230_1_oEX.root",
sampleBaseDir+"PATtuple_21_2_QKQ.root",
sampleBaseDir+"PATtuple_541_1_eKt.root",
sampleBaseDir+"PATtuple_67_2_xij.root",
sampleBaseDir+"PATtuple_491_1_iY7.root",
sampleBaseDir+"PATtuple_435_1_Upj.root",
sampleBaseDir+"PATtuple_459_2_ys1.root",
sampleBaseDir+"PATtuple_667_1_FGj.root",
sampleBaseDir+"PATtuple_232_2_SNy.root",
sampleBaseDir+"PATtuple_361_2_c5R.root",
sampleBaseDir+"PATtuple_395_2_kll.root",
sampleBaseDir+"PATtuple_418_1_TP8.root",
sampleBaseDir+"PATtuple_391_1_BNE.root",
sampleBaseDir+"PATtuple_233_1_zn4.root",
sampleBaseDir+"PATtuple_207_2_Z7E.root",
sampleBaseDir+"PATtuple_174_1_1co.root",
sampleBaseDir+"PATtuple_668_1_Xyt.root",
sampleBaseDir+"PATtuple_536_1_2LK.root",
sampleBaseDir+"PATtuple_277_1_Q0M.root",
sampleBaseDir+"PATtuple_171_2_DC9.root",
sampleBaseDir+"PATtuple_419_1_CQc.root",
sampleBaseDir+"PATtuple_669_1_7ru.root",
sampleBaseDir+"PATtuple_50_1_0mK.root",
sampleBaseDir+"PATtuple_84_1_zye.root",
sampleBaseDir+"PATtuple_52_1_f0K.root",
sampleBaseDir+"PATtuple_172_1_WTV.root",
sampleBaseDir+"PATtuple_83_1_l4M.root",
sampleBaseDir+"PATtuple_210_1_dLC.root",
sampleBaseDir+"PATtuple_23_1_bKf.root",
sampleBaseDir+"PATtuple_556_1_XBO.root",
sampleBaseDir+"PATtuple_73_1_ecV.root",
sampleBaseDir+"PATtuple_41_1_N9M.root",
sampleBaseDir+"PATtuple_32_1_KLw.root",
sampleBaseDir+"PATtuple_33_1_HFF.root",
sampleBaseDir+"PATtuple_40_1_k88.root",
sampleBaseDir+"PATtuple_53_1_7qO.root",
sampleBaseDir+"PATtuple_49_1_Q0s.root",
sampleBaseDir+"PATtuple_4_1_S4y.root",
sampleBaseDir+"PATtuple_51_1_W81.root",
sampleBaseDir+"PATtuple_34_1_hdM.root",
sampleBaseDir+"PATtuple_35_1_f7B.root",
sampleBaseDir+"PATtuple_57_1_viB.root",
sampleBaseDir+"PATtuple_54_1_Hur.root",
sampleBaseDir+"PATtuple_36_1_EZh.root",
]