sampleDataSet = '/WW_TuneZ2star_8TeV_pythia6_tauola/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM'  

sampleCMSEnergy = 8000

sampleRelease = "CMSSW_5_3_2_patch4" # original (i.e. RECO file) release, not the one we plan to process them with
sampleProcessRelease = "CMSSW_5_3_5" # release used to create new files with

sampleNumEvents = 10000431

sampleXSec = 54.8 # pb

# global tag can be extracted from file using edmProvDump filename|grep globaltag
# note however that this is the tag for *further* processing, not the original tag
sampleGlobalTag = 'START53_V7F::All'

sampleDuplicateCheckMode = 'checkAllFilesOpened'

sampleType = "BKGMC"

sampleBaseDir="root://eoscms//eos/cms///store/caf/user/ejclemen//WW_pat_20120726/ejclemen/WW_TuneZ2star_8TeV_pythia6_tauola/WW_pat_20120726/d0bbde228835224f42d621e7d54b0549/"
samplePatFiles = [
sampleBaseDir+"PATtuple_100_0_mf8.root",
sampleBaseDir+"PATtuple_101_0_Idi.root",
sampleBaseDir+"PATtuple_102_0_iKd.root",
sampleBaseDir+"PATtuple_103_0_4p8.root",
sampleBaseDir+"PATtuple_104_0_XrT.root",
sampleBaseDir+"PATtuple_105_0_HS3.root",
sampleBaseDir+"PATtuple_106_0_0Jm.root",
sampleBaseDir+"PATtuple_107_0_ULA.root",
sampleBaseDir+"PATtuple_108_0_r5H.root",
sampleBaseDir+"PATtuple_109_0_JH0.root",
sampleBaseDir+"PATtuple_10_0_REd.root",
sampleBaseDir+"PATtuple_110_0_6lw.root",
sampleBaseDir+"PATtuple_111_0_IX0.root",
sampleBaseDir+"PATtuple_112_0_rxp.root",
sampleBaseDir+"PATtuple_113_0_pUm.root",
sampleBaseDir+"PATtuple_114_0_J0f.root",
sampleBaseDir+"PATtuple_115_0_8Lb.root",
sampleBaseDir+"PATtuple_116_0_9cq.root",
sampleBaseDir+"PATtuple_117_0_ShE.root",
sampleBaseDir+"PATtuple_118_0_0ZX.root",
sampleBaseDir+"PATtuple_119_0_AJY.root",
sampleBaseDir+"PATtuple_11_0_XBp.root",
sampleBaseDir+"PATtuple_120_0_TfJ.root",
sampleBaseDir+"PATtuple_121_0_t1i.root",
sampleBaseDir+"PATtuple_122_0_uaC.root",
sampleBaseDir+"PATtuple_123_0_E70.root",
sampleBaseDir+"PATtuple_124_0_uDC.root",
sampleBaseDir+"PATtuple_125_0_Cv3.root",
sampleBaseDir+"PATtuple_126_0_13m.root",
sampleBaseDir+"PATtuple_127_0_Zzd.root",
sampleBaseDir+"PATtuple_128_0_Opw.root",
sampleBaseDir+"PATtuple_129_0_cu5.root",
sampleBaseDir+"PATtuple_12_0_eh7.root",
sampleBaseDir+"PATtuple_130_0_dXS.root",
sampleBaseDir+"PATtuple_131_0_voc.root",
sampleBaseDir+"PATtuple_132_0_1JQ.root",
sampleBaseDir+"PATtuple_133_0_wxQ.root",
sampleBaseDir+"PATtuple_134_0_F1e.root",
sampleBaseDir+"PATtuple_135_0_KKo.root",
sampleBaseDir+"PATtuple_136_0_n3j.root",
sampleBaseDir+"PATtuple_137_0_B8I.root",
sampleBaseDir+"PATtuple_138_0_pGB.root",
sampleBaseDir+"PATtuple_139_0_ik9.root",
sampleBaseDir+"PATtuple_13_0_dUd.root",
sampleBaseDir+"PATtuple_140_0_Vx3.root",
sampleBaseDir+"PATtuple_141_0_6gF.root",
sampleBaseDir+"PATtuple_142_0_4JP.root",
sampleBaseDir+"PATtuple_143_0_A5K.root",
sampleBaseDir+"PATtuple_144_0_dRj.root",
sampleBaseDir+"PATtuple_145_0_4yD.root",
sampleBaseDir+"PATtuple_146_0_afr.root",
sampleBaseDir+"PATtuple_147_0_nwa.root",
sampleBaseDir+"PATtuple_148_0_sLd.root",
sampleBaseDir+"PATtuple_149_0_q8c.root",
sampleBaseDir+"PATtuple_14_0_KXk.root",
sampleBaseDir+"PATtuple_150_0_BGp.root",
sampleBaseDir+"PATtuple_151_0_xt9.root",
sampleBaseDir+"PATtuple_152_0_0of.root",
sampleBaseDir+"PATtuple_153_0_ghm.root",
sampleBaseDir+"PATtuple_154_0_XJT.root",
sampleBaseDir+"PATtuple_155_0_b5Z.root",
sampleBaseDir+"PATtuple_156_0_xsg.root",
sampleBaseDir+"PATtuple_157_0_Zgx.root",
sampleBaseDir+"PATtuple_158_0_56r.root",
sampleBaseDir+"PATtuple_159_0_ISE.root",
sampleBaseDir+"PATtuple_15_0_8fK.root",
sampleBaseDir+"PATtuple_160_0_V5h.root",
sampleBaseDir+"PATtuple_161_0_pGm.root",
sampleBaseDir+"PATtuple_162_0_R0b.root",
sampleBaseDir+"PATtuple_163_0_9tk.root",
sampleBaseDir+"PATtuple_164_0_GK7.root",
sampleBaseDir+"PATtuple_165_0_pD4.root",
sampleBaseDir+"PATtuple_166_0_9fW.root",
sampleBaseDir+"PATtuple_167_0_iXw.root",
sampleBaseDir+"PATtuple_168_0_Loc.root",
sampleBaseDir+"PATtuple_169_0_ywe.root",
sampleBaseDir+"PATtuple_16_0_Wqy.root",
sampleBaseDir+"PATtuple_170_0_vdh.root",
sampleBaseDir+"PATtuple_171_0_9Fg.root",
sampleBaseDir+"PATtuple_172_0_8oq.root",
sampleBaseDir+"PATtuple_173_0_uvl.root",
sampleBaseDir+"PATtuple_174_0_kTI.root",
sampleBaseDir+"PATtuple_175_0_FTU.root",
sampleBaseDir+"PATtuple_176_0_CSl.root",
sampleBaseDir+"PATtuple_177_0_iku.root",
sampleBaseDir+"PATtuple_178_0_Lzv.root",
sampleBaseDir+"PATtuple_179_0_1bt.root",
sampleBaseDir+"PATtuple_17_0_HrA.root",
sampleBaseDir+"PATtuple_180_0_a9O.root",
sampleBaseDir+"PATtuple_181_0_GWY.root",
sampleBaseDir+"PATtuple_182_0_wCW.root",
sampleBaseDir+"PATtuple_183_0_Qv9.root",
sampleBaseDir+"PATtuple_184_0_cPW.root",
sampleBaseDir+"PATtuple_185_0_v24.root",
sampleBaseDir+"PATtuple_186_0_szm.root",
sampleBaseDir+"PATtuple_187_0_IhX.root",
sampleBaseDir+"PATtuple_188_0_kpE.root",
sampleBaseDir+"PATtuple_189_0_7CF.root",
sampleBaseDir+"PATtuple_18_0_jAK.root",
sampleBaseDir+"PATtuple_190_0_LbU.root",
sampleBaseDir+"PATtuple_191_0_x2t.root",
sampleBaseDir+"PATtuple_192_0_UCU.root",
sampleBaseDir+"PATtuple_193_0_W5T.root",
sampleBaseDir+"PATtuple_194_0_Te7.root",
sampleBaseDir+"PATtuple_195_0_45J.root",
sampleBaseDir+"PATtuple_196_0_5xM.root",
sampleBaseDir+"PATtuple_197_0_Qoo.root",
sampleBaseDir+"PATtuple_198_0_Fje.root",
sampleBaseDir+"PATtuple_199_0_tAz.root",
sampleBaseDir+"PATtuple_19_0_MQo.root",
sampleBaseDir+"PATtuple_1_1_kw6.root",
sampleBaseDir+"PATtuple_200_0_jIK.root",
sampleBaseDir+"PATtuple_201_0_SWN.root",
sampleBaseDir+"PATtuple_202_1_WyL.root",
sampleBaseDir+"PATtuple_203_1_lhy.root",
sampleBaseDir+"PATtuple_204_1_3EE.root",
sampleBaseDir+"PATtuple_205_1_Vs5.root",
sampleBaseDir+"PATtuple_206_1_42g.root",
sampleBaseDir+"PATtuple_207_1_up3.root",
sampleBaseDir+"PATtuple_208_1_8Xk.root",
sampleBaseDir+"PATtuple_209_1_Svm.root",
sampleBaseDir+"PATtuple_20_0_rsb.root",
sampleBaseDir+"PATtuple_210_1_YLU.root",
sampleBaseDir+"PATtuple_211_1_v2S.root",
sampleBaseDir+"PATtuple_212_1_MiU.root",
sampleBaseDir+"PATtuple_213_1_Y90.root",
sampleBaseDir+"PATtuple_214_1_RAZ.root",
sampleBaseDir+"PATtuple_215_1_bmT.root",
sampleBaseDir+"PATtuple_216_1_BLH.root",
sampleBaseDir+"PATtuple_217_1_nx7.root",
sampleBaseDir+"PATtuple_218_1_oid.root",
sampleBaseDir+"PATtuple_219_1_xWH.root",
sampleBaseDir+"PATtuple_21_0_Ql5.root",
sampleBaseDir+"PATtuple_220_1_aMv.root",
sampleBaseDir+"PATtuple_221_1_oAw.root",
sampleBaseDir+"PATtuple_222_1_PyK.root",
sampleBaseDir+"PATtuple_223_1_4uE.root",
sampleBaseDir+"PATtuple_224_1_SXg.root",
sampleBaseDir+"PATtuple_225_1_RAg.root",
sampleBaseDir+"PATtuple_226_1_Os4.root",
sampleBaseDir+"PATtuple_227_1_ALX.root",
sampleBaseDir+"PATtuple_228_1_Jal.root",
sampleBaseDir+"PATtuple_229_1_pIz.root",
sampleBaseDir+"PATtuple_22_0_RDH.root",
sampleBaseDir+"PATtuple_230_1_nUP.root",
sampleBaseDir+"PATtuple_231_1_DLd.root",
sampleBaseDir+"PATtuple_232_1_YPf.root",
sampleBaseDir+"PATtuple_233_1_SuV.root",
sampleBaseDir+"PATtuple_234_1_Asb.root",
sampleBaseDir+"PATtuple_235_1_spJ.root",
sampleBaseDir+"PATtuple_236_1_cYI.root",
sampleBaseDir+"PATtuple_237_1_Vdk.root",
sampleBaseDir+"PATtuple_238_1_ipF.root",
sampleBaseDir+"PATtuple_239_1_G84.root",
sampleBaseDir+"PATtuple_23_0_ZdA.root",
sampleBaseDir+"PATtuple_240_1_FIm.root",
sampleBaseDir+"PATtuple_241_1_7dm.root",
sampleBaseDir+"PATtuple_242_1_srl.root",
sampleBaseDir+"PATtuple_243_1_owB.root",
sampleBaseDir+"PATtuple_244_1_2AH.root",
sampleBaseDir+"PATtuple_245_1_XK6.root",
sampleBaseDir+"PATtuple_246_1_wnP.root",
sampleBaseDir+"PATtuple_247_1_iZZ.root",
sampleBaseDir+"PATtuple_248_1_Hny.root",
sampleBaseDir+"PATtuple_249_1_D5t.root",
sampleBaseDir+"PATtuple_24_0_ZaL.root",
sampleBaseDir+"PATtuple_250_1_PQr.root",
sampleBaseDir+"PATtuple_251_1_hd1.root",
sampleBaseDir+"PATtuple_252_1_EVa.root",
sampleBaseDir+"PATtuple_253_1_C5t.root",
sampleBaseDir+"PATtuple_254_1_5GK.root",
sampleBaseDir+"PATtuple_255_1_jaD.root",
sampleBaseDir+"PATtuple_256_1_C2o.root",
sampleBaseDir+"PATtuple_257_1_aZF.root",
sampleBaseDir+"PATtuple_258_1_fdk.root",
sampleBaseDir+"PATtuple_259_1_0KZ.root",
sampleBaseDir+"PATtuple_25_0_1Uu.root",
sampleBaseDir+"PATtuple_260_1_A3F.root",
sampleBaseDir+"PATtuple_261_1_OxS.root",
sampleBaseDir+"PATtuple_262_1_FuJ.root",
sampleBaseDir+"PATtuple_263_1_B5y.root",
sampleBaseDir+"PATtuple_264_1_dKc.root",
sampleBaseDir+"PATtuple_265_1_nmP.root",
sampleBaseDir+"PATtuple_266_1_cmM.root",
sampleBaseDir+"PATtuple_267_1_BVu.root",
sampleBaseDir+"PATtuple_268_1_lvS.root",
sampleBaseDir+"PATtuple_269_1_s9z.root",
sampleBaseDir+"PATtuple_26_0_lzJ.root",
sampleBaseDir+"PATtuple_270_1_ikG.root",
sampleBaseDir+"PATtuple_271_1_gwt.root",
sampleBaseDir+"PATtuple_272_1_bzJ.root",
sampleBaseDir+"PATtuple_273_1_3fn.root",
sampleBaseDir+"PATtuple_274_1_Nin.root",
sampleBaseDir+"PATtuple_275_1_3ow.root",
sampleBaseDir+"PATtuple_276_1_aUD.root",
sampleBaseDir+"PATtuple_277_1_cW9.root",
sampleBaseDir+"PATtuple_278_1_3HM.root",
sampleBaseDir+"PATtuple_279_1_63W.root",
sampleBaseDir+"PATtuple_27_0_Ot9.root",
sampleBaseDir+"PATtuple_280_1_rho.root",
sampleBaseDir+"PATtuple_281_1_FZU.root",
sampleBaseDir+"PATtuple_282_1_zAn.root",
sampleBaseDir+"PATtuple_283_1_7uj.root",
sampleBaseDir+"PATtuple_284_1_Y0a.root",
sampleBaseDir+"PATtuple_285_1_ZEN.root",
sampleBaseDir+"PATtuple_286_1_Efe.root",
sampleBaseDir+"PATtuple_287_1_bhv.root",
sampleBaseDir+"PATtuple_288_1_jQl.root",
sampleBaseDir+"PATtuple_289_1_1Uj.root",
sampleBaseDir+"PATtuple_28_0_DAg.root",
sampleBaseDir+"PATtuple_290_1_Dwn.root",
sampleBaseDir+"PATtuple_291_1_M4n.root",
sampleBaseDir+"PATtuple_292_1_4El.root",
sampleBaseDir+"PATtuple_293_1_YAt.root",
sampleBaseDir+"PATtuple_294_1_YA8.root",
sampleBaseDir+"PATtuple_295_1_EaK.root",
sampleBaseDir+"PATtuple_296_1_Ofl.root",
sampleBaseDir+"PATtuple_297_1_7EN.root",
sampleBaseDir+"PATtuple_298_1_Yaz.root",
sampleBaseDir+"PATtuple_299_1_ViE.root",
sampleBaseDir+"PATtuple_29_0_OD5.root",
sampleBaseDir+"PATtuple_2_0_zJy.root",
sampleBaseDir+"PATtuple_300_1_pdK.root",
sampleBaseDir+"PATtuple_301_1_Had.root",
sampleBaseDir+"PATtuple_302_1_4bx.root",
sampleBaseDir+"PATtuple_303_1_ogL.root",
sampleBaseDir+"PATtuple_304_1_5Z6.root",
sampleBaseDir+"PATtuple_305_1_sHu.root",
sampleBaseDir+"PATtuple_306_1_Ecg.root",
sampleBaseDir+"PATtuple_307_1_Gqo.root",
sampleBaseDir+"PATtuple_308_1_f46.root",
sampleBaseDir+"PATtuple_309_1_JZb.root",
sampleBaseDir+"PATtuple_30_0_ePK.root",
sampleBaseDir+"PATtuple_310_1_1N7.root",
sampleBaseDir+"PATtuple_311_1_NqR.root",
sampleBaseDir+"PATtuple_312_1_yxC.root",
sampleBaseDir+"PATtuple_313_1_THi.root",
sampleBaseDir+"PATtuple_314_1_SUR.root",
sampleBaseDir+"PATtuple_315_1_yG7.root",
sampleBaseDir+"PATtuple_316_1_7Ew.root",
sampleBaseDir+"PATtuple_317_1_ZYY.root",
sampleBaseDir+"PATtuple_318_1_2ov.root",
sampleBaseDir+"PATtuple_319_1_SQb.root",
sampleBaseDir+"PATtuple_31_0_ILD.root",
sampleBaseDir+"PATtuple_320_1_zOx.root",
sampleBaseDir+"PATtuple_321_1_7Sf.root",
sampleBaseDir+"PATtuple_322_1_5T6.root",
sampleBaseDir+"PATtuple_323_1_YwI.root",
sampleBaseDir+"PATtuple_324_1_tgl.root",
sampleBaseDir+"PATtuple_325_1_IvW.root",
sampleBaseDir+"PATtuple_326_1_Za7.root",
sampleBaseDir+"PATtuple_327_1_8LC.root",
sampleBaseDir+"PATtuple_328_1_zmS.root",
sampleBaseDir+"PATtuple_329_1_pyy.root",
sampleBaseDir+"PATtuple_32_0_GW9.root",
sampleBaseDir+"PATtuple_330_1_uHe.root",
sampleBaseDir+"PATtuple_331_1_tbv.root",
sampleBaseDir+"PATtuple_332_1_FK2.root",
sampleBaseDir+"PATtuple_333_1_3FW.root",
sampleBaseDir+"PATtuple_334_1_kOv.root",
sampleBaseDir+"PATtuple_335_1_oLi.root",
sampleBaseDir+"PATtuple_336_1_5Wk.root",
sampleBaseDir+"PATtuple_337_2_FxG.root",
sampleBaseDir+"PATtuple_338_1_cDW.root",
sampleBaseDir+"PATtuple_339_1_VJn.root",
sampleBaseDir+"PATtuple_33_0_p0j.root",
sampleBaseDir+"PATtuple_340_1_73V.root",
sampleBaseDir+"PATtuple_341_1_s8B.root",
sampleBaseDir+"PATtuple_342_1_5CY.root",
sampleBaseDir+"PATtuple_343_1_aQU.root",
sampleBaseDir+"PATtuple_344_1_AIK.root",
sampleBaseDir+"PATtuple_345_1_evm.root",
sampleBaseDir+"PATtuple_346_1_hb8.root",
sampleBaseDir+"PATtuple_347_1_5RY.root",
sampleBaseDir+"PATtuple_348_1_upG.root",
sampleBaseDir+"PATtuple_349_1_orM.root",
sampleBaseDir+"PATtuple_34_0_hxp.root",
sampleBaseDir+"PATtuple_350_1_Xr7.root",
sampleBaseDir+"PATtuple_351_1_pBv.root",
sampleBaseDir+"PATtuple_352_1_Duy.root",
sampleBaseDir+"PATtuple_353_1_75O.root",
sampleBaseDir+"PATtuple_354_1_XPh.root",
sampleBaseDir+"PATtuple_355_1_UfD.root",
sampleBaseDir+"PATtuple_356_1_wOa.root",
sampleBaseDir+"PATtuple_357_1_OXS.root",
sampleBaseDir+"PATtuple_358_1_h23.root",
sampleBaseDir+"PATtuple_359_1_q1E.root",
sampleBaseDir+"PATtuple_35_0_u4L.root",
sampleBaseDir+"PATtuple_360_1_QGm.root",
sampleBaseDir+"PATtuple_361_1_kfZ.root",
sampleBaseDir+"PATtuple_362_1_y2J.root",
sampleBaseDir+"PATtuple_363_1_M5C.root",
sampleBaseDir+"PATtuple_364_1_Lwj.root",
sampleBaseDir+"PATtuple_365_1_SU5.root",
sampleBaseDir+"PATtuple_366_1_obD.root",
sampleBaseDir+"PATtuple_367_1_k3W.root",
sampleBaseDir+"PATtuple_368_1_CWX.root",
sampleBaseDir+"PATtuple_369_1_wLz.root",
sampleBaseDir+"PATtuple_36_0_ANY.root",
sampleBaseDir+"PATtuple_370_1_OZK.root",
sampleBaseDir+"PATtuple_371_1_C4T.root",
sampleBaseDir+"PATtuple_372_1_k3G.root",
sampleBaseDir+"PATtuple_373_1_epq.root",
sampleBaseDir+"PATtuple_374_1_rlN.root",
sampleBaseDir+"PATtuple_375_1_Vhg.root",
sampleBaseDir+"PATtuple_376_1_I1p.root",
sampleBaseDir+"PATtuple_377_1_aFt.root",
sampleBaseDir+"PATtuple_378_1_UlX.root",
sampleBaseDir+"PATtuple_379_1_Inn.root",
sampleBaseDir+"PATtuple_37_0_riZ.root",
sampleBaseDir+"PATtuple_380_1_iJ8.root",
sampleBaseDir+"PATtuple_381_1_8bu.root",
sampleBaseDir+"PATtuple_382_1_5nn.root",
sampleBaseDir+"PATtuple_383_1_lzy.root",
sampleBaseDir+"PATtuple_384_1_jbT.root",
sampleBaseDir+"PATtuple_385_1_fWu.root",
sampleBaseDir+"PATtuple_386_1_VMZ.root",
sampleBaseDir+"PATtuple_387_1_78u.root",
sampleBaseDir+"PATtuple_388_1_QqB.root",
sampleBaseDir+"PATtuple_389_1_w7o.root",
sampleBaseDir+"PATtuple_38_0_j4f.root",
sampleBaseDir+"PATtuple_390_1_eYF.root",
sampleBaseDir+"PATtuple_391_1_2cx.root",
sampleBaseDir+"PATtuple_392_1_15z.root",
sampleBaseDir+"PATtuple_393_1_1EP.root",
sampleBaseDir+"PATtuple_394_1_arz.root",
sampleBaseDir+"PATtuple_395_1_mTN.root",
sampleBaseDir+"PATtuple_396_1_68j.root",
sampleBaseDir+"PATtuple_397_1_RkB.root",
sampleBaseDir+"PATtuple_398_1_MBj.root",
sampleBaseDir+"PATtuple_399_1_N67.root",
sampleBaseDir+"PATtuple_39_0_yLl.root",
sampleBaseDir+"PATtuple_3_0_0NK.root",
sampleBaseDir+"PATtuple_400_1_6f2.root",
sampleBaseDir+"PATtuple_401_1_Kmr.root",
sampleBaseDir+"PATtuple_402_1_Jh1.root",
sampleBaseDir+"PATtuple_403_1_Hp6.root",
sampleBaseDir+"PATtuple_404_1_C0g.root",
sampleBaseDir+"PATtuple_405_1_cQD.root",
sampleBaseDir+"PATtuple_406_1_U1J.root",
sampleBaseDir+"PATtuple_407_1_sHy.root",
sampleBaseDir+"PATtuple_408_1_EZH.root",
sampleBaseDir+"PATtuple_409_1_qbz.root",
sampleBaseDir+"PATtuple_40_0_0Yz.root",
sampleBaseDir+"PATtuple_410_1_Rf0.root",
sampleBaseDir+"PATtuple_411_1_nTy.root",
sampleBaseDir+"PATtuple_412_1_FGk.root",
sampleBaseDir+"PATtuple_413_1_wMQ.root",
sampleBaseDir+"PATtuple_414_1_cwB.root",
sampleBaseDir+"PATtuple_415_1_V0q.root",
sampleBaseDir+"PATtuple_416_1_D4n.root",
sampleBaseDir+"PATtuple_417_1_HHt.root",
sampleBaseDir+"PATtuple_418_1_l6v.root",
sampleBaseDir+"PATtuple_419_1_NvF.root",
sampleBaseDir+"PATtuple_41_0_Tza.root",
sampleBaseDir+"PATtuple_420_1_c43.root",
sampleBaseDir+"PATtuple_421_1_Mce.root",
sampleBaseDir+"PATtuple_422_1_Ew4.root",
sampleBaseDir+"PATtuple_423_1_nW5.root",
sampleBaseDir+"PATtuple_424_1_xwj.root",
sampleBaseDir+"PATtuple_425_1_Do7.root",
sampleBaseDir+"PATtuple_426_1_WGz.root",
sampleBaseDir+"PATtuple_427_1_Iec.root",
sampleBaseDir+"PATtuple_428_1_RFi.root",
sampleBaseDir+"PATtuple_429_1_haN.root",
sampleBaseDir+"PATtuple_42_0_B7s.root",
sampleBaseDir+"PATtuple_430_1_Hly.root",
sampleBaseDir+"PATtuple_431_1_3j6.root",
sampleBaseDir+"PATtuple_432_1_gWZ.root",
sampleBaseDir+"PATtuple_433_1_J87.root",
sampleBaseDir+"PATtuple_434_1_q29.root",
sampleBaseDir+"PATtuple_435_1_OTP.root",
sampleBaseDir+"PATtuple_436_1_zl1.root",
sampleBaseDir+"PATtuple_437_1_Pb4.root",
sampleBaseDir+"PATtuple_438_1_NhF.root",
sampleBaseDir+"PATtuple_439_1_e5r.root",
sampleBaseDir+"PATtuple_43_0_cPr.root",
sampleBaseDir+"PATtuple_440_1_1rK.root",
sampleBaseDir+"PATtuple_441_1_9yl.root",
sampleBaseDir+"PATtuple_442_1_HAa.root",
sampleBaseDir+"PATtuple_443_1_Mqs.root",
sampleBaseDir+"PATtuple_444_1_uC7.root",
sampleBaseDir+"PATtuple_445_1_UQQ.root",
sampleBaseDir+"PATtuple_446_1_Brd.root",
sampleBaseDir+"PATtuple_447_1_Hiy.root",
sampleBaseDir+"PATtuple_448_1_EIm.root",
sampleBaseDir+"PATtuple_449_1_7Pc.root",
sampleBaseDir+"PATtuple_44_0_FDL.root",
sampleBaseDir+"PATtuple_450_1_U13.root",
sampleBaseDir+"PATtuple_451_1_IGD.root",
sampleBaseDir+"PATtuple_452_1_aBm.root",
sampleBaseDir+"PATtuple_453_1_4eu.root",
sampleBaseDir+"PATtuple_454_1_aQe.root",
sampleBaseDir+"PATtuple_455_1_78z.root",
sampleBaseDir+"PATtuple_456_1_tsl.root",
sampleBaseDir+"PATtuple_457_1_SvA.root",
sampleBaseDir+"PATtuple_458_1_Nia.root",
sampleBaseDir+"PATtuple_459_1_Ig2.root",
sampleBaseDir+"PATtuple_45_0_zAR.root",
sampleBaseDir+"PATtuple_460_1_RsA.root",
sampleBaseDir+"PATtuple_461_1_7Wz.root",
sampleBaseDir+"PATtuple_462_1_7Pe.root",
sampleBaseDir+"PATtuple_463_1_WrH.root",
sampleBaseDir+"PATtuple_464_1_By0.root",
sampleBaseDir+"PATtuple_465_1_hgO.root",
sampleBaseDir+"PATtuple_466_1_1gz.root",
sampleBaseDir+"PATtuple_467_1_vY0.root",
sampleBaseDir+"PATtuple_468_1_X9h.root",
sampleBaseDir+"PATtuple_469_1_IC1.root",
sampleBaseDir+"PATtuple_46_0_ujH.root",
sampleBaseDir+"PATtuple_470_1_ew2.root",
sampleBaseDir+"PATtuple_471_1_zzv.root",
sampleBaseDir+"PATtuple_472_1_ZB7.root",
sampleBaseDir+"PATtuple_473_1_Jpz.root",
sampleBaseDir+"PATtuple_474_1_y7r.root",
sampleBaseDir+"PATtuple_475_1_RXl.root",
sampleBaseDir+"PATtuple_476_1_6u9.root",
sampleBaseDir+"PATtuple_477_1_WM5.root",
sampleBaseDir+"PATtuple_478_1_di0.root",
sampleBaseDir+"PATtuple_479_1_gZ4.root",
sampleBaseDir+"PATtuple_47_0_gJX.root",
sampleBaseDir+"PATtuple_480_1_8ge.root",
sampleBaseDir+"PATtuple_481_1_qoM.root",
sampleBaseDir+"PATtuple_482_1_zt0.root",
sampleBaseDir+"PATtuple_483_1_45Q.root",
sampleBaseDir+"PATtuple_484_1_Bn1.root",
sampleBaseDir+"PATtuple_485_1_jMV.root",
sampleBaseDir+"PATtuple_486_1_5mI.root",
sampleBaseDir+"PATtuple_487_1_k3l.root",
sampleBaseDir+"PATtuple_488_1_9Ub.root",
sampleBaseDir+"PATtuple_489_1_Mgt.root",
sampleBaseDir+"PATtuple_48_0_LZx.root",
sampleBaseDir+"PATtuple_490_1_vIl.root",
sampleBaseDir+"PATtuple_491_1_8BC.root",
sampleBaseDir+"PATtuple_492_1_WXi.root",
sampleBaseDir+"PATtuple_493_1_WS5.root",
sampleBaseDir+"PATtuple_494_1_oBT.root",
sampleBaseDir+"PATtuple_495_1_LTR.root",
sampleBaseDir+"PATtuple_496_1_vkj.root",
sampleBaseDir+"PATtuple_497_1_rDJ.root",
sampleBaseDir+"PATtuple_498_1_1MC.root",
sampleBaseDir+"PATtuple_499_1_Cr9.root",
sampleBaseDir+"PATtuple_49_0_8wv.root",
sampleBaseDir+"PATtuple_4_0_RF0.root",
sampleBaseDir+"PATtuple_500_1_ijv.root",
sampleBaseDir+"PATtuple_501_1_X6U.root",
sampleBaseDir+"PATtuple_502_1_4ZE.root",
sampleBaseDir+"PATtuple_503_1_9cd.root",
sampleBaseDir+"PATtuple_504_1_eSc.root",
sampleBaseDir+"PATtuple_505_1_XMp.root",
sampleBaseDir+"PATtuple_506_1_DsV.root",
sampleBaseDir+"PATtuple_507_1_P9f.root",
sampleBaseDir+"PATtuple_508_1_8ZW.root",
sampleBaseDir+"PATtuple_509_1_g9B.root",
sampleBaseDir+"PATtuple_50_0_aFY.root",
sampleBaseDir+"PATtuple_510_1_BSp.root",
sampleBaseDir+"PATtuple_511_1_BUD.root",
sampleBaseDir+"PATtuple_512_1_EwC.root",
sampleBaseDir+"PATtuple_513_1_zon.root",
sampleBaseDir+"PATtuple_514_1_te4.root",
sampleBaseDir+"PATtuple_515_1_IOj.root",
sampleBaseDir+"PATtuple_516_1_Phy.root",
sampleBaseDir+"PATtuple_517_1_HnX.root",
sampleBaseDir+"PATtuple_518_1_N8o.root",
sampleBaseDir+"PATtuple_519_1_hGg.root",
sampleBaseDir+"PATtuple_51_0_0j7.root",
sampleBaseDir+"PATtuple_520_1_zuw.root",
sampleBaseDir+"PATtuple_521_1_NUX.root",
sampleBaseDir+"PATtuple_522_1_fc6.root",
sampleBaseDir+"PATtuple_523_1_Qfe.root",
sampleBaseDir+"PATtuple_524_1_Gtj.root",
sampleBaseDir+"PATtuple_525_1_HrM.root",
sampleBaseDir+"PATtuple_526_1_9Re.root",
sampleBaseDir+"PATtuple_527_1_JMl.root",
sampleBaseDir+"PATtuple_528_1_u8h.root",
sampleBaseDir+"PATtuple_529_1_NAm.root",
sampleBaseDir+"PATtuple_52_0_2GG.root",
sampleBaseDir+"PATtuple_530_1_qFR.root",
sampleBaseDir+"PATtuple_531_1_5V0.root",
sampleBaseDir+"PATtuple_532_1_YYw.root",
sampleBaseDir+"PATtuple_533_1_cvp.root",
sampleBaseDir+"PATtuple_534_1_n9k.root",
sampleBaseDir+"PATtuple_535_1_WKO.root",
sampleBaseDir+"PATtuple_536_1_8qq.root",
sampleBaseDir+"PATtuple_537_1_oZU.root",
sampleBaseDir+"PATtuple_538_1_2vB.root",
sampleBaseDir+"PATtuple_539_1_wCL.root",
sampleBaseDir+"PATtuple_53_0_wlP.root",
sampleBaseDir+"PATtuple_540_1_M5b.root",
sampleBaseDir+"PATtuple_541_1_dss.root",
sampleBaseDir+"PATtuple_542_1_thL.root",
sampleBaseDir+"PATtuple_543_1_4Ki.root",
sampleBaseDir+"PATtuple_544_1_xKC.root",
sampleBaseDir+"PATtuple_545_1_NKM.root",
sampleBaseDir+"PATtuple_546_1_o1l.root",
sampleBaseDir+"PATtuple_547_1_Q6k.root",
sampleBaseDir+"PATtuple_548_1_ZIO.root",
sampleBaseDir+"PATtuple_549_1_o3w.root",
sampleBaseDir+"PATtuple_54_0_uvM.root",
sampleBaseDir+"PATtuple_550_1_5N1.root",
sampleBaseDir+"PATtuple_551_1_Wwp.root",
sampleBaseDir+"PATtuple_552_1_8FS.root",
sampleBaseDir+"PATtuple_553_1_EYI.root",
sampleBaseDir+"PATtuple_554_1_Nq5.root",
sampleBaseDir+"PATtuple_555_1_zMo.root",
sampleBaseDir+"PATtuple_556_1_Mz2.root",
sampleBaseDir+"PATtuple_557_1_pec.root",
sampleBaseDir+"PATtuple_558_1_9lj.root",
sampleBaseDir+"PATtuple_559_1_MTF.root",
sampleBaseDir+"PATtuple_55_0_UmH.root",
sampleBaseDir+"PATtuple_560_1_3XD.root",
sampleBaseDir+"PATtuple_561_1_9pd.root",
sampleBaseDir+"PATtuple_562_1_5Jb.root",
sampleBaseDir+"PATtuple_563_1_Psi.root",
sampleBaseDir+"PATtuple_564_1_5Ny.root",
sampleBaseDir+"PATtuple_565_1_v7n.root",
sampleBaseDir+"PATtuple_566_1_RnI.root",
sampleBaseDir+"PATtuple_567_1_QYp.root",
sampleBaseDir+"PATtuple_568_1_n93.root",
sampleBaseDir+"PATtuple_569_1_vlV.root",
sampleBaseDir+"PATtuple_56_0_HIR.root",
sampleBaseDir+"PATtuple_570_1_3ET.root",
sampleBaseDir+"PATtuple_571_1_o7J.root",
sampleBaseDir+"PATtuple_572_1_bau.root",
sampleBaseDir+"PATtuple_573_1_05f.root",
sampleBaseDir+"PATtuple_574_1_RhH.root",
sampleBaseDir+"PATtuple_575_1_PhW.root",
sampleBaseDir+"PATtuple_576_1_OlZ.root",
sampleBaseDir+"PATtuple_577_1_rJc.root",
sampleBaseDir+"PATtuple_578_1_jyh.root",
sampleBaseDir+"PATtuple_579_1_Ehp.root",
sampleBaseDir+"PATtuple_57_0_4la.root",
sampleBaseDir+"PATtuple_580_1_dCY.root",
sampleBaseDir+"PATtuple_581_1_Th5.root",
sampleBaseDir+"PATtuple_582_1_GbQ.root",
sampleBaseDir+"PATtuple_583_1_8MB.root",
sampleBaseDir+"PATtuple_584_1_I1g.root",
sampleBaseDir+"PATtuple_585_1_wTR.root",
sampleBaseDir+"PATtuple_586_1_8i1.root",
sampleBaseDir+"PATtuple_587_1_Xmv.root",
sampleBaseDir+"PATtuple_588_1_EUx.root",
sampleBaseDir+"PATtuple_589_1_ZgS.root",
sampleBaseDir+"PATtuple_58_0_1YO.root",
sampleBaseDir+"PATtuple_590_1_vEO.root",
sampleBaseDir+"PATtuple_591_1_AwI.root",
sampleBaseDir+"PATtuple_592_1_33e.root",
sampleBaseDir+"PATtuple_593_1_Zdr.root",
sampleBaseDir+"PATtuple_594_1_0M8.root",
sampleBaseDir+"PATtuple_595_1_fG9.root",
sampleBaseDir+"PATtuple_596_1_s6j.root",
sampleBaseDir+"PATtuple_597_1_k3z.root",
sampleBaseDir+"PATtuple_598_1_MBU.root",
sampleBaseDir+"PATtuple_599_1_yay.root",
sampleBaseDir+"PATtuple_59_0_vaH.root",
sampleBaseDir+"PATtuple_5_0_ni3.root",
sampleBaseDir+"PATtuple_600_1_Hkm.root",
sampleBaseDir+"PATtuple_601_1_0Gn.root",
sampleBaseDir+"PATtuple_602_1_spz.root",
sampleBaseDir+"PATtuple_603_1_A9c.root",
sampleBaseDir+"PATtuple_604_1_rsj.root",
sampleBaseDir+"PATtuple_605_1_cQE.root",
sampleBaseDir+"PATtuple_606_1_2KF.root",
sampleBaseDir+"PATtuple_607_1_gJi.root",
sampleBaseDir+"PATtuple_608_1_qKg.root",
sampleBaseDir+"PATtuple_609_1_G9I.root",
sampleBaseDir+"PATtuple_60_0_Quo.root",
sampleBaseDir+"PATtuple_610_1_C6P.root",
sampleBaseDir+"PATtuple_611_1_zpd.root",
sampleBaseDir+"PATtuple_612_1_b0a.root",
sampleBaseDir+"PATtuple_613_1_JGf.root",
sampleBaseDir+"PATtuple_614_1_yCh.root",
sampleBaseDir+"PATtuple_615_1_kc7.root",
sampleBaseDir+"PATtuple_616_1_4Z1.root",
sampleBaseDir+"PATtuple_617_1_fsy.root",
sampleBaseDir+"PATtuple_618_1_mo0.root",
sampleBaseDir+"PATtuple_619_1_Mqd.root",
sampleBaseDir+"PATtuple_61_0_EqB.root",
sampleBaseDir+"PATtuple_620_1_nLJ.root",
sampleBaseDir+"PATtuple_621_1_pX2.root",
sampleBaseDir+"PATtuple_622_1_oJf.root",
sampleBaseDir+"PATtuple_623_1_hFv.root",
sampleBaseDir+"PATtuple_624_1_d43.root",
sampleBaseDir+"PATtuple_625_1_ruE.root",
sampleBaseDir+"PATtuple_626_1_urh.root",
sampleBaseDir+"PATtuple_627_1_ASN.root",
sampleBaseDir+"PATtuple_628_1_dbX.root",
sampleBaseDir+"PATtuple_629_1_qDz.root",
sampleBaseDir+"PATtuple_62_0_cWC.root",
sampleBaseDir+"PATtuple_630_1_MqH.root",
sampleBaseDir+"PATtuple_631_1_Jpu.root",
sampleBaseDir+"PATtuple_632_1_x9d.root",
sampleBaseDir+"PATtuple_633_1_7Cu.root",
sampleBaseDir+"PATtuple_634_1_t7o.root",
sampleBaseDir+"PATtuple_635_1_xNS.root",
sampleBaseDir+"PATtuple_636_1_Q8Z.root",
sampleBaseDir+"PATtuple_637_1_MWk.root",
sampleBaseDir+"PATtuple_638_1_3S8.root",
sampleBaseDir+"PATtuple_639_1_A7d.root",
sampleBaseDir+"PATtuple_63_0_txE.root",
sampleBaseDir+"PATtuple_640_1_LUp.root",
sampleBaseDir+"PATtuple_641_1_zOQ.root",
sampleBaseDir+"PATtuple_642_1_yaX.root",
sampleBaseDir+"PATtuple_643_1_yQz.root",
sampleBaseDir+"PATtuple_644_1_EFM.root",
sampleBaseDir+"PATtuple_645_1_N3P.root",
sampleBaseDir+"PATtuple_646_1_yuR.root",
sampleBaseDir+"PATtuple_647_1_IR0.root",
sampleBaseDir+"PATtuple_648_1_pTF.root",
sampleBaseDir+"PATtuple_649_1_g4U.root",
sampleBaseDir+"PATtuple_64_0_Q3W.root",
sampleBaseDir+"PATtuple_650_1_0AC.root",
sampleBaseDir+"PATtuple_651_1_1Nv.root",
sampleBaseDir+"PATtuple_652_1_CYM.root",
sampleBaseDir+"PATtuple_653_1_AeW.root",
sampleBaseDir+"PATtuple_654_1_RNd.root",
sampleBaseDir+"PATtuple_655_1_PDN.root",
sampleBaseDir+"PATtuple_656_1_KhG.root",
sampleBaseDir+"PATtuple_657_1_rwE.root",
sampleBaseDir+"PATtuple_658_1_hYV.root",
sampleBaseDir+"PATtuple_659_1_Pos.root",
sampleBaseDir+"PATtuple_65_0_u7o.root",
sampleBaseDir+"PATtuple_660_1_t6Z.root",
sampleBaseDir+"PATtuple_661_1_PY5.root",
sampleBaseDir+"PATtuple_662_1_2XG.root",
sampleBaseDir+"PATtuple_663_1_9eZ.root",
sampleBaseDir+"PATtuple_664_1_FW5.root",
sampleBaseDir+"PATtuple_665_1_TQI.root",
sampleBaseDir+"PATtuple_666_1_oDF.root",
sampleBaseDir+"PATtuple_667_1_zGR.root",
sampleBaseDir+"PATtuple_668_1_fSd.root",
sampleBaseDir+"PATtuple_669_1_j0B.root",
sampleBaseDir+"PATtuple_66_0_LI9.root",
sampleBaseDir+"PATtuple_670_1_vHc.root",
sampleBaseDir+"PATtuple_671_1_yuE.root",
sampleBaseDir+"PATtuple_672_1_Mek.root",
sampleBaseDir+"PATtuple_673_1_86I.root",
sampleBaseDir+"PATtuple_674_1_RGC.root",
sampleBaseDir+"PATtuple_675_1_cMJ.root",
sampleBaseDir+"PATtuple_676_1_1gy.root",
sampleBaseDir+"PATtuple_677_1_8MB.root",
sampleBaseDir+"PATtuple_678_1_iKM.root",
sampleBaseDir+"PATtuple_679_1_vBI.root",
sampleBaseDir+"PATtuple_67_0_8hU.root",
sampleBaseDir+"PATtuple_680_1_Y2I.root",
sampleBaseDir+"PATtuple_681_1_0Q5.root",
sampleBaseDir+"PATtuple_682_1_Uta.root",
sampleBaseDir+"PATtuple_683_1_prJ.root",
sampleBaseDir+"PATtuple_684_1_2VU.root",
sampleBaseDir+"PATtuple_685_1_zw6.root",
sampleBaseDir+"PATtuple_686_1_y0o.root",
sampleBaseDir+"PATtuple_687_1_5QM.root",
sampleBaseDir+"PATtuple_688_1_2Lk.root",
sampleBaseDir+"PATtuple_689_1_s54.root",
sampleBaseDir+"PATtuple_68_0_nlR.root",
sampleBaseDir+"PATtuple_690_1_zRi.root",
sampleBaseDir+"PATtuple_691_1_t02.root",
sampleBaseDir+"PATtuple_692_1_nQM.root",
sampleBaseDir+"PATtuple_693_1_O4G.root",
sampleBaseDir+"PATtuple_694_1_GXW.root",
sampleBaseDir+"PATtuple_695_1_WHO.root",
sampleBaseDir+"PATtuple_696_1_eJr.root",
sampleBaseDir+"PATtuple_697_1_FVe.root",
sampleBaseDir+"PATtuple_698_1_zzh.root",
sampleBaseDir+"PATtuple_699_1_AqI.root",
sampleBaseDir+"PATtuple_69_0_YOa.root",
sampleBaseDir+"PATtuple_6_0_edl.root",
sampleBaseDir+"PATtuple_700_1_fJv.root",
sampleBaseDir+"PATtuple_701_1_kZr.root",
sampleBaseDir+"PATtuple_702_1_xkC.root",
sampleBaseDir+"PATtuple_703_1_pFV.root",
sampleBaseDir+"PATtuple_704_1_61Y.root",
sampleBaseDir+"PATtuple_705_1_M0K.root",
sampleBaseDir+"PATtuple_706_1_u43.root",
sampleBaseDir+"PATtuple_707_1_lhZ.root",
sampleBaseDir+"PATtuple_708_1_jnr.root",
sampleBaseDir+"PATtuple_709_1_NP7.root",
sampleBaseDir+"PATtuple_70_0_MMg.root",
sampleBaseDir+"PATtuple_710_1_vmz.root",
sampleBaseDir+"PATtuple_711_1_LTs.root",
sampleBaseDir+"PATtuple_712_1_JFU.root",
sampleBaseDir+"PATtuple_713_1_a9M.root",
sampleBaseDir+"PATtuple_714_1_LYO.root",
sampleBaseDir+"PATtuple_715_1_eDH.root",
sampleBaseDir+"PATtuple_716_1_oBV.root",
sampleBaseDir+"PATtuple_717_1_vnF.root",
sampleBaseDir+"PATtuple_718_1_FfG.root",
sampleBaseDir+"PATtuple_719_1_FYF.root",
sampleBaseDir+"PATtuple_71_0_ofr.root",
sampleBaseDir+"PATtuple_720_1_bvH.root",
sampleBaseDir+"PATtuple_721_1_dDh.root",
sampleBaseDir+"PATtuple_722_1_32x.root",
sampleBaseDir+"PATtuple_723_1_rkx.root",
sampleBaseDir+"PATtuple_724_1_5qY.root",
sampleBaseDir+"PATtuple_725_1_iRO.root",
sampleBaseDir+"PATtuple_726_1_7js.root",
sampleBaseDir+"PATtuple_727_1_kEQ.root",
sampleBaseDir+"PATtuple_728_1_vLs.root",
sampleBaseDir+"PATtuple_729_1_1Nx.root",
sampleBaseDir+"PATtuple_72_0_8on.root",
sampleBaseDir+"PATtuple_730_1_zHZ.root",
sampleBaseDir+"PATtuple_731_1_2OL.root",
sampleBaseDir+"PATtuple_732_1_HHn.root",
sampleBaseDir+"PATtuple_733_1_3TF.root",
sampleBaseDir+"PATtuple_734_1_8hT.root",
sampleBaseDir+"PATtuple_735_1_eN7.root",
sampleBaseDir+"PATtuple_736_1_Vya.root",
sampleBaseDir+"PATtuple_737_1_oMR.root",
sampleBaseDir+"PATtuple_738_1_rOg.root",
sampleBaseDir+"PATtuple_739_1_Pwl.root",
sampleBaseDir+"PATtuple_73_0_fTN.root",
sampleBaseDir+"PATtuple_740_1_9vk.root",
sampleBaseDir+"PATtuple_741_1_IhD.root",
sampleBaseDir+"PATtuple_742_1_jYz.root",
sampleBaseDir+"PATtuple_743_1_qIX.root",
sampleBaseDir+"PATtuple_744_1_Rtn.root",
sampleBaseDir+"PATtuple_745_1_3Py.root",
sampleBaseDir+"PATtuple_746_1_0FE.root",
sampleBaseDir+"PATtuple_747_1_kpX.root",
sampleBaseDir+"PATtuple_748_1_XQD.root",
sampleBaseDir+"PATtuple_749_1_BzL.root",
sampleBaseDir+"PATtuple_74_0_s4f.root",
sampleBaseDir+"PATtuple_750_1_Pjo.root",
sampleBaseDir+"PATtuple_751_1_kHT.root",
sampleBaseDir+"PATtuple_752_1_F2L.root",
sampleBaseDir+"PATtuple_753_1_VNw.root",
sampleBaseDir+"PATtuple_75_0_Yz2.root",
sampleBaseDir+"PATtuple_76_0_yhU.root",
sampleBaseDir+"PATtuple_77_0_ObK.root",
sampleBaseDir+"PATtuple_78_0_bj0.root",
sampleBaseDir+"PATtuple_79_0_LQG.root",
sampleBaseDir+"PATtuple_7_0_HQW.root",
sampleBaseDir+"PATtuple_80_0_yhK.root",
sampleBaseDir+"PATtuple_81_0_HIT.root",
sampleBaseDir+"PATtuple_82_0_CCl.root",
sampleBaseDir+"PATtuple_83_0_yWv.root",
sampleBaseDir+"PATtuple_84_0_v0K.root",
sampleBaseDir+"PATtuple_85_0_Rbg.root",
sampleBaseDir+"PATtuple_86_0_mNV.root",
sampleBaseDir+"PATtuple_87_0_x7z.root",
sampleBaseDir+"PATtuple_88_0_jz6.root",
sampleBaseDir+"PATtuple_89_0_oQm.root",
sampleBaseDir+"PATtuple_8_0_5I5.root",
sampleBaseDir+"PATtuple_90_0_k4l.root",
sampleBaseDir+"PATtuple_91_0_SCg.root",
sampleBaseDir+"PATtuple_92_0_eb0.root",
sampleBaseDir+"PATtuple_93_0_0SD.root",
sampleBaseDir+"PATtuple_94_0_eBS.root",
sampleBaseDir+"PATtuple_95_0_z18.root",
sampleBaseDir+"PATtuple_96_0_eaQ.root",
sampleBaseDir+"PATtuple_97_0_tGi.root",
sampleBaseDir+"PATtuple_98_0_QiJ.root",
sampleBaseDir+"PATtuple_99_0_1Ok.root",
sampleBaseDir+"PATtuple_9_0_uFt.root",
]
