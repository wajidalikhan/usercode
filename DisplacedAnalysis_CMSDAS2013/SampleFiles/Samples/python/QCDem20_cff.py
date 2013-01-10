sampleDataSet = '/QCD_Pt_20_30_EMEnriched_TuneZ2star_8TeV_pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM'  

sampleCMSEnergy = 8000

sampleRelease = "CMSSW_5_3_2_patch4" # original (i.e. RECO file) release, not the one we plan to process them with
sampleProcessRelease = "CMSSW_5_3_5" # release used to create new files with

sampleNumEvents = 35040695

sampleXSec = 2.886E8 * 0.0101 # pb

# global tag can be extracted from file using edmProvDump filename|grep globaltag
# note however that this is the tag for *further* processing, not the original tag
sampleGlobalTag = 'START53_V7F::All'

sampleDuplicateCheckMode = 'checkAllFilesOpened'

sampleType = "BKGMC"


samplePatDBSName="/QCD_Pt_20_30_EMEnriched_TuneZ2star_8TeV_pythia6/ejclemen-QCDem20_pat_20121105-771324b3ed1c70ee461af1193683b519/USER"

sampleBaseDir="dcap://dcap.pp.rl.ac.uk///pnfs/pp.rl.ac.uk/data/cms/store/user/ejclemen//QCD_Pt_20_30_EMEnriched_TuneZ2star_8TeV_pythia6/QCDem20_pat_20121105/771324b3ed1c70ee461af1193683b519/"
samplePatFiles = [
sampleBaseDir+"PATtuple_159_1_1mV.root",
sampleBaseDir+"PATtuple_658_1_dMm.root",
sampleBaseDir+"PATtuple_559_1_OXs.root",
sampleBaseDir+"PATtuple_433_1_xud.root",
sampleBaseDir+"PATtuple_415_1_GFA.root",
sampleBaseDir+"PATtuple_147_1_GVp.root",
sampleBaseDir+"PATtuple_434_1_P7I.root",
sampleBaseDir+"PATtuple_153_1_leV.root",
sampleBaseDir+"PATtuple_437_1_JFZ.root",
sampleBaseDir+"PATtuple_268_0_3iv.root",
sampleBaseDir+"PATtuple_157_1_OSy.root",
sampleBaseDir+"PATtuple_557_1_XYp.root",
sampleBaseDir+"PATtuple_441_1_DgM.root",
sampleBaseDir+"PATtuple_338_0_xpD.root",
sampleBaseDir+"PATtuple_154_1_ebE.root",
sampleBaseDir+"PATtuple_439_1_n09.root",
sampleBaseDir+"PATtuple_435_1_LLk.root",
sampleBaseDir+"PATtuple_561_1_2y6.root",
sampleBaseDir+"PATtuple_438_1_V9N.root",
sampleBaseDir+"PATtuple_683_1_Mws.root",
sampleBaseDir+"PATtuple_149_1_YDz.root",
sampleBaseDir+"PATtuple_416_1_S4y.root",
sampleBaseDir+"PATtuple_560_1_AWu.root",
sampleBaseDir+"PATtuple_690_1_530.root",
sampleBaseDir+"PATtuple_602_1_Nwc.root",
sampleBaseDir+"PATtuple_685_1_ee6.root",
sampleBaseDir+"PATtuple_596_1_sTr.root",
sampleBaseDir+"PATtuple_558_1_IIy.root",
sampleBaseDir+"PATtuple_350_0_kEh.root",
sampleBaseDir+"PATtuple_431_1_ZqR.root",
sampleBaseDir+"PATtuple_70_1_i9r.root",
sampleBaseDir+"PATtuple_585_1_ore.root",
sampleBaseDir+"PATtuple_432_1_OLZ.root",
sampleBaseDir+"PATtuple_404_1_Exo.root",
sampleBaseDir+"PATtuple_406_1_TLx.root",
sampleBaseDir+"PATtuple_428_1_9gp.root",
sampleBaseDir+"PATtuple_578_1_aup.root",
sampleBaseDir+"PATtuple_264_0_VH7.root",
sampleBaseDir+"PATtuple_584_1_92y.root",
sampleBaseDir+"PATtuple_436_1_FoD.root",
sampleBaseDir+"PATtuple_442_1_Fwf.root",
sampleBaseDir+"PATtuple_604_1_P4P.root",
sampleBaseDir+"PATtuple_573_1_sKs.root",
sampleBaseDir+"PATtuple_329_0_foU.root",
sampleBaseDir+"PATtuple_694_1_qb9.root",
sampleBaseDir+"PATtuple_68_1_NnC.root",
sampleBaseDir+"PATtuple_96_1_J4K.root",
sampleBaseDir+"PATtuple_228_0_Jbd.root",
sampleBaseDir+"PATtuple_696_1_ewe.root",
sampleBaseDir+"PATtuple_680_1_8TK.root",
sampleBaseDir+"PATtuple_594_1_Avw.root",
sampleBaseDir+"PATtuple_155_1_1k0.root",
sampleBaseDir+"PATtuple_697_1_BQq.root",
sampleBaseDir+"PATtuple_595_1_NLB.root",
sampleBaseDir+"PATtuple_593_1_zEy.root",
sampleBaseDir+"PATtuple_152_1_muI.root",
sampleBaseDir+"PATtuple_555_1_hWh.root",
sampleBaseDir+"PATtuple_410_1_6H0.root",
sampleBaseDir+"PATtuple_266_0_EJP.root",
sampleBaseDir+"PATtuple_342_0_q39.root",
sampleBaseDir+"PATtuple_692_1_ElB.root",
sampleBaseDir+"PATtuple_599_1_CxF.root",
sampleBaseDir+"PATtuple_206_1_jfe.root",
sampleBaseDir+"PATtuple_550_1_aF3.root",
sampleBaseDir+"PATtuple_148_1_LtL.root",
sampleBaseDir+"PATtuple_90_1_GsV.root",
sampleBaseDir+"PATtuple_263_0_h91.root",
sampleBaseDir+"PATtuple_246_0_J9Y.root",
sampleBaseDir+"PATtuple_151_1_aKd.root",
sampleBaseDir+"PATtuple_598_1_yRi.root",
sampleBaseDir+"PATtuple_603_1_9gM.root",
sampleBaseDir+"PATtuple_695_1_Fxq.root",
sampleBaseDir+"PATtuple_554_1_QeG.root",
sampleBaseDir+"PATtuple_576_1_YNE.root",
sampleBaseDir+"PATtuple_207_1_W9v.root",
sampleBaseDir+"PATtuple_409_1_8PE.root",
sampleBaseDir+"PATtuple_600_1_GzZ.root",
sampleBaseDir+"PATtuple_444_1_rl9.root",
sampleBaseDir+"PATtuple_241_0_FgG.root",
sampleBaseDir+"PATtuple_689_1_4Eq.root",
sampleBaseDir+"PATtuple_242_0_mjM.root",
sampleBaseDir+"PATtuple_674_1_s7T.root",
sampleBaseDir+"PATtuple_570_1_ZrS.root",
sampleBaseDir+"PATtuple_671_1_F8v.root",
sampleBaseDir+"PATtuple_551_1_fP0.root",
sampleBaseDir+"PATtuple_670_1_yDH.root",
sampleBaseDir+"PATtuple_249_0_YwD.root",
sampleBaseDir+"PATtuple_543_1_gYH.root",
sampleBaseDir+"PATtuple_296_0_MRT.root",
sampleBaseDir+"PATtuple_305_0_9Ga.root",
sampleBaseDir+"PATtuple_289_0_sEO.root",
sampleBaseDir+"PATtuple_534_1_S1b.root",
sampleBaseDir+"PATtuple_256_0_hyx.root",
sampleBaseDir+"PATtuple_145_1_01x.root",
sampleBaseDir+"PATtuple_668_1_IsW.root",
sampleBaseDir+"PATtuple_274_0_t2x.root",
sampleBaseDir+"PATtuple_386_1_BYe.root",
sampleBaseDir+"PATtuple_240_0_hKA.root",
sampleBaseDir+"PATtuple_643_1_InU.root",
sampleBaseDir+"PATtuple_230_0_rcK.root",
sampleBaseDir+"PATtuple_136_1_lCq.root",
sampleBaseDir+"PATtuple_339_0_5td.root",
sampleBaseDir+"PATtuple_223_0_Gg7.root",
sampleBaseDir+"PATtuple_185_1_RLE.root",
sampleBaseDir+"PATtuple_233_0_W2i.root",
sampleBaseDir+"PATtuple_660_1_J4e.root",
sampleBaseDir+"PATtuple_698_1_2g9.root",
sampleBaseDir+"PATtuple_687_1_2Yk.root",
sampleBaseDir+"PATtuple_238_0_aVr.root",
sampleBaseDir+"PATtuple_652_1_jF0.root",
sampleBaseDir+"PATtuple_334_0_JMu.root",
sampleBaseDir+"PATtuple_232_0_Ntd.root",
sampleBaseDir+"PATtuple_227_0_nfX.root",
sampleBaseDir+"PATtuple_276_0_3qc.root",
sampleBaseDir+"PATtuple_681_1_fhf.root",
sampleBaseDir+"PATtuple_331_0_oZo.root",
sampleBaseDir+"PATtuple_225_0_RG1.root",
sampleBaseDir+"PATtuple_572_1_X5M.root",
sampleBaseDir+"PATtuple_535_1_WF9.root",
sampleBaseDir+"PATtuple_267_0_PUD.root",
sampleBaseDir+"PATtuple_327_0_vdm.root",
sampleBaseDir+"PATtuple_538_1_jm8.root",
sampleBaseDir+"PATtuple_649_1_Kpo.root",
sampleBaseDir+"PATtuple_528_1_aIT.root",
sampleBaseDir+"PATtuple_669_1_mHm.root",
sampleBaseDir+"PATtuple_676_1_8b7.root",
sampleBaseDir+"PATtuple_568_1_B5m.root",
sampleBaseDir+"PATtuple_645_1_Z4k.root",
sampleBaseDir+"PATtuple_653_1_MwP.root",
sampleBaseDir+"PATtuple_248_0_Yhv.root",
sampleBaseDir+"PATtuple_440_1_Ofr.root",
sampleBaseDir+"PATtuple_156_1_5ri.root",
sampleBaseDir+"PATtuple_443_1_b9P.root",
sampleBaseDir+"PATtuple_556_1_P4t.root",
sampleBaseDir+"PATtuple_158_1_NrR.root",
sampleBaseDir+"PATtuple_589_1_O9r.root",
sampleBaseDir+"PATtuple_345_0_jT8.root",
sampleBaseDir+"PATtuple_160_1_G3C.root",
sampleBaseDir+"PATtuple_273_0_16f.root",
sampleBaseDir+"PATtuple_693_1_8bM.root",
sampleBaseDir+"PATtuple_407_1_zY0.root",
sampleBaseDir+"PATtuple_580_1_ODU.root",
sampleBaseDir+"PATtuple_657_1_a7K.root",
sampleBaseDir+"PATtuple_659_1_uQs.root",
sampleBaseDir+"PATtuple_142_1_bMq.root",
sampleBaseDir+"PATtuple_277_0_jwl.root",
sampleBaseDir+"PATtuple_340_0_crC.root",
sampleBaseDir+"PATtuple_539_1_PFU.root",
sampleBaseDir+"PATtuple_609_1_lIb.root",
sampleBaseDir+"PATtuple_646_1_qOa.root",
sampleBaseDir+"PATtuple_213_0_XyK.root",
sampleBaseDir+"PATtuple_323_0_rgs.root",
sampleBaseDir+"PATtuple_265_0_8AX.root",
sampleBaseDir+"PATtuple_326_0_ujS.root",
sampleBaseDir+"PATtuple_651_1_y6G.root",
sampleBaseDir+"PATtuple_324_0_hek.root",
sampleBaseDir+"PATtuple_529_1_BkT.root",
sampleBaseDir+"PATtuple_251_0_KYN.root",
sampleBaseDir+"PATtuple_672_1_Ga3.root",
sampleBaseDir+"PATtuple_236_0_HrW.root",
sampleBaseDir+"PATtuple_591_1_mZV.root",
sampleBaseDir+"PATtuple_330_0_rLe.root",
sampleBaseDir+"PATtuple_422_1_dLx.root",
sampleBaseDir+"PATtuple_425_1_P56.root",
sampleBaseDir+"PATtuple_243_0_z76.root",
sampleBaseDir+"PATtuple_647_1_Bto.root",
sampleBaseDir+"PATtuple_262_0_HFi.root",
sampleBaseDir+"PATtuple_412_1_chF.root",
sampleBaseDir+"PATtuple_575_1_ri1.root",
sampleBaseDir+"PATtuple_418_1_9dp.root",
sampleBaseDir+"PATtuple_545_1_oDc.root",
sampleBaseDir+"PATtuple_234_0_mYO.root",
sampleBaseDir+"PATtuple_526_1_n7k.root",
sampleBaseDir+"PATtuple_581_1_ouT.root",
sampleBaseDir+"PATtuple_640_1_inz.root",
sampleBaseDir+"PATtuple_642_1_vRI.root",
sampleBaseDir+"PATtuple_258_0_QhN.root",
sampleBaseDir+"PATtuple_370_1_41C.root",
sampleBaseDir+"PATtuple_623_1_IrO.root",
sampleBaseDir+"PATtuple_395_1_JLh.root",
sampleBaseDir+"PATtuple_66_1_PFc.root",
sampleBaseDir+"PATtuple_639_1_AOD.root",
sampleBaseDir+"PATtuple_74_1_FnI.root",
sampleBaseDir+"PATtuple_71_1_zLc.root",
sampleBaseDir+"PATtuple_641_1_Jh2.root",
sampleBaseDir+"PATtuple_636_1_CnV.root",
sampleBaseDir+"PATtuple_606_1_dPH.root",
sampleBaseDir+"PATtuple_198_1_v6p.root",
sampleBaseDir+"PATtuple_380_1_Yga.root",
sampleBaseDir+"PATtuple_67_1_VaA.root",
sampleBaseDir+"PATtuple_325_0_lz3.root",
sampleBaseDir+"PATtuple_586_1_71r.root",
sampleBaseDir+"PATtuple_627_1_3bF.root",
sampleBaseDir+"PATtuple_500_1_v5R.root",
sampleBaseDir+"PATtuple_76_1_gzb.root",
sampleBaseDir+"PATtuple_628_1_qTI.root",
sampleBaseDir+"PATtuple_506_1_hDM.root",
sampleBaseDir+"PATtuple_517_1_K8Q.root",
sampleBaseDir+"PATtuple_524_1_OKm.root",
sampleBaseDir+"PATtuple_250_0_3Wr.root",
sampleBaseDir+"PATtuple_611_1_BNd.root",
sampleBaseDir+"PATtuple_181_1_xTW.root",
sampleBaseDir+"PATtuple_509_1_q1z.root",
sampleBaseDir+"PATtuple_387_1_SHE.root",
sampleBaseDir+"PATtuple_496_1_zlQ.root",
sampleBaseDir+"PATtuple_365_1_TZD.root",
sampleBaseDir+"PATtuple_371_1_FZ9.root",
sampleBaseDir+"PATtuple_490_1_KhD.root",
sampleBaseDir+"PATtuple_179_1_Gr5.root",
sampleBaseDir+"PATtuple_637_1_EYt.root",
sampleBaseDir+"PATtuple_525_1_a4t.root",
sampleBaseDir+"PATtuple_527_1_Pik.root",
sampleBaseDir+"PATtuple_455_1_91Y.root",
sampleBaseDir+"PATtuple_492_1_EBl.root",
sampleBaseDir+"PATtuple_169_1_mE6.root",
sampleBaseDir+"PATtuple_401_1_677.root",
sampleBaseDir+"PATtuple_622_1_hzG.root",
sampleBaseDir+"PATtuple_357_1_9gw.root",
sampleBaseDir+"PATtuple_564_1_qxg.root",
sampleBaseDir+"PATtuple_499_1_Bv5.root",
sampleBaseDir+"PATtuple_398_1_cta.root",
sampleBaseDir+"PATtuple_202_1_BiC.root",
sampleBaseDir+"PATtuple_662_1_spm.root",
sampleBaseDir+"PATtuple_237_0_aGI.root",
sampleBaseDir+"PATtuple_288_0_eh8.root",
sampleBaseDir+"PATtuple_613_1_q54.root",
sampleBaseDir+"PATtuple_344_0_fDl.root",
sampleBaseDir+"PATtuple_137_1_wam.root",
sampleBaseDir+"PATtuple_298_0_SNx.root",
sampleBaseDir+"PATtuple_346_0_ENI.root",
sampleBaseDir+"PATtuple_317_0_j3A.root",
sampleBaseDir+"PATtuple_146_1_M7k.root",
sampleBaseDir+"PATtuple_310_0_WR1.root",
sampleBaseDir+"PATtuple_279_0_aSP.root",
sampleBaseDir+"PATtuple_139_1_y5N.root",
sampleBaseDir+"PATtuple_271_0_4Fb.root",
sampleBaseDir+"PATtuple_571_1_tzD.root",
sampleBaseDir+"PATtuple_125_1_rpm.root",
sampleBaseDir+"PATtuple_381_1_WIQ.root",
sampleBaseDir+"PATtuple_297_0_1aB.root",
sampleBaseDir+"PATtuple_269_0_XJY.root",
sampleBaseDir+"PATtuple_131_1_WnB.root",
sampleBaseDir+"PATtuple_318_0_Xnc.root",
sampleBaseDir+"PATtuple_303_0_qFV.root",
sampleBaseDir+"PATtuple_132_1_0lO.root",
sampleBaseDir+"PATtuple_178_1_QdX.root",
sampleBaseDir+"PATtuple_335_0_xhM.root",
sampleBaseDir+"PATtuple_311_0_xmW.root",
sampleBaseDir+"PATtuple_302_0_QUl.root",
sampleBaseDir+"PATtuple_341_0_udg.root",
sampleBaseDir+"PATtuple_295_0_PIc.root",
sampleBaseDir+"PATtuple_313_0_9rf.root",
sampleBaseDir+"PATtuple_294_0_3xP.root",
sampleBaseDir+"PATtuple_312_0_D4W.root",
sampleBaseDir+"PATtuple_194_1_nPn.root",
sampleBaseDir+"PATtuple_546_1_GO3.root",
sampleBaseDir+"PATtuple_231_0_AEO.root",
sampleBaseDir+"PATtuple_314_0_Lga.root",
sampleBaseDir+"PATtuple_291_0_hBo.root",
sampleBaseDir+"PATtuple_540_1_id7.root",
sampleBaseDir+"PATtuple_391_1_pLm.root",
sampleBaseDir+"PATtuple_290_0_oVP.root",
sampleBaseDir+"PATtuple_419_1_cy2.root",
sampleBaseDir+"PATtuple_686_1_Bbi.root",
sampleBaseDir+"PATtuple_644_1_Y8b.root",
sampleBaseDir+"PATtuple_661_1_hZ8.root",
sampleBaseDir+"PATtuple_270_0_oGo.root",
sampleBaseDir+"PATtuple_278_0_XNd.root",
sampleBaseDir+"PATtuple_648_1_lRj.root",
sampleBaseDir+"PATtuple_336_0_M2h.root",
sampleBaseDir+"PATtuple_663_1_Itr.root",
sampleBaseDir+"PATtuple_304_0_bYc.root",
sampleBaseDir+"PATtuple_673_1_OVe.root",
sampleBaseDir+"PATtuple_309_0_bXZ.root",
sampleBaseDir+"PATtuple_333_0_CU1.root",
sampleBaseDir+"PATtuple_141_1_pg8.root",
sampleBaseDir+"PATtuple_281_0_FPM.root",
sampleBaseDir+"PATtuple_320_0_vpB.root",
sampleBaseDir+"PATtuple_135_1_yay.root",
sampleBaseDir+"PATtuple_224_0_tRw.root",
sampleBaseDir+"PATtuple_299_0_bXC.root",
sampleBaseDir+"PATtuple_282_0_1cH.root",
sampleBaseDir+"PATtuple_306_0_0oK.root",
sampleBaseDir+"PATtuple_688_1_pqL.root",
sampleBaseDir+"PATtuple_417_1_VQO.root",
sampleBaseDir+"PATtuple_190_1_pUX.root",
sampleBaseDir+"PATtuple_678_1_qbJ.root",
sampleBaseDir+"PATtuple_328_0_uJ4.root",
sampleBaseDir+"PATtuple_569_1_kNs.root",
sampleBaseDir+"PATtuple_369_1_6IO.root",
sampleBaseDir+"PATtuple_252_0_oVC.root",
sampleBaseDir+"PATtuple_239_0_wHu.root",
sampleBaseDir+"PATtuple_284_0_4wM.root",
sampleBaseDir+"PATtuple_192_1_TYU.root",
sampleBaseDir+"PATtuple_530_1_OcK.root",
sampleBaseDir+"PATtuple_396_1_4EA.root",
sampleBaseDir+"PATtuple_183_1_Bes.root",
sampleBaseDir+"PATtuple_498_1_NwV.root",
sampleBaseDir+"PATtuple_638_1_G7K.root",
sampleBaseDir+"PATtuple_445_1_KLZ.root",
sampleBaseDir+"PATtuple_384_1_obI.root",
sampleBaseDir+"PATtuple_195_1_8Bf.root",
sampleBaseDir+"PATtuple_393_1_qXo.root",
sampleBaseDir+"PATtuple_519_1_kdK.root",
sampleBaseDir+"PATtuple_394_1_jqB.root",
sampleBaseDir+"PATtuple_351_1_9tJ.root",
sampleBaseDir+"PATtuple_140_1_OAH.root",
sampleBaseDir+"PATtuple_495_1_CW8.root",
sampleBaseDir+"PATtuple_493_1_YN1.root",
sampleBaseDir+"PATtuple_507_1_TJ0.root",
sampleBaseDir+"PATtuple_516_1_SPi.root",
sampleBaseDir+"PATtuple_532_1_Go4.root",
sampleBaseDir+"PATtuple_522_1_gcq.root",
sampleBaseDir+"PATtuple_503_1_GVK.root",
sampleBaseDir+"PATtuple_504_1_2u4.root",
sampleBaseDir+"PATtuple_164_1_I6j.root",
sampleBaseDir+"PATtuple_197_1_VgQ.root",
sampleBaseDir+"PATtuple_184_1_uvF.root",
sampleBaseDir+"PATtuple_502_1_TkW.root",
sampleBaseDir+"PATtuple_515_1_jkW.root",
sampleBaseDir+"PATtuple_186_1_akI.root",
sampleBaseDir+"PATtuple_200_1_ZWL.root",
sampleBaseDir+"PATtuple_705_1_1EH.root",
sampleBaseDir+"PATtuple_565_1_pn1.root",
sampleBaseDir+"PATtuple_205_1_5UN.root",
sampleBaseDir+"PATtuple_400_1_hfS.root",
sampleBaseDir+"PATtuple_383_1_Di4.root",
sampleBaseDir+"PATtuple_364_1_Zcf.root",
sampleBaseDir+"PATtuple_521_1_hZH.root",
sampleBaseDir+"PATtuple_431_1_A4c.root",
sampleBaseDir+"PATtuple_447_1_S57.root",
sampleBaseDir+"PATtuple_78_1_112.root",
sampleBaseDir+"PATtuple_461_1_pzC.root",
sampleBaseDir+"PATtuple_465_1_p5I.root",
sampleBaseDir+"PATtuple_133_1_p9Z.root",
sampleBaseDir+"PATtuple_563_1_zJA.root",
sampleBaseDir+"PATtuple_477_1_Pcc.root",
sampleBaseDir+"PATtuple_470_1_VJM.root",
sampleBaseDir+"PATtuple_68_1_yZ7.root",
sampleBaseDir+"PATtuple_483_1_oVm.root",
sampleBaseDir+"PATtuple_415_1_FhG.root",
sampleBaseDir+"PATtuple_471_1_yfi.root",
sampleBaseDir+"PATtuple_75_1_ks3.root",
sampleBaseDir+"PATtuple_454_1_ClP.root",
sampleBaseDir+"PATtuple_476_1_il3.root",
sampleBaseDir+"PATtuple_204_1_j70.root",
sampleBaseDir+"PATtuple_449_1_PpI.root",
sampleBaseDir+"PATtuple_478_1_4Sq.root",
sampleBaseDir+"PATtuple_487_1_RLW.root",
sampleBaseDir+"PATtuple_486_1_7fZ.root",
sampleBaseDir+"PATtuple_459_1_f4B.root",
sampleBaseDir+"PATtuple_94_1_ctI.root",
sampleBaseDir+"PATtuple_482_1_obu.root",
sampleBaseDir+"PATtuple_463_1_iM3.root",
sampleBaseDir+"PATtuple_456_1_co2.root",
sampleBaseDir+"PATtuple_706_1_Nxx.root",
sampleBaseDir+"PATtuple_39_1_Jbf.root",
sampleBaseDir+"PATtuple_474_1_fWY.root",
sampleBaseDir+"PATtuple_123_1_uid.root",
sampleBaseDir+"PATtuple_484_1_Lec.root",
sampleBaseDir+"PATtuple_363_1_z8x.root",
sampleBaseDir+"PATtuple_472_1_Fs8.root",
sampleBaseDir+"PATtuple_134_1_Voo.root",
sampleBaseDir+"PATtuple_117_1_hup.root",
sampleBaseDir+"PATtuple_19_1_LWl.root",
sampleBaseDir+"PATtuple_33_1_jH1.root",
sampleBaseDir+"PATtuple_30_1_8xF.root",
sampleBaseDir+"PATtuple_481_1_fEA.root",
sampleBaseDir+"PATtuple_172_1_JsI.root",
sampleBaseDir+"PATtuple_479_1_v29.root",
sampleBaseDir+"PATtuple_451_1_cDe.root",
sampleBaseDir+"PATtuple_32_1_2Fz.root",
sampleBaseDir+"PATtuple_61_1_pwW.root",
sampleBaseDir+"PATtuple_47_1_hkX.root",
sampleBaseDir+"PATtuple_109_1_kZw.root",
sampleBaseDir+"PATtuple_173_1_w4X.root",
sampleBaseDir+"PATtuple_114_1_3hw.root",
sampleBaseDir+"PATtuple_245_0_sWI.root",
sampleBaseDir+"PATtuple_677_1_J6l.root",
sampleBaseDir+"PATtuple_255_0_Y3Q.root",
sampleBaseDir+"PATtuple_567_1_w90.root",
sampleBaseDir+"PATtuple_368_1_jXm.root",
sampleBaseDir+"PATtuple_420_1_YfV.root",
sampleBaseDir+"PATtuple_211_0_nwD.root",
sampleBaseDir+"PATtuple_608_1_Wq4.root",
sampleBaseDir+"PATtuple_699_1_Y48.root",
sampleBaseDir+"PATtuple_583_1_8Cu.root",
sampleBaseDir+"PATtuple_621_1_z3i.root",
sampleBaseDir+"PATtuple_218_0_mKw.root",
sampleBaseDir+"PATtuple_408_1_scg.root",
sampleBaseDir+"PATtuple_376_1_M3P.root",
sampleBaseDir+"PATtuple_633_1_uj4.root",
sampleBaseDir+"PATtuple_244_0_V6H.root",
sampleBaseDir+"PATtuple_601_1_dnt.root",
sampleBaseDir+"PATtuple_191_1_34c.root",
sampleBaseDir+"PATtuple_630_1_aBk.root",
sampleBaseDir+"PATtuple_620_1_jvm.root",
sampleBaseDir+"PATtuple_614_1_dNz.root",
sampleBaseDir+"PATtuple_632_1_8aq.root",
sampleBaseDir+"PATtuple_215_0_xaD.root",
sampleBaseDir+"PATtuple_392_1_PVQ.root",
sampleBaseDir+"PATtuple_578_1_3SJ.root",
sampleBaseDir+"PATtuple_128_1_Q2W.root",
sampleBaseDir+"PATtuple_254_0_vI6.root",
sampleBaseDir+"PATtuple_219_0_43l.root",
sampleBaseDir+"PATtuple_259_0_1hZ.root",
sampleBaseDir+"PATtuple_624_1_w7m.root",
sampleBaseDir+"PATtuple_610_1_GvS.root",
sampleBaseDir+"PATtuple_619_1_YJ4.root",
sampleBaseDir+"PATtuple_607_1_Wwh.root",
sampleBaseDir+"PATtuple_625_1_HWB.root",
sampleBaseDir+"PATtuple_514_1_9Nt.root",
sampleBaseDir+"PATtuple_209_0_ond.root",
sampleBaseDir+"PATtuple_260_0_tRZ.root",
sampleBaseDir+"PATtuple_617_1_cWd.root",
sampleBaseDir+"PATtuple_69_1_xyU.root",
sampleBaseDir+"PATtuple_261_0_HQP.root",
sampleBaseDir+"PATtuple_587_1_kTO.root",
sampleBaseDir+"PATtuple_700_1_cWj.root",
sampleBaseDir+"PATtuple_615_1_fTk.root",
sampleBaseDir+"PATtuple_702_1_GLY.root",
sampleBaseDir+"PATtuple_585_1_vN3.root",
sampleBaseDir+"PATtuple_378_1_OJb.root",
sampleBaseDir+"PATtuple_217_0_6ml.root",
sampleBaseDir+"PATtuple_214_0_Wsw.root",
sampleBaseDir+"PATtuple_577_1_U5J.root",
sampleBaseDir+"PATtuple_177_1_kMN.root",
sampleBaseDir+"PATtuple_629_1_hpM.root",
sampleBaseDir+"PATtuple_446_1_Kra.root",
sampleBaseDir+"PATtuple_631_1_NWz.root",
sampleBaseDir+"PATtuple_222_0_mbh.root",
sampleBaseDir+"PATtuple_257_0_53q.root",
sampleBaseDir+"PATtuple_597_1_3Eb.root",
sampleBaseDir+"PATtuple_612_1_ig5.root",
sampleBaseDir+"PATtuple_605_1_35R.root",
sampleBaseDir+"PATtuple_377_1_THt.root",
sampleBaseDir+"PATtuple_129_1_CcR.root",
sampleBaseDir+"PATtuple_216_0_ef2.root",
sampleBaseDir+"PATtuple_618_1_XiO.root",
sampleBaseDir+"PATtuple_582_1_sVR.root",
sampleBaseDir+"PATtuple_221_0_aYC.root",
sampleBaseDir+"PATtuple_220_0_azt.root",
sampleBaseDir+"PATtuple_208_0_ftt.root",
sampleBaseDir+"PATtuple_450_1_V6M.root",
sampleBaseDir+"PATtuple_616_1_AnA.root",
sampleBaseDir+"PATtuple_588_1_XGr.root",
sampleBaseDir+"PATtuple_81_1_quo.root",
sampleBaseDir+"PATtuple_488_1_4sz.root",
sampleBaseDir+"PATtuple_635_1_VNS.root",
sampleBaseDir+"PATtuple_584_1_ZAy.root",
sampleBaseDir+"PATtuple_63_1_wII.root",
sampleBaseDir+"PATtuple_212_0_d0y.root",
sampleBaseDir+"PATtuple_21_1_1zD.root",
sampleBaseDir+"PATtuple_143_1_U9Z.root",
sampleBaseDir+"PATtuple_2_1_s9D.root",
sampleBaseDir+"PATtuple_104_1_oba.root",
sampleBaseDir+"PATtuple_112_1_71e.root",
sampleBaseDir+"PATtuple_37_1_qGl.root",
sampleBaseDir+"PATtuple_27_1_c2o.root",
sampleBaseDir+"PATtuple_52_1_HWe.root",
sampleBaseDir+"PATtuple_120_1_fj8.root",
sampleBaseDir+"PATtuple_161_1_oav.root",
sampleBaseDir+"PATtuple_175_1_rAK.root",
sampleBaseDir+"PATtuple_115_1_yFF.root",
sampleBaseDir+"PATtuple_43_1_bsQ.root",
sampleBaseDir+"PATtuple_38_1_ZtZ.root",
sampleBaseDir+"PATtuple_62_1_PXY.root",
sampleBaseDir+"PATtuple_116_1_gpc.root",
sampleBaseDir+"PATtuple_119_1_FxM.root",
sampleBaseDir+"PATtuple_56_1_WZt.root",
sampleBaseDir+"PATtuple_108_1_8Tk.root",
sampleBaseDir+"PATtuple_171_1_MDX.root",
sampleBaseDir+"PATtuple_59_1_f74.root",
sampleBaseDir+"PATtuple_17_1_MyR.root",
sampleBaseDir+"PATtuple_46_1_RI0.root",
sampleBaseDir+"PATtuple_106_1_IJ0.root",
sampleBaseDir+"PATtuple_15_1_Jxb.root",
sampleBaseDir+"PATtuple_20_1_GqG.root",
sampleBaseDir+"PATtuple_105_1_na2.root",
sampleBaseDir+"PATtuple_29_1_O0j.root",
sampleBaseDir+"PATtuple_110_1_DNl.root",
sampleBaseDir+"PATtuple_174_1_rK1.root",
sampleBaseDir+"PATtuple_55_1_TuV.root",
sampleBaseDir+"PATtuple_31_1_A3r.root",
sampleBaseDir+"PATtuple_28_1_Bib.root",
sampleBaseDir+"PATtuple_366_1_r2v.root",
sampleBaseDir+"PATtuple_83_1_EcH.root",
sampleBaseDir+"PATtuple_367_1_bNK.root",
sampleBaseDir+"PATtuple_82_1_TMg.root",
sampleBaseDir+"PATtuple_24_1_G5C.root",
sampleBaseDir+"PATtuple_118_1_s68.root",
sampleBaseDir+"PATtuple_111_1_BdX.root",
sampleBaseDir+"PATtuple_26_1_b4l.root",
sampleBaseDir+"PATtuple_53_1_3QE.root",
sampleBaseDir+"PATtuple_50_1_HJd.root",
sampleBaseDir+"PATtuple_13_1_i1B.root",
sampleBaseDir+"PATtuple_93_1_vqF.root",
sampleBaseDir+"PATtuple_176_1_XBI.root",
sampleBaseDir+"PATtuple_92_1_TxT.root",
sampleBaseDir+"PATtuple_121_1_42M.root",
sampleBaseDir+"PATtuple_5_1_CNp.root",
sampleBaseDir+"PATtuple_51_1_E4J.root",
sampleBaseDir+"PATtuple_102_1_rXc.root",
sampleBaseDir+"PATtuple_40_1_J33.root",
sampleBaseDir+"PATtuple_42_1_9M8.root",
sampleBaseDir+"PATtuple_95_1_Ioc.root",
sampleBaseDir+"PATtuple_103_1_hb4.root",
sampleBaseDir+"PATtuple_58_1_6j4.root",
sampleBaseDir+"PATtuple_11_1_4aV.root",
sampleBaseDir+"PATtuple_49_1_7XE.root",
sampleBaseDir+"PATtuple_107_1_P7Z.root",
sampleBaseDir+"PATtuple_170_1_K9u.root",
sampleBaseDir+"PATtuple_353_1_aic.root",
sampleBaseDir+"PATtuple_35_1_8VS.root",
sampleBaseDir+"PATtuple_6_1_nwJ.root",
sampleBaseDir+"PATtuple_359_1_7XD.root",
sampleBaseDir+"PATtuple_354_1_Xtk.root",
sampleBaseDir+"PATtuple_86_1_8JC.root",
sampleBaseDir+"PATtuple_84_1_c0V.root",
sampleBaseDir+"PATtuple_362_1_xzc.root",
sampleBaseDir+"PATtuple_54_1_8o2.root",
sampleBaseDir+"PATtuple_22_1_psw.root",
sampleBaseDir+"PATtuple_23_1_ZWC.root",
sampleBaseDir+"PATtuple_41_1_RUB.root",
sampleBaseDir+"PATtuple_57_1_YYN.root",
sampleBaseDir+"PATtuple_100_1_AzL.root",
sampleBaseDir+"PATtuple_44_1_uvs.root",
sampleBaseDir+"PATtuple_25_1_E8t.root",
sampleBaseDir+"PATtuple_34_1_vlI.root",
sampleBaseDir+"PATtuple_48_1_hX6.root",
sampleBaseDir+"PATtuple_10_1_pzf.root",
sampleBaseDir+"PATtuple_45_1_rKH.root",
sampleBaseDir+"PATtuple_101_1_50Y.root",
sampleBaseDir+"PATtuple_80_1_GIZ.root",
sampleBaseDir+"PATtuple_675_1_Wxh.root",
sampleBaseDir+"PATtuple_691_1_aSC.root",
sampleBaseDir+"PATtuple_679_1_N7z.root",
sampleBaseDir+"PATtuple_308_0_19f.root",
sampleBaseDir+"PATtuple_592_1_NcH.root",
sampleBaseDir+"PATtuple_682_1_Dka.root",
sampleBaseDir+"PATtuple_590_1_SfV.root",
sampleBaseDir+"PATtuple_579_1_6l0.root",
sampleBaseDir+"PATtuple_247_0_KBU.root",
sampleBaseDir+"PATtuple_253_0_1Gs.root",
sampleBaseDir+"PATtuple_684_1_W2r.root",
sampleBaseDir+"PATtuple_549_1_uYM.root",
sampleBaseDir+"PATtuple_414_1_SYt.root",
sampleBaseDir+"PATtuple_189_1_Krg.root",
sampleBaseDir+"PATtuple_424_1_Z6F.root",
sampleBaseDir+"PATtuple_703_1_NDZ.root",
sampleBaseDir+"PATtuple_542_1_YKB.root",
sampleBaseDir+"PATtuple_536_1_Rnb.root",
sampleBaseDir+"PATtuple_512_1_QtU.root",
sampleBaseDir+"PATtuple_544_1_ktL.root",
sampleBaseDir+"PATtuple_552_1_lKe.root",
sampleBaseDir+"PATtuple_430_1_nXo.root",
sampleBaseDir+"PATtuple_533_1_IBD.root",
sampleBaseDir+"PATtuple_229_0_dPi.root",
sampleBaseDir+"PATtuple_531_1_rox.root",
sampleBaseDir+"PATtuple_427_1_iMP.root",
sampleBaseDir+"PATtuple_421_1_aqv.root",
sampleBaseDir+"PATtuple_547_1_UP4.root",
sampleBaseDir+"PATtuple_553_1_V3I.root",
sampleBaseDir+"PATtuple_537_1_iEe.root",
sampleBaseDir+"PATtuple_411_1_4Jj.root",
sampleBaseDir+"PATtuple_307_0_fUF.root",
sampleBaseDir+"PATtuple_347_0_ZeW.root",
sampleBaseDir+"PATtuple_429_1_RGZ.root",
sampleBaseDir+"PATtuple_316_0_LeE.root",
sampleBaseDir+"PATtuple_285_0_uGg.root",
sampleBaseDir+"PATtuple_280_0_L1P.root",
sampleBaseDir+"PATtuple_348_0_HWV.root",
sampleBaseDir+"PATtuple_292_0_nvq.root",
sampleBaseDir+"PATtuple_319_0_7w5.root",
sampleBaseDir+"PATtuple_124_1_GW8.root",
sampleBaseDir+"PATtuple_300_0_QlL.root",
sampleBaseDir+"PATtuple_130_1_6mE.root",
sampleBaseDir+"PATtuple_349_0_V2x.root",
sampleBaseDir+"PATtuple_321_0_AL3.root",
sampleBaseDir+"PATtuple_343_0_V2A.root",
sampleBaseDir+"PATtuple_287_0_DzW.root",
sampleBaseDir+"PATtuple_275_0_mo1.root",
sampleBaseDir+"PATtuple_315_0_kJD.root",
sampleBaseDir+"PATtuple_337_0_i0P.root",
sampleBaseDir+"PATtuple_272_0_6pR.root",
sampleBaseDir+"PATtuple_301_0_t8d.root",
sampleBaseDir+"PATtuple_293_0_lZ8.root",
sampleBaseDir+"PATtuple_283_0_8z0.root",
sampleBaseDir+"PATtuple_286_0_5MP.root",
sampleBaseDir+"PATtuple_127_1_6rr.root",
sampleBaseDir+"PATtuple_322_0_r2o.root",
sampleBaseDir+"PATtuple_180_1_bcI.root",
sampleBaseDir+"PATtuple_656_1_RQl.root",
sampleBaseDir+"PATtuple_665_1_Po6.root",
sampleBaseDir+"PATtuple_226_0_7Ut.root",
sampleBaseDir+"PATtuple_650_1_FYE.root",
sampleBaseDir+"PATtuple_235_0_fGS.root",
sampleBaseDir+"PATtuple_413_1_acT.root",
sampleBaseDir+"PATtuple_667_1_4Np.root",
sampleBaseDir+"PATtuple_654_1_xps.root",
sampleBaseDir+"PATtuple_426_1_l2A.root",
sampleBaseDir+"PATtuple_574_1_eUn.root",
sampleBaseDir+"PATtuple_704_1_CAp.root",
sampleBaseDir+"PATtuple_423_1_Sa6.root",
sampleBaseDir+"PATtuple_562_1_zX5.root",
sampleBaseDir+"PATtuple_210_0_iBo.root",
sampleBaseDir+"PATtuple_666_1_Jio.root",
sampleBaseDir+"PATtuple_541_1_FV6.root",
sampleBaseDir+"PATtuple_182_1_339.root",
sampleBaseDir+"PATtuple_664_1_TYS.root",
sampleBaseDir+"PATtuple_350_0_dpq.root",
sampleBaseDir+"PATtuple_655_1_EcN.root",
sampleBaseDir+"PATtuple_548_1_WP0.root",
sampleBaseDir+"PATtuple_626_1_0Ud.root",
sampleBaseDir+"PATtuple_566_1_sqq.root",
sampleBaseDir+"PATtuple_332_0_12s.root",
sampleBaseDir+"PATtuple_126_1_UPA.root",
sampleBaseDir+"PATtuple_634_1_hYZ.root",
sampleBaseDir+"PATtuple_520_1_QP3.root",
sampleBaseDir+"PATtuple_511_1_uUi.root",
sampleBaseDir+"PATtuple_361_1_Hea.root",
sampleBaseDir+"PATtuple_385_1_XJS.root",
sampleBaseDir+"PATtuple_494_1_aDt.root",
sampleBaseDir+"PATtuple_188_1_LPW.root",
sampleBaseDir+"PATtuple_501_1_olw.root",
sampleBaseDir+"PATtuple_389_1_Gic.root",
sampleBaseDir+"PATtuple_375_1_GEZ.root",
sampleBaseDir+"PATtuple_193_1_jzl.root",
sampleBaseDir+"PATtuple_199_1_gHq.root",
sampleBaseDir+"PATtuple_379_1_nYD.root",
sampleBaseDir+"PATtuple_138_1_EyO.root",
sampleBaseDir+"PATtuple_508_1_3sz.root",
sampleBaseDir+"PATtuple_518_1_AR0.root",
sampleBaseDir+"PATtuple_397_1_Uy3.root",
sampleBaseDir+"PATtuple_505_1_DeX.root",
sampleBaseDir+"PATtuple_373_1_5iY.root",
sampleBaseDir+"PATtuple_144_1_Cf0.root",
sampleBaseDir+"PATtuple_65_1_tVj.root",
sampleBaseDir+"PATtuple_510_1_23i.root",
sampleBaseDir+"PATtuple_513_1_tDl.root",
sampleBaseDir+"PATtuple_701_1_WNY.root",
sampleBaseDir+"PATtuple_374_1_sJe.root",
sampleBaseDir+"PATtuple_491_1_mEg.root",
sampleBaseDir+"PATtuple_150_1_rWY.root",
sampleBaseDir+"PATtuple_390_1_pKY.root",
sampleBaseDir+"PATtuple_203_1_xaC.root",
sampleBaseDir+"PATtuple_523_1_q5v.root",
sampleBaseDir+"PATtuple_497_1_ppE.root",
sampleBaseDir+"PATtuple_201_1_uU1.root",
sampleBaseDir+"PATtuple_382_1_blb.root",
sampleBaseDir+"PATtuple_372_1_oAn.root",
sampleBaseDir+"PATtuple_399_1_7UU.root",
sampleBaseDir+"PATtuple_448_1_y7e.root",
sampleBaseDir+"PATtuple_460_1_ibv.root",
sampleBaseDir+"PATtuple_196_1_vW7.root",
sampleBaseDir+"PATtuple_64_1_Uyw.root",
sampleBaseDir+"PATtuple_489_1_75j.root",
sampleBaseDir+"PATtuple_432_1_nbg.root",
sampleBaseDir+"PATtuple_187_1_zRR.root",
sampleBaseDir+"PATtuple_462_1_vMy.root",
sampleBaseDir+"PATtuple_388_1_xUV.root",
sampleBaseDir+"PATtuple_468_1_Jda.root",
sampleBaseDir+"PATtuple_165_1_5v7.root",
sampleBaseDir+"PATtuple_469_1_SR8.root",
sampleBaseDir+"PATtuple_475_1_ysY.root",
sampleBaseDir+"PATtuple_473_1_FOZ.root",
sampleBaseDir+"PATtuple_73_1_Abm.root",
sampleBaseDir+"PATtuple_457_1_wPc.root",
sampleBaseDir+"PATtuple_72_1_X3v.root",
sampleBaseDir+"PATtuple_452_1_N9j.root",
sampleBaseDir+"PATtuple_70_1_7TA.root",
sampleBaseDir+"PATtuple_466_1_fN3.root",
sampleBaseDir+"PATtuple_406_1_8Gv.root",
sampleBaseDir+"PATtuple_458_1_k83.root",
sampleBaseDir+"PATtuple_79_1_iKC.root",
sampleBaseDir+"PATtuple_464_1_2uD.root",
sampleBaseDir+"PATtuple_485_1_5hb.root",
sampleBaseDir+"PATtuple_77_1_B01.root",
sampleBaseDir+"PATtuple_467_1_Jwd.root",
sampleBaseDir+"PATtuple_480_1_Ufa.root",
sampleBaseDir+"PATtuple_428_1_4HN.root",
sampleBaseDir+"PATtuple_404_1_azf.root",
sampleBaseDir+"PATtuple_36_1_An0.root",
sampleBaseDir+"PATtuple_60_1_C1W.root",
sampleBaseDir+"PATtuple_113_1_PVj.root",
sampleBaseDir+"PATtuple_355_1_u5w.root",
sampleBaseDir+"PATtuple_356_1_k5S.root",
sampleBaseDir+"PATtuple_12_1_pmW.root",
sampleBaseDir+"PATtuple_91_1_ESY.root",
sampleBaseDir+"PATtuple_14_1_RrE.root",
sampleBaseDir+"PATtuple_402_1_J58.root",
sampleBaseDir+"PATtuple_88_1_uB0.root",
sampleBaseDir+"PATtuple_8_1_rgD.root",
sampleBaseDir+"PATtuple_18_1_XfS.root",
sampleBaseDir+"PATtuple_7_1_zUC.root",
sampleBaseDir+"PATtuple_352_1_PSZ.root",
sampleBaseDir+"PATtuple_87_1_og1.root",
sampleBaseDir+"PATtuple_9_1_U6c.root",
sampleBaseDir+"PATtuple_358_1_Kva.root",
sampleBaseDir+"PATtuple_1_1_mPH.root",
sampleBaseDir+"PATtuple_16_1_FXm.root",
sampleBaseDir+"PATtuple_405_1_kaP.root",
sampleBaseDir+"PATtuple_89_1_Bpk.root",
sampleBaseDir+"PATtuple_163_1_OEw.root",
sampleBaseDir+"PATtuple_167_1_qzA.root",
sampleBaseDir+"PATtuple_85_1_lhk.root",
sampleBaseDir+"PATtuple_168_1_PM6.root",
sampleBaseDir+"PATtuple_360_1_0vR.root",
sampleBaseDir+"PATtuple_3_1_RHY.root",
sampleBaseDir+"PATtuple_98_1_bfh.root",
sampleBaseDir+"PATtuple_162_1_XAC.root",
sampleBaseDir+"PATtuple_166_1_vze.root",
sampleBaseDir+"PATtuple_403_1_65x.root",
sampleBaseDir+"PATtuple_97_1_Aa5.root",
sampleBaseDir+"PATtuple_453_1_juT.root",
sampleBaseDir+"PATtuple_99_1_I3f.root",
sampleBaseDir+"PATtuple_4_1_DLI.root",
sampleBaseDir+"PATtuple_122_1_AAj.root",
]
