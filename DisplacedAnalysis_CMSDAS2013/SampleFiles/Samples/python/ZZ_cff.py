sampleDataSet = '/ZZ_TuneZ2star_8TeV_pythia6_tauola/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM'  

sampleCMSEnergy = 8000

sampleRelease = "CMSSW_5_3_2_patch4" # original (i.e. RECO file) release, not the one we plan to process them with
sampleProcessRelease = "CMSSW_5_3_5" # release used to create new files with

sampleNumEvents = 9799908

sampleXSec = 8.3;

# global tag can be extracted from file using edmProvDump filename|grep globaltag
# note however that this is the tag for *further* processing, not the original tag
sampleGlobalTag = 'START53_V7F::All'

sampleDuplicateCheckMode = 'checkAllFilesOpened'

sampleType = "BKGMC"

samplePatDBSName="/ZZ_TuneZ2star_8TeV_pythia6_tauola/demattia-ZZ_pat_20121107-5b849df0084f9d2351a5ea462097a0b5/USER"

sampleBaseDir="root://eoscms//eos/cms///store/caf/user/ejclemen//ZZ_pat_20120726/ejclemen/ZZ_TuneZ2star_8TeV_pythia6_tauola/ZZ_pat_20120726/d0bbde228835224f42d621e7d54b0549/"

samplePatFiles = [
sampleBaseDir+"PATtuple_100_1_I5O.root",
sampleBaseDir+"PATtuple_101_1_dKO.root",
sampleBaseDir+"PATtuple_102_1_9RB.root",
sampleBaseDir+"PATtuple_103_1_Xcu.root",
sampleBaseDir+"PATtuple_104_1_S0E.root",
sampleBaseDir+"PATtuple_105_1_xky.root",
sampleBaseDir+"PATtuple_106_1_63q.root",
sampleBaseDir+"PATtuple_107_1_tmB.root",
sampleBaseDir+"PATtuple_108_1_VMw.root",
sampleBaseDir+"PATtuple_109_1_jHR.root",
sampleBaseDir+"PATtuple_10_1_6Br.root",
sampleBaseDir+"PATtuple_110_1_07D.root",
sampleBaseDir+"PATtuple_111_1_zQc.root",
sampleBaseDir+"PATtuple_116_1_IZV.root",
sampleBaseDir+"PATtuple_117_1_WcB.root",
sampleBaseDir+"PATtuple_119_1_D43.root",
sampleBaseDir+"PATtuple_11_1_G1q.root",
sampleBaseDir+"PATtuple_121_1_ChD.root",
sampleBaseDir+"PATtuple_123_1_28w.root",
sampleBaseDir+"PATtuple_12_1_wnR.root",
sampleBaseDir+"PATtuple_133_1_anB.root",
sampleBaseDir+"PATtuple_136_1_bEx.root",
sampleBaseDir+"PATtuple_138_1_6aD.root",
sampleBaseDir+"PATtuple_139_1_dho.root",
sampleBaseDir+"PATtuple_13_1_1OV.root",
sampleBaseDir+"PATtuple_140_1_3gd.root",
sampleBaseDir+"PATtuple_142_1_Eh7.root",
sampleBaseDir+"PATtuple_148_1_ChX.root",
sampleBaseDir+"PATtuple_14_1_TDC.root",
sampleBaseDir+"PATtuple_150_1_bLr.root",
sampleBaseDir+"PATtuple_152_1_mnM.root",
sampleBaseDir+"PATtuple_154_1_gHg.root",
sampleBaseDir+"PATtuple_155_1_1Gp.root",
sampleBaseDir+"PATtuple_158_1_HST.root",
sampleBaseDir+"PATtuple_159_1_AWf.root",
sampleBaseDir+"PATtuple_15_1_a94.root",
sampleBaseDir+"PATtuple_161_1_TfD.root",
sampleBaseDir+"PATtuple_163_1_8CS.root",
sampleBaseDir+"PATtuple_165_1_emi.root",
sampleBaseDir+"PATtuple_166_1_tlE.root",
sampleBaseDir+"PATtuple_16_1_KI5.root",
sampleBaseDir+"PATtuple_170_1_lie.root",
sampleBaseDir+"PATtuple_173_1_1rE.root",
sampleBaseDir+"PATtuple_174_1_m4l.root",
sampleBaseDir+"PATtuple_176_1_soI.root",
sampleBaseDir+"PATtuple_177_1_XD5.root",
sampleBaseDir+"PATtuple_179_1_U90.root",
sampleBaseDir+"PATtuple_17_1_psI.root",
sampleBaseDir+"PATtuple_180_1_Gan.root",
sampleBaseDir+"PATtuple_182_1_fTp.root",
sampleBaseDir+"PATtuple_184_1_fJq.root",
sampleBaseDir+"PATtuple_187_1_dKp.root",
sampleBaseDir+"PATtuple_188_1_mpt.root",
sampleBaseDir+"PATtuple_191_1_UB6.root",
sampleBaseDir+"PATtuple_192_1_btv.root",
sampleBaseDir+"PATtuple_194_1_XZU.root",
sampleBaseDir+"PATtuple_19_1_lCE.root",
sampleBaseDir+"PATtuple_203_1_qkh.root",
sampleBaseDir+"PATtuple_204_1_gYD.root",
sampleBaseDir+"PATtuple_206_1_NkX.root",
sampleBaseDir+"PATtuple_207_1_mQs.root",
sampleBaseDir+"PATtuple_20_1_HIC.root",
sampleBaseDir+"PATtuple_210_1_82n.root",
sampleBaseDir+"PATtuple_211_1_RTd.root",
sampleBaseDir+"PATtuple_212_1_OcQ.root",
sampleBaseDir+"PATtuple_215_1_EJX.root",
sampleBaseDir+"PATtuple_219_1_NUR.root",
sampleBaseDir+"PATtuple_21_1_ZXL.root",
sampleBaseDir+"PATtuple_221_1_tew.root",
sampleBaseDir+"PATtuple_222_1_QT3.root",
sampleBaseDir+"PATtuple_22_1_snA.root",
sampleBaseDir+"PATtuple_236_1_V6M.root",
sampleBaseDir+"PATtuple_24_1_AWU.root",
sampleBaseDir+"PATtuple_251_1_nIt.root",
sampleBaseDir+"PATtuple_25_1_Caj.root",
sampleBaseDir+"PATtuple_266_1_BTw.root",
sampleBaseDir+"PATtuple_27_1_SeK.root",
sampleBaseDir+"PATtuple_28_1_C7w.root",
sampleBaseDir+"PATtuple_29_1_qvX.root",
sampleBaseDir+"PATtuple_2_1_xyR.root",
sampleBaseDir+"PATtuple_30_1_cii.root",
sampleBaseDir+"PATtuple_31_1_y1r.root",
sampleBaseDir+"PATtuple_32_1_T1L.root",
sampleBaseDir+"PATtuple_34_1_ChR.root",
sampleBaseDir+"PATtuple_35_1_mVq.root",
sampleBaseDir+"PATtuple_36_1_dqb.root",
sampleBaseDir+"PATtuple_37_1_cx9.root",
sampleBaseDir+"PATtuple_38_1_nwX.root",
sampleBaseDir+"PATtuple_39_1_okj.root",
sampleBaseDir+"PATtuple_3_1_VrA.root",
sampleBaseDir+"PATtuple_40_1_ntj.root",
sampleBaseDir+"PATtuple_41_1_flR.root",
sampleBaseDir+"PATtuple_42_1_TUj.root",
sampleBaseDir+"PATtuple_43_1_u8y.root",
sampleBaseDir+"PATtuple_44_1_8Oz.root",
sampleBaseDir+"PATtuple_48_1_NY6.root",
sampleBaseDir+"PATtuple_49_1_qXF.root",
sampleBaseDir+"PATtuple_4_1_zGg.root",
sampleBaseDir+"PATtuple_50_1_u7B.root",
sampleBaseDir+"PATtuple_51_1_4qQ.root",
sampleBaseDir+"PATtuple_54_1_Gow.root",
sampleBaseDir+"PATtuple_55_1_g18.root",
sampleBaseDir+"PATtuple_56_1_iyW.root",
sampleBaseDir+"PATtuple_57_1_i2H.root",
sampleBaseDir+"PATtuple_5_1_wNG.root",
sampleBaseDir+"PATtuple_62_1_o9d.root",
sampleBaseDir+"PATtuple_66_1_uMF.root",
sampleBaseDir+"PATtuple_67_1_jNh.root",
sampleBaseDir+"PATtuple_68_1_yva.root",
sampleBaseDir+"PATtuple_70_1_XuK.root",
sampleBaseDir+"PATtuple_71_1_Wi7.root",
sampleBaseDir+"PATtuple_72_1_jzR.root",
sampleBaseDir+"PATtuple_73_1_kR0.root",
sampleBaseDir+"PATtuple_74_1_EBy.root",
sampleBaseDir+"PATtuple_75_1_dbY.root",
sampleBaseDir+"PATtuple_76_1_Osb.root",
sampleBaseDir+"PATtuple_77_1_BPO.root",
sampleBaseDir+"PATtuple_78_1_03f.root",
sampleBaseDir+"PATtuple_79_1_gNp.root",
sampleBaseDir+"PATtuple_7_1_9DP.root",
sampleBaseDir+"PATtuple_80_1_pkI.root",
sampleBaseDir+"PATtuple_81_1_Zev.root",
sampleBaseDir+"PATtuple_82_1_R3m.root",
sampleBaseDir+"PATtuple_83_1_aL8.root",
sampleBaseDir+"PATtuple_84_1_YjU.root",
sampleBaseDir+"PATtuple_85_1_eOq.root",
sampleBaseDir+"PATtuple_86_1_i79.root",
sampleBaseDir+"PATtuple_87_1_Kph.root",
sampleBaseDir+"PATtuple_88_1_XEG.root",
sampleBaseDir+"PATtuple_8_1_ZOI.root",
sampleBaseDir+"PATtuple_90_1_HT6.root",
sampleBaseDir+"PATtuple_91_1_39b.root",
sampleBaseDir+"PATtuple_95_1_h9D.root",
sampleBaseDir+"PATtuple_96_1_LH2.root",
sampleBaseDir+"PATtuple_97_1_cha.root",
sampleBaseDir+"PATtuple_98_1_54F.root",
sampleBaseDir+"PATtuple_99_1_pGg.root",
sampleBaseDir+"PATtuple_9_1_04k.root",
sampleBaseDir+"",
sampleBaseDir+"PATtuple_243_1_gSL.root",
sampleBaseDir+"PATtuple_244_1_oF6.root",
sampleBaseDir+"PATtuple_246_1_HHF.root",
sampleBaseDir+"PATtuple_248_1_k3p.root",
sampleBaseDir+"PATtuple_249_1_sNS.root",
sampleBaseDir+"PATtuple_24_0_49A.root",
sampleBaseDir+"PATtuple_250_1_5xu.root",
sampleBaseDir+"PATtuple_251_1_H20.root",
sampleBaseDir+"PATtuple_252_1_34t.root",
sampleBaseDir+"PATtuple_253_1_BcB.root",
sampleBaseDir+"PATtuple_254_1_LGz.root",
sampleBaseDir+"PATtuple_255_1_BXf.root",
sampleBaseDir+"PATtuple_256_1_yGo.root",
sampleBaseDir+"PATtuple_257_1_SYU.root",
sampleBaseDir+"PATtuple_258_1_RAP.root",
sampleBaseDir+"PATtuple_259_1_2Mh.root",
sampleBaseDir+"PATtuple_25_0_CyC.root",
sampleBaseDir+"PATtuple_260_1_bMH.root",
sampleBaseDir+"PATtuple_261_1_PUz.root",
sampleBaseDir+"PATtuple_262_1_vP9.root",
sampleBaseDir+"PATtuple_263_1_bsI.root",
sampleBaseDir+"PATtuple_264_1_gxD.root",
sampleBaseDir+"PATtuple_265_1_G9G.root",
sampleBaseDir+"PATtuple_266_1_TTK.root",
sampleBaseDir+"PATtuple_267_1_rvI.root",
sampleBaseDir+"PATtuple_268_1_dad.root",
sampleBaseDir+"PATtuple_269_1_3ic.root",
sampleBaseDir+"PATtuple_26_0_G9C.root",
sampleBaseDir+"PATtuple_270_1_Y32.root",
sampleBaseDir+"PATtuple_271_1_cyj.root",
sampleBaseDir+"PATtuple_272_1_IJF.root",
sampleBaseDir+"PATtuple_273_1_F7Y.root",
sampleBaseDir+"PATtuple_274_1_nLU.root",
sampleBaseDir+"PATtuple_275_1_QBw.root",
sampleBaseDir+"PATtuple_276_1_Y4L.root",
sampleBaseDir+"PATtuple_277_1_tg2.root",
sampleBaseDir+"PATtuple_278_1_Wyg.root",
sampleBaseDir+"PATtuple_279_1_55Z.root",
sampleBaseDir+"PATtuple_27_0_Qn8.root",
sampleBaseDir+"PATtuple_280_1_Vgh.root",
sampleBaseDir+"PATtuple_281_1_03n.root",
sampleBaseDir+"PATtuple_282_1_0jw.root",
sampleBaseDir+"PATtuple_283_1_Of4.root",
sampleBaseDir+"PATtuple_284_0_uMF.root",
sampleBaseDir+"PATtuple_286_0_XzG.root",
sampleBaseDir+"PATtuple_287_0_AFC.root",
sampleBaseDir+"PATtuple_288_0_x1a.root",
sampleBaseDir+"PATtuple_289_0_OIK.root",
sampleBaseDir+"PATtuple_28_0_UFx.root",
sampleBaseDir+"PATtuple_290_0_Dw3.root",
sampleBaseDir+"PATtuple_291_0_r92.root",
sampleBaseDir+"PATtuple_292_0_LGy.root",
sampleBaseDir+"PATtuple_293_0_AjR.root",
sampleBaseDir+"PATtuple_294_0_334.root",
sampleBaseDir+"PATtuple_295_0_BIZ.root",
sampleBaseDir+"PATtuple_296_0_xH4.root",
sampleBaseDir+"PATtuple_297_0_9V6.root",
sampleBaseDir+"PATtuple_298_0_nAn.root",
sampleBaseDir+"PATtuple_299_0_6lN.root",
sampleBaseDir+"PATtuple_29_0_ZeK.root",
sampleBaseDir+"PATtuple_2_0_cNt.root",
sampleBaseDir+"PATtuple_300_0_jJ0.root",
sampleBaseDir+"PATtuple_301_0_nAI.root",
sampleBaseDir+"PATtuple_302_0_4Qu.root",
sampleBaseDir+"PATtuple_303_0_duO.root",
sampleBaseDir+"PATtuple_304_0_OfL.root",
sampleBaseDir+"PATtuple_305_0_a5l.root",
sampleBaseDir+"PATtuple_306_0_sZb.root",
sampleBaseDir+"PATtuple_307_0_lGP.root",
sampleBaseDir+"PATtuple_30_0_Slz.root",
sampleBaseDir+"PATtuple_311_0_70Y.root",
sampleBaseDir+"PATtuple_315_0_yqO.root",
sampleBaseDir+"PATtuple_316_0_LnU.root",
sampleBaseDir+"PATtuple_317_0_6mw.root",
sampleBaseDir+"PATtuple_318_0_kIQ.root",
sampleBaseDir+"PATtuple_319_0_YWg.root",
sampleBaseDir+"PATtuple_320_0_prm.root",
sampleBaseDir+"PATtuple_321_0_5RX.root",
sampleBaseDir+"PATtuple_322_0_Tsn.root",
sampleBaseDir+"PATtuple_323_0_QCt.root",
sampleBaseDir+"PATtuple_324_0_fHK.root",
sampleBaseDir+"PATtuple_325_0_vsc.root",
sampleBaseDir+"PATtuple_329_0_0VX.root",
sampleBaseDir+"PATtuple_32_0_iNM.root",
sampleBaseDir+"PATtuple_330_0_uZe.root",
sampleBaseDir+"PATtuple_333_0_QVr.root",
sampleBaseDir+"PATtuple_334_0_3vL.root",
sampleBaseDir+"PATtuple_337_0_7N0.root",
sampleBaseDir+"PATtuple_338_0_Fta.root",
sampleBaseDir+"PATtuple_339_0_s6o.root",
sampleBaseDir+"PATtuple_33_0_TEE.root",
sampleBaseDir+"PATtuple_340_0_yPT.root",
sampleBaseDir+"PATtuple_344_0_TQ6.root",
sampleBaseDir+"PATtuple_348_0_9Nl.root",
sampleBaseDir+"PATtuple_349_0_hcl.root",
sampleBaseDir+"PATtuple_34_0_QAJ.root",
sampleBaseDir+"PATtuple_354_0_BfF.root",
sampleBaseDir+"PATtuple_357_0_dK6.root",
sampleBaseDir+"PATtuple_358_0_lyZ.root",
sampleBaseDir+"PATtuple_35_0_RIo.root",
sampleBaseDir+"PATtuple_360_0_XJJ.root",
sampleBaseDir+"PATtuple_361_0_eUE.root",
sampleBaseDir+"PATtuple_362_0_vqr.root",
sampleBaseDir+"PATtuple_363_0_9my.root",
sampleBaseDir+"PATtuple_364_0_jd2.root",
sampleBaseDir+"PATtuple_365_0_PpP.root",
sampleBaseDir+"PATtuple_366_0_Sgu.root",
sampleBaseDir+"PATtuple_367_0_jYD.root",
sampleBaseDir+"PATtuple_36_0_p8y.root",
sampleBaseDir+"PATtuple_372_0_l1j.root",
sampleBaseDir+"PATtuple_373_0_OWi.root",
sampleBaseDir+"PATtuple_374_0_OAG.root",
sampleBaseDir+"PATtuple_375_0_65G.root",
sampleBaseDir+"PATtuple_376_0_K5k.root",
sampleBaseDir+"PATtuple_378_0_NY0.root",
sampleBaseDir+"PATtuple_379_0_VZh.root",
sampleBaseDir+"PATtuple_37_0_Oxc.root",
sampleBaseDir+"PATtuple_381_0_cyG.root",
sampleBaseDir+"PATtuple_382_0_ofb.root",
sampleBaseDir+"PATtuple_389_0_8wH.root",
sampleBaseDir+"PATtuple_38_0_lqu.root",
sampleBaseDir+"PATtuple_391_0_xtO.root",
sampleBaseDir+"PATtuple_393_0_M7B.root",
sampleBaseDir+"PATtuple_394_0_9an.root",
sampleBaseDir+"PATtuple_395_0_B8Z.root",
sampleBaseDir+"PATtuple_396_0_uQr.root",
sampleBaseDir+"PATtuple_397_0_qs6.root",
sampleBaseDir+"PATtuple_398_0_j75.root",
sampleBaseDir+"PATtuple_399_0_BCD.root",
sampleBaseDir+"PATtuple_39_0_fKP.root",
sampleBaseDir+"PATtuple_400_0_R0O.root",
sampleBaseDir+"PATtuple_401_0_n8l.root",
sampleBaseDir+"PATtuple_402_0_PS7.root",
sampleBaseDir+"PATtuple_404_0_0lj.root",
sampleBaseDir+"PATtuple_405_0_PS2.root",
sampleBaseDir+"PATtuple_407_0_kpo.root",
sampleBaseDir+"PATtuple_408_0_f8i.root",
sampleBaseDir+"PATtuple_409_0_lQb.root",
sampleBaseDir+"PATtuple_40_0_5bB.root",
sampleBaseDir+"PATtuple_410_0_NiW.root",
sampleBaseDir+"PATtuple_411_0_KY4.root",
sampleBaseDir+"PATtuple_412_0_QAW.root",
sampleBaseDir+"PATtuple_413_0_PfE.root",
sampleBaseDir+"PATtuple_414_0_Qz4.root",
sampleBaseDir+"PATtuple_415_0_usn.root",
sampleBaseDir+"PATtuple_416_0_hSK.root",
sampleBaseDir+"PATtuple_41_0_awc.root",
sampleBaseDir+"PATtuple_422_0_xtM.root",
sampleBaseDir+"PATtuple_426_0_jz8.root",
sampleBaseDir+"PATtuple_429_0_cpf.root",
sampleBaseDir+"PATtuple_42_0_UNi.root",
sampleBaseDir+"PATtuple_432_0_s9b.root",
sampleBaseDir+"PATtuple_434_0_2xw.root",
sampleBaseDir+"PATtuple_436_0_eTb.root",
sampleBaseDir+"PATtuple_438_0_Z18.root",
sampleBaseDir+"PATtuple_439_0_NjG.root",
sampleBaseDir+"PATtuple_43_0_pvW.root",
sampleBaseDir+"PATtuple_443_0_0ca.root",
sampleBaseDir+"PATtuple_444_0_nsD.root",
sampleBaseDir+"PATtuple_445_0_xiu.root",
sampleBaseDir+"PATtuple_446_0_BOj.root",
sampleBaseDir+"PATtuple_447_0_Odg.root",
sampleBaseDir+"PATtuple_448_0_uvo.root",
sampleBaseDir+"PATtuple_449_0_dUq.root",
sampleBaseDir+"PATtuple_450_0_ItW.root",
sampleBaseDir+"PATtuple_451_0_Gof.root",
sampleBaseDir+"PATtuple_452_0_kCJ.root",
sampleBaseDir+"PATtuple_453_0_KMU.root",
sampleBaseDir+"PATtuple_454_0_WA1.root",
sampleBaseDir+"PATtuple_455_0_wKm.root",
sampleBaseDir+"PATtuple_456_0_ANh.root",
sampleBaseDir+"PATtuple_45_0_Num.root",
sampleBaseDir+"PATtuple_46_0_uOB.root",
sampleBaseDir+"PATtuple_47_0_Nbk.root",
sampleBaseDir+"PATtuple_48_0_uEY.root",
sampleBaseDir+"PATtuple_493_0_u1Y.root",
sampleBaseDir+"PATtuple_49_0_LjK.root",
sampleBaseDir+"PATtuple_4_0_xDi.root",
sampleBaseDir+"PATtuple_506_0_GsB.root",
sampleBaseDir+"PATtuple_509_0_vQd.root",
sampleBaseDir+"PATtuple_50_0_jla.root",
sampleBaseDir+"PATtuple_510_0_c96.root",
sampleBaseDir+"PATtuple_511_0_Qag.root",
sampleBaseDir+"PATtuple_512_0_4OD.root",
sampleBaseDir+"PATtuple_513_0_4sY.root",
sampleBaseDir+"PATtuple_514_0_tqz.root",
sampleBaseDir+"PATtuple_515_0_275.root",
sampleBaseDir+"PATtuple_516_0_xYx.root",
sampleBaseDir+"PATtuple_517_0_nlo.root",
sampleBaseDir+"PATtuple_518_0_uzE.root",
sampleBaseDir+"PATtuple_519_0_dP2.root",
sampleBaseDir+"PATtuple_51_0_9xO.root",
sampleBaseDir+"PATtuple_520_0_f6A.root",
sampleBaseDir+"PATtuple_521_0_10a.root",
sampleBaseDir+"PATtuple_522_0_wNk.root",
sampleBaseDir+"PATtuple_523_0_HxC.root",
sampleBaseDir+"PATtuple_524_0_Bc2.root",
sampleBaseDir+"PATtuple_525_0_wHd.root",
sampleBaseDir+"PATtuple_526_0_sTO.root",
sampleBaseDir+"PATtuple_527_0_NmT.root",
sampleBaseDir+"PATtuple_528_0_w85.root",
sampleBaseDir+"PATtuple_529_0_e1L.root",
sampleBaseDir+"PATtuple_52_0_h4h.root",
sampleBaseDir+"PATtuple_530_0_bHF.root",
sampleBaseDir+"PATtuple_531_0_a4m.root",
sampleBaseDir+"PATtuple_532_0_xdk.root",
sampleBaseDir+"PATtuple_533_0_7Az.root",
sampleBaseDir+"PATtuple_534_0_Go6.root",
sampleBaseDir+"PATtuple_535_0_9NV.root",
sampleBaseDir+"PATtuple_536_0_Ajg.root",
sampleBaseDir+"PATtuple_537_0_Q6R.root",
sampleBaseDir+"PATtuple_538_0_d72.root",
sampleBaseDir+"PATtuple_539_0_MQ5.root",
sampleBaseDir+"PATtuple_53_0_Rrh.root",
sampleBaseDir+"PATtuple_540_0_aJz.root",
sampleBaseDir+"PATtuple_541_0_oQ4.root",
sampleBaseDir+"PATtuple_542_0_uYv.root",
sampleBaseDir+"PATtuple_543_0_CNG.root",
sampleBaseDir+"PATtuple_544_0_VVS.root",
sampleBaseDir+"PATtuple_545_0_XkN.root",
sampleBaseDir+"PATtuple_546_0_nKH.root",
sampleBaseDir+"PATtuple_54_0_sSD.root",
sampleBaseDir+"PATtuple_55_0_6Yo.root",
sampleBaseDir+"PATtuple_56_0_MTz.root",
sampleBaseDir+"PATtuple_58_0_2en.root",
sampleBaseDir+"PATtuple_59_0_Bvj.root",
sampleBaseDir+"PATtuple_5_0_AEd.root",
sampleBaseDir+"PATtuple_604_0_DuJ.root",
sampleBaseDir+"PATtuple_605_0_VIb.root",
sampleBaseDir+"PATtuple_606_0_PtA.root",
sampleBaseDir+"PATtuple_608_0_lTa.root",
sampleBaseDir+"PATtuple_609_0_4Zy.root",
sampleBaseDir+"PATtuple_60_0_aap.root",
sampleBaseDir+"PATtuple_610_0_h7F.root",
sampleBaseDir+"PATtuple_611_0_yvI.root",
sampleBaseDir+"PATtuple_612_0_lMS.root",
sampleBaseDir+"PATtuple_613_0_vV4.root",
sampleBaseDir+"PATtuple_615_0_qxl.root",
sampleBaseDir+"PATtuple_616_0_HRi.root",
sampleBaseDir+"PATtuple_618_0_PSa.root",
sampleBaseDir+"PATtuple_619_0_fTK.root",
sampleBaseDir+"PATtuple_61_0_Xgp.root",
sampleBaseDir+"PATtuple_621_0_Udl.root",
sampleBaseDir+"PATtuple_622_0_CyQ.root",
sampleBaseDir+"PATtuple_625_0_5ow.root",
sampleBaseDir+"PATtuple_626_0_I7t.root",
sampleBaseDir+"PATtuple_62_0_Edy.root",
sampleBaseDir+"PATtuple_632_0_UeT.root",
sampleBaseDir+"PATtuple_634_0_5SU.root",
sampleBaseDir+"PATtuple_636_0_wLv.root",
sampleBaseDir+"PATtuple_639_0_jyN.root",
sampleBaseDir+"PATtuple_63_0_2xY.root",
sampleBaseDir+"PATtuple_640_0_EnS.root",
sampleBaseDir+"PATtuple_641_0_JCP.root",
sampleBaseDir+"PATtuple_642_0_ifQ.root",
sampleBaseDir+"PATtuple_644_0_W2u.root",
sampleBaseDir+"PATtuple_645_0_7Px.root",
sampleBaseDir+"PATtuple_647_0_pGC.root",
sampleBaseDir+"PATtuple_649_0_J1J.root",
sampleBaseDir+"PATtuple_64_0_fwf.root",
sampleBaseDir+"PATtuple_652_0_Hmq.root",
sampleBaseDir+"PATtuple_654_0_y6U.root",
sampleBaseDir+"PATtuple_655_0_RAe.root",
sampleBaseDir+"PATtuple_656_0_tb4.root",
sampleBaseDir+"PATtuple_658_0_MFt.root",
sampleBaseDir+"PATtuple_65_0_l4x.root",
sampleBaseDir+"PATtuple_660_0_OvR.root",
sampleBaseDir+"PATtuple_661_0_Rz5.root",
sampleBaseDir+"PATtuple_663_0_b57.root",
sampleBaseDir+"PATtuple_66_0_1Ls.root",
sampleBaseDir+"PATtuple_670_0_E1p.root",
sampleBaseDir+"PATtuple_672_0_1bf.root",
sampleBaseDir+"PATtuple_674_0_mZs.root",
sampleBaseDir+"PATtuple_684_0_j04.root",
sampleBaseDir+"PATtuple_687_0_aaI.root",
sampleBaseDir+"PATtuple_688_0_QO9.root",
sampleBaseDir+"PATtuple_689_0_oS4.root",
sampleBaseDir+"PATtuple_690_0_Jci.root",
sampleBaseDir+"PATtuple_691_0_fIJ.root",
sampleBaseDir+"PATtuple_692_0_qub.root",
sampleBaseDir+"PATtuple_69_0_o04.root",
sampleBaseDir+"PATtuple_6_0_E7A.root",
sampleBaseDir+"PATtuple_70_0_pl0.root",
sampleBaseDir+"PATtuple_71_0_Qig.root",
sampleBaseDir+"PATtuple_72_0_zvJ.root",
sampleBaseDir+"PATtuple_74_0_eDD.root",
sampleBaseDir+"PATtuple_76_0_esP.root",
sampleBaseDir+"PATtuple_77_0_lBw.root",
sampleBaseDir+"PATtuple_78_0_qBP.root",
sampleBaseDir+"PATtuple_79_0_dW5.root",
sampleBaseDir+"PATtuple_7_0_EHF.root",
sampleBaseDir+"PATtuple_80_0_e7i.root",
sampleBaseDir+"PATtuple_81_0_9Xl.root",
sampleBaseDir+"PATtuple_82_0_6K9.root",
sampleBaseDir+"PATtuple_83_0_nXT.root",
sampleBaseDir+"PATtuple_84_0_kxR.root",
sampleBaseDir+"PATtuple_85_0_yzs.root",
sampleBaseDir+"PATtuple_86_0_VmM.root",
sampleBaseDir+"PATtuple_87_0_mGZ.root",
sampleBaseDir+"PATtuple_88_0_zsU.root",
sampleBaseDir+"PATtuple_89_0_aaf.root",
sampleBaseDir+"PATtuple_8_0_5ry.root",
sampleBaseDir+"PATtuple_90_0_puA.root",
sampleBaseDir+"PATtuple_91_0_bi9.root",
sampleBaseDir+"PATtuple_92_0_hTV.root",
sampleBaseDir+"PATtuple_93_0_Bbg.root",
sampleBaseDir+"PATtuple_94_0_448.root",
sampleBaseDir+"PATtuple_95_0_Mpb.root",
sampleBaseDir+"PATtuple_96_1_OE9.root",
sampleBaseDir+"PATtuple_98_1_erJ.root",
sampleBaseDir+"PATtuple_99_1_LVQ.root",
sampleBaseDir+"PATtuple_9_0_deO.root",
sampleBaseDir+"PATtuple_568_1_8MI.root",
sampleBaseDir+"PATtuple_569_1_CxP.root",
sampleBaseDir+"PATtuple_56_1_58h.root",
sampleBaseDir+"PATtuple_570_1_9RP.root",
sampleBaseDir+"PATtuple_571_2_ifG.root",
sampleBaseDir+"PATtuple_572_1_Iuz.root",
sampleBaseDir+"PATtuple_573_1_m68.root",
sampleBaseDir+"PATtuple_574_1_e82.root",
sampleBaseDir+"PATtuple_575_1_TZw.root",
sampleBaseDir+"PATtuple_576_1_bwB.root",
sampleBaseDir+"PATtuple_577_1_F9v.root",
sampleBaseDir+"PATtuple_578_1_hrk.root",
sampleBaseDir+"PATtuple_579_1_tu1.root",
sampleBaseDir+"PATtuple_57_1_jxh.root",
sampleBaseDir+"PATtuple_580_1_GvP.root",
sampleBaseDir+"PATtuple_581_1_KmW.root",
sampleBaseDir+"PATtuple_582_1_K8t.root",
sampleBaseDir+"PATtuple_583_1_Z0Z.root",
sampleBaseDir+"PATtuple_584_1_CN1.root",
sampleBaseDir+"PATtuple_585_1_7XG.root",
sampleBaseDir+"PATtuple_586_1_GBr.root",
sampleBaseDir+"PATtuple_587_1_g2G.root",
sampleBaseDir+"",
sampleBaseDir+"",
sampleBaseDir+"PATtuple_589_1_jHJ.root",
sampleBaseDir+"PATtuple_58_1_2zM.root",
sampleBaseDir+"PATtuple_590_1_zdk.root",
sampleBaseDir+"PATtuple_592_1_2ci.root",
sampleBaseDir+"PATtuple_593_1_CcB.root",
sampleBaseDir+"PATtuple_594_1_uvZ.root",
sampleBaseDir+"PATtuple_595_1_GIw.root",
sampleBaseDir+"PATtuple_596_1_CU5.root",
sampleBaseDir+"PATtuple_597_1_BJ3.root",
sampleBaseDir+"PATtuple_598_1_N7q.root",
sampleBaseDir+"PATtuple_599_1_Ogl.root",
sampleBaseDir+"PATtuple_59_1_lAg.root",
sampleBaseDir+"PATtuple_5_1_QPe.root",
sampleBaseDir+"PATtuple_600_1_DlY.root",
sampleBaseDir+"PATtuple_601_1_4MD.root",
sampleBaseDir+"PATtuple_602_1_YxY.root",
sampleBaseDir+"PATtuple_603_1_tfy.root",
sampleBaseDir+"PATtuple_604_1_VzG.root",
sampleBaseDir+"PATtuple_605_1_k8N.root",
sampleBaseDir+"PATtuple_606_1_cfB.root",
sampleBaseDir+"PATtuple_607_1_vPP.root",
sampleBaseDir+"PATtuple_608_1_n5I.root",
sampleBaseDir+"PATtuple_609_1_Psv.root",
sampleBaseDir+"PATtuple_60_1_qnS.root",
sampleBaseDir+"PATtuple_611_1_Nvc.root",
sampleBaseDir+"PATtuple_612_1_zeW.root",
sampleBaseDir+"PATtuple_613_1_40t.root",
sampleBaseDir+"PATtuple_614_1_4zD.root",
sampleBaseDir+"PATtuple_615_1_kzP.root",
sampleBaseDir+"PATtuple_616_1_mrH.root",
sampleBaseDir+"PATtuple_617_1_T06.root",
sampleBaseDir+"PATtuple_618_1_vd7.root",
sampleBaseDir+"PATtuple_619_1_571.root",
sampleBaseDir+"PATtuple_61_1_t6v.root",
sampleBaseDir+"PATtuple_620_1_lCO.root",
sampleBaseDir+"PATtuple_621_1_b15.root",
sampleBaseDir+"PATtuple_622_1_yM7.root",
sampleBaseDir+"PATtuple_623_1_8WO.root",
sampleBaseDir+"PATtuple_624_1_Xzh.root",
sampleBaseDir+"PATtuple_625_1_HMO.root",
sampleBaseDir+"PATtuple_626_1_Ucu.root",
sampleBaseDir+"PATtuple_627_1_zNG.root",
sampleBaseDir+"PATtuple_628_1_VlM.root",
sampleBaseDir+"PATtuple_629_1_ROI.root",
sampleBaseDir+"PATtuple_62_1_Euc.root",
sampleBaseDir+"PATtuple_630_1_77v.root",
sampleBaseDir+"PATtuple_631_1_zzP.root",
sampleBaseDir+"PATtuple_632_1_oDK.root",
sampleBaseDir+"PATtuple_633_1_psD.root",
sampleBaseDir+"PATtuple_634_1_RqO.root",
sampleBaseDir+"PATtuple_635_1_H9o.root",
sampleBaseDir+"PATtuple_636_1_9vo.root",
sampleBaseDir+"PATtuple_637_1_lWE.root",
sampleBaseDir+"PATtuple_638_1_SNy.root",
sampleBaseDir+"PATtuple_639_1_tRO.root",
sampleBaseDir+"PATtuple_63_1_SoK.root",
sampleBaseDir+"PATtuple_640_1_ixe.root",
sampleBaseDir+"PATtuple_641_1_Vuj.root",
sampleBaseDir+"PATtuple_642_1_EQw.root",
sampleBaseDir+"PATtuple_643_1_9gE.root",
sampleBaseDir+"PATtuple_644_1_F0v.root",
sampleBaseDir+"PATtuple_645_1_riU.root",
sampleBaseDir+"PATtuple_646_1_OaL.root",
sampleBaseDir+"PATtuple_647_1_gUP.root",
sampleBaseDir+"PATtuple_648_1_vT2.root",
sampleBaseDir+"PATtuple_649_2_zqU.root",
sampleBaseDir+"PATtuple_64_1_K6X.root",
sampleBaseDir+"PATtuple_650_1_LLj.root",
sampleBaseDir+"PATtuple_651_1_4wH.root",
sampleBaseDir+"PATtuple_652_1_d59.root",
sampleBaseDir+"PATtuple_653_1_fHT.root",
sampleBaseDir+"PATtuple_654_1_M6h.root",
sampleBaseDir+"PATtuple_655_0_Duu.root",
sampleBaseDir+"PATtuple_656_0_LPr.root",
sampleBaseDir+"PATtuple_657_0_tJJ.root",
sampleBaseDir+"PATtuple_658_0_e8G.root",
sampleBaseDir+"PATtuple_659_0_8cQ.root",
sampleBaseDir+"PATtuple_65_1_BP6.root",
sampleBaseDir+"PATtuple_660_0_lUs.root",
sampleBaseDir+"PATtuple_661_0_TTG.root",
sampleBaseDir+"PATtuple_662_0_fri.root",
sampleBaseDir+"PATtuple_663_0_DZO.root",
sampleBaseDir+"PATtuple_664_0_zCj.root",
sampleBaseDir+"PATtuple_665_0_d6l.root",
sampleBaseDir+"PATtuple_667_0_vNn.root",
sampleBaseDir+"PATtuple_668_0_PMT.root",
sampleBaseDir+"PATtuple_669_0_MfF.root",
sampleBaseDir+"PATtuple_66_1_api.root",
sampleBaseDir+"PATtuple_670_0_CwD.root",
sampleBaseDir+"PATtuple_671_0_aWD.root",
sampleBaseDir+"PATtuple_672_0_cVu.root",
sampleBaseDir+"PATtuple_673_0_n5C.root",
sampleBaseDir+"PATtuple_676_0_6HT.root",
sampleBaseDir+"PATtuple_677_0_Md2.root",
sampleBaseDir+"PATtuple_678_0_9tR.root",
sampleBaseDir+"PATtuple_679_0_tQB.root",
sampleBaseDir+"PATtuple_67_1_doU.root",
sampleBaseDir+"PATtuple_680_0_duM.root",
sampleBaseDir+"PATtuple_681_0_vLz.root",
sampleBaseDir+"PATtuple_682_0_0uj.root",
sampleBaseDir+"PATtuple_683_0_res.root",
sampleBaseDir+"PATtuple_684_0_CrG.root",
sampleBaseDir+"PATtuple_685_0_rnq.root",
sampleBaseDir+"PATtuple_687_0_PlW.root",
sampleBaseDir+"PATtuple_688_0_FYW.root",
sampleBaseDir+"PATtuple_689_0_6Hq.root",
sampleBaseDir+"PATtuple_68_1_XmY.root",
sampleBaseDir+"PATtuple_690_0_3ND.root",
sampleBaseDir+"PATtuple_691_0_0hP.root",
sampleBaseDir+"PATtuple_692_0_ftH.root",
sampleBaseDir+"PATtuple_693_0_I1D.root",
sampleBaseDir+"PATtuple_694_0_2Hc.root",
sampleBaseDir+"PATtuple_695_0_aUy.root",
sampleBaseDir+"PATtuple_696_0_cVJ.root",
sampleBaseDir+"PATtuple_697_0_Kt7.root",
sampleBaseDir+"PATtuple_698_0_dM7.root",
sampleBaseDir+"PATtuple_699_0_3Ws.root",
sampleBaseDir+"PATtuple_69_1_rEM.root",
sampleBaseDir+"PATtuple_6_1_dLx.root",
sampleBaseDir+"PATtuple_700_0_JYk.root",
sampleBaseDir+"PATtuple_701_0_qve.root",
sampleBaseDir+"PATtuple_702_0_RKp.root",
sampleBaseDir+"PATtuple_703_0_jAi.root",
sampleBaseDir+"PATtuple_704_0_jMt.root",
sampleBaseDir+"PATtuple_705_0_Zln.root",
sampleBaseDir+"PATtuple_706_0_iyH.root",
sampleBaseDir+"PATtuple_707_0_2W2.root",
sampleBaseDir+"PATtuple_708_0_vHs.root",
sampleBaseDir+"PATtuple_70_1_UCp.root",
sampleBaseDir+"PATtuple_710_0_Db9.root",
sampleBaseDir+"PATtuple_711_0_MVH.root",
sampleBaseDir+"PATtuple_712_0_XMk.root",
sampleBaseDir+"PATtuple_713_0_isV.root",
sampleBaseDir+"PATtuple_714_0_b6T.root",
sampleBaseDir+"PATtuple_715_0_m0Z.root",
sampleBaseDir+"PATtuple_716_0_3PK.root",
sampleBaseDir+"PATtuple_717_0_bM4.root",
sampleBaseDir+"PATtuple_718_0_CXp.root",
sampleBaseDir+"PATtuple_719_0_mBe.root",
sampleBaseDir+"PATtuple_71_1_vaO.root",
sampleBaseDir+"PATtuple_720_0_imp.root",
sampleBaseDir+"PATtuple_721_0_q1L.root",
sampleBaseDir+"PATtuple_722_0_ZLs.root",
sampleBaseDir+"PATtuple_723_0_mUu.root",
sampleBaseDir+"PATtuple_724_0_t6U.root",
sampleBaseDir+"PATtuple_725_0_yOk.root",
sampleBaseDir+"PATtuple_726_0_puc.root",
sampleBaseDir+"PATtuple_727_0_CXU.root",
sampleBaseDir+"PATtuple_728_0_sf8.root",
sampleBaseDir+"PATtuple_729_0_Eon.root",
sampleBaseDir+"PATtuple_72_1_lLQ.root",
sampleBaseDir+"PATtuple_730_0_prq.root",
sampleBaseDir+"PATtuple_731_0_aUi.root",
sampleBaseDir+"PATtuple_732_0_qoi.root",
sampleBaseDir+"PATtuple_733_0_aq1.root",
sampleBaseDir+"PATtuple_734_0_h2x.root",
sampleBaseDir+"PATtuple_735_0_uL1.root",
sampleBaseDir+"PATtuple_736_0_D3r.root",
sampleBaseDir+"PATtuple_737_0_kbS.root",
sampleBaseDir+"PATtuple_738_0_mep.root",
sampleBaseDir+"PATtuple_739_0_c0S.root",
sampleBaseDir+"PATtuple_73_1_lQS.root",
sampleBaseDir+"PATtuple_740_0_Y1K.root",
sampleBaseDir+"PATtuple_741_0_FOW.root",
sampleBaseDir+"PATtuple_742_0_pPm.root",
sampleBaseDir+"PATtuple_743_0_rr4.root",
sampleBaseDir+"PATtuple_744_0_zpA.root",
sampleBaseDir+"PATtuple_745_0_eYS.root",
sampleBaseDir+"PATtuple_746_0_Kll.root",
sampleBaseDir+"PATtuple_747_0_AHU.root",
sampleBaseDir+"PATtuple_748_0_e0d.root",
sampleBaseDir+"PATtuple_749_0_9Hd.root",
sampleBaseDir+"PATtuple_74_1_GsS.root",
sampleBaseDir+"PATtuple_750_0_rIH.root",
sampleBaseDir+"PATtuple_751_0_csT.root",
sampleBaseDir+"PATtuple_752_0_YY5.root",
sampleBaseDir+"PATtuple_77_1_lnm.root",
sampleBaseDir+"PATtuple_78_1_Bql.root",
sampleBaseDir+"PATtuple_79_1_VBa.root",
sampleBaseDir+"PATtuple_7_1_bJ1.root",
sampleBaseDir+"PATtuple_80_1_vhk.root",
sampleBaseDir+"PATtuple_81_1_KZI.root",
sampleBaseDir+"PATtuple_82_1_RfT.root",
sampleBaseDir+"PATtuple_83_1_Sry.root",
sampleBaseDir+"PATtuple_84_1_dDj.root",
sampleBaseDir+"PATtuple_85_1_hEJ.root",
sampleBaseDir+"PATtuple_86_1_YRx.root",
sampleBaseDir+"PATtuple_87_1_8s4.root",
sampleBaseDir+"PATtuple_88_1_oxj.root",
sampleBaseDir+"PATtuple_89_1_ODi.root",
sampleBaseDir+"PATtuple_8_1_QQ7.root",
sampleBaseDir+"PATtuple_90_1_Mwb.root",
sampleBaseDir+"PATtuple_91_1_AeG.root",
sampleBaseDir+"PATtuple_92_1_ckh.root",
sampleBaseDir+"PATtuple_93_1_8wU.root",
sampleBaseDir+"PATtuple_94_1_YP4.root",
sampleBaseDir+"PATtuple_95_1_ADM.root",
sampleBaseDir+"PATtuple_96_1_0wu.root",
sampleBaseDir+"PATtuple_97_1_nZg.root",
sampleBaseDir+"PATtuple_98_1_rCv.root",
sampleBaseDir+"PATtuple_99_1_Pf9.root",
sampleBaseDir+"PATtuple_9_1_CWz.root",
sampleBaseDir+"",
sampleBaseDir+"PATtuple_9_1_tIF.root",
]
