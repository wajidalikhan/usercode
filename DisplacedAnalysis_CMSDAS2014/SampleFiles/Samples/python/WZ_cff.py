sampleDataSet = '/WZ_TuneZ2star_8TeV_pythia6_tauola/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM'  

sampleCMSEnergy = 8000

sampleRelease = "CMSSW_5_3_2_patch4" # original (i.e. RECO file) release, not the one we plan to process them with
sampleProcessRelease = "CMSSW_5_3_5" # release used to create new files with

sampleNumEvents = 10000283

sampleXSec = 33.2 # pb

# global tag can be extracted from file using edmProvDump filename|grep globaltag
# note however that this is the tag for *further* processing, not the original tag
sampleGlobalTag = 'START53_V7F::All'

sampleDuplicateCheckMode = 'checkAllFilesOpened'

sampleType = "BKGMC"

samplePatDBSName="/WZ_TuneZ2star_8TeV_pythia6_tauola/demattia-WZ_pat_20121107-5b849df0084f9d2351a5ea462097a0b5/USER"

sampleBaseDir="root://eoscms//eos/cms///store/caf/user/ejclemen//WZ_pat_20120726/ejclemen/WZ_TuneZ2star_8TeV_pythia6_tauola/WZ_pat_20120726/d0bbde228835224f42d621e7d54b0549/"
samplePatFiles = [
sampleBaseDir+"PATtuple_100_1_rgB.root",
sampleBaseDir+"PATtuple_101_1_Cps.root",
sampleBaseDir+"PATtuple_102_1_pBB.root",
sampleBaseDir+"PATtuple_103_1_Skn.root",
sampleBaseDir+"PATtuple_104_1_VGb.root",
sampleBaseDir+"PATtuple_105_1_qCa.root",
sampleBaseDir+"PATtuple_106_1_5GA.root",
sampleBaseDir+"PATtuple_107_1_IR2.root",
sampleBaseDir+"PATtuple_108_1_Jtw.root",
sampleBaseDir+"PATtuple_109_1_DCu.root",
sampleBaseDir+"PATtuple_10_1_i3S.root",
sampleBaseDir+"PATtuple_110_1_pPR.root",
sampleBaseDir+"PATtuple_111_1_VDp.root",
sampleBaseDir+"PATtuple_112_1_tB6.root",
sampleBaseDir+"PATtuple_113_1_tzh.root",
sampleBaseDir+"PATtuple_114_1_tOS.root",
sampleBaseDir+"PATtuple_115_1_Dgf.root",
sampleBaseDir+"PATtuple_116_1_PxX.root",
sampleBaseDir+"PATtuple_117_1_GLt.root",
sampleBaseDir+"PATtuple_118_1_A9O.root",
sampleBaseDir+"PATtuple_119_1_ry1.root",
sampleBaseDir+"PATtuple_11_1_R9v.root",
sampleBaseDir+"PATtuple_120_1_hgw.root",
sampleBaseDir+"PATtuple_121_1_PTQ.root",
sampleBaseDir+"PATtuple_122_1_WxM.root",
sampleBaseDir+"PATtuple_123_1_zEo.root",
sampleBaseDir+"PATtuple_124_1_YRP.root",
sampleBaseDir+"PATtuple_125_1_RHI.root",
sampleBaseDir+"PATtuple_126_1_VvB.root",
sampleBaseDir+"PATtuple_127_1_XQM.root",
sampleBaseDir+"PATtuple_128_1_TkV.root",
sampleBaseDir+"PATtuple_129_1_mvq.root",
sampleBaseDir+"PATtuple_12_1_xuy.root",
sampleBaseDir+"PATtuple_130_1_tVj.root",
sampleBaseDir+"PATtuple_131_1_ueY.root",
sampleBaseDir+"PATtuple_132_1_RZK.root",
sampleBaseDir+"PATtuple_133_1_qOE.root",
sampleBaseDir+"PATtuple_134_1_SDJ.root",
sampleBaseDir+"PATtuple_135_1_6HR.root",
sampleBaseDir+"PATtuple_136_1_yEs.root",
sampleBaseDir+"PATtuple_137_1_oSF.root",
sampleBaseDir+"PATtuple_138_1_WD4.root",
sampleBaseDir+"PATtuple_139_1_UJ3.root",
sampleBaseDir+"PATtuple_140_1_bjk.root",
sampleBaseDir+"PATtuple_141_1_DTL.root",
sampleBaseDir+"PATtuple_142_1_KE5.root",
sampleBaseDir+"PATtuple_143_1_Ac9.root",
sampleBaseDir+"PATtuple_144_1_wn7.root",
sampleBaseDir+"PATtuple_145_1_8ik.root",
sampleBaseDir+"PATtuple_146_1_nLY.root",
sampleBaseDir+"PATtuple_147_1_Wi9.root",
sampleBaseDir+"PATtuple_148_1_xyI.root",
sampleBaseDir+"PATtuple_149_1_XGc.root",
sampleBaseDir+"PATtuple_14_1_hbe.root",
sampleBaseDir+"PATtuple_150_1_9S2.root",
sampleBaseDir+"PATtuple_151_1_zpW.root",
sampleBaseDir+"PATtuple_152_1_BDG.root",
sampleBaseDir+"PATtuple_153_1_sZC.root",
sampleBaseDir+"PATtuple_154_1_izD.root",
sampleBaseDir+"PATtuple_155_1_Nd9.root",
sampleBaseDir+"PATtuple_156_1_OrP.root",
sampleBaseDir+"PATtuple_157_1_wRN.root",
sampleBaseDir+"PATtuple_158_1_KL4.root",
sampleBaseDir+"PATtuple_159_1_Qsp.root",
sampleBaseDir+"PATtuple_15_1_9oC.root",
sampleBaseDir+"PATtuple_160_1_IPt.root",
sampleBaseDir+"PATtuple_161_1_sVi.root",
sampleBaseDir+"PATtuple_162_1_Fr3.root",
sampleBaseDir+"PATtuple_163_1_kf8.root",
sampleBaseDir+"PATtuple_164_1_5SQ.root",
sampleBaseDir+"PATtuple_165_1_khY.root",
sampleBaseDir+"PATtuple_166_1_1PT.root",
sampleBaseDir+"PATtuple_167_1_TN8.root",
sampleBaseDir+"PATtuple_168_1_GUj.root",
sampleBaseDir+"PATtuple_169_1_wlZ.root",
sampleBaseDir+"PATtuple_16_1_TkK.root",
sampleBaseDir+"PATtuple_170_1_wzz.root",
sampleBaseDir+"PATtuple_171_1_uaA.root",
sampleBaseDir+"PATtuple_172_1_WBt.root",
sampleBaseDir+"PATtuple_173_1_R2E.root",
sampleBaseDir+"PATtuple_174_1_Q2C.root",
sampleBaseDir+"PATtuple_175_1_e39.root",
sampleBaseDir+"PATtuple_176_1_NJ9.root",
sampleBaseDir+"PATtuple_177_1_LNJ.root",
sampleBaseDir+"PATtuple_178_1_r7g.root",
sampleBaseDir+"PATtuple_179_1_a8m.root",
sampleBaseDir+"PATtuple_17_1_O8y.root",
sampleBaseDir+"PATtuple_180_1_HVQ.root",
sampleBaseDir+"PATtuple_181_1_GUA.root",
sampleBaseDir+"PATtuple_182_1_Uc8.root",
sampleBaseDir+"PATtuple_183_1_ix1.root",
sampleBaseDir+"PATtuple_184_1_QOL.root",
sampleBaseDir+"PATtuple_185_1_O3U.root",
sampleBaseDir+"PATtuple_186_1_6tp.root",
sampleBaseDir+"PATtuple_187_1_yPF.root",
sampleBaseDir+"PATtuple_188_1_Z20.root",
sampleBaseDir+"PATtuple_189_1_S5n.root",
sampleBaseDir+"PATtuple_18_1_V3u.root",
sampleBaseDir+"PATtuple_190_1_aVa.root",
sampleBaseDir+"PATtuple_191_1_HqJ.root",
sampleBaseDir+"PATtuple_192_1_oqC.root",
sampleBaseDir+"PATtuple_193_1_Rkp.root",
sampleBaseDir+"PATtuple_194_1_sFx.root",
sampleBaseDir+"PATtuple_195_1_UsY.root",
sampleBaseDir+"PATtuple_196_1_R2X.root",
sampleBaseDir+"PATtuple_197_1_iD7.root",
sampleBaseDir+"PATtuple_198_1_Mck.root",
sampleBaseDir+"PATtuple_199_1_2Vy.root",
sampleBaseDir+"PATtuple_19_1_irg.root",
sampleBaseDir+"PATtuple_1_1_YBT.root",
sampleBaseDir+"PATtuple_200_1_B45.root",
sampleBaseDir+"PATtuple_201_1_UhC.root",
sampleBaseDir+"PATtuple_202_1_bwl.root",
sampleBaseDir+"PATtuple_203_1_KMm.root",
sampleBaseDir+"PATtuple_204_1_JKP.root",
sampleBaseDir+"PATtuple_205_1_iii.root",
sampleBaseDir+"PATtuple_206_1_8sn.root",
sampleBaseDir+"PATtuple_207_1_lME.root",
sampleBaseDir+"PATtuple_208_1_dtT.root",
sampleBaseDir+"PATtuple_209_1_3p1.root",
sampleBaseDir+"PATtuple_20_1_rCn.root",
sampleBaseDir+"PATtuple_210_1_axw.root",
sampleBaseDir+"PATtuple_211_1_l80.root",
sampleBaseDir+"PATtuple_212_1_6as.root",
sampleBaseDir+"PATtuple_213_1_IJg.root",
sampleBaseDir+"PATtuple_214_1_aqi.root",
sampleBaseDir+"PATtuple_215_1_JaJ.root",
sampleBaseDir+"PATtuple_216_1_9JL.root",
sampleBaseDir+"PATtuple_217_1_2Hv.root",
sampleBaseDir+"PATtuple_218_1_60J.root",
sampleBaseDir+"PATtuple_219_1_QVh.root",
sampleBaseDir+"PATtuple_21_1_GQV.root",
sampleBaseDir+"PATtuple_220_1_X5i.root",
sampleBaseDir+"PATtuple_221_1_ge0.root",
sampleBaseDir+"PATtuple_222_1_PXa.root",
sampleBaseDir+"PATtuple_223_1_sPZ.root",
sampleBaseDir+"PATtuple_224_1_bJ4.root",
sampleBaseDir+"PATtuple_225_1_lIl.root",
sampleBaseDir+"PATtuple_226_1_lde.root",
sampleBaseDir+"PATtuple_227_1_STY.root",
sampleBaseDir+"PATtuple_228_1_tr6.root",
sampleBaseDir+"PATtuple_229_1_rUQ.root",
sampleBaseDir+"PATtuple_22_1_RVB.root",
sampleBaseDir+"PATtuple_230_1_SJj.root",
sampleBaseDir+"PATtuple_231_1_aRH.root",
sampleBaseDir+"PATtuple_232_1_jZ7.root",
sampleBaseDir+"PATtuple_233_1_qA1.root",
sampleBaseDir+"PATtuple_234_1_Uks.root",
sampleBaseDir+"PATtuple_235_1_ana.root",
sampleBaseDir+"PATtuple_236_1_H29.root",
sampleBaseDir+"PATtuple_237_1_laS.root",
sampleBaseDir+"PATtuple_238_1_UA3.root",
sampleBaseDir+"PATtuple_239_1_pBH.root",
sampleBaseDir+"PATtuple_23_1_rmM.root",
sampleBaseDir+"PATtuple_240_1_TxJ.root",
sampleBaseDir+"PATtuple_241_1_2fJ.root",
sampleBaseDir+"PATtuple_242_1_9e1.root",
sampleBaseDir+"PATtuple_243_1_65X.root",
sampleBaseDir+"PATtuple_244_1_zus.root",
sampleBaseDir+"PATtuple_245_1_GB3.root",
sampleBaseDir+"PATtuple_246_1_4Jb.root",
sampleBaseDir+"PATtuple_247_1_QzU.root",
sampleBaseDir+"PATtuple_248_1_lQs.root",
sampleBaseDir+"PATtuple_249_1_Gc4.root",
sampleBaseDir+"PATtuple_24_1_rON.root",
sampleBaseDir+"PATtuple_250_1_eyW.root",
sampleBaseDir+"PATtuple_251_1_R1i.root",
sampleBaseDir+"PATtuple_252_1_gGy.root",
sampleBaseDir+"PATtuple_254_1_F7u.root",
sampleBaseDir+"PATtuple_255_1_6Pm.root",
sampleBaseDir+"PATtuple_256_1_4WY.root",
sampleBaseDir+"PATtuple_257_1_0Um.root",
sampleBaseDir+"PATtuple_258_1_52B.root",
sampleBaseDir+"PATtuple_259_1_u6C.root",
sampleBaseDir+"PATtuple_25_1_3DQ.root",
sampleBaseDir+"PATtuple_260_1_HA6.root",
sampleBaseDir+"PATtuple_261_1_Yxc.root",
sampleBaseDir+"PATtuple_262_1_O8b.root",
sampleBaseDir+"PATtuple_263_1_lIN.root",
sampleBaseDir+"PATtuple_264_1_boy.root",
sampleBaseDir+"PATtuple_265_1_hJm.root",
sampleBaseDir+"PATtuple_266_1_P1x.root",
sampleBaseDir+"PATtuple_267_1_PWp.root",
sampleBaseDir+"PATtuple_268_1_5OD.root",
sampleBaseDir+"PATtuple_269_1_za1.root",
sampleBaseDir+"PATtuple_26_1_UDb.root",
sampleBaseDir+"PATtuple_270_1_IxS.root",
sampleBaseDir+"PATtuple_271_1_ah0.root",
sampleBaseDir+"PATtuple_272_1_nWS.root",
sampleBaseDir+"PATtuple_273_1_cIA.root",
sampleBaseDir+"PATtuple_274_1_z1w.root",
sampleBaseDir+"PATtuple_275_1_JAK.root",
sampleBaseDir+"PATtuple_276_1_oVT.root",
sampleBaseDir+"PATtuple_277_1_9Ib.root",
sampleBaseDir+"PATtuple_278_1_Ly9.root",
sampleBaseDir+"PATtuple_279_1_95w.root",
sampleBaseDir+"PATtuple_27_1_c0o.root",
sampleBaseDir+"PATtuple_280_1_eG2.root",
sampleBaseDir+"PATtuple_281_1_JRV.root",
sampleBaseDir+"PATtuple_282_1_zzV.root",
sampleBaseDir+"PATtuple_283_1_m0T.root",
sampleBaseDir+"PATtuple_284_1_ZSq.root",
sampleBaseDir+"PATtuple_285_1_mu7.root",
sampleBaseDir+"PATtuple_286_1_DUa.root",
sampleBaseDir+"PATtuple_287_1_guA.root",
sampleBaseDir+"PATtuple_288_1_TWL.root",
sampleBaseDir+"PATtuple_289_1_ysC.root",
sampleBaseDir+"PATtuple_290_1_vUv.root",
sampleBaseDir+"PATtuple_291_1_OtH.root",
sampleBaseDir+"PATtuple_292_1_DDX.root",
sampleBaseDir+"PATtuple_293_1_HV1.root",
sampleBaseDir+"PATtuple_294_1_Gsr.root",
sampleBaseDir+"PATtuple_295_1_fDy.root",
sampleBaseDir+"PATtuple_296_1_Lvf.root",
sampleBaseDir+"PATtuple_297_1_QCE.root",
sampleBaseDir+"PATtuple_298_1_lPw.root",
sampleBaseDir+"PATtuple_299_1_USd.root",
sampleBaseDir+"PATtuple_29_1_kaM.root",
sampleBaseDir+"PATtuple_2_1_inN.root",
sampleBaseDir+"PATtuple_300_1_UCA.root",
sampleBaseDir+"PATtuple_301_1_jsy.root",
sampleBaseDir+"PATtuple_302_1_hfJ.root",
sampleBaseDir+"PATtuple_303_1_TWa.root",
sampleBaseDir+"PATtuple_304_1_9ET.root",
sampleBaseDir+"PATtuple_305_1_7SW.root",
sampleBaseDir+"PATtuple_306_1_WGo.root",
sampleBaseDir+"PATtuple_307_1_tsQ.root",
sampleBaseDir+"PATtuple_308_1_Bnl.root",
sampleBaseDir+"PATtuple_309_1_h8S.root",
sampleBaseDir+"PATtuple_30_1_t5W.root",
sampleBaseDir+"PATtuple_310_0_whF.root",
sampleBaseDir+"PATtuple_311_0_hB4.root",
sampleBaseDir+"PATtuple_312_0_PQ8.root",
sampleBaseDir+"PATtuple_313_0_Q1S.root",
sampleBaseDir+"PATtuple_314_0_AkR.root",
sampleBaseDir+"PATtuple_315_0_iuh.root",
sampleBaseDir+"PATtuple_316_0_PwK.root",
sampleBaseDir+"PATtuple_316_0_cUX.root",
sampleBaseDir+"PATtuple_317_0_fuX.root",
sampleBaseDir+"PATtuple_318_0_k94.root",
sampleBaseDir+"PATtuple_319_0_jqP.root",
sampleBaseDir+"PATtuple_31_1_h72.root",
sampleBaseDir+"PATtuple_320_0_SnY.root",
sampleBaseDir+"PATtuple_321_0_nda.root",
sampleBaseDir+"PATtuple_322_0_q5g.root",
sampleBaseDir+"PATtuple_323_0_ZcD.root",
sampleBaseDir+"PATtuple_324_0_4Or.root",
sampleBaseDir+"PATtuple_325_0_Bsd.root",
sampleBaseDir+"PATtuple_326_0_7zZ.root",
sampleBaseDir+"PATtuple_327_0_yJi.root",
sampleBaseDir+"PATtuple_328_0_9Ea.root",
sampleBaseDir+"PATtuple_329_0_0py.root",
sampleBaseDir+"PATtuple_32_1_xlm.root",
sampleBaseDir+"PATtuple_330_0_tT0.root",
sampleBaseDir+"PATtuple_331_0_Yni.root",
sampleBaseDir+"PATtuple_332_0_Ezn.root",
sampleBaseDir+"PATtuple_333_0_iCA.root",
sampleBaseDir+"PATtuple_334_0_YL4.root",
sampleBaseDir+"PATtuple_335_0_xYy.root",
sampleBaseDir+"PATtuple_336_0_ng3.root",
sampleBaseDir+"PATtuple_337_0_Get.root",
sampleBaseDir+"PATtuple_338_0_UCH.root",
sampleBaseDir+"PATtuple_339_0_PMB.root",
sampleBaseDir+"PATtuple_33_1_b9Z.root",
sampleBaseDir+"PATtuple_340_0_Hfz.root",
sampleBaseDir+"PATtuple_341_0_Bay.root",
sampleBaseDir+"PATtuple_342_0_JCf.root",
sampleBaseDir+"PATtuple_343_0_Czx.root",
sampleBaseDir+"PATtuple_344_0_pNx.root",
sampleBaseDir+"PATtuple_345_0_FIN.root",
sampleBaseDir+"PATtuple_346_0_Eh1.root",
sampleBaseDir+"PATtuple_348_0_tJK.root",
sampleBaseDir+"PATtuple_349_0_APW.root",
sampleBaseDir+"PATtuple_34_1_RLj.root",
sampleBaseDir+"PATtuple_350_0_bSj.root",
sampleBaseDir+"PATtuple_351_0_11K.root",
sampleBaseDir+"PATtuple_351_0_Zhg.root",
sampleBaseDir+"PATtuple_352_0_xKv.root",
sampleBaseDir+"PATtuple_353_0_7YJ.root",
sampleBaseDir+"PATtuple_354_0_n3v.root",
sampleBaseDir+"PATtuple_355_0_6oN.root",
sampleBaseDir+"PATtuple_356_0_51L.root",
sampleBaseDir+"PATtuple_356_0_ncO.root",
sampleBaseDir+"PATtuple_357_0_Bxc.root",
sampleBaseDir+"PATtuple_357_0_Pmj.root",
sampleBaseDir+"PATtuple_358_0_Wbq.root",
sampleBaseDir+"PATtuple_358_0_WoW.root",
sampleBaseDir+"PATtuple_359_0_zTc.root",
sampleBaseDir+"PATtuple_35_1_g5i.root",
sampleBaseDir+"PATtuple_360_0_ULX.root",
sampleBaseDir+"PATtuple_361_0_Lu0.root",
sampleBaseDir+"PATtuple_362_0_dfk.root",
sampleBaseDir+"PATtuple_363_0_uDZ.root",
sampleBaseDir+"PATtuple_364_0_d2I.root",
sampleBaseDir+"PATtuple_365_0_6BK.root",
sampleBaseDir+"PATtuple_366_0_JeE.root",
sampleBaseDir+"PATtuple_367_0_R7l.root",
sampleBaseDir+"PATtuple_368_0_lMh.root",
sampleBaseDir+"PATtuple_369_0_5n0.root",
sampleBaseDir+"PATtuple_36_1_tlu.root",
sampleBaseDir+"PATtuple_370_0_FmI.root",
sampleBaseDir+"PATtuple_371_0_kpv.root",
sampleBaseDir+"PATtuple_372_0_Qtv.root",
sampleBaseDir+"PATtuple_372_0_fl0.root",
sampleBaseDir+"PATtuple_373_0_SkW.root",
sampleBaseDir+"PATtuple_373_0_awH.root",
sampleBaseDir+"PATtuple_374_0_DxI.root",
sampleBaseDir+"PATtuple_374_0_ZI7.root",
sampleBaseDir+"PATtuple_375_0_aJM.root",
sampleBaseDir+"PATtuple_376_0_52B.root",
sampleBaseDir+"PATtuple_377_0_JnE.root",
sampleBaseDir+"PATtuple_378_0_Kxn.root",
sampleBaseDir+"PATtuple_379_0_kZa.root",
sampleBaseDir+"PATtuple_37_1_F7j.root",
sampleBaseDir+"PATtuple_380_0_0Yd.root",
sampleBaseDir+"PATtuple_381_0_TFd.root",
sampleBaseDir+"PATtuple_382_0_qKT.root",
sampleBaseDir+"PATtuple_383_0_XwG.root",
sampleBaseDir+"PATtuple_384_0_yUe.root",
sampleBaseDir+"PATtuple_385_0_eo5.root",
sampleBaseDir+"PATtuple_386_0_YzY.root",
sampleBaseDir+"PATtuple_387_0_bUh.root",
sampleBaseDir+"PATtuple_388_0_rFA.root",
sampleBaseDir+"PATtuple_389_0_Ywf.root",
sampleBaseDir+"PATtuple_390_0_H3a.root",
sampleBaseDir+"PATtuple_390_0_yiU.root",
sampleBaseDir+"PATtuple_391_0_gOY.root",
sampleBaseDir+"PATtuple_391_0_lZP.root",
sampleBaseDir+"PATtuple_392_0_N6z.root",
sampleBaseDir+"PATtuple_392_1_mq9.root",
sampleBaseDir+"PATtuple_393_0_1t2.root",
sampleBaseDir+"PATtuple_393_1_JMk.root",
sampleBaseDir+"PATtuple_394_0_a7H.root",
sampleBaseDir+"PATtuple_394_1_uY8.root",
sampleBaseDir+"PATtuple_395_0_UPF.root",
sampleBaseDir+"PATtuple_395_0_r8A.root",
sampleBaseDir+"PATtuple_396_0_PsS.root",
sampleBaseDir+"PATtuple_396_0_WPZ.root",
sampleBaseDir+"PATtuple_397_0_493.root",
sampleBaseDir+"PATtuple_397_0_U9E.root",
sampleBaseDir+"PATtuple_398_0_0OS.root",
sampleBaseDir+"PATtuple_398_0_kpA.root",
sampleBaseDir+"PATtuple_399_0_ARc.root",
sampleBaseDir+"PATtuple_399_0_v41.root",
sampleBaseDir+"PATtuple_39_1_S8L.root",
sampleBaseDir+"PATtuple_3_1_LET.root",
sampleBaseDir+"PATtuple_400_0_P6h.root",
sampleBaseDir+"PATtuple_400_0_WZG.root",
sampleBaseDir+"PATtuple_401_0_HaP.root",
sampleBaseDir+"PATtuple_401_0_zJj.root",
sampleBaseDir+"PATtuple_402_0_9iU.root",
sampleBaseDir+"PATtuple_402_0_T1j.root",
sampleBaseDir+"PATtuple_403_0_uVo.root",
sampleBaseDir+"PATtuple_404_0_gcQ.root",
sampleBaseDir+"PATtuple_404_0_jKH.root",
sampleBaseDir+"PATtuple_405_0_PtB.root",
sampleBaseDir+"PATtuple_406_0_ARf.root",
sampleBaseDir+"PATtuple_407_0_Cht.root",
sampleBaseDir+"PATtuple_408_0_hRV.root",
sampleBaseDir+"PATtuple_409_0_oTh.root",
sampleBaseDir+"PATtuple_40_1_Stt.root",
sampleBaseDir+"PATtuple_410_0_tOM.root",
sampleBaseDir+"PATtuple_411_0_qoz.root",
sampleBaseDir+"PATtuple_412_0_K7l.root",
sampleBaseDir+"PATtuple_413_0_cdu.root",
sampleBaseDir+"PATtuple_414_0_Lgv.root",
sampleBaseDir+"PATtuple_415_0_KSs.root",
sampleBaseDir+"PATtuple_416_0_3Pk.root",
sampleBaseDir+"PATtuple_417_0_RzL.root",
sampleBaseDir+"PATtuple_418_0_Ts4.root",
sampleBaseDir+"PATtuple_419_0_Ob7.root",
sampleBaseDir+"PATtuple_41_1_rz5.root",
sampleBaseDir+"PATtuple_420_0_N7l.root",
sampleBaseDir+"PATtuple_420_0_wwg.root",
sampleBaseDir+"PATtuple_421_0_WKw.root",
sampleBaseDir+"PATtuple_422_0_Xiu.root",
sampleBaseDir+"PATtuple_423_0_HHm.root",
sampleBaseDir+"PATtuple_424_0_jEr.root",
sampleBaseDir+"PATtuple_425_0_Lwg.root",
sampleBaseDir+"PATtuple_426_0_vfd.root",
sampleBaseDir+"PATtuple_427_0_7Ij.root",
sampleBaseDir+"PATtuple_428_0_iOZ.root",
sampleBaseDir+"PATtuple_429_0_5wg.root",
sampleBaseDir+"PATtuple_42_1_AXP.root",
sampleBaseDir+"PATtuple_430_0_UPi.root",
sampleBaseDir+"PATtuple_431_0_nkC.root",
sampleBaseDir+"PATtuple_432_0_2A5.root",
sampleBaseDir+"PATtuple_433_0_6el.root",
sampleBaseDir+"PATtuple_434_0_bei.root",
sampleBaseDir+"PATtuple_435_0_mLb.root",
sampleBaseDir+"PATtuple_435_0_qqL.root",
sampleBaseDir+"PATtuple_436_0_2Yr.root",
sampleBaseDir+"PATtuple_437_0_NOr.root",
sampleBaseDir+"PATtuple_438_0_JcZ.root",
sampleBaseDir+"PATtuple_439_0_471.root",
sampleBaseDir+"PATtuple_43_1_U1P.root",
sampleBaseDir+"PATtuple_440_0_XQq.root",
sampleBaseDir+"PATtuple_441_0_Z7D.root",
sampleBaseDir+"PATtuple_442_0_Qh6.root",
sampleBaseDir+"PATtuple_443_0_38I.root",
sampleBaseDir+"PATtuple_444_0_dOI.root",
sampleBaseDir+"PATtuple_445_0_EzL.root",
sampleBaseDir+"PATtuple_446_0_13B.root",
sampleBaseDir+"PATtuple_447_0_i0p.root",
sampleBaseDir+"PATtuple_448_0_FT5.root",
sampleBaseDir+"PATtuple_449_0_gKu.root",
sampleBaseDir+"PATtuple_44_1_HWH.root",
sampleBaseDir+"PATtuple_450_0_vig.root",
sampleBaseDir+"PATtuple_451_0_du5.root",
sampleBaseDir+"PATtuple_452_0_Unk.root",
sampleBaseDir+"PATtuple_452_0_ZiV.root",
sampleBaseDir+"PATtuple_453_0_6Aw.root",
sampleBaseDir+"PATtuple_454_0_bxt.root",
sampleBaseDir+"PATtuple_455_0_zvQ.root",
sampleBaseDir+"PATtuple_456_0_eMh.root",
sampleBaseDir+"PATtuple_457_0_46E.root",
sampleBaseDir+"PATtuple_458_0_LCi.root",
sampleBaseDir+"PATtuple_459_0_Fpj.root",
sampleBaseDir+"PATtuple_45_1_sVw.root",
sampleBaseDir+"PATtuple_460_0_4aJ.root",
sampleBaseDir+"PATtuple_461_0_Vbx.root",
sampleBaseDir+"PATtuple_462_0_bKK.root",
sampleBaseDir+"PATtuple_463_0_WWo.root",
sampleBaseDir+"PATtuple_464_0_36N.root",
sampleBaseDir+"PATtuple_465_0_kc9.root",
sampleBaseDir+"PATtuple_466_0_hQc.root",
sampleBaseDir+"PATtuple_467_0_6BS.root",
sampleBaseDir+"PATtuple_468_0_iIH.root",
sampleBaseDir+"PATtuple_469_0_fCU.root",
sampleBaseDir+"PATtuple_46_1_RE0.root",
sampleBaseDir+"PATtuple_470_0_LBX.root",
sampleBaseDir+"PATtuple_471_0_114.root",
sampleBaseDir+"PATtuple_472_0_JaV.root",
sampleBaseDir+"PATtuple_473_0_s3y.root",
sampleBaseDir+"PATtuple_474_0_lvj.root",
sampleBaseDir+"PATtuple_475_0_gxA.root",
sampleBaseDir+"PATtuple_476_0_Hgx.root",
sampleBaseDir+"PATtuple_477_0_S68.root",
sampleBaseDir+"PATtuple_478_0_zZO.root",
sampleBaseDir+"PATtuple_479_0_Ich.root",
sampleBaseDir+"PATtuple_47_1_Avg.root",
sampleBaseDir+"PATtuple_480_0_Ec3.root",
sampleBaseDir+"PATtuple_481_0_QdT.root",
sampleBaseDir+"PATtuple_482_0_6h6.root",
sampleBaseDir+"PATtuple_483_0_DEh.root",
sampleBaseDir+"PATtuple_483_0_eyv.root",
sampleBaseDir+"PATtuple_484_0_Scu.root",
sampleBaseDir+"PATtuple_485_0_Nps.root",
sampleBaseDir+"PATtuple_486_0_10b.root",
sampleBaseDir+"PATtuple_487_0_Wzb.root",
sampleBaseDir+"PATtuple_488_0_sog.root",
sampleBaseDir+"PATtuple_489_0_s67.root",
sampleBaseDir+"PATtuple_48_1_aKg.root",
sampleBaseDir+"PATtuple_490_0_Y1A.root",
sampleBaseDir+"PATtuple_491_0_wTL.root",
sampleBaseDir+"PATtuple_492_0_J9F.root",
sampleBaseDir+"PATtuple_493_0_z7x.root",
sampleBaseDir+"PATtuple_494_0_lE4.root",
sampleBaseDir+"PATtuple_495_0_fnY.root",
sampleBaseDir+"PATtuple_495_0_x3E.root",
sampleBaseDir+"PATtuple_496_0_xj0.root",
sampleBaseDir+"PATtuple_497_0_BDv.root",
sampleBaseDir+"PATtuple_497_0_bM2.root",
sampleBaseDir+"PATtuple_498_0_vb8.root",
sampleBaseDir+"PATtuple_499_0_7wX.root",
sampleBaseDir+"PATtuple_49_1_VWA.root",
sampleBaseDir+"PATtuple_4_1_eEz.root",
sampleBaseDir+"PATtuple_500_0_fFF.root",
sampleBaseDir+"PATtuple_501_0_hVp.root",
sampleBaseDir+"PATtuple_502_0_Tcg.root",
sampleBaseDir+"PATtuple_502_0_s4Z.root",
sampleBaseDir+"PATtuple_503_0_Gs2.root",
sampleBaseDir+"PATtuple_503_1_F3j.root",
sampleBaseDir+"PATtuple_504_0_A1R.root",
sampleBaseDir+"PATtuple_504_0_wBV.root",
sampleBaseDir+"PATtuple_505_0_TVr.root",
sampleBaseDir+"PATtuple_506_0_09v.root",
sampleBaseDir+"PATtuple_507_0_bQS.root",
sampleBaseDir+"PATtuple_508_0_KCH.root",
sampleBaseDir+"PATtuple_509_0_2Gm.root",
sampleBaseDir+"PATtuple_50_1_XdA.root",
sampleBaseDir+"PATtuple_510_0_b25.root",
sampleBaseDir+"PATtuple_511_1_iz3.root",
sampleBaseDir+"PATtuple_512_1_88v.root",
sampleBaseDir+"PATtuple_513_1_pKF.root",
sampleBaseDir+"PATtuple_514_1_zbC.root",
sampleBaseDir+"PATtuple_515_1_k6i.root",
sampleBaseDir+"PATtuple_516_1_7s3.root",
sampleBaseDir+"PATtuple_517_1_TrB.root",
sampleBaseDir+"PATtuple_518_1_fnR.root",
sampleBaseDir+"PATtuple_519_1_H4p.root",
sampleBaseDir+"PATtuple_51_1_qgS.root",
sampleBaseDir+"PATtuple_520_1_BsB.root",
sampleBaseDir+"PATtuple_521_1_1nH.root",
sampleBaseDir+"PATtuple_522_1_qEo.root",
sampleBaseDir+"PATtuple_523_1_4E3.root",
sampleBaseDir+"PATtuple_524_1_kt0.root",
sampleBaseDir+"PATtuple_525_1_mpo.root",
sampleBaseDir+"PATtuple_526_1_tzp.root",
sampleBaseDir+"PATtuple_527_1_jcY.root",
sampleBaseDir+"PATtuple_528_1_XNK.root",
sampleBaseDir+"PATtuple_529_1_nQj.root",
sampleBaseDir+"PATtuple_52_1_tkW.root",
sampleBaseDir+"PATtuple_530_1_KLQ.root",
sampleBaseDir+"PATtuple_530_1_x8U.root",
sampleBaseDir+"PATtuple_531_1_jdk.root",
sampleBaseDir+"PATtuple_532_1_2F4.root",
sampleBaseDir+"PATtuple_532_2_wlA.root",
sampleBaseDir+"PATtuple_533_1_amp.root",
sampleBaseDir+"PATtuple_533_1_zWk.root",
sampleBaseDir+"PATtuple_534_1_Skf.root",
sampleBaseDir+"PATtuple_534_1_yeq.root",
sampleBaseDir+"PATtuple_535_1_K9h.root",
sampleBaseDir+"PATtuple_536_1_09A.root",
sampleBaseDir+"PATtuple_536_1_TbW.root",
sampleBaseDir+"PATtuple_537_1_gee.root",
sampleBaseDir+"PATtuple_537_1_y8w.root",
sampleBaseDir+"PATtuple_538_1_m0g.root",
sampleBaseDir+"PATtuple_538_1_nHN.root",
sampleBaseDir+"PATtuple_539_1_1Xb.root",
sampleBaseDir+"PATtuple_539_1_VsK.root",
sampleBaseDir+"PATtuple_540_1_WbL.root",
sampleBaseDir+"PATtuple_540_1_dii.root",
sampleBaseDir+"PATtuple_541_1_Ttq.root",
sampleBaseDir+"PATtuple_541_1_gS8.root",
sampleBaseDir+"PATtuple_542_1_dFo.root",
sampleBaseDir+"PATtuple_543_1_9Fg.root",
sampleBaseDir+"PATtuple_544_1_EfF.root",
sampleBaseDir+"PATtuple_544_1_np0.root",
sampleBaseDir+"PATtuple_545_1_Kdb.root",
sampleBaseDir+"PATtuple_546_1_qUl.root",
sampleBaseDir+"PATtuple_547_1_5ih.root",
sampleBaseDir+"PATtuple_548_1_FPq.root",
sampleBaseDir+"PATtuple_549_1_6Lb.root",
sampleBaseDir+"PATtuple_54_1_qgI.root",
sampleBaseDir+"PATtuple_550_1_Pqr.root",
sampleBaseDir+"PATtuple_551_1_spk.root",
sampleBaseDir+"PATtuple_552_1_3Q2.root",
sampleBaseDir+"PATtuple_553_1_5JP.root",
sampleBaseDir+"PATtuple_554_1_a50.root",
sampleBaseDir+"PATtuple_555_1_5dV.root",
sampleBaseDir+"PATtuple_556_1_xdc.root",
sampleBaseDir+"PATtuple_557_1_0Bg.root",
sampleBaseDir+"PATtuple_558_1_A82.root",
sampleBaseDir+"PATtuple_559_1_3pD.root",
sampleBaseDir+"PATtuple_55_1_rBY.root",
sampleBaseDir+"PATtuple_560_1_Ca6.root",
sampleBaseDir+"PATtuple_560_2_BcD.root",
sampleBaseDir+"PATtuple_561_1_4xs.root",
sampleBaseDir+"PATtuple_562_1_dnc.root",
sampleBaseDir+"PATtuple_563_1_imb.root",
sampleBaseDir+"PATtuple_564_1_9eZ.root",
sampleBaseDir+"PATtuple_565_1_8eb.root",
sampleBaseDir+"PATtuple_566_1_h8k.root",
sampleBaseDir+"PATtuple_567_1_vYE.root",
sampleBaseDir+"PATtuple_568_1_atg.root",
sampleBaseDir+"PATtuple_569_1_PCJ.root",
sampleBaseDir+"PATtuple_56_1_mlC.root",
sampleBaseDir+"PATtuple_570_1_V8J.root",
sampleBaseDir+"PATtuple_571_1_Bu5.root",
sampleBaseDir+"PATtuple_572_1_vVt.root",
sampleBaseDir+"PATtuple_573_1_Xy4.root",
sampleBaseDir+"PATtuple_574_1_dtm.root",
sampleBaseDir+"PATtuple_575_1_MhG.root",
sampleBaseDir+"PATtuple_575_1_hwh.root",
sampleBaseDir+"PATtuple_576_1_HDd.root",
sampleBaseDir+"PATtuple_577_1_Oem.root",
sampleBaseDir+"PATtuple_578_1_WJU.root",
sampleBaseDir+"PATtuple_579_1_p8S.root",
sampleBaseDir+"PATtuple_57_1_ALS.root",
sampleBaseDir+"PATtuple_580_1_7a2.root",
sampleBaseDir+"PATtuple_581_1_HEx.root",
sampleBaseDir+"PATtuple_582_1_VgJ.root",
sampleBaseDir+"PATtuple_583_1_Ath.root",
sampleBaseDir+"PATtuple_584_1_6of.root",
sampleBaseDir+"PATtuple_584_1_RLG.root",
sampleBaseDir+"PATtuple_585_1_JlW.root",
sampleBaseDir+"PATtuple_586_1_AtI.root",
sampleBaseDir+"PATtuple_587_1_iv9.root",
sampleBaseDir+"PATtuple_588_1_p9u.root",
sampleBaseDir+"PATtuple_589_1_TA4.root",
sampleBaseDir+"PATtuple_58_1_hh8.root",
sampleBaseDir+"PATtuple_590_1_X3v.root",
sampleBaseDir+"PATtuple_591_1_9bg.root",
sampleBaseDir+"PATtuple_592_1_FC8.root",
sampleBaseDir+"PATtuple_593_1_fe6.root",
sampleBaseDir+"PATtuple_594_1_8rU.root",
sampleBaseDir+"PATtuple_595_1_8zX.root",
sampleBaseDir+"PATtuple_596_1_bj4.root",
sampleBaseDir+"PATtuple_597_1_JTP.root",
sampleBaseDir+"PATtuple_598_1_Hni.root",
sampleBaseDir+"PATtuple_599_1_ouF.root",
sampleBaseDir+"PATtuple_59_1_pWc.root",
sampleBaseDir+"PATtuple_5_1_zgF.root",
sampleBaseDir+"PATtuple_600_1_BMD.root",
sampleBaseDir+"PATtuple_601_1_nVa.root",
sampleBaseDir+"PATtuple_602_1_Han.root",
sampleBaseDir+"PATtuple_603_1_FPE.root",
sampleBaseDir+"PATtuple_604_1_StT.root",
sampleBaseDir+"PATtuple_605_1_NTu.root",
sampleBaseDir+"PATtuple_606_1_6OU.root",
sampleBaseDir+"PATtuple_607_1_wdC.root",
sampleBaseDir+"PATtuple_608_1_Bzo.root",
sampleBaseDir+"PATtuple_609_1_anx.root",
sampleBaseDir+"PATtuple_60_1_GYO.root",
sampleBaseDir+"PATtuple_610_1_MSv.root",
sampleBaseDir+"PATtuple_611_1_YGE.root",
sampleBaseDir+"PATtuple_612_1_G4s.root",
sampleBaseDir+"PATtuple_613_1_Lw8.root",
sampleBaseDir+"PATtuple_614_1_JKZ.root",
sampleBaseDir+"PATtuple_615_1_s2R.root",
sampleBaseDir+"PATtuple_616_1_Xal.root",
sampleBaseDir+"PATtuple_617_1_QHf.root",
sampleBaseDir+"PATtuple_618_1_8Dc.root",
sampleBaseDir+"PATtuple_619_1_ClP.root",
sampleBaseDir+"PATtuple_61_1_s0D.root",
sampleBaseDir+"PATtuple_620_1_BBO.root",
sampleBaseDir+"PATtuple_621_1_EyZ.root",
sampleBaseDir+"PATtuple_622_1_Ble.root",
sampleBaseDir+"PATtuple_623_1_a0y.root",
sampleBaseDir+"PATtuple_623_2_GB7.root",
sampleBaseDir+"PATtuple_624_1_6Mj.root",
sampleBaseDir+"PATtuple_625_1_TnI.root",
sampleBaseDir+"PATtuple_626_1_YRB.root",
sampleBaseDir+"PATtuple_627_1_OME.root",
sampleBaseDir+"PATtuple_628_1_i88.root",
sampleBaseDir+"PATtuple_629_1_u6w.root",
sampleBaseDir+"PATtuple_629_1_wCD.root",
sampleBaseDir+"PATtuple_62_1_nXp.root",
sampleBaseDir+"PATtuple_630_1_dEa.root",
sampleBaseDir+"PATtuple_630_1_kN2.root",
sampleBaseDir+"PATtuple_631_1_27H.root",
sampleBaseDir+"PATtuple_631_1_vqz.root",
sampleBaseDir+"PATtuple_632_1_LlQ.root",
sampleBaseDir+"PATtuple_633_1_x7i.root",
sampleBaseDir+"PATtuple_634_1_EkJ.root",
sampleBaseDir+"PATtuple_635_1_qGl.root",
sampleBaseDir+"PATtuple_636_1_kB5.root",
sampleBaseDir+"PATtuple_637_1_oFM.root",
sampleBaseDir+"PATtuple_638_1_WYi.root",
sampleBaseDir+"PATtuple_639_1_Ktv.root",
sampleBaseDir+"PATtuple_63_1_4ms.root",
sampleBaseDir+"PATtuple_640_1_fXH.root",
sampleBaseDir+"PATtuple_641_1_qqT.root",
sampleBaseDir+"PATtuple_642_1_jdJ.root",
sampleBaseDir+"PATtuple_643_1_sGX.root",
sampleBaseDir+"PATtuple_644_1_oTZ.root",
sampleBaseDir+"PATtuple_645_1_RFm.root",
sampleBaseDir+"PATtuple_646_1_b7F.root",
sampleBaseDir+"PATtuple_647_1_lt6.root",
sampleBaseDir+"PATtuple_648_1_Apy.root",
sampleBaseDir+"PATtuple_649_1_Dtm.root",
sampleBaseDir+"PATtuple_64_1_CCN.root",
sampleBaseDir+"PATtuple_650_1_Crj.root",
sampleBaseDir+"PATtuple_651_1_dXO.root",
sampleBaseDir+"PATtuple_652_1_J8F.root",
sampleBaseDir+"PATtuple_653_1_xjw.root",
sampleBaseDir+"PATtuple_654_1_rvG.root",
sampleBaseDir+"PATtuple_655_1_D6i.root",
sampleBaseDir+"PATtuple_656_1_kEB.root",
sampleBaseDir+"PATtuple_657_1_xs1.root",
sampleBaseDir+"PATtuple_658_1_Nkc.root",
sampleBaseDir+"PATtuple_659_2_xLn.root",
sampleBaseDir+"PATtuple_659_3_7n7.root",
sampleBaseDir+"PATtuple_65_1_L8z.root",
sampleBaseDir+"PATtuple_660_1_ND4.root",
sampleBaseDir+"PATtuple_661_1_GR0.root",
sampleBaseDir+"PATtuple_662_1_nWh.root",
sampleBaseDir+"PATtuple_663_1_pos.root",
sampleBaseDir+"PATtuple_664_1_raC.root",
sampleBaseDir+"PATtuple_665_1_NGI.root",
sampleBaseDir+"PATtuple_666_1_Zch.root",
sampleBaseDir+"PATtuple_667_1_tvZ.root",
sampleBaseDir+"PATtuple_668_1_p7d.root",
sampleBaseDir+"PATtuple_669_1_0Uo.root",
sampleBaseDir+"PATtuple_66_1_n8j.root",
sampleBaseDir+"PATtuple_670_1_6o9.root",
sampleBaseDir+"PATtuple_671_1_v6y.root",
sampleBaseDir+"PATtuple_672_2_67T.root",
sampleBaseDir+"PATtuple_672_3_aVu.root",
sampleBaseDir+"PATtuple_673_2_c4o.root",
sampleBaseDir+"PATtuple_673_3_JSX.root",
sampleBaseDir+"PATtuple_674_2_GmG.root",
sampleBaseDir+"PATtuple_674_3_2DW.root",
sampleBaseDir+"PATtuple_675_1_wKa.root",
sampleBaseDir+"PATtuple_676_1_hoF.root",
sampleBaseDir+"PATtuple_677_1_zd5.root",
sampleBaseDir+"PATtuple_678_1_qeS.root",
sampleBaseDir+"PATtuple_679_1_n2y.root",
sampleBaseDir+"PATtuple_67_1_o3L.root",
sampleBaseDir+"PATtuple_680_1_Q6z.root",
sampleBaseDir+"PATtuple_681_1_3cT.root",
sampleBaseDir+"PATtuple_682_2_q0o.root",
sampleBaseDir+"PATtuple_682_3_wGC.root",
sampleBaseDir+"PATtuple_683_1_in2.root",
sampleBaseDir+"PATtuple_684_2_ALG.root",
sampleBaseDir+"PATtuple_684_3_TrJ.root",
sampleBaseDir+"PATtuple_685_2_5Wz.root",
sampleBaseDir+"PATtuple_685_3_Uj4.root",
sampleBaseDir+"PATtuple_686_1_wAY.root",
sampleBaseDir+"PATtuple_687_1_aOk.root",
sampleBaseDir+"PATtuple_688_1_zju.root",
sampleBaseDir+"PATtuple_689_1_vxH.root",
sampleBaseDir+"PATtuple_68_1_aKf.root",
sampleBaseDir+"PATtuple_690_1_H1h.root",
sampleBaseDir+"PATtuple_691_1_aTV.root",
sampleBaseDir+"PATtuple_692_1_7au.root",
sampleBaseDir+"PATtuple_693_1_t1q.root",
sampleBaseDir+"PATtuple_694_1_g30.root",
sampleBaseDir+"PATtuple_695_2_TeR.root",
sampleBaseDir+"PATtuple_695_3_vZj.root",
sampleBaseDir+"PATtuple_696_3_bAO.root",
sampleBaseDir+"PATtuple_697_2_TYO.root",
sampleBaseDir+"PATtuple_697_3_On3.root",
sampleBaseDir+"PATtuple_698_3_8it.root",
sampleBaseDir+"PATtuple_699_3_zSZ.root",
sampleBaseDir+"PATtuple_69_1_2fo.root",
sampleBaseDir+"PATtuple_6_1_Xvl.root",
sampleBaseDir+"PATtuple_700_3_Irw.root",
sampleBaseDir+"PATtuple_701_3_3dt.root",
sampleBaseDir+"PATtuple_702_3_fIQ.root",
sampleBaseDir+"PATtuple_703_3_mDf.root",
sampleBaseDir+"PATtuple_704_3_3Bf.root",
sampleBaseDir+"PATtuple_705_3_Pb2.root",
sampleBaseDir+"PATtuple_706_3_Vzf.root",
sampleBaseDir+"PATtuple_707_3_7qe.root",
sampleBaseDir+"PATtuple_708_2_wM7.root",
sampleBaseDir+"PATtuple_708_3_jUY.root",
sampleBaseDir+"PATtuple_709_1_95f.root",
sampleBaseDir+"PATtuple_70_1_tAJ.root",
sampleBaseDir+"PATtuple_710_1_Egz.root",
sampleBaseDir+"PATtuple_711_1_1dM.root",
sampleBaseDir+"PATtuple_712_1_8hN.root",
sampleBaseDir+"PATtuple_713_1_4yP.root",
sampleBaseDir+"PATtuple_714_1_PII.root",
sampleBaseDir+"PATtuple_715_1_w4e.root",
sampleBaseDir+"PATtuple_716_1_VKT.root",
sampleBaseDir+"PATtuple_717_1_dMo.root",
sampleBaseDir+"PATtuple_718_1_SrH.root",
sampleBaseDir+"PATtuple_719_1_Daj.root",
sampleBaseDir+"PATtuple_71_1_4P0.root",
sampleBaseDir+"PATtuple_720_1_vSm.root",
sampleBaseDir+"PATtuple_721_1_X5f.root",
sampleBaseDir+"PATtuple_722_1_ylx.root",
sampleBaseDir+"PATtuple_723_1_gpU.root",
sampleBaseDir+"PATtuple_724_1_FaT.root",
sampleBaseDir+"PATtuple_725_1_fA1.root",
sampleBaseDir+"PATtuple_726_1_75M.root",
sampleBaseDir+"PATtuple_727_1_lzq.root",
sampleBaseDir+"PATtuple_728_1_xa3.root",
sampleBaseDir+"PATtuple_729_1_5V2.root",
sampleBaseDir+"PATtuple_72_1_rOw.root",
sampleBaseDir+"PATtuple_730_1_juM.root",
sampleBaseDir+"PATtuple_731_2_TrF.root",
sampleBaseDir+"PATtuple_731_3_3zw.root",
sampleBaseDir+"PATtuple_732_1_W3b.root",
sampleBaseDir+"PATtuple_733_1_hzr.root",
sampleBaseDir+"PATtuple_734_1_5oe.root",
sampleBaseDir+"PATtuple_735_1_Qwu.root",
sampleBaseDir+"PATtuple_736_1_o1l.root",
sampleBaseDir+"PATtuple_737_1_nQv.root",
sampleBaseDir+"PATtuple_738_1_pYG.root",
sampleBaseDir+"PATtuple_739_1_CH8.root",
sampleBaseDir+"PATtuple_73_1_u8H.root",
sampleBaseDir+"PATtuple_740_1_BKz.root",
sampleBaseDir+"PATtuple_741_1_dWW.root",
sampleBaseDir+"PATtuple_742_1_sM0.root",
sampleBaseDir+"PATtuple_743_1_K8s.root",
sampleBaseDir+"PATtuple_744_1_Dyt.root",
sampleBaseDir+"PATtuple_745_1_sTy.root",
sampleBaseDir+"PATtuple_746_2_q2N.root",
sampleBaseDir+"PATtuple_746_3_MwZ.root",
sampleBaseDir+"PATtuple_747_1_Ct5.root",
sampleBaseDir+"PATtuple_748_1_D52.root",
sampleBaseDir+"PATtuple_749_1_cFH.root",
sampleBaseDir+"PATtuple_74_1_nCJ.root",
sampleBaseDir+"PATtuple_750_1_RZW.root",
sampleBaseDir+"PATtuple_751_1_TWT.root",
sampleBaseDir+"PATtuple_752_1_8Te.root",
sampleBaseDir+"PATtuple_75_1_ObB.root",
sampleBaseDir+"PATtuple_76_1_NMy.root",
sampleBaseDir+"PATtuple_77_1_TO4.root",
sampleBaseDir+"PATtuple_78_1_06A.root",
sampleBaseDir+"PATtuple_79_1_Xfl.root",
sampleBaseDir+"PATtuple_7_1_UxQ.root",
sampleBaseDir+"PATtuple_80_1_yIg.root",
sampleBaseDir+"PATtuple_81_1_nLX.root",
sampleBaseDir+"PATtuple_82_2_NvI.root",
sampleBaseDir+"PATtuple_83_2_w73.root",
sampleBaseDir+"PATtuple_84_2_EgT.root",
sampleBaseDir+"PATtuple_85_2_dvo.root",
sampleBaseDir+"PATtuple_86_2_iYb.root",
sampleBaseDir+"PATtuple_87_3_7pm.root",
sampleBaseDir+"PATtuple_88_2_oMq.root",
sampleBaseDir+"PATtuple_89_1_g4B.root",
sampleBaseDir+"PATtuple_8_1_Wu8.root",
sampleBaseDir+"PATtuple_90_1_gas.root",
sampleBaseDir+"PATtuple_91_1_030.root",
sampleBaseDir+"PATtuple_92_1_eGM.root",
sampleBaseDir+"PATtuple_93_1_qkX.root",
sampleBaseDir+"PATtuple_94_1_Lfr.root",
sampleBaseDir+"PATtuple_95_1_u9L.root",
sampleBaseDir+"PATtuple_96_1_kMe.root",
sampleBaseDir+"PATtuple_97_1_AeU.root",
sampleBaseDir+"PATtuple_98_1_cVt.root",
sampleBaseDir+"PATtuple_99_1_kuD.root",
sampleBaseDir+"PATtuple_9_1_LlM.root",
]
