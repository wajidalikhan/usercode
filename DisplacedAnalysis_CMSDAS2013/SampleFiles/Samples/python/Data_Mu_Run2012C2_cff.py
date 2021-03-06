sampleDataSet = '/DoubleMu/Run2012C-PromptReco-v2/AOD'

# original (i.e. RECO file) release,
# not the one we plan to process them with
sampleRelease = "CMSSW_5_3_2_patch4" 
# release used to create new files with
sampleProcessRelease = "CMSSW_5_3_5" 

sampleNumEvents = 26816721 # according to DBS, as of 29 October 2012

# global tag needs to be chosen to match release, trigger menu and alignment conditions.
# see https://twiki.cern.ch/twiki/bin/view/CMS/SWGuideFrontierConditions
sampleGlobalTag = 'GR_P_V41_AN2::All'

# data quality run/lumi section selection
sampleJSON = "https://cms-service-dqm.web.cern.ch/cms-service-dqm/CAF/certification/Collisions12/8TeV/Prompt/Cert_190456-203002_8TeV_PromptReco_Collisions12_JSON_MuonPhys_v2.txt"
        
# restrict run range (mainly to get a sample with consistent trigger configuration)
sampleRunRange = [190456-99999999]

# use checkAllFilesOpened whenever possible, and noDuplicateCheck when necessary
sampleDuplicateCheckMode = "checkAllFilesOpened"

# "DATA" or "MC"
sampleType = "DATA"





samplePatDBSName=""

sampleBaseDir="dcap://dcap.pp.rl.ac.uk///pnfs/pp.rl.ac.uk/data/cms/store/user/ejclemen//DoubleMu/Data_Mu_Run2012C2_pat_20121101/c50c5bf922918961d6703f23449eaeb8/"
samplePatFiles = [
sampleBaseDir+"PATtuple_357_0_9EE.root",
sampleBaseDir+"PATtuple_356_0_MkK.root",
sampleBaseDir+"PATtuple_57_0_XOR.root",
sampleBaseDir+"PATtuple_475_0_mSO.root",
sampleBaseDir+"PATtuple_179_0_Syp.root",
sampleBaseDir+"PATtuple_507_0_IkF.root",
sampleBaseDir+"PATtuple_344_0_WI4.root",
sampleBaseDir+"PATtuple_508_0_eXG.root",
sampleBaseDir+"PATtuple_438_0_dSo.root",
sampleBaseDir+"PATtuple_620_0_1Yr.root",
sampleBaseDir+"PATtuple_426_0_6i9.root",
sampleBaseDir+"PATtuple_230_0_aHq.root",
sampleBaseDir+"PATtuple_509_0_f8B.root",
sampleBaseDir+"PATtuple_512_0_Lrt.root",
sampleBaseDir+"PATtuple_402_0_ECG.root",
sampleBaseDir+"PATtuple_93_2_XpB.root",
sampleBaseDir+"PATtuple_403_0_b0Z.root",
sampleBaseDir+"PATtuple_506_0_UG2.root",
sampleBaseDir+"PATtuple_371_0_NKB.root",
sampleBaseDir+"PATtuple_400_0_Ny7.root",
sampleBaseDir+"PATtuple_462_0_YAG.root",
sampleBaseDir+"PATtuple_621_0_8NA.root",
sampleBaseDir+"PATtuple_370_0_TQJ.root",
sampleBaseDir+"PATtuple_215_2_iNr.root",
sampleBaseDir+"PATtuple_380_2_t0c.root",
sampleBaseDir+"PATtuple_300_0_dWW.root",
sampleBaseDir+"PATtuple_407_0_vk0.root",
sampleBaseDir+"PATtuple_618_0_ozm.root",
sampleBaseDir+"PATtuple_611_0_Sj2.root",
sampleBaseDir+"PATtuple_221_0_X1z.root",
sampleBaseDir+"PATtuple_105_0_Mmb.root",
sampleBaseDir+"PATtuple_465_0_eTg.root",
sampleBaseDir+"PATtuple_6_1_Uim.root",
sampleBaseDir+"PATtuple_84_0_rde.root",
sampleBaseDir+"PATtuple_222_0_O31.root",
sampleBaseDir+"PATtuple_429_0_M5N.root",
sampleBaseDir+"PATtuple_557_0_GQn.root",
sampleBaseDir+"PATtuple_224_0_AEx.root",
sampleBaseDir+"PATtuple_77_0_P6f.root",
sampleBaseDir+"PATtuple_293_1_MF5.root",
sampleBaseDir+"PATtuple_286_1_KLH.root",
sampleBaseDir+"PATtuple_326_0_hkp.root",
sampleBaseDir+"PATtuple_244_1_lax.root",
sampleBaseDir+"PATtuple_289_0_X38.root",
sampleBaseDir+"PATtuple_589_0_0TQ.root",
sampleBaseDir+"PATtuple_612_0_FEX.root",
sampleBaseDir+"PATtuple_422_1_CUB.root",
sampleBaseDir+"PATtuple_82_0_TBG.root",
sampleBaseDir+"PATtuple_501_0_nQV.root",
sampleBaseDir+"PATtuple_229_0_OrH.root",
sampleBaseDir+"PATtuple_427_1_WIw.root",
sampleBaseDir+"PATtuple_579_0_Oyn.root",
sampleBaseDir+"PATtuple_37_1_emQ.root",
sampleBaseDir+"PATtuple_318_0_6fl.root",
sampleBaseDir+"PATtuple_327_0_AaW.root",
sampleBaseDir+"PATtuple_261_0_FOt.root",
sampleBaseDir+"PATtuple_585_0_HJI.root",
sampleBaseDir+"PATtuple_260_0_Nzk.root",
sampleBaseDir+"PATtuple_515_0_ZWL.root",
sampleBaseDir+"PATtuple_239_0_4pC.root",
sampleBaseDir+"PATtuple_437_0_WLo.root",
sampleBaseDir+"PATtuple_423_1_7lm.root",
sampleBaseDir+"PATtuple_259_0_Pp6.root",
sampleBaseDir+"PATtuple_558_0_zXc.root",
sampleBaseDir+"PATtuple_417_0_Zmb.root",
sampleBaseDir+"PATtuple_392_0_7St.root",
sampleBaseDir+"PATtuple_555_0_bXC.root",
sampleBaseDir+"PATtuple_137_1_qAG.root",
sampleBaseDir+"PATtuple_592_0_B2z.root",
sampleBaseDir+"PATtuple_330_0_m9z.root",
sampleBaseDir+"PATtuple_473_0_uEZ.root",
sampleBaseDir+"PATtuple_532_0_Lze.root",
sampleBaseDir+"PATtuple_488_0_YPf.root",
sampleBaseDir+"PATtuple_418_0_qWv.root",
sampleBaseDir+"PATtuple_412_0_aKk.root",
sampleBaseDir+"PATtuple_317_0_Tef.root",
sampleBaseDir+"PATtuple_301_0_zOb.root",
sampleBaseDir+"PATtuple_304_0_lFx.root",
sampleBaseDir+"PATtuple_534_0_Rd6.root",
sampleBaseDir+"PATtuple_241_0_0Eu.root",
sampleBaseDir+"PATtuple_489_0_18Z.root",
sampleBaseDir+"PATtuple_599_0_EL7.root",
sampleBaseDir+"PATtuple_443_1_Bxf.root",
sampleBaseDir+"PATtuple_119_0_j4Y.root",
sampleBaseDir+"PATtuple_138_1_uSP.root",
sampleBaseDir+"PATtuple_243_0_9ax.root",
sampleBaseDir+"PATtuple_352_0_P4M.root",
sampleBaseDir+"PATtuple_581_0_JNK.root",
sampleBaseDir+"PATtuple_549_0_yhy.root",
sampleBaseDir+"PATtuple_550_0_m50.root",
sampleBaseDir+"PATtuple_468_0_xHm.root",
sampleBaseDir+"PATtuple_533_0_dl2.root",
sampleBaseDir+"PATtuple_540_0_H0j.root",
sampleBaseDir+"PATtuple_288_0_xLP.root",
sampleBaseDir+"PATtuple_329_0_1bn.root",
sampleBaseDir+"PATtuple_499_0_HDp.root",
sampleBaseDir+"PATtuple_213_1_pBB.root",
sampleBaseDir+"PATtuple_262_0_bar.root",
sampleBaseDir+"PATtuple_177_0_8Vk.root",
sampleBaseDir+"PATtuple_366_0_Nvg.root",
sampleBaseDir+"PATtuple_246_0_cLu.root",
sampleBaseDir+"PATtuple_604_0_T0Q.root",
sampleBaseDir+"PATtuple_580_0_gJ8.root",
sampleBaseDir+"PATtuple_319_0_55H.root",
sampleBaseDir+"PATtuple_460_0_Ji5.root",
sampleBaseDir+"PATtuple_459_0_Pz2.root",
sampleBaseDir+"PATtuple_586_0_FQF.root",
sampleBaseDir+"PATtuple_522_0_ibn.root",
sampleBaseDir+"PATtuple_525_0_GFA.root",
sampleBaseDir+"PATtuple_605_0_x2a.root",
sampleBaseDir+"PATtuple_354_0_X8l.root",
sampleBaseDir+"PATtuple_362_0_5eb.root",
sampleBaseDir+"PATtuple_552_0_cGR.root",
sampleBaseDir+"PATtuple_307_0_IiY.root",
sampleBaseDir+"PATtuple_472_0_TwO.root",
sampleBaseDir+"PATtuple_103_0_e5F.root",
sampleBaseDir+"PATtuple_298_0_CW6.root",
sampleBaseDir+"PATtuple_474_0_nkd.root",
sampleBaseDir+"PATtuple_476_0_wMa.root",
sampleBaseDir+"PATtuple_582_0_5vX.root",
sampleBaseDir+"PATtuple_419_0_Nxl.root",
sampleBaseDir+"PATtuple_369_0_y5v.root",
sampleBaseDir+"PATtuple_617_0_n7I.root",
sampleBaseDir+"PATtuple_332_0_kyI.root",
sampleBaseDir+"PATtuple_214_1_je3.root",
sampleBaseDir+"PATtuple_100_1_At4.root",
sampleBaseDir+"PATtuple_269_0_mPQ.root",
sampleBaseDir+"PATtuple_140_2_jUi.root",
sampleBaseDir+"PATtuple_204_0_VUi.root",
sampleBaseDir+"PATtuple_505_0_3iT.root",
sampleBaseDir+"PATtuple_54_0_U4P.root",
sampleBaseDir+"PATtuple_190_3_piW.root",
sampleBaseDir+"PATtuple_587_0_Hdj.root",
sampleBaseDir+"PATtuple_343_0_hYM.root",
sampleBaseDir+"PATtuple_302_1_v20.root",
sampleBaseDir+"PATtuple_320_1_XrY.root",
sampleBaseDir+"PATtuple_578_0_fUW.root",
sampleBaseDir+"PATtuple_270_2_d3Y.root",
sampleBaseDir+"PATtuple_342_0_6TW.root",
sampleBaseDir+"PATtuple_416_0_g2c.root",
sampleBaseDir+"PATtuple_420_0_ckt.root",
sampleBaseDir+"PATtuple_421_0_CZJ.root",
sampleBaseDir+"PATtuple_616_0_1Zn.root",
sampleBaseDir+"PATtuple_287_0_wnl.root",
sampleBaseDir+"PATtuple_202_0_kK1.root",
sampleBaseDir+"PATtuple_619_0_dQr.root",
sampleBaseDir+"PATtuple_397_0_AyE.root",
sampleBaseDir+"PATtuple_205_0_OXJ.root",
sampleBaseDir+"PATtuple_176_0_hMd.root",
sampleBaseDir+"PATtuple_151_0_E0m.root",
sampleBaseDir+"PATtuple_554_0_XND.root",
sampleBaseDir+"PATtuple_123_0_JP2.root",
sampleBaseDir+"PATtuple_584_0_M0u.root",
sampleBaseDir+"PATtuple_390_0_XUq.root",
sampleBaseDir+"PATtuple_149_0_Qo5.root",
sampleBaseDir+"PATtuple_614_0_jeE.root",
sampleBaseDir+"PATtuple_238_0_RDI.root",
sampleBaseDir+"PATtuple_295_0_xrV.root",
sampleBaseDir+"PATtuple_148_0_nda.root",
sampleBaseDir+"PATtuple_127_0_KgI.root",
sampleBaseDir+"PATtuple_30_1_nEL.root",
sampleBaseDir+"PATtuple_541_0_gLo.root",
sampleBaseDir+"PATtuple_455_1_DjR.root",
sampleBaseDir+"PATtuple_542_0_F78.root",
sampleBaseDir+"PATtuple_247_0_zI5.root",
sampleBaseDir+"PATtuple_490_0_jhg.root",
sampleBaseDir+"PATtuple_553_0_wnD.root",
sampleBaseDir+"PATtuple_531_0_KN0.root",
sampleBaseDir+"PATtuple_294_0_pO0.root",
sampleBaseDir+"PATtuple_121_0_IQP.root",
sampleBaseDir+"PATtuple_331_0_geJ.root",
sampleBaseDir+"PATtuple_551_0_15J.root",
sampleBaseDir+"PATtuple_139_1_dxG.root",
sampleBaseDir+"PATtuple_220_0_yZE.root",
sampleBaseDir+"PATtuple_414_0_Lpg.root",
sampleBaseDir+"PATtuple_398_0_yFG.root",
sampleBaseDir+"PATtuple_524_0_1WT.root",
sampleBaseDir+"PATtuple_58_0_qK2.root",
sampleBaseDir+"PATtuple_271_1_CVF.root",
sampleBaseDir+"PATtuple_391_0_MY9.root",
sampleBaseDir+"PATtuple_249_0_iAo.root",
sampleBaseDir+"PATtuple_162_0_kZe.root",
sampleBaseDir+"PATtuple_323_0_iEa.root",
sampleBaseDir+"PATtuple_487_0_fYC.root",
sampleBaseDir+"PATtuple_478_0_PjD.root",
sampleBaseDir+"PATtuple_546_0_b1C.root",
sampleBaseDir+"PATtuple_16_0_2IM.root",
sampleBaseDir+"PATtuple_236_0_Xmz.root",
sampleBaseDir+"PATtuple_233_0_jJq.root",
sampleBaseDir+"PATtuple_312_0_OC4.root",
sampleBaseDir+"PATtuple_237_0_ouN.root",
sampleBaseDir+"PATtuple_564_0_h5E.root",
sampleBaseDir+"PATtuple_174_0_ERT.root",
sampleBaseDir+"PATtuple_172_0_gp3.root",
sampleBaseDir+"PATtuple_266_0_OXU.root",
sampleBaseDir+"PATtuple_161_0_AYk.root",
sampleBaseDir+"PATtuple_562_0_uZ2.root",
sampleBaseDir+"PATtuple_39_0_TMT.root",
sampleBaseDir+"PATtuple_306_0_6OS.root",
sampleBaseDir+"PATtuple_267_0_jHj.root",
sampleBaseDir+"PATtuple_461_0_CJK.root",
sampleBaseDir+"PATtuple_183_0_4bT.root",
sampleBaseDir+"PATtuple_184_0_nek.root",
sampleBaseDir+"PATtuple_435_0_UuW.root",
sampleBaseDir+"PATtuple_197_0_9Q5.root",
sampleBaseDir+"PATtuple_106_0_nQB.root",
sampleBaseDir+"PATtuple_389_1_N1j.root",
sampleBaseDir+"PATtuple_372_0_kQ9.root",
sampleBaseDir+"PATtuple_543_0_C8Q.root",
sampleBaseDir+"PATtuple_85_1_fm8.root",
sampleBaseDir+"PATtuple_528_0_Sp2.root",
sampleBaseDir+"PATtuple_311_0_OAY.root",
sampleBaseDir+"PATtuple_18_1_daN.root",
sampleBaseDir+"PATtuple_351_0_bWU.root",
sampleBaseDir+"PATtuple_142_0_QEQ.root",
sampleBaseDir+"PATtuple_404_0_xUw.root",
sampleBaseDir+"PATtuple_14_0_LdH.root",
sampleBaseDir+"PATtuple_252_0_H0B.root",
sampleBaseDir+"PATtuple_27_0_oA5.root",
sampleBaseDir+"PATtuple_310_0_4Xu.root",
sampleBaseDir+"PATtuple_548_0_HDZ.root",
sampleBaseDir+"PATtuple_74_0_Vb0.root",
sampleBaseDir+"PATtuple_315_0_Gho.root",
sampleBaseDir+"PATtuple_324_0_T8H.root",
sampleBaseDir+"PATtuple_96_1_1ap.root",
sampleBaseDir+"PATtuple_235_0_TEP.root",
sampleBaseDir+"PATtuple_25_0_ZXk.root",
sampleBaseDir+"PATtuple_467_0_lkV.root",
sampleBaseDir+"PATtuple_539_0_0Re.root",
sampleBaseDir+"PATtuple_353_0_WBR.root",
sampleBaseDir+"PATtuple_436_0_gRS.root",
sampleBaseDir+"PATtuple_175_0_jiN.root",
sampleBaseDir+"PATtuple_560_0_Cn0.root",
sampleBaseDir+"PATtuple_87_2_yGt.root",
sampleBaseDir+"PATtuple_147_0_cuM.root",
sampleBaseDir+"PATtuple_556_0_M8d.root",
sampleBaseDir+"PATtuple_498_0_VYb.root",
sampleBaseDir+"PATtuple_537_0_zLV.root",
sampleBaseDir+"PATtuple_2_1_mrv.root",
sampleBaseDir+"PATtuple_129_0_3Q9.root",
sampleBaseDir+"PATtuple_530_0_zhr.root",
sampleBaseDir+"PATtuple_615_0_Jlz.root",
sampleBaseDir+"PATtuple_240_0_0Vc.root",
sampleBaseDir+"PATtuple_242_0_uoj.root",
sampleBaseDir+"PATtuple_393_0_yLm.root",
sampleBaseDir+"PATtuple_424_1_eun.root",
sampleBaseDir+"PATtuple_523_0_OEg.root",
sampleBaseDir+"PATtuple_378_1_q2Y.root",
sampleBaseDir+"PATtuple_191_1_op3.root",
sampleBaseDir+"PATtuple_590_0_UFE.root",
sampleBaseDir+"PATtuple_367_0_ad1.root",
sampleBaseDir+"PATtuple_535_0_nJ7.root",
sampleBaseDir+"PATtuple_503_0_Yhq.root",
sampleBaseDir+"PATtuple_379_1_vKv.root",
sampleBaseDir+"PATtuple_97_1_Syv.root",
sampleBaseDir+"PATtuple_245_0_hm5.root",
sampleBaseDir+"PATtuple_305_0_w59.root",
sampleBaseDir+"PATtuple_328_0_A9b.root",
sampleBaseDir+"PATtuple_504_0_8Zi.root",
sampleBaseDir+"PATtuple_536_0_RPG.root",
sampleBaseDir+"PATtuple_359_0_CNG.root",
sampleBaseDir+"PATtuple_60_0_RzH.root",
sampleBaseDir+"PATtuple_439_0_RVO.root",
sampleBaseDir+"PATtuple_595_0_UCD.root",
sampleBaseDir+"PATtuple_98_1_ZfY.root",
sampleBaseDir+"PATtuple_1_1_zX8.root",
sampleBaseDir+"PATtuple_303_0_xnz.root",
sampleBaseDir+"PATtuple_368_0_602.root",
sampleBaseDir+"PATtuple_180_0_pt8.root",
sampleBaseDir+"PATtuple_75_0_nBo.root",
sampleBaseDir+"PATtuple_141_0_TDc.root",
sampleBaseDir+"PATtuple_227_0_Vie.root",
sampleBaseDir+"PATtuple_325_0_iS5.root",
sampleBaseDir+"PATtuple_348_0_dbp.root",
sampleBaseDir+"PATtuple_95_1_n6q.root",
sampleBaseDir+"PATtuple_109_0_uon.root",
sampleBaseDir+"PATtuple_428_0_mvr.root",
sampleBaseDir+"PATtuple_154_0_0eM.root",
sampleBaseDir+"PATtuple_510_0_C5d.root",
sampleBaseDir+"PATtuple_463_0_K8y.root",
sampleBaseDir+"PATtuple_570_0_scd.root",
sampleBaseDir+"PATtuple_349_0_vcv.root",
sampleBaseDir+"PATtuple_33_1_1p7.root",
sampleBaseDir+"PATtuple_29_1_nHY.root",
sampleBaseDir+"PATtuple_225_0_xam.root",
sampleBaseDir+"PATtuple_24_0_Nga.root",
sampleBaseDir+"PATtuple_597_0_r5G.root",
sampleBaseDir+"PATtuple_511_0_rpT.root",
sampleBaseDir+"PATtuple_406_0_7sX.root",
sampleBaseDir+"PATtuple_226_0_qwV.root",
sampleBaseDir+"PATtuple_146_0_tXe.root",
sampleBaseDir+"PATtuple_209_1_SRo.root",
sampleBaseDir+"PATtuple_187_1_H9r.root",
sampleBaseDir+"PATtuple_219_1_9tW.root",
sampleBaseDir+"PATtuple_335_0_zEl.root",
sampleBaseDir+"PATtuple_32_1_IKu.root",
sampleBaseDir+"PATtuple_526_0_jh5.root",
sampleBaseDir+"PATtuple_600_0_dtg.root",
sampleBaseDir+"PATtuple_486_0_WGX.root",
sampleBaseDir+"PATtuple_596_0_GQe.root",
sampleBaseDir+"PATtuple_399_0_dnJ.root",
sampleBaseDir+"PATtuple_388_1_I2P.root",
sampleBaseDir+"PATtuple_470_0_KzM.root",
sampleBaseDir+"PATtuple_275_1_v1O.root",
sampleBaseDir+"PATtuple_296_0_k0t.root",
sampleBaseDir+"PATtuple_374_0_i7h.root",
sampleBaseDir+"PATtuple_277_1_m5r.root",
sampleBaseDir+"PATtuple_456_1_dAL.root",
sampleBaseDir+"PATtuple_355_0_lmM.root",
sampleBaseDir+"PATtuple_274_1_Vzv.root",
sampleBaseDir+"PATtuple_40_0_8IJ.root",
sampleBaseDir+"PATtuple_471_0_01L.root",
sampleBaseDir+"PATtuple_563_0_UVN.root",
sampleBaseDir+"PATtuple_610_0_01T.root",
sampleBaseDir+"PATtuple_234_0_Uca.root",
sampleBaseDir+"PATtuple_591_0_6dv.root",
sampleBaseDir+"PATtuple_598_0_1R3.root",
sampleBaseDir+"PATtuple_469_0_RIP.root",
sampleBaseDir+"PATtuple_173_0_kn9.root",
sampleBaseDir+"PATtuple_181_0_d8L.root",
sampleBaseDir+"PATtuple_23_0_p0A.root",
sampleBaseDir+"PATtuple_199_0_1D6.root",
sampleBaseDir+"PATtuple_232_0_DzH.root",
sampleBaseDir+"PATtuple_408_0_0FT.root",
sampleBaseDir+"PATtuple_514_0_s2N.root",
sampleBaseDir+"PATtuple_133_1_7o8.root",
sampleBaseDir+"PATtuple_448_0_2bq.root",
sampleBaseDir+"PATtuple_350_0_81F.root",
sampleBaseDir+"PATtuple_194_0_izq.root",
sampleBaseDir+"PATtuple_134_1_nVU.root",
sampleBaseDir+"PATtuple_254_0_UKg.root",
sampleBaseDir+"PATtuple_78_0_TTq.root",
sampleBaseDir+"PATtuple_314_0_rw0.root",
sampleBaseDir+"PATtuple_170_0_Hj3.root",
sampleBaseDir+"PATtuple_92_1_aMd.root",
sampleBaseDir+"PATtuple_144_0_3cC.root",
sampleBaseDir+"PATtuple_185_1_h5O.root",
sampleBaseDir+"PATtuple_62_0_Dcq.root",
sampleBaseDir+"PATtuple_574_0_YFx.root",
sampleBaseDir+"PATtuple_42_0_mdG.root",
sampleBaseDir+"PATtuple_484_0_jkE.root",
sampleBaseDir+"PATtuple_373_0_KYC.root",
sampleBaseDir+"PATtuple_76_0_ZVy.root",
sampleBaseDir+"PATtuple_223_0_L6d.root",
sampleBaseDir+"PATtuple_394_0_bOV.root",
sampleBaseDir+"PATtuple_415_0_Xm4.root",
sampleBaseDir+"PATtuple_31_1_1UF.root",
sampleBaseDir+"PATtuple_122_0_tYd.root",
sampleBaseDir+"PATtuple_208_1_Idn.root",
sampleBaseDir+"PATtuple_381_1_QEX.root",
sampleBaseDir+"PATtuple_19_0_NSm.root",
sampleBaseDir+"PATtuple_273_1_Yuw.root",
sampleBaseDir+"PATtuple_291_0_AEF.root",
sampleBaseDir+"PATtuple_358_0_Gas.root",
sampleBaseDir+"PATtuple_336_0_MiW.root",
sampleBaseDir+"PATtuple_47_0_IzT.root",
sampleBaseDir+"PATtuple_102_1_OTs.root",
sampleBaseDir+"PATtuple_56_0_IIL.root",
sampleBaseDir+"PATtuple_495_0_HDM.root",
sampleBaseDir+"PATtuple_364_0_8MV.root",
sampleBaseDir+"PATtuple_593_0_VfJ.root",
sampleBaseDir+"PATtuple_464_0_HGS.root",
sampleBaseDir+"PATtuple_333_0_zVF.root",
sampleBaseDir+"PATtuple_5_1_sL1.root",
sampleBaseDir+"PATtuple_276_1_OE8.root",
sampleBaseDir+"PATtuple_338_0_SVk.root",
sampleBaseDir+"PATtuple_363_0_TBV.root",
sampleBaseDir+"PATtuple_497_0_pea.root",
sampleBaseDir+"PATtuple_500_0_RWd.root",
sampleBaseDir+"PATtuple_55_0_EUb.root",
sampleBaseDir+"PATtuple_178_0_vfg.root",
sampleBaseDir+"PATtuple_263_0_ibp.root",
sampleBaseDir+"PATtuple_192_0_kYv.root",
sampleBaseDir+"PATtuple_203_0_IfE.root",
sampleBaseDir+"PATtuple_334_0_r32.root",
sampleBaseDir+"PATtuple_321_0_7oH.root",
sampleBaseDir+"PATtuple_449_0_SAN.root",
sampleBaseDir+"PATtuple_607_0_CIG.root",
sampleBaseDir+"PATtuple_17_1_6r7.root",
sampleBaseDir+"PATtuple_217_1_vVr.root",
sampleBaseDir+"PATtuple_35_0_adc.root",
sampleBaseDir+"PATtuple_527_0_Thv.root",
sampleBaseDir+"PATtuple_601_0_oIi.root",
sampleBaseDir+"PATtuple_440_0_UN4.root",
sampleBaseDir+"PATtuple_160_0_4mc.root",
sampleBaseDir+"PATtuple_64_0_gjy.root",
sampleBaseDir+"PATtuple_268_0_9Ro.root",
sampleBaseDir+"PATtuple_297_0_4PX.root",
sampleBaseDir+"PATtuple_544_0_TVY.root",
sampleBaseDir+"PATtuple_444_0_z1j.root",
sampleBaseDir+"PATtuple_493_0_OBN.root",
sampleBaseDir+"PATtuple_442_0_EFh.root",
sampleBaseDir+"PATtuple_20_0_ksJ.root",
sampleBaseDir+"PATtuple_496_0_ve2.root",
sampleBaseDir+"PATtuple_494_0_x4c.root",
sampleBaseDir+"PATtuple_365_0_Uql.root",
sampleBaseDir+"PATtuple_107_0_Ltv.root",
sampleBaseDir+"PATtuple_480_0_EfH.root",
sampleBaseDir+"PATtuple_345_0_ruR.root",
sampleBaseDir+"PATtuple_481_0_G8m.root",
sampleBaseDir+"PATtuple_316_0_KcZ.root",
sampleBaseDir+"PATtuple_250_0_63S.root",
sampleBaseDir+"PATtuple_114_0_AzU.root",
sampleBaseDir+"PATtuple_483_0_OSi.root",
sampleBaseDir+"PATtuple_340_0_uis.root",
sampleBaseDir+"PATtuple_482_0_yKs.root",
sampleBaseDir+"PATtuple_193_0_bjX.root",
sampleBaseDir+"PATtuple_248_0_6JJ.root",
sampleBaseDir+"PATtuple_136_1_cNX.root",
sampleBaseDir+"PATtuple_253_0_LJG.root",
sampleBaseDir+"PATtuple_434_0_CGZ.root",
sampleBaseDir+"PATtuple_145_0_ItB.root",
sampleBaseDir+"PATtuple_602_0_pPK.root",
sampleBaseDir+"PATtuple_572_0_0tQ.root",
sampleBaseDir+"PATtuple_71_0_jzd.root",
sampleBaseDir+"PATtuple_51_0_JRC.root",
sampleBaseDir+"PATtuple_457_1_Hgs.root",
sampleBaseDir+"PATtuple_450_0_a4y.root",
sampleBaseDir+"PATtuple_132_2_ZfV.root",
sampleBaseDir+"PATtuple_8_1_Xe5.root",
sampleBaseDir+"PATtuple_200_0_PHX.root",
sampleBaseDir+"PATtuple_258_0_Q3O.root",
sampleBaseDir+"PATtuple_125_0_o7s.root",
sampleBaseDir+"PATtuple_594_0_58E.root",
sampleBaseDir+"PATtuple_447_0_uM1.root",
sampleBaseDir+"PATtuple_94_1_bEZ.root",
sampleBaseDir+"PATtuple_431_0_m7b.root",
sampleBaseDir+"PATtuple_124_0_GGD.root",
sampleBaseDir+"PATtuple_163_0_dDt.root",
sampleBaseDir+"PATtuple_313_0_aOT.root",
sampleBaseDir+"PATtuple_152_0_yUj.root",
sampleBaseDir+"PATtuple_433_0_1XY.root",
sampleBaseDir+"PATtuple_383_1_7Jm.root",
sampleBaseDir+"PATtuple_165_0_vZP.root",
sampleBaseDir+"PATtuple_430_0_xvM.root",
sampleBaseDir+"PATtuple_405_0_Y2I.root",
sampleBaseDir+"PATtuple_409_0_QkJ.root",
sampleBaseDir+"PATtuple_50_0_dwz.root",
sampleBaseDir+"PATtuple_26_0_sdr.root",
sampleBaseDir+"PATtuple_299_0_QL3.root",
sampleBaseDir+"PATtuple_410_0_G40.root",
sampleBaseDir+"PATtuple_466_0_TUd.root",
sampleBaseDir+"PATtuple_108_0_4DB.root",
sampleBaseDir+"PATtuple_588_0_xA1.root",
sampleBaseDir+"PATtuple_376_1_ePb.root",
sampleBaseDir+"PATtuple_11_0_2zp.root",
sampleBaseDir+"PATtuple_88_1_fOA.root",
sampleBaseDir+"PATtuple_168_0_QUE.root",
sampleBaseDir+"PATtuple_280_1_urx.root",
sampleBaseDir+"PATtuple_167_0_G0I.root",
sampleBaseDir+"PATtuple_156_0_rUF.root",
sampleBaseDir+"PATtuple_341_0_7GZ.root",
sampleBaseDir+"PATtuple_164_0_8Kf.root",
sampleBaseDir+"PATtuple_89_1_3nV.root",
sampleBaseDir+"PATtuple_188_1_oNM.root",
sampleBaseDir+"PATtuple_21_0_on0.root",
sampleBaseDir+"PATtuple_69_0_3jK.root",
sampleBaseDir+"PATtuple_561_0_GfJ.root",
sampleBaseDir+"PATtuple_189_1_H3w.root",
sampleBaseDir+"PATtuple_135_1_AIs.root",
sampleBaseDir+"PATtuple_186_1_BlO.root",
sampleBaseDir+"PATtuple_46_0_9vD.root",
sampleBaseDir+"PATtuple_68_0_OsE.root",
sampleBaseDir+"PATtuple_7_1_a2i.root",
sampleBaseDir+"PATtuple_66_0_Auv.root",
sampleBaseDir+"PATtuple_382_1_s1w.root",
sampleBaseDir+"PATtuple_452_1_sBA.root",
sampleBaseDir+"PATtuple_44_0_DfJ.root",
sampleBaseDir+"PATtuple_79_0_RyY.root",
sampleBaseDir+"PATtuple_576_0_V4g.root",
sampleBaseDir+"PATtuple_9_1_a3W.root",
sampleBaseDir+"PATtuple_519_0_21N.root",
sampleBaseDir+"PATtuple_577_0_TW6.root",
sampleBaseDir+"PATtuple_445_0_h8Y.root",
sampleBaseDir+"PATtuple_281_1_bvk.root",
sampleBaseDir+"PATtuple_547_0_0e7.root",
sampleBaseDir+"PATtuple_41_0_cj4.root",
sampleBaseDir+"PATtuple_575_0_WMI.root",
sampleBaseDir+"PATtuple_117_0_Wth.root",
sampleBaseDir+"PATtuple_22_0_6yb.root",
sampleBaseDir+"PATtuple_485_0_S3j.root",
sampleBaseDir+"PATtuple_375_0_XCB.root",
sampleBaseDir+"PATtuple_322_0_Pl7.root",
sampleBaseDir+"PATtuple_360_0_Rre.root",
sampleBaseDir+"PATtuple_413_0_q6r.root",
sampleBaseDir+"PATtuple_361_0_SAK.root",
sampleBaseDir+"PATtuple_491_0_JWS.root",
sampleBaseDir+"PATtuple_207_1_nY7.root",
sampleBaseDir+"PATtuple_613_0_PX4.root",
sampleBaseDir+"PATtuple_272_1_d1m.root",
sampleBaseDir+"PATtuple_120_0_18e.root",
sampleBaseDir+"PATtuple_265_0_bm2.root",
sampleBaseDir+"PATtuple_441_0_GSN.root",
sampleBaseDir+"PATtuple_395_0_aD2.root",
sampleBaseDir+"PATtuple_477_0_vbT.root",
sampleBaseDir+"PATtuple_502_0_sRl.root",
sampleBaseDir+"PATtuple_565_0_e7N.root",
sampleBaseDir+"PATtuple_396_0_x1R.root",
sampleBaseDir+"PATtuple_492_0_pQB.root",
sampleBaseDir+"PATtuple_80_0_7Uz.root",
sampleBaseDir+"PATtuple_346_0_kH5.root",
sampleBaseDir+"PATtuple_264_0_p2Z.root",
sampleBaseDir+"PATtuple_309_0_Lfn.root",
sampleBaseDir+"PATtuple_290_0_KX8.root",
sampleBaseDir+"PATtuple_583_0_ul5.root",
sampleBaseDir+"PATtuple_101_1_dhk.root",
sampleBaseDir+"PATtuple_545_0_U2n.root",
sampleBaseDir+"PATtuple_104_0_DGK.root",
sampleBaseDir+"PATtuple_308_0_eXD.root",
sampleBaseDir+"PATtuple_198_0_Q8J.root",
sampleBaseDir+"PATtuple_48_0_380.root",
sampleBaseDir+"PATtuple_479_0_wPu.root",
sampleBaseDir+"PATtuple_158_0_o0q.root",
sampleBaseDir+"PATtuple_216_1_9F7.root",
sampleBaseDir+"PATtuple_559_0_fdl.root",
sampleBaseDir+"PATtuple_231_0_Mdp.root",
sampleBaseDir+"PATtuple_53_0_9ZT.root",
sampleBaseDir+"PATtuple_538_0_Gyp.root",
sampleBaseDir+"PATtuple_81_0_JSr.root",
sampleBaseDir+"PATtuple_212_1_gEL.root",
sampleBaseDir+"PATtuple_72_0_AM8.root",
sampleBaseDir+"PATtuple_45_0_iLc.root",
sampleBaseDir+"PATtuple_150_0_wGh.root",
sampleBaseDir+"PATtuple_453_1_DGr.root",
sampleBaseDir+"PATtuple_38_0_8BC.root",
sampleBaseDir+"PATtuple_128_0_gIX.root",
sampleBaseDir+"PATtuple_401_0_7rJ.root",
sampleBaseDir+"PATtuple_131_1_1Tu.root",
sampleBaseDir+"PATtuple_61_0_Rhm.root",
sampleBaseDir+"PATtuple_425_0_6e5.root",
sampleBaseDir+"PATtuple_257_0_bJa.root",
sampleBaseDir+"PATtuple_36_0_XRt.root",
sampleBaseDir+"PATtuple_516_0_YEi.root",
sampleBaseDir+"PATtuple_99_1_6G7.root",
sampleBaseDir+"PATtuple_73_0_As9.root",
sampleBaseDir+"PATtuple_608_0_zXN.root",
sampleBaseDir+"PATtuple_251_0_JRZ.root",
sampleBaseDir+"PATtuple_569_0_9SD.root",
sampleBaseDir+"PATtuple_182_0_WYJ.root",
sampleBaseDir+"PATtuple_86_1_Ofm.root",
sampleBaseDir+"PATtuple_529_0_8cc.root",
sampleBaseDir+"PATtuple_513_0_DXw.root",
sampleBaseDir+"PATtuple_292_0_ibh.root",
sampleBaseDir+"PATtuple_3_1_UqP.root",
sampleBaseDir+"PATtuple_411_0_iAB.root",
sampleBaseDir+"PATtuple_609_0_dnF.root",
sampleBaseDir+"PATtuple_4_1_Y7q.root",
sampleBaseDir+"PATtuple_571_0_LL3.root",
sampleBaseDir+"PATtuple_256_0_pcb.root",
sampleBaseDir+"PATtuple_517_0_E0c.root",
sampleBaseDir+"PATtuple_377_1_jrt.root",
sampleBaseDir+"PATtuple_520_0_iOS.root",
sampleBaseDir+"PATtuple_206_1_R2Y.root",
sampleBaseDir+"PATtuple_218_1_7tO.root",
sampleBaseDir+"PATtuple_171_0_s23.root",
sampleBaseDir+"PATtuple_567_0_m6i.root",
sampleBaseDir+"PATtuple_49_0_aTd.root",
sampleBaseDir+"PATtuple_10_0_EiS.root",
sampleBaseDir+"PATtuple_518_0_hiA.root",
sampleBaseDir+"PATtuple_34_1_nzz.root",
sampleBaseDir+"PATtuple_255_0_mTJ.root",
sampleBaseDir+"PATtuple_603_0_TlU.root",
sampleBaseDir+"PATtuple_347_0_0sD.root",
sampleBaseDir+"PATtuple_384_1_fGN.root",
sampleBaseDir+"PATtuple_83_0_Tkx.root",
sampleBaseDir+"PATtuple_573_0_Mhe.root",
sampleBaseDir+"PATtuple_606_0_V5v.root",
sampleBaseDir+"PATtuple_446_0_lOc.root",
sampleBaseDir+"PATtuple_153_0_YUD.root",
sampleBaseDir+"PATtuple_284_1_U0X.root",
sampleBaseDir+"PATtuple_283_1_XyK.root",
sampleBaseDir+"PATtuple_201_0_DCE.root",
sampleBaseDir+"PATtuple_568_0_rZu.root",
sampleBaseDir+"PATtuple_211_1_Rkg.root",
sampleBaseDir+"PATtuple_67_0_K02.root",
sampleBaseDir+"PATtuple_196_0_HCW.root",
sampleBaseDir+"PATtuple_111_0_09v.root",
sampleBaseDir+"PATtuple_13_0_TFM.root",
sampleBaseDir+"PATtuple_126_0_lxg.root",
sampleBaseDir+"PATtuple_113_0_Pbf.root",
sampleBaseDir+"PATtuple_279_1_06K.root",
sampleBaseDir+"PATtuple_110_0_Amo.root",
sampleBaseDir+"PATtuple_159_0_b8g.root",
sampleBaseDir+"PATtuple_387_1_lnh.root",
sampleBaseDir+"PATtuple_432_0_dU8.root",
sampleBaseDir+"PATtuple_282_1_dWN.root",
sampleBaseDir+"PATtuple_521_0_O9V.root",
sampleBaseDir+"PATtuple_566_0_ZCZ.root",
sampleBaseDir+"PATtuple_143_0_HnG.root",
sampleBaseDir+"PATtuple_337_0_n2j.root",
sampleBaseDir+"PATtuple_385_1_5np.root",
sampleBaseDir+"PATtuple_65_0_6wI.root",
sampleBaseDir+"PATtuple_28_0_Qn5.root",
sampleBaseDir+"PATtuple_115_0_uGR.root",
sampleBaseDir+"PATtuple_458_1_mc2.root",
sampleBaseDir+"PATtuple_339_0_bNn.root",
sampleBaseDir+"PATtuple_112_0_JTx.root",
sampleBaseDir+"PATtuple_210_1_GJ7.root",
sampleBaseDir+"PATtuple_52_0_zV3.root",
sampleBaseDir+"PATtuple_43_0_q83.root",
sampleBaseDir+"PATtuple_130_1_EJO.root",
sampleBaseDir+"PATtuple_454_1_aC1.root",
sampleBaseDir+"PATtuple_90_1_ORq.root",
sampleBaseDir+"PATtuple_157_0_xVs.root",
sampleBaseDir+"PATtuple_451_0_nXA.root",
sampleBaseDir+"PATtuple_228_0_6X5.root",
sampleBaseDir+"PATtuple_166_0_euX.root",
sampleBaseDir+"PATtuple_169_0_vix.root",
sampleBaseDir+"PATtuple_118_0_6QW.root",
sampleBaseDir+"PATtuple_195_0_41y.root",
sampleBaseDir+"PATtuple_63_0_iEo.root",
sampleBaseDir+"PATtuple_155_0_H0z.root",
sampleBaseDir+"PATtuple_91_1_6ih.root",
sampleBaseDir+"PATtuple_59_0_IXq.root",
sampleBaseDir+"PATtuple_70_0_V2K.root",
sampleBaseDir+"PATtuple_116_0_cRQ.root",
sampleBaseDir+"PATtuple_12_0_yEL.root",
sampleBaseDir+"PATtuple_386_1_3Lc.root",
sampleBaseDir+"PATtuple_285_1_YKQ.root",
sampleBaseDir+"PATtuple_278_1_Tnj.root",
sampleBaseDir+"PATtuple_15_0_RkF.root",
]
