import ROOT as r
import math
from GetParameters import *

# Be aware of the following hardcoded parameters:
#  * range of mass fit [15,500]
#  * details of background PDFs (now both electron and muon)
#
# The upper bound of the sigma search space is now
# dynamically determined -- given that we expect a limit
# of approximately 3/(lumi*eff) I've set the upper bound at
# 10x this.

# return RooWorkspace given the mass hypothesis

def GetWorkspaceSigma(M,LeptonType,eff,efferr):

	# GetParameters for mass hypothesis
	pars = GetParameters(M,"dataFile"+LeptonType)
	
	# Create RooRealVars for input parameters (hardcoded for now)
	Bkg = r.RooRealVar("Bkg","Bkg",pars['Bkg'])
	#BkgE = r.RooRealVar("BkgE","BkgE",pars['BkgE']) # for Gaussian
	BkgE = r.RooRealVar("BkgE","BkgE",1 + pars['BkgE']/pars['Bkg']) # for lognormal
	SigWidth = r.RooRealVar("SigWidth","SigWidth",pars['SigWidth'])

	# Total error = error + systematic
	SigWidthE = pars['SigWidthE']
	SigWidthSyst = pars['SigWidthSyst']*pars['SigWidth']
	SigWidthTotE = math.sqrt(SigWidthE*SigWidthE+SigWidthSyst*SigWidthSyst)
	# Now include the systematic as well
	#SigWidthE = r.RooRealVar("SigWidthE","SigWidthE",SigWidthTotE) # for Gaussian 
	SigWidthE = r.RooRealVar("SigWidthE","SigWidthE",1 + SigWidthTotE/pars['SigWidth']) # for Lognormal

	SigEff = r.RooRealVar("SigEff","SigEff",eff)
	# now we read the sigeff directly from the command line
	#SigEffE = r.RooRealVar("SigEffE","SigEffE",pars['SigEffE']*eff) # for Gaussian
	#SigEffE = r.RooRealVar("SigEffE","SigEffE",1 + pars['SigEffE']) # for lognormal
	#SigEffE = r.RooRealVar("SigEffE","SigEffE",efferr) # for Gaussian
	if (eff > 0):
		SigEffE = r.RooRealVar("SigEffE","SigEffE",1 + efferr/eff) # for lognormal
	else:
		SigEffE = r.RooRealVar("SigEffE", "SigEffE", 1)

	Lumi = r.RooRealVar("Lumi", "Lumi", pars['Lumi'])
	#LumiE = r.RooRealVar("LumiE", "LumiE", pars['LumiErr']*Lumi.getVal()) # for Gaussian
	LumiE = r.RooRealVar("LumiE", "LumiE", 1+pars['LumiErr']) # for lognormal

	# observable 
	mass = r.RooRealVar("mass","mass",15,500)

	# some variables to work with, s, b, mean, sigWidth, sigEff
	sUpperBound = 30/(pars['Lumi']*eff)
	print "upper limit of search space is: " + str(sUpperBound)
	s = r.RooRealVar("S","S",0,0,sUpperBound)
	b = r.RooRealVar("B","B",Bkg.getVal(),max(0,Bkg.getVal()-5*pars['BkgE'],Bkg.getVal()+5*pars['BkgE']))
	b.Print()
	mean = r.RooRealVar("mean","mean",M)
	sigWidth = r.RooRealVar("sigWidth","sigWidth",SigWidth.getVal(),SigWidth.getVal()-5*pars['SigWidthE'],SigWidth.getVal()+5*pars['SigWidthE'])
	sigEff = r.RooRealVar("sigEff","sigEff",SigEff.getVal(),SigEff.getVal()*(1-5*pars['SigEffE']),SigEff.getVal()*(1+5*pars['SigEffE']))
	lumi = r.RooRealVar("lumi","lumi",Lumi.getVal(),Lumi.getVal()*(1-5*pars['LumiErr']),Lumi.getVal()*(1+5*pars['LumiErr']))
	seff = r.RooFormulaVar("seff","@0*@1*@2",r.RooArgList(s,sigEff,lumi))

	# prior PDFs on nuisance parameters; now use lognormal as preferred by statistics committee
	#prior_sigWidth = r.RooGaussian("prior_sigWidth","prior_sigWidth",sigWidth,SigWidth,SigWidthE)
	prior_sigWidth = r.RooLognormal("prior_sigWidth","prior_sigWidth",sigWidth,SigWidth,SigWidthE)
	#prior_b = r.RooGaussian("prior_b","prior_b",b,Bkg,BkgE)
	prior_b = r.RooLognormal("prior_b","prior_b",b,Bkg,BkgE)
	#prior_sigEff = r.RooGaussian("prior_sigEff","prior_sigEFf",sigEff,SigEff,SigEffE)
	prior_sigEff = r.RooLognormal("prior_sigEff","prior_sigEFf",sigEff,SigEff,SigEffE)
	#prior_lumi = r.RooGaussian("prior_lumi", "prior_lumi", lumi, Lumi, LumiE)
	prior_lumi = r.RooLognormal("prior_lumi", "prior_lumi", lumi, Lumi, LumiE)

	prior_nuisance = r.RooProdPdf("prior_nuisance","prior_nuisance",r.RooArgList(prior_sigWidth,prior_b,prior_sigEff,prior_lumi))

	# shapes of signal and background
	signalPdf = r.RooGaussian("signalPdf","signalPdf",mass,mean,sigWidth)

	weight = r.RooRealVar("weight","weight",1,0,50)

	if LeptonType.find("Electron") == 0:
		bkgdataTmp = r.RooDataSet.read("WinterSelection/masses_data_elecloose_1.txt",r.RooArgList(mass,weight))
	elif LeptonType.find("Muon") == 0:
		bkgdataTmp = r.RooDataSet.read("WinterSelection/masses_data_muloose_1.txt",r.RooArgList(mass,weight))
	else:
		print "Don't know how to construct background model for "+LeptonType

	bkgdata = r.RooDataSet(bkgdataTmp.GetName(),bkgdataTmp.GetTitle(),bkgdataTmp,bkgdataTmp.get(),"",weight.GetName())

	if (LeptonType.find("Electron") == 0):
		mean_bw = r.RooRealVar("mean_bw", "mean_bw", 91.20)
		width_bw = r.RooRealVar("width_bw", "width_bw", 3.60)
		c = r.RooRealVar("c", "c", 0.868)
		turnon = r.RooRealVar("turnon", "turnon", 120.8)
		turnon_width = r.RooRealVar("turnon_width", "turnon_width", 51.7)
	else:
		mean_bw = r.RooRealVar("mean_bw", "mean_bw", 90.98)
		width_bw = r.RooRealVar("width_bw", "width_bw", 4.16)
		c = r.RooRealVar("c", "c", 0.961)
		turnon = r.RooRealVar("turnon", "turnon", 124.1)
		turnon_width = r.RooRealVar("turnon_width", "turnon_width", 52.1)

	bkg_bw = r.RooBreitWigner("BW", "BW", mass, mean_bw, width_bw)
	bkg_m4 = r.RooGenericPdf("powerWithTurnOn", "(TMath::Erf((@0-@1)/@2)+1)/(@0*@0*@0)", r.RooArgList(mass, turnon, turnon_width))
	bkgPdf = r.RooAddPdf("bkgPdf", "bkgPdf", bkg_bw, bkg_m4, c)
	# bkgPdf.fitTo(bkgdata,r.RooFit.SumW2Error(r.kTRUE))

	# model 
	model_no_nuis = r.RooAddPdf("model_no_nuis","model_no_nuis",r.RooArgList(signalPdf,bkgPdf),r.RooArgList(seff,b))
	model = r.RooProdPdf("model","model",model_no_nuis,prior_nuisance)

	# define parameter sets
	observables = r.RooArgSet(mass)
	nuisanceParameters = r.RooArgSet(b,sigWidth,sigEff,lumi)
	POI = r.RooArgSet(s)

	# modelConfig
	w = r.RooWorkspace('WS'+str(int(M)))
	modelCfg = r.RooStats.ModelConfig('modelCfg',w)
	modelCfg.SetPdf(model)
	modelCfg.SetObservables(observables)
	modelCfg.SetNuisanceParameters(nuisanceParameters)
	modelCfg.SetParametersOfInterest(POI)

	w.Print()

	return w
