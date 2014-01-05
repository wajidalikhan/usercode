sampleDataSet = '/QCD_Pt_250_350_EMEnriched_TuneZ2star_8TeV_pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM'  

sampleCMSEnergy = 8000

sampleRelease = "CMSSW_5_3_2_patch4" # original (i.e. RECO file) release, not the one we plan to process them with
sampleProcessRelease = "CMSSW_5_3_5" # release used to create new files with

sampleNumEvents = 34611322

sampleXSec = 4250.0 * 0.131 # pb

# global tag can be extracted from file using edmProvDump filename|grep globaltag
# note however that this is the tag for *further* processing, not the original tag
sampleGlobalTag = 'START53_V7F::All'

sampleDuplicateCheckMode = 'checkAllFilesOpened'

sampleType = "BKGMC"



samplePatDBSName="/QCD_Pt_250_350_EMEnriched_TuneZ2star_8TeV_pythia6/ejclemen-QCDem250_pat_20121105-771324b3ed1c70ee461af1193683b519/USER"

sampleBaseDir="dcap://dcap.pp.rl.ac.uk///pnfs/pp.rl.ac.uk/data/cms/store/user/ejclemen//QCD_Pt_250_350_EMEnriched_TuneZ2star_8TeV_pythia6/QCDem250_pat_20121105/771324b3ed1c70ee461af1193683b519/"
samplePatFiles = [
sampleBaseDir+"PATtuple_586_1_HTW.root",
sampleBaseDir+"PATtuple_530_1_KHn.root",
sampleBaseDir+"PATtuple_597_1_yuA.root",
sampleBaseDir+"PATtuple_516_1_VzG.root",
sampleBaseDir+"PATtuple_548_1_PZW.root",
sampleBaseDir+"PATtuple_531_1_QaE.root",
sampleBaseDir+"PATtuple_595_1_zH3.root",
sampleBaseDir+"PATtuple_568_1_FGl.root",
sampleBaseDir+"PATtuple_498_1_NNB.root",
sampleBaseDir+"PATtuple_501_1_dLF.root",
sampleBaseDir+"PATtuple_602_1_wfL.root",
sampleBaseDir+"PATtuple_577_1_fS9.root",
sampleBaseDir+"PATtuple_571_1_0mn.root",
sampleBaseDir+"PATtuple_616_1_IHC.root",
sampleBaseDir+"PATtuple_529_1_iI8.root",
sampleBaseDir+"PATtuple_544_1_3UY.root",
sampleBaseDir+"PATtuple_598_1_Ecr.root",
sampleBaseDir+"PATtuple_432_1_CFD.root",
sampleBaseDir+"PATtuple_338_1_HEs.root",
sampleBaseDir+"PATtuple_351_1_XGK.root",
sampleBaseDir+"PATtuple_269_1_CRN.root",
sampleBaseDir+"PATtuple_537_1_RzK.root",
sampleBaseDir+"PATtuple_394_1_FRv.root",
sampleBaseDir+"PATtuple_534_1_9Uw.root",
sampleBaseDir+"PATtuple_532_1_Ht5.root",
sampleBaseDir+"PATtuple_341_1_MbU.root",
sampleBaseDir+"PATtuple_347_1_YhX.root",
sampleBaseDir+"PATtuple_536_1_kMO.root",
sampleBaseDir+"PATtuple_278_1_mUa.root",
sampleBaseDir+"PATtuple_353_2_iFB.root",
sampleBaseDir+"PATtuple_361_1_1lE.root",
sampleBaseDir+"PATtuple_596_1_wdp.root",
sampleBaseDir+"PATtuple_290_1_fXA.root",
sampleBaseDir+"PATtuple_415_1_y9Z.root",
sampleBaseDir+"PATtuple_617_1_DLX.root",
sampleBaseDir+"PATtuple_349_1_nOZ.root",
sampleBaseDir+"PATtuple_386_1_4OU.root",
sampleBaseDir+"PATtuple_320_1_uB3.root",
sampleBaseDir+"PATtuple_395_1_9EG.root",
sampleBaseDir+"PATtuple_336_1_iZs.root",
sampleBaseDir+"PATtuple_626_1_C66.root",
sampleBaseDir+"PATtuple_393_1_0ae.root",
sampleBaseDir+"PATtuple_576_1_vj8.root",
sampleBaseDir+"PATtuple_345_1_C6M.root",
sampleBaseDir+"PATtuple_496_1_0Xa.root",
sampleBaseDir+"PATtuple_256_1_FHP.root",
sampleBaseDir+"PATtuple_317_1_woB.root",
sampleBaseDir+"PATtuple_337_1_y4U.root",
sampleBaseDir+"PATtuple_316_1_Vk9.root",
sampleBaseDir+"PATtuple_500_1_Mxe.root",
sampleBaseDir+"PATtuple_411_1_4ab.root",
sampleBaseDir+"PATtuple_360_1_pJg.root",
sampleBaseDir+"PATtuple_372_1_vuF.root",
sampleBaseDir+"PATtuple_303_1_3MD.root",
sampleBaseDir+"PATtuple_628_1_SFA.root",
sampleBaseDir+"PATtuple_400_1_Ec1.root",
sampleBaseDir+"PATtuple_273_1_c2N.root",
sampleBaseDir+"PATtuple_468_1_mfu.root",
sampleBaseDir+"PATtuple_279_1_gpD.root",
sampleBaseDir+"PATtuple_362_1_Rrh.root",
sampleBaseDir+"PATtuple_253_1_ld6.root",
sampleBaseDir+"PATtuple_249_1_Yk5.root",
sampleBaseDir+"PATtuple_357_1_59t.root",
sampleBaseDir+"PATtuple_202_1_Usb.root",
sampleBaseDir+"PATtuple_429_1_Rya.root",
sampleBaseDir+"PATtuple_369_1_c0s.root",
sampleBaseDir+"PATtuple_367_1_HYU.root",
sampleBaseDir+"PATtuple_254_1_M6k.root",
sampleBaseDir+"PATtuple_346_1_OtV.root",
sampleBaseDir+"PATtuple_332_1_zrF.root",
sampleBaseDir+"PATtuple_251_2_oOt.root",
sampleBaseDir+"PATtuple_342_1_dYQ.root",
sampleBaseDir+"PATtuple_229_1_8yc.root",
sampleBaseDir+"PATtuple_305_1_pMs.root",
sampleBaseDir+"PATtuple_343_1_DVK.root",
sampleBaseDir+"PATtuple_197_1_lvc.root",
sampleBaseDir+"PATtuple_354_1_TUS.root",
sampleBaseDir+"PATtuple_182_1_duQ.root",
sampleBaseDir+"PATtuple_268_1_fWu.root",
sampleBaseDir+"PATtuple_245_1_lOq.root",
sampleBaseDir+"PATtuple_364_1_Wnl.root",
sampleBaseDir+"PATtuple_314_1_ZGK.root",
sampleBaseDir+"PATtuple_358_1_y09.root",
sampleBaseDir+"PATtuple_176_1_rFZ.root",
sampleBaseDir+"PATtuple_271_1_3vK.root",
sampleBaseDir+"PATtuple_284_1_Z8w.root",
sampleBaseDir+"PATtuple_330_1_z5I.root",
sampleBaseDir+"PATtuple_282_1_vZb.root",
sampleBaseDir+"PATtuple_223_1_hn2.root",
sampleBaseDir+"PATtuple_285_1_rZF.root",
sampleBaseDir+"PATtuple_179_1_cVR.root",
sampleBaseDir+"PATtuple_348_1_DBU.root",
sampleBaseDir+"PATtuple_272_1_R0Q.root",
sampleBaseDir+"PATtuple_177_1_mPv.root",
sampleBaseDir+"PATtuple_252_1_QFP.root",
sampleBaseDir+"PATtuple_231_1_Kh7.root",
sampleBaseDir+"PATtuple_274_1_aMl.root",
sampleBaseDir+"PATtuple_286_1_KYQ.root",
sampleBaseDir+"PATtuple_321_1_pY5.root",
sampleBaseDir+"PATtuple_131_1_80D.root",
sampleBaseDir+"PATtuple_262_1_BFw.root",
sampleBaseDir+"PATtuple_185_1_Vaq.root",
sampleBaseDir+"PATtuple_207_1_V62.root",
sampleBaseDir+"PATtuple_651_1_Clg.root",
sampleBaseDir+"PATtuple_189_1_dHE.root",
sampleBaseDir+"PATtuple_203_1_PSw.root",
sampleBaseDir+"PATtuple_209_1_AU7.root",
sampleBaseDir+"PATtuple_448_2_hIM.root",
sampleBaseDir+"PATtuple_174_1_Xne.root",
sampleBaseDir+"PATtuple_217_1_oMH.root",
sampleBaseDir+"PATtuple_205_1_lSP.root",
sampleBaseDir+"PATtuple_464_1_tak.root",
sampleBaseDir+"PATtuple_188_1_uC2.root",
sampleBaseDir+"PATtuple_183_1_4Ib.root",
sampleBaseDir+"PATtuple_406_1_oXT.root",
sampleBaseDir+"PATtuple_422_1_7bl.root",
sampleBaseDir+"PATtuple_600_1_MrM.root",
sampleBaseDir+"PATtuple_634_1_Gd9.root",
sampleBaseDir+"PATtuple_423_1_TzN.root",
sampleBaseDir+"PATtuple_652_1_qT7.root",
sampleBaseDir+"PATtuple_140_1_YJo.root",
sampleBaseDir+"PATtuple_599_1_4G4.root",
sampleBaseDir+"PATtuple_608_1_ps9.root",
sampleBaseDir+"PATtuple_578_1_6BC.root",
sampleBaseDir+"PATtuple_561_1_3hF.root",
sampleBaseDir+"PATtuple_478_1_Zwv.root",
sampleBaseDir+"PATtuple_591_1_WTS.root",
sampleBaseDir+"PATtuple_636_1_YDU.root",
sampleBaseDir+"PATtuple_622_1_IDk.root",
sampleBaseDir+"PATtuple_565_1_lcB.root",
sampleBaseDir+"PATtuple_458_1_kax.root",
sampleBaseDir+"PATtuple_555_1_ZWL.root",
sampleBaseDir+"PATtuple_589_1_vti.root",
sampleBaseDir+"PATtuple_494_1_ChN.root",
sampleBaseDir+"PATtuple_610_1_Bj0.root",
sampleBaseDir+"PATtuple_572_1_h0i.root",
sampleBaseDir+"PATtuple_560_1_bcx.root",
sampleBaseDir+"PATtuple_470_1_YKB.root",
sampleBaseDir+"PATtuple_579_1_fV5.root",
sampleBaseDir+"PATtuple_580_1_qhs.root",
sampleBaseDir+"PATtuple_625_1_hx6.root",
sampleBaseDir+"PATtuple_533_1_qaX.root",
sampleBaseDir+"PATtuple_573_1_k94.root",
sampleBaseDir+"PATtuple_633_1_2Xd.root",
sampleBaseDir+"PATtuple_497_1_inA.root",
sampleBaseDir+"PATtuple_606_1_Ulk.root",
sampleBaseDir+"PATtuple_495_1_Wwj.root",
sampleBaseDir+"PATtuple_624_1_Qpr.root",
sampleBaseDir+"PATtuple_574_1_3eR.root",
sampleBaseDir+"PATtuple_545_1_kdo.root",
sampleBaseDir+"PATtuple_587_1_Irt.root",
sampleBaseDir+"PATtuple_631_1_Vzc.root",
sampleBaseDir+"PATtuple_588_1_w4O.root",
sampleBaseDir+"PATtuple_540_1_WpD.root",
sampleBaseDir+"PATtuple_585_1_rmg.root",
sampleBaseDir+"PATtuple_582_1_qrm.root",
sampleBaseDir+"PATtuple_493_1_ieP.root",
sampleBaseDir+"PATtuple_538_1_96q.root",
sampleBaseDir+"PATtuple_605_1_4IP.root",
sampleBaseDir+"PATtuple_551_1_pcM.root",
sampleBaseDir+"PATtuple_611_1_kUf.root",
sampleBaseDir+"PATtuple_581_1_4o2.root",
sampleBaseDir+"PATtuple_546_1_feM.root",
sampleBaseDir+"PATtuple_374_1_8m4.root",
sampleBaseDir+"PATtuple_399_1_cu9.root",
sampleBaseDir+"PATtuple_371_1_80b.root",
sampleBaseDir+"PATtuple_365_1_cuj.root",
sampleBaseDir+"PATtuple_603_1_nuI.root",
sampleBaseDir+"PATtuple_366_1_Afq.root",
sampleBaseDir+"PATtuple_558_1_YBt.root",
sampleBaseDir+"PATtuple_592_1_TwO.root",
sampleBaseDir+"PATtuple_435_1_NTJ.root",
sampleBaseDir+"PATtuple_492_1_3bQ.root",
sampleBaseDir+"PATtuple_519_1_3D3.root",
sampleBaseDir+"PATtuple_527_1_t9X.root",
sampleBaseDir+"PATtuple_524_1_HYV.root",
sampleBaseDir+"PATtuple_562_1_Mi2.root",
sampleBaseDir+"PATtuple_661_1_uNa.root",
sampleBaseDir+"PATtuple_512_1_ov3.root",
sampleBaseDir+"PATtuple_119_1_tyS.root",
sampleBaseDir+"PATtuple_543_1_Vaf.root",
sampleBaseDir+"PATtuple_480_1_2Rz.root",
sampleBaseDir+"PATtuple_488_1_h79.root",
sampleBaseDir+"PATtuple_526_1_NJX.root",
sampleBaseDir+"PATtuple_559_1_a5f.root",
sampleBaseDir+"PATtuple_590_1_4h5.root",
sampleBaseDir+"PATtuple_594_1_TlZ.root",
sampleBaseDir+"PATtuple_522_1_NTw.root",
sampleBaseDir+"PATtuple_554_1_Lz8.root",
sampleBaseDir+"PATtuple_563_1_zct.root",
sampleBaseDir+"PATtuple_479_1_B9p.root",
sampleBaseDir+"PATtuple_326_1_RKh.root",
sampleBaseDir+"PATtuple_583_1_GS6.root",
sampleBaseDir+"PATtuple_491_1_uS3.root",
sampleBaseDir+"PATtuple_513_1_eGO.root",
sampleBaseDir+"PATtuple_525_1_DXM.root",
sampleBaseDir+"PATtuple_505_1_sMn.root",
sampleBaseDir+"PATtuple_463_1_rd4.root",
sampleBaseDir+"PATtuple_476_1_mL7.root",
sampleBaseDir+"PATtuple_485_1_DkA.root",
sampleBaseDir+"PATtuple_471_1_mUZ.root",
sampleBaseDir+"PATtuple_482_1_2nL.root",
sampleBaseDir+"PATtuple_489_1_FlT.root",
sampleBaseDir+"PATtuple_549_1_wfT.root",
sampleBaseDir+"PATtuple_331_1_R4S.root",
sampleBaseDir+"PATtuple_475_1_Nlq.root",
sampleBaseDir+"PATtuple_445_1_pQT.root",
sampleBaseDir+"PATtuple_451_1_EpE.root",
sampleBaseDir+"PATtuple_459_1_ihY.root",
sampleBaseDir+"PATtuple_511_1_vm0.root",
sampleBaseDir+"PATtuple_542_1_T7F.root",
sampleBaseDir+"PATtuple_454_1_e36.root",
sampleBaseDir+"PATtuple_165_1_CDl.root",
sampleBaseDir+"PATtuple_620_1_v9J.root",
sampleBaseDir+"PATtuple_473_1_LpT.root",
sampleBaseDir+"PATtuple_593_1_hmb.root",
sampleBaseDir+"PATtuple_398_1_jDO.root",
sampleBaseDir+"PATtuple_452_1_ro9.root",
sampleBaseDir+"PATtuple_460_1_lK9.root",
sampleBaseDir+"PATtuple_557_1_bfZ.root",
sampleBaseDir+"PATtuple_528_1_EAT.root",
sampleBaseDir+"PATtuple_396_1_QmF.root",
sampleBaseDir+"PATtuple_391_1_nEW.root",
sampleBaseDir+"PATtuple_518_1_zWz.root",
sampleBaseDir+"PATtuple_539_1_Hte.root",
sampleBaseDir+"PATtuple_514_1_P0c.root",
sampleBaseDir+"PATtuple_483_1_JYu.root",
sampleBaseDir+"PATtuple_584_1_9XJ.root",
sampleBaseDir+"PATtuple_506_1_OY9.root",
sampleBaseDir+"PATtuple_414_1_rp9.root",
sampleBaseDir+"PATtuple_116_1_wYY.root",
sampleBaseDir+"PATtuple_469_1_9v0.root",
sampleBaseDir+"PATtuple_118_1_shN.root",
sampleBaseDir+"PATtuple_413_1_cYI.root",
sampleBaseDir+"PATtuple_408_1_umD.root",
sampleBaseDir+"PATtuple_440_1_3n4.root",
sampleBaseDir+"PATtuple_456_1_dSh.root",
sampleBaseDir+"PATtuple_449_1_NQQ.root",
sampleBaseDir+"PATtuple_390_1_6iy.root",
sampleBaseDir+"PATtuple_442_1_Ra4.root",
sampleBaseDir+"PATtuple_499_1_x8r.root",
sampleBaseDir+"PATtuple_453_1_HR2.root",
sampleBaseDir+"PATtuple_441_1_seR.root",
sampleBaseDir+"PATtuple_657_1_7zP.root",
sampleBaseDir+"PATtuple_447_1_wEV.root",
sampleBaseDir+"PATtuple_503_1_my9.root",
sampleBaseDir+"PATtuple_660_1_Pc0.root",
sampleBaseDir+"PATtuple_553_1_WmL.root",
sampleBaseDir+"PATtuple_654_1_lHh.root",
sampleBaseDir+"PATtuple_520_1_X1p.root",
sampleBaseDir+"PATtuple_352_1_wik.root",
sampleBaseDir+"PATtuple_226_1_uZu.root",
sampleBaseDir+"PATtuple_160_1_njl.root",
sampleBaseDir+"PATtuple_191_1_437.root",
sampleBaseDir+"PATtuple_609_2_caR.root",
sampleBaseDir+"PATtuple_523_2_BZA.root",
sampleBaseDir+"PATtuple_222_1_Ru4.root",
sampleBaseDir+"PATtuple_373_1_ItH.root",
sampleBaseDir+"PATtuple_250_1_Cqe.root",
sampleBaseDir+"PATtuple_175_1_qvm.root",
sampleBaseDir+"PATtuple_280_1_JsX.root",
sampleBaseDir+"PATtuple_263_1_I7G.root",
sampleBaseDir+"PATtuple_208_1_0a9.root",
sampleBaseDir+"PATtuple_319_1_bQf.root",
sampleBaseDir+"PATtuple_173_1_YjI.root",
sampleBaseDir+"PATtuple_204_1_aS6.root",
sampleBaseDir+"PATtuple_318_1_Wqc.root",
sampleBaseDir+"PATtuple_167_1_IxS.root",
sampleBaseDir+"PATtuple_275_1_iok.root",
sampleBaseDir+"PATtuple_323_1_rzI.root",
sampleBaseDir+"PATtuple_224_1_uqq.root",
sampleBaseDir+"PATtuple_260_1_sLR.root",
sampleBaseDir+"PATtuple_288_1_iyy.root",
sampleBaseDir+"PATtuple_281_1_Lja.root",
sampleBaseDir+"PATtuple_213_1_Yl7.root",
sampleBaseDir+"PATtuple_192_1_QQP.root",
sampleBaseDir+"PATtuple_267_1_xFZ.root",
sampleBaseDir+"PATtuple_181_1_46e.root",
sampleBaseDir+"PATtuple_238_1_xBD.root",
sampleBaseDir+"PATtuple_248_1_9ga.root",
sampleBaseDir+"PATtuple_161_1_exp.root",
sampleBaseDir+"PATtuple_283_1_8IE.root",
sampleBaseDir+"PATtuple_212_1_MSp.root",
sampleBaseDir+"PATtuple_164_1_mf2.root",
sampleBaseDir+"PATtuple_162_1_uky.root",
sampleBaseDir+"PATtuple_210_1_3JL.root",
sampleBaseDir+"PATtuple_233_1_uUc.root",
sampleBaseDir+"PATtuple_225_1_4uE.root",
sampleBaseDir+"PATtuple_184_1_AZ3.root",
sampleBaseDir+"PATtuple_187_1_M1d.root",
sampleBaseDir+"PATtuple_227_1_pFB.root",
sampleBaseDir+"PATtuple_168_1_xJL.root",
sampleBaseDir+"PATtuple_304_1_RZj.root",
sampleBaseDir+"PATtuple_412_1_bsl.root",
sampleBaseDir+"PATtuple_234_1_Ubw.root",
sampleBaseDir+"PATtuple_158_1_H8J.root",
sampleBaseDir+"PATtuple_264_1_eaj.root",
sampleBaseDir+"PATtuple_236_1_JJx.root",
sampleBaseDir+"PATtuple_232_1_3TX.root",
sampleBaseDir+"PATtuple_178_1_Q80.root",
sampleBaseDir+"PATtuple_201_1_cDR.root",
sampleBaseDir+"PATtuple_659_1_EHe.root",
sampleBaseDir+"PATtuple_655_1_fXb.root",
sampleBaseDir+"PATtuple_389_1_J1O.root",
sampleBaseDir+"PATtuple_658_1_P3i.root",
sampleBaseDir+"PATtuple_653_1_nbX.root",
sampleBaseDir+"PATtuple_682_1_ECj.root",
sampleBaseDir+"PATtuple_504_1_pcH.root",
sampleBaseDir+"PATtuple_656_1_rCR.root",
sampleBaseDir+"PATtuple_295_1_PEQ.root",
sampleBaseDir+"PATtuple_428_1_3YJ.root",
sampleBaseDir+"PATtuple_681_1_jpn.root",
sampleBaseDir+"PATtuple_618_1_Nx2.root",
sampleBaseDir+"PATtuple_508_1_iay.root",
sampleBaseDir+"PATtuple_627_1_93K.root",
sampleBaseDir+"PATtuple_667_1_elI.root",
sampleBaseDir+"PATtuple_690_1_3QJ.root",
sampleBaseDir+"PATtuple_198_2_HRG.root",
sampleBaseDir+"PATtuple_444_2_vOa.root",
sampleBaseDir+"PATtuple_387_1_iUF.root",
sampleBaseDir+"PATtuple_206_1_HOn.root",
sampleBaseDir+"PATtuple_381_1_OO5.root",
sampleBaseDir+"PATtuple_638_1_dgx.root",
sampleBaseDir+"PATtuple_673_1_CUo.root",
sampleBaseDir+"PATtuple_439_1_fZj.root",
sampleBaseDir+"PATtuple_643_1_Yk4.root",
sampleBaseDir+"PATtuple_566_1_1cK.root",
sampleBaseDir+"PATtuple_517_1_58l.root",
sampleBaseDir+"PATtuple_637_1_gnq.root",
sampleBaseDir+"PATtuple_689_1_5Ry.root",
sampleBaseDir+"PATtuple_607_1_5rG.root",
sampleBaseDir+"PATtuple_639_1_Hj0.root",
sampleBaseDir+"PATtuple_687_1_6LU.root",
sampleBaseDir+"PATtuple_677_1_TQF.root",
sampleBaseDir+"PATtuple_613_1_VX5.root",
sampleBaseDir+"PATtuple_679_1_Lf8.root",
sampleBaseDir+"PATtuple_692_1_yDR.root",
sampleBaseDir+"PATtuple_680_1_2BN.root",
sampleBaseDir+"PATtuple_668_1_sGb.root",
sampleBaseDir+"PATtuple_630_1_rdr.root",
sampleBaseDir+"PATtuple_623_1_ddu.root",
sampleBaseDir+"PATtuple_149_1_D4D.root",
sampleBaseDir+"PATtuple_143_1_PfK.root",
sampleBaseDir+"PATtuple_144_1_Jbz.root",
sampleBaseDir+"PATtuple_159_1_kxf.root",
sampleBaseDir+"PATtuple_325_1_vYa.root",
sampleBaseDir+"PATtuple_246_1_oBj.root",
sampleBaseDir+"PATtuple_313_1_b0r.root",
sampleBaseDir+"PATtuple_195_1_xkW.root",
sampleBaseDir+"PATtuple_127_1_0Pf.root",
sampleBaseDir+"PATtuple_230_1_oS3.root",
sampleBaseDir+"PATtuple_193_1_B41.root",
sampleBaseDir+"PATtuple_133_1_bCO.root",
sampleBaseDir+"PATtuple_126_1_2Dt.root",
sampleBaseDir+"PATtuple_235_1_d6b.root",
sampleBaseDir+"PATtuple_215_1_Wof.root",
sampleBaseDir+"PATtuple_138_1_SAw.root",
sampleBaseDir+"PATtuple_155_1_TYF.root",
sampleBaseDir+"PATtuple_310_1_Mrs.root",
sampleBaseDir+"PATtuple_142_1_QPD.root",
sampleBaseDir+"PATtuple_156_1_P75.root",
sampleBaseDir+"PATtuple_301_1_43L.root",
sampleBaseDir+"PATtuple_294_1_PGk.root",
sampleBaseDir+"PATtuple_123_1_Egr.root",
sampleBaseDir+"PATtuple_122_1_1sF.root",
sampleBaseDir+"PATtuple_145_1_UMB.root",
sampleBaseDir+"PATtuple_109_1_Shx.root",
sampleBaseDir+"PATtuple_270_1_hWl.root",
sampleBaseDir+"PATtuple_154_1_uPp.root",
sampleBaseDir+"PATtuple_148_1_MXS.root",
sampleBaseDir+"PATtuple_107_1_JSG.root",
sampleBaseDir+"PATtuple_302_1_6Kd.root",
sampleBaseDir+"PATtuple_186_1_AUz.root",
sampleBaseDir+"PATtuple_243_1_8DR.root",
sampleBaseDir+"PATtuple_102_1_mft.root",
sampleBaseDir+"PATtuple_29_1_Lg0.root",
sampleBaseDir+"PATtuple_105_1_niL.root",
sampleBaseDir+"PATtuple_312_1_BhR.root",
sampleBaseDir+"PATtuple_124_1_YEi.root",
sampleBaseDir+"PATtuple_117_1_EO0.root",
sampleBaseDir+"PATtuple_240_1_qou.root",
sampleBaseDir+"PATtuple_218_1_Y7A.root",
sampleBaseDir+"PATtuple_228_1_qIy.root",
sampleBaseDir+"PATtuple_450_1_pLu.root",
sampleBaseDir+"PATtuple_486_1_Ucp.root",
sampleBaseDir+"PATtuple_552_1_8Wm.root",
sampleBaseDir+"PATtuple_575_1_YTT.root",
sampleBaseDir+"PATtuple_481_1_DmJ.root",
sampleBaseDir+"PATtuple_547_1_HZo.root",
sampleBaseDir+"PATtuple_462_1_inQ.root",
sampleBaseDir+"PATtuple_550_1_GJF.root",
sampleBaseDir+"PATtuple_521_1_FLa.root",
sampleBaseDir+"PATtuple_569_1_XAd.root",
sampleBaseDir+"PATtuple_564_1_YCr.root",
sampleBaseDir+"PATtuple_541_1_z6R.root",
sampleBaseDir+"PATtuple_434_1_mf1.root",
sampleBaseDir+"PATtuple_477_1_8gC.root",
sampleBaseDir+"PATtuple_461_1_mU1.root",
sampleBaseDir+"PATtuple_484_1_rcd.root",
sampleBaseDir+"PATtuple_166_1_ze8.root",
sampleBaseDir+"PATtuple_457_1_TRr.root",
sampleBaseDir+"PATtuple_446_1_09k.root",
sampleBaseDir+"PATtuple_570_1_ahW.root",
sampleBaseDir+"PATtuple_535_1_Ihg.root",
sampleBaseDir+"PATtuple_465_1_jrj.root",
sampleBaseDir+"PATtuple_487_1_Idn.root",
sampleBaseDir+"PATtuple_242_1_BMx.root",
sampleBaseDir+"PATtuple_291_1_NTp.root",
sampleBaseDir+"PATtuple_151_1_ZOx.root",
sampleBaseDir+"PATtuple_237_1_PcP.root",
sampleBaseDir+"PATtuple_139_1_gIo.root",
sampleBaseDir+"PATtuple_239_1_18F.root",
sampleBaseDir+"PATtuple_90_1_nu7.root",
sampleBaseDir+"PATtuple_259_1_C9k.root",
sampleBaseDir+"PATtuple_292_1_Hff.root",
sampleBaseDir+"PATtuple_194_1_0zC.root",
sampleBaseDir+"PATtuple_220_1_pzm.root",
sampleBaseDir+"PATtuple_110_1_yqk.root",
sampleBaseDir+"PATtuple_98_1_tBm.root",
sampleBaseDir+"PATtuple_99_1_29p.root",
sampleBaseDir+"PATtuple_114_1_MCe.root",
sampleBaseDir+"PATtuple_157_1_hBd.root",
sampleBaseDir+"PATtuple_108_1_d0S.root",
sampleBaseDir+"PATtuple_132_1_88g.root",
sampleBaseDir+"PATtuple_92_1_e1w.root",
sampleBaseDir+"PATtuple_309_1_5uh.root",
sampleBaseDir+"PATtuple_101_1_mDi.root",
sampleBaseDir+"PATtuple_134_1_dr1.root",
sampleBaseDir+"PATtuple_129_1_6aQ.root",
sampleBaseDir+"PATtuple_112_1_wcH.root",
sampleBaseDir+"PATtuple_136_1_bnb.root",
sampleBaseDir+"PATtuple_111_1_RUr.root",
sampleBaseDir+"PATtuple_74_1_6AE.root",
sampleBaseDir+"PATtuple_103_1_XQo.root",
sampleBaseDir+"PATtuple_73_1_pdd.root",
sampleBaseDir+"PATtuple_135_1_U5o.root",
sampleBaseDir+"PATtuple_69_1_Uer.root",
sampleBaseDir+"PATtuple_196_1_4II.root",
sampleBaseDir+"PATtuple_95_1_coj.root",
sampleBaseDir+"PATtuple_172_1_9ue.root",
sampleBaseDir+"PATtuple_89_1_uy7.root",
sampleBaseDir+"PATtuple_266_1_lH5.root",
sampleBaseDir+"PATtuple_93_1_ckf.root",
sampleBaseDir+"PATtuple_80_1_XUP.root",
sampleBaseDir+"PATtuple_113_1_FrH.root",
sampleBaseDir+"PATtuple_106_1_cKY.root",
sampleBaseDir+"PATtuple_153_1_cob.root",
sampleBaseDir+"PATtuple_87_1_qOf.root",
sampleBaseDir+"PATtuple_76_1_JBY.root",
sampleBaseDir+"PATtuple_120_1_C2G.root",
sampleBaseDir+"PATtuple_77_1_cmy.root",
sampleBaseDir+"PATtuple_72_1_4yg.root",
sampleBaseDir+"PATtuple_70_1_csH.root",
sampleBaseDir+"PATtuple_88_1_o8L.root",
sampleBaseDir+"PATtuple_83_1_tbq.root",
sampleBaseDir+"PATtuple_78_1_eRv.root",
sampleBaseDir+"PATtuple_152_1_paV.root",
sampleBaseDir+"PATtuple_216_1_ILe.root",
sampleBaseDir+"PATtuple_97_1_E2k.root",
sampleBaseDir+"PATtuple_79_1_lXh.root",
sampleBaseDir+"PATtuple_75_1_FwJ.root",
sampleBaseDir+"PATtuple_65_1_E3l.root",
sampleBaseDir+"PATtuple_71_1_bQw.root",
sampleBaseDir+"PATtuple_82_1_oYe.root",
sampleBaseDir+"PATtuple_128_1_Reg.root",
sampleBaseDir+"PATtuple_81_1_G8E.root",
sampleBaseDir+"PATtuple_68_1_wKV.root",
sampleBaseDir+"PATtuple_94_1_kTM.root",
sampleBaseDir+"PATtuple_86_1_nbS.root",
sampleBaseDir+"PATtuple_55_1_w0N.root",
sampleBaseDir+"PATtuple_91_1_I7m.root",
sampleBaseDir+"PATtuple_84_1_idJ.root",
sampleBaseDir+"PATtuple_85_1_2LT.root",
sampleBaseDir+"PATtuple_58_1_y9l.root",
sampleBaseDir+"PATtuple_63_1_L65.root",
sampleBaseDir+"PATtuple_67_1_hw2.root",
sampleBaseDir+"PATtuple_66_1_ck3.root",
sampleBaseDir+"PATtuple_64_1_AV4.root",
sampleBaseDir+"PATtuple_59_1_1Zp.root",
sampleBaseDir+"PATtuple_61_1_vCP.root",
sampleBaseDir+"PATtuple_48_1_jfZ.root",
sampleBaseDir+"PATtuple_52_1_G1p.root",
sampleBaseDir+"PATtuple_46_1_2pA.root",
sampleBaseDir+"PATtuple_51_1_guL.root",
sampleBaseDir+"PATtuple_62_1_cIc.root",
sampleBaseDir+"PATtuple_57_1_vZO.root",
sampleBaseDir+"PATtuple_53_1_mSX.root",
sampleBaseDir+"PATtuple_60_1_yt2.root",
sampleBaseDir+"PATtuple_683_1_cnC.root",
sampleBaseDir+"PATtuple_601_1_k7z.root",
sampleBaseDir+"PATtuple_645_1_iWU.root",
sampleBaseDir+"PATtuple_629_1_ypg.root",
sampleBaseDir+"PATtuple_644_1_W7p.root",
sampleBaseDir+"PATtuple_676_1_PSP.root",
sampleBaseDir+"PATtuple_621_1_qn8.root",
sampleBaseDir+"PATtuple_663_1_u7I.root",
sampleBaseDir+"PATtuple_425_1_pBj.root",
sampleBaseDir+"PATtuple_641_1_QpT.root",
sampleBaseDir+"PATtuple_619_1_SYy.root",
sampleBaseDir+"PATtuple_693_1_4Lj.root",
sampleBaseDir+"PATtuple_649_1_TlQ.root",
sampleBaseDir+"PATtuple_612_1_MDG.root",
sampleBaseDir+"PATtuple_678_1_g9v.root",
sampleBaseDir+"PATtuple_675_1_6Tx.root",
sampleBaseDir+"PATtuple_642_1_zyy.root",
sampleBaseDir+"PATtuple_650_1_2FA.root",
sampleBaseDir+"PATtuple_640_1_LhM.root",
sampleBaseDir+"PATtuple_686_1_Bbf.root",
sampleBaseDir+"PATtuple_694_1_3d0.root",
sampleBaseDir+"PATtuple_647_1_iOX.root",
sampleBaseDir+"PATtuple_662_1_NvQ.root",
sampleBaseDir+"PATtuple_688_1_s9B.root",
sampleBaseDir+"PATtuple_502_1_STD.root",
sampleBaseDir+"PATtuple_635_1_7Px.root",
sampleBaseDir+"PATtuple_632_1_oHl.root",
sampleBaseDir+"PATtuple_604_1_Boa.root",
sampleBaseDir+"PATtuple_665_1_YNy.root",
sampleBaseDir+"PATtuple_171_2_XxT.root",
sampleBaseDir+"PATtuple_674_1_dHO.root",
sampleBaseDir+"PATtuple_671_1_Y3O.root",
sampleBaseDir+"PATtuple_691_1_5CM.root",
sampleBaseDir+"PATtuple_614_1_SSn.root",
sampleBaseDir+"PATtuple_684_1_jcu.root",
sampleBaseDir+"PATtuple_669_1_vwk.root",
sampleBaseDir+"PATtuple_416_1_V4T.root",
sampleBaseDir+"PATtuple_666_1_0RF.root",
sampleBaseDir+"PATtuple_646_1_GdQ.root",
sampleBaseDir+"PATtuple_672_1_sW3.root",
sampleBaseDir+"PATtuple_556_1_WkR.root",
sampleBaseDir+"PATtuple_615_1_UGi.root",
sampleBaseDir+"PATtuple_466_1_LP1.root",
sampleBaseDir+"PATtuple_648_1_c4H.root",
sampleBaseDir+"PATtuple_96_1_9Xi.root",
sampleBaseDir+"PATtuple_418_1_AFM.root",
sampleBaseDir+"PATtuple_375_1_BdI.root",
sampleBaseDir+"PATtuple_403_1_3GF.root",
sampleBaseDir+"PATtuple_472_1_A6A.root",
sampleBaseDir+"PATtuple_474_1_lpc.root",
sampleBaseDir+"PATtuple_507_1_7ZD.root",
sampleBaseDir+"PATtuple_515_1_pq3.root",
sampleBaseDir+"PATtuple_467_1_jiM.root",
sampleBaseDir+"PATtuple_438_1_ad7.root",
sampleBaseDir+"PATtuple_419_1_z7n.root",
sampleBaseDir+"PATtuple_436_1_KZn.root",
sampleBaseDir+"PATtuple_385_1_Ebf.root",
sampleBaseDir+"PATtuple_695_1_CzC.root",
sampleBaseDir+"PATtuple_417_1_PTd.root",
sampleBaseDir+"PATtuple_437_1_fVp.root",
sampleBaseDir+"PATtuple_420_1_zXv.root",
sampleBaseDir+"PATtuple_433_1_NRI.root",
sampleBaseDir+"PATtuple_370_1_Ipx.root",
sampleBaseDir+"PATtuple_322_1_V93.root",
sampleBaseDir+"PATtuple_510_1_4ww.root",
sampleBaseDir+"PATtuple_328_1_mFS.root",
sampleBaseDir+"PATtuple_410_1_6f0.root",
sampleBaseDir+"PATtuple_333_1_XLv.root",
sampleBaseDir+"PATtuple_329_1_414.root",
sampleBaseDir+"PATtuple_244_1_HUI.root",
sampleBaseDir+"PATtuple_376_1_hsJ.root",
sampleBaseDir+"PATtuple_455_1_hR5.root",
sampleBaseDir+"PATtuple_427_1_r3d.root",
sampleBaseDir+"PATtuple_315_1_LCO.root",
sampleBaseDir+"PATtuple_363_1_cYX.root",
sampleBaseDir+"PATtuple_392_1_91R.root",
sampleBaseDir+"PATtuple_509_1_JDU.root",
sampleBaseDir+"PATtuple_307_1_uje.root",
sampleBaseDir+"PATtuple_384_1_xls.root",
sampleBaseDir+"PATtuple_356_1_Udn.root",
sampleBaseDir+"PATtuple_334_1_JWs.root",
sampleBaseDir+"PATtuple_377_1_NS1.root",
sampleBaseDir+"PATtuple_407_1_H2q.root",
sampleBaseDir+"PATtuple_199_1_rML.root",
sampleBaseDir+"PATtuple_696_1_dml.root",
sampleBaseDir+"PATtuple_121_1_6GD.root",
sampleBaseDir+"PATtuple_567_1_zlR.root",
sampleBaseDir+"PATtuple_324_1_YRC.root",
sampleBaseDir+"PATtuple_431_1_h3k.root",
sampleBaseDir+"PATtuple_289_1_lMt.root",
sampleBaseDir+"PATtuple_382_1_TTC.root",
sampleBaseDir+"PATtuple_344_1_Fc5.root",
sampleBaseDir+"PATtuple_430_1_3km.root",
sampleBaseDir+"PATtuple_359_1_NZy.root",
sampleBaseDir+"PATtuple_297_1_ZVV.root",
sampleBaseDir+"PATtuple_265_1_KxQ.root",
sampleBaseDir+"PATtuple_380_1_XbI.root",
sampleBaseDir+"PATtuple_308_1_ZLl.root",
sampleBaseDir+"PATtuple_300_1_XY6.root",
sampleBaseDir+"PATtuple_426_1_44B.root",
sampleBaseDir+"PATtuple_200_1_H5U.root",
sampleBaseDir+"PATtuple_424_1_s97.root",
sampleBaseDir+"PATtuple_355_1_RKT.root",
sampleBaseDir+"PATtuple_397_1_zlx.root",
sampleBaseDir+"PATtuple_350_1_g6V.root",
sampleBaseDir+"PATtuple_490_1_nZx.root",
sampleBaseDir+"PATtuple_277_1_PgG.root",
sampleBaseDir+"PATtuple_421_1_n48.root",
sampleBaseDir+"PATtuple_276_1_mDQ.root",
sampleBaseDir+"PATtuple_339_1_QAS.root",
sampleBaseDir+"PATtuple_404_1_lEs.root",
sampleBaseDir+"PATtuple_383_1_YqY.root",
sampleBaseDir+"PATtuple_163_1_BWM.root",
sampleBaseDir+"PATtuple_115_1_HJa.root",
sampleBaseDir+"PATtuple_402_1_nUS.root",
sampleBaseDir+"PATtuple_401_1_PS5.root",
sampleBaseDir+"PATtuple_306_1_clr.root",
sampleBaseDir+"PATtuple_378_1_KIn.root",
sampleBaseDir+"PATtuple_257_1_10s.root",
sampleBaseDir+"PATtuple_335_1_oF7.root",
sampleBaseDir+"PATtuple_258_1_i7t.root",
sampleBaseDir+"PATtuple_311_1_9fV.root",
sampleBaseDir+"PATtuple_180_1_9pu.root",
sampleBaseDir+"PATtuple_379_1_4JE.root",
sampleBaseDir+"PATtuple_340_1_aX5.root",
sampleBaseDir+"PATtuple_147_1_XQa.root",
sampleBaseDir+"PATtuple_150_1_lGf.root",
sampleBaseDir+"PATtuple_137_1_5EW.root",
sampleBaseDir+"PATtuple_405_1_wea.root",
sampleBaseDir+"PATtuple_221_1_jlQ.root",
sampleBaseDir+"PATtuple_214_1_1mn.root",
sampleBaseDir+"PATtuple_293_1_n5p.root",
sampleBaseDir+"PATtuple_299_1_jfm.root",
sampleBaseDir+"PATtuple_409_1_Q1h.root",
sampleBaseDir+"PATtuple_255_1_RvQ.root",
sampleBaseDir+"PATtuple_170_1_iAp.root",
sampleBaseDir+"PATtuple_368_1_dCY.root",
sampleBaseDir+"PATtuple_241_1_26Z.root",
sampleBaseDir+"PATtuple_261_1_c6m.root",
sampleBaseDir+"PATtuple_247_1_2Bv.root",
sampleBaseDir+"PATtuple_141_1_X9V.root",
sampleBaseDir+"PATtuple_287_1_JDA.root",
sampleBaseDir+"PATtuple_104_1_nae.root",
sampleBaseDir+"PATtuple_388_1_wYq.root",
sampleBaseDir+"PATtuple_169_1_rTB.root",
sampleBaseDir+"PATtuple_296_1_mnm.root",
sampleBaseDir+"PATtuple_125_1_aOr.root",
sampleBaseDir+"PATtuple_130_1_Oez.root",
sampleBaseDir+"PATtuple_100_1_uOk.root",
sampleBaseDir+"PATtuple_211_1_0VK.root",
sampleBaseDir+"PATtuple_146_1_w65.root",
sampleBaseDir+"PATtuple_219_1_L8B.root",
sampleBaseDir+"PATtuple_190_1_LPY.root",
sampleBaseDir+"PATtuple_298_1_63g.root",
sampleBaseDir+"PATtuple_327_1_vZf.root",
sampleBaseDir+"PATtuple_670_1_Fz7.root",
sampleBaseDir+"PATtuple_685_1_QVB.root",
sampleBaseDir+"PATtuple_664_1_RVl.root",
sampleBaseDir+"PATtuple_56_1_Mk1.root",
sampleBaseDir+"PATtuple_49_1_my6.root",
sampleBaseDir+"PATtuple_50_1_BCY.root",
sampleBaseDir+"PATtuple_47_1_jVi.root",
sampleBaseDir+"PATtuple_54_1_rmY.root",
sampleBaseDir+"PATtuple_45_1_3Hw.root",
sampleBaseDir+"PATtuple_24_1_dwa.root",
sampleBaseDir+"PATtuple_40_1_Sr0.root",
sampleBaseDir+"PATtuple_30_1_xXt.root",
sampleBaseDir+"PATtuple_22_1_xbe.root",
sampleBaseDir+"PATtuple_16_1_FZz.root",
sampleBaseDir+"PATtuple_25_1_1sN.root",
sampleBaseDir+"PATtuple_18_1_2kZ.root",
sampleBaseDir+"PATtuple_33_1_yMY.root",
sampleBaseDir+"PATtuple_39_1_K77.root",
sampleBaseDir+"PATtuple_35_1_04s.root",
sampleBaseDir+"PATtuple_5_1_qGJ.root",
sampleBaseDir+"PATtuple_19_1_Dyf.root",
sampleBaseDir+"PATtuple_37_1_O6a.root",
sampleBaseDir+"PATtuple_17_1_zWa.root",
sampleBaseDir+"PATtuple_43_1_Shy.root",
sampleBaseDir+"PATtuple_44_1_gn7.root",
sampleBaseDir+"PATtuple_21_1_bKk.root",
sampleBaseDir+"PATtuple_41_1_5Az.root",
sampleBaseDir+"PATtuple_13_1_WMT.root",
sampleBaseDir+"PATtuple_15_1_yOm.root",
sampleBaseDir+"PATtuple_32_1_FTc.root",
sampleBaseDir+"PATtuple_2_1_46K.root",
sampleBaseDir+"PATtuple_26_1_rMC.root",
sampleBaseDir+"PATtuple_27_1_BO4.root",
sampleBaseDir+"PATtuple_36_1_OQj.root",
sampleBaseDir+"PATtuple_11_1_3zb.root",
sampleBaseDir+"PATtuple_31_1_oVX.root",
sampleBaseDir+"PATtuple_34_1_h7d.root",
sampleBaseDir+"PATtuple_14_1_OET.root",
sampleBaseDir+"PATtuple_12_1_HrL.root",
sampleBaseDir+"PATtuple_8_1_MAx.root",
sampleBaseDir+"PATtuple_20_1_62K.root",
sampleBaseDir+"PATtuple_10_1_aEF.root",
sampleBaseDir+"PATtuple_28_1_Xnj.root",
sampleBaseDir+"PATtuple_6_1_Lgw.root",
sampleBaseDir+"PATtuple_42_1_2DN.root",
sampleBaseDir+"PATtuple_3_1_uI6.root",
sampleBaseDir+"PATtuple_38_1_uEb.root",
sampleBaseDir+"PATtuple_9_1_Oss.root",
sampleBaseDir+"PATtuple_1_1_WLw.root",
sampleBaseDir+"PATtuple_7_1_woT.root",
sampleBaseDir+"PATtuple_23_1_Mmr.root",
sampleBaseDir+"PATtuple_4_1_TkW.root",
]
