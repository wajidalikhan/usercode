#ifndef __CINT__
#include "RooGlobalFunc.h"
#endif

#include "RooRealVar.h"
#include "RooDataSet.h"
#include "RooAddPdf.h"
#include "RooGaussian.h"
#include "RooChebychev.h"
#include "RooCBShape.h"
#include "RooPlot.h"
#include "RooMCStudy.h"
#include "RooFitResult.h"
#include "RooWorkspace.h"
#include "RooKeysPdf.h"
#include "RooConstVar.h"

#include "RooStats/ModelConfig.h"
#include "RooStats/ProfileLikelihoodCalculator.h"
#include "RooStats/LikelihoodInterval.h"
#include "RooStats/LikelihoodIntervalPlot.h"

#include "TROOT.h"
#include "TStyle.h"
#include "TDirectory.h"
#include "TCanvas.h"
#include "TFile.h"
#include "TAxis.h"
#include "TPaveLabel.h"
#include "RooHist.h"
#include "TPaveText.h"
#include "TText.h"
//#include "TMath"

/*INPUTs*/

double mass_l = 7.0;
double mass_h = 14.0;
#define mmin_ mass_l 
#define mmax_ mass_h
#define fmin_ mass_l
#define fmax_ mass_h
double muonpTcut = 4;  //single muon pT cut
double binw_ = 0.1;    //bin width of the histogram

bool PbPb = 1;         //Input data sample.  1: PbPb data;   0: pp data

bool fitMB = 1;        //1: fit the the Minbias sample(0-100%);   0: fit the each centrality bin
double width_ = 0.0782;//new resolution for 2011 HI data

bool plotpars = 0;     //1: plot parameters;   0: plot CMS label
bool doMinos = 0;      //kFALSE;

int bkgdModel = 3;     //Background Model.  1: LS erf*exp + polynomial; 2: LS RookeyPdf + polynomial; 3: erf*exp; 4: polynomial; 5: erf*exp+polynomial
bool plotLikeSign = 0; //1: plot likesign or trkRot data points and fit lines; 0: hide likesign or trkRot
bool TRKROT = 0;       //0: use likesign;   1: use track rotation
bool LS_constrain = 0; //1: use constrain method

bool PR_plot = 0;      //1: draw the PR plot
bool RAA = 0;          //1: raa PR plot;   0: double ratio PR plot

RooRealVar *f2Svs1S_pp = new RooRealVar("N_{2S}/N_{1S}pp","Y(3S)/Y(1S) yields pp ratio",0.59,-1,5);
RooRealVar *f3Svs1S_pp = new RooRealVar("N_{3S}/N_{1S}pp","Y(2S)/Y(1S) yields pp ratio",0.41,-1,5);
ofstream outfile("fitresults.out", ios_base::app);

TString finput;
TString figName_;

TString figs_("finalplots/"); //output fig location
const TString dirname_("");//"upsilonYield"); tree location in input file 
TString paramOn_("");
TString suffix_, cut_;

using namespace RooFit;
using namespace RooStats;
void fitpeaks(int bin);
void sidebandFit(bool, RooRealVar*, RooRealVar*, RooRealVar*, RooAbsPdf*, RooAbsPdf*, RooDataSet*, RooPlot*);
void suppression(RooRealVar*, RooFitResult*, RooAbsPdf*, RooAbsPdf*, int, RooDataSet*, RooPlot*);
void setUpLimits(float xMin, float xMax, RooAbsPdf*, RooDataSet*, RooRealVar*, float baseNll);
pair<double, double> ConfidencInterval(float, RooRealVar *fnll, RooDataSet *data, RooAbsPdf *pdf);

void fitUpsilonYields(){
	gROOT->LoadMacro("setTDRStyle_modified.C");
	//setTDRStyle();

	if (PbPb) {
		finput = "/home/zhenhu/HI2011/dimuonTree_HI2011_fulldataset_trkRot.root";
		figName_ = "masspeak_Hi"; //output fig names
	}
	else {
		finput = "/home/zhenhu/HI2011/dimuonTree_2011_pp.root";
		figName_ = "masspeak_pp_HIrereco";
	}

	//different binning:
	fitpeaks(0);
	//	fitpeaks(1);
	//	fitpeaks(2);
	//	fitpeaks(3);
	//	fitpeaks(4);
	//	fitpeaks(5);
	//	fitpeaks(6);
	//	fitpeaks(7);
	//	fitpeaks(8);
	//	fitpeaks(9);
	//	fitpeaks(10);
	//	fitpeaks(11);
	//	fitpeaks(12);
	//	fitpeaks(13);
}

	void fitpeaks(int bin){
		switch (bin)
		{
			case 0:
				cut_="abs(upsRapidity)<2.4";
				//cut_="( (muPlusPt>3.5 && abs(muPlusEta)<1.6) || (muPlusPt>2.5 && abs(muPlusEta)>=1.6 && abs(muPlusEta)<2.4) ) && ( (muMinusPt>3.5 && abs(muMinusEta)<1.6) || (muMinusPt>2.5 && abs(muMinusEta)>=1.6 && abs(muMinusEta)<2.4) ) && abs(upsRapidity)<2.0";   //pp acceptance for Upsilon 
				suffix_="";
				f2Svs1S_pp->setVal(0.5569);
				//f2Svs1S_pp->setVal(0);
				f3Svs1S_pp->setVal(0.4140);
				//f3Svs1S_pp->setVal(0);
				break;
			case 1:
				cut_="abs(upsRapidity)>=0.0 && abs(upsRapidity)<1.2";
				suffix_="_eta0-12"; binw_=0.14;
				break;
			case 2:
				cut_="abs(upsRapidity)>=1.2 && abs(upsRapidity)<2.4";
				suffix_="_eta12-24"; binw_=0.14;
				break;
			case 3:
				cut_="Centrality>=0 && Centrality<2";
				suffix_="_cntr0-5"; binw_=0.14;
				break;
			case 4:
				cut_="Centrality>=2 && Centrality<4";
				suffix_="_cntr5-10"; binw_=0.14;
				break;
			case 5:
				cut_="Centrality>=4 && Centrality<8";
				suffix_="_cntr10-20"; binw_=0.14;
				break;
			case 6:
				cut_="Centrality>=8 && Centrality<12";
				suffix_="_cntr20-30"; binw_=0.14;
				break;
			case 7:
				cut_="Centrality>=12 && Centrality<16";
				suffix_="_cntr30-40"; binw_=0.14;
				break;
			case 8:
				cut_="Centrality>=16 && Centrality<20";
				suffix_="_cntr40-50"; binw_=0.14;
				break;
			case 9:
				cut_="Centrality>=20 && Centrality<50";
				suffix_="_cntr50-100"; binw_=0.14;
				break;
			case 10:
				cut_="Centrality>=20 && Centrality<24";
				suffix_="_cntr50-60"; binw_=0.14;
				break;
			case 11:
				cut_="Centrality>=0 && Centrality<8";
				suffix_="_cntr0-20"; binw_=0.1;
				break;
			case 12:
				cut_="Centrality>=16 && Centrality<50";
				suffix_="_cntr40-100"; binw_=0.14;
				break;
			case 13:
				cut_="Centrality>=8 && Centrality<50";
				suffix_="_cntr20-100"; binw_=0.1;
				break;
			default:
				cout<<"error in binning"<<endl;
				break;
		}

		cout << "oniafitter processing"
			<< "\n\tInput:  \t" << finput
			<< "\n\tresults:\t" << figs_
			<< endl;
		ofstream outfile("fitresults.out", ios_base::app);
		outfile<<endl<<"**********"<<suffix_<<"**********"<<endl<<endl;

		//read the data
		TFile f(finput,"read");
		gDirectory->Cd(finput+":/"+dirname_);
		TTree* theTree     = (TTree*)gROOT->FindObject("UpsilonTree");
		TTree* allsignTree     = (TTree*)gROOT->FindObject("UpsilonTree_allsign");
		if (PR_plot) {TRKROT = 1; PbPb=1;}
		if (TRKROT) TTree* trkRotTree = (TTree*)gROOT->FindObject("UpsilonTree_trkRot");

		RooRealVar* mass  = new RooRealVar("invariantMass","#mu#mu mass",mmin_,mmax_,"GeV/c^{2}");
		RooRealVar* upsPt  = new RooRealVar("upsPt","p_{T}(#Upsilon)",0,60,"GeV");
		RooRealVar* upsEta = new RooRealVar("upsEta",  "upsEta"  ,-7,7);
		RooRealVar* upsRapidity = new RooRealVar("upsRapidity",  "upsRapidity"  ,-2.4,2.4);
		RooRealVar* vProb = new RooRealVar("vProb",  "vProb"  ,0.05,1.00);
		RooRealVar* QQsign = new RooRealVar("QQsign",  "QQsign"  ,-1,5);
		RooRealVar* weight = new RooRealVar("weight",  "weight"  ,-2,2);
		if (PbPb) RooRealVar* Centrality = new RooRealVar("Centrality",  "Centrality"  ,0,40);
		RooRealVar* muPlusPt = new RooRealVar("muPlusPt","muPlusPt",muonpTcut,50);
		RooRealVar* muPlusEta = new RooRealVar("muPlusEta","muPlusEta",-2.5,2.5);
		RooRealVar* muMinusPt = new RooRealVar("muMinusPt","muMinusPt",muonpTcut,50);
		RooRealVar* muMinusEta = new RooRealVar("muMinusEta","muMinusEta",-2.5,2.5);


		//import unlike-sign data set
		RooDataSet* data0, *data, *likesignData0, *likesignData, *TrkRotData0, *TrkRotData;
		if (PbPb) data0 = new RooDataSet("data","data",theTree,RooArgSet(*mass,*upsRapidity,*vProb,*upsPt,*Centrality,*muPlusPt,*muMinusPt));
		//data0 = new RooDataSet("data","data",theTree,RooArgSet(*mass,*upsRapidity,*upsPt,*muPlusPt,*muMinusPt,*QQsign,*weight));
		else data0 = new RooDataSet("data","data",theTree,RooArgSet(*mass,*upsRapidity,*vProb,*upsPt,*muPlusPt,*muMinusPt,*muPlusEta,*muMinusEta));
		data0->Print();
		data = ( RooDataSet*) data0->reduce(Cut(cut_));
		data->Print();

		//import like-sign data set
		if (PbPb) likesignData0 = new RooDataSet("likesignData","likesignData",allsignTree,RooArgSet(*mass,*upsRapidity,*vProb,*upsPt,*Centrality,*muPlusPt,*muMinusPt,*QQsign));
		else likesignData0 = new RooDataSet("likesignData","likesignData",allsignTree,RooArgSet(*mass,*upsRapidity,*vProb,*upsPt,*muPlusPt,*muMinusPt,*QQsign));
		likesignData0->Print();
		likesignData = ( RooDataSet*) likesignData0->reduce(Cut(cut_+" && QQsign != 0"));
		likesignData->Print();


		//import track-rotation data set
		if (TRKROT) {
			if (PbPb) TrkRotData0 = new RooDataSet("TrkRotData","TrkRotData",trkRotTree,RooArgSet(*mass,*upsRapidity,*vProb,*upsPt,*Centrality,*muPlusPt,*muMinusPt,*QQsign));
			else TrkRotData0 = new RooDataSet("TrkRotData","TrkRotData",trkRotTree,RooArgSet(*mass,*upsRapidity,*upsPt,*vProb,*muPlusPt,*muMinusPt,*QQsign));
			TrkRotData0->Print();
			if (PR_plot && RAA) TrkRotData = ( RooDataSet*) TrkRotData0->reduce(Cut(cut_+" && upsPt < 8.1"));
			else if (PR_plot && !RAA) TrkRotData = ( RooDataSet*) TrkRotData0->reduce(Cut(cut_+" && upsPt < 7.07"));
			else TrkRotData = ( RooDataSet*) TrkRotData0->reduce(Cut(cut_+" && QQsign != 0"));
			TrkRotData->Print();
		}

		mass->setRange("R1",7.0,10.2);
		mass->setRange("R2",7,14);
		mass->setRange("R3",10.8,14);
		const double M1S = 9.46;   //upsilon 1S pgd mass value
		const double M2S = 10.02;  //upsilon 2S pgd mass value
		const double M3S = 10.35;  //upsilon 3S pgd mass value

		RooRealVar *mean    = new RooRealVar("#mu_{#Upsilon(1S)}","#Upsilon mean",M1S,M1S-0.1,M1S+0.1);
		RooRealVar *shift21 = new RooRealVar("shift2","mass diff #Upsilon(1,2S)",M2S-M1S);
		RooRealVar *shift31 = new RooRealVar("shift3","mass diff #Upsilon(1,3S)",M3S-M1S);
		RooRealVar *mscale  = new RooRealVar("mscale","mass scale factor",1.,0.7,1.3);
		mscale->setConstant(kTRUE); /* the def. parameter value is fixed in the fit */
		RooFormulaVar *mean1S = new RooFormulaVar("mean1S","@0",
				RooArgList(*mean));
		RooFormulaVar *mean2S = new RooFormulaVar("mean2S","@0+@1*@2",
				RooArgList(*mean,*mscale,*shift21));
		RooFormulaVar *mean3S = new RooFormulaVar("mean3S","@0+@1*@2",
				RooArgList(*mean,*mscale,*shift31));

		RooRealVar *sigma1 = new RooRealVar("sigma","Sigma_1",0.10,0.01,0.30);    //detector resolution
		RooRealVar *sigma2 = new RooRealVar("#sigma_{#Upsilon(1S)}","Sigma_1S",0.08,0.01,0.30); //Y(1S) resolution
		RooFormulaVar *reso1S = new RooFormulaVar("reso1S","@0"             ,RooArgList(*sigma2));
		RooFormulaVar *reso2S = new RooFormulaVar("reso2S","@0*10.023/9.460",RooArgList(*sigma2));
		RooFormulaVar *reso3S = new RooFormulaVar("reso3S","@0*10.355/9.460",RooArgList(*sigma2));

		/// to describe final state radiation tail on the left of the peaks
		RooRealVar *alpha  = new RooRealVar("alpha","tail shift",0.982,0,2.4);   // minbias fit value
		//RooRealVar *alpha  = new RooRealVar("alpha","tail shift",1.6,0.2,4);   // MC value
		RooRealVar *npow   = new RooRealVar("npow","power order",2.3,1,3);       // MC value
		npow ->setConstant(kTRUE);
		if (!fitMB) alpha->setConstant(kTRUE);
		// relative fraction of the two peak components 
		RooRealVar *sigmaFraction = new RooRealVar("sigmaFraction","Sigma Fraction",0.3,0.,1.);
		sigmaFraction->setVal(0);
		sigmaFraction->setConstant(kTRUE);

		/// Upsilon 1S
		//RooCBShape  *gauss1S1 = new RooCBShape ("gauss1S1", "FSR cb 1s",
		//                  *mass,*mean1S,*sigma1,*alpha,*npow);
		RooCBShape  *gauss1S2 = new RooCBShape ("gauss1S2", "FSR cb 1s",
				*mass,*mean1S,*reso1S,*alpha,*npow);
		//RooAddPdf *sig1S      = new RooAddPdf  ("sig1S","1S mass pdf",
		//                  RooArgList(*gauss1S1,*gauss1S2),*sigmaFraction);

		//mean->setVal(9.46);
		//mean->setConstant(kTRUE);
		sigma1->setVal(0);
		sigma1->setConstant(kTRUE);
		if (!fitMB) {
			sigma2->setVal(width_);        //fix the resolution
			sigma2->setConstant(kTRUE);
		}
		/// Upsilon 2S
		RooCBShape  *gauss2S1 = new RooCBShape ("gauss2S1", "FSR cb 2s", 
				*mass,*mean2S,*sigma1,*alpha,*npow); 
		RooCBShape  *gauss2S2 = new RooCBShape ("gauss2S2", "FSR cb 2s", 
				*mass,*mean2S,*reso2S,*alpha,*npow); 
		RooAddPdf *sig2S      = new RooAddPdf  ("sig2S","2S mass pdf",
				RooArgList(*gauss2S1,*gauss2S2),*sigmaFraction);

		/// Upsilon 3S
		RooCBShape  *gauss3S1 = new RooCBShape ("gauss3S1", "FSR cb 3s", 
				*mass,*mean3S,*sigma1,*alpha,*npow); 
		RooCBShape  *gauss3S2 = new RooCBShape ("gauss3S2", "FSR cb 3s", 
				*mass,*mean3S,*reso3S,*alpha,*npow); 
		RooAddPdf *sig3S      = new RooAddPdf  ("sig3S","3S mass pdf",
				RooArgList(*gauss3S1,*gauss3S2),*sigmaFraction);

		/// Background
		RooRealVar *bkg_a1  = new RooRealVar("bkg_{a1}", "background a1", 0, -2, 2);
		RooRealVar *bkg_a2  = new RooRealVar("bkg_{a2}", "background a2", 0, -1, 1);
		//RooRealVar *bkg_a3  = new RooRealVar("bkg_{a3}", "background a3", 0, -1, 1);
		RooAbsPdf  *bkgPdf  = new RooChebychev("bkg","background",
				*mass, RooArgList(*bkg_a1,*bkg_a2));
		//bkg_a1->setVal(0);
		//bkg_a1->setConstant(kTRUE);
		//bkg_a2->setVal(0);
		//bkg_a2->setConstant(kTRUE); //set constant for liner background

		// only sideband region pdf, using RooPolynomial instead of RooChebychev for multiple ranges fit
		RooRealVar *SB_bkg_a1  = new RooRealVar("SB bkg_{a1}", "background a1", 0, -1, 1);
		RooRealVar *SB_bkg_a2  = new RooRealVar("SB bkg_{a2}", "background a2", 0, -1, 1);
		RooAbsPdf  *SB_bkgPdf  = new RooPolynomial("SB_bkg","side-band background",
				*mass, RooArgList(*SB_bkg_a1,*SB_bkg_a2));
		//SB_bkg_a1->setVal(0);
		//SB_bkg_a1->setConstant(kTRUE);
		//SB_bkg_a2->setVal(0);
		//SB_bkg_a2->setConstant(kTRUE);

		/// Combined pdf
		int nt = 100000;
		//bool fitfraction = true;
		RooRealVar *nbkgd = new RooRealVar("N_{bkg}","nbkgd",nt*0.75,0,10*nt);
		RooRealVar *SB_nbkgd = new RooRealVar("SB N_{bkg}","SB_nbkgd",nt*0.75,0,10*nt);
		RooRealVar *nsig1f  = new RooRealVar("N_{#Upsilon(1S)}","nsig1S",nt*0.25,0,10*nt);
		/*
		//use the YIELDs of 2S and 3S as free parameters
		RooRealVar *nsig2f  = new RooRealVar("N_{#Upsilon(2S)}","nsig2S",   nt*0.25,-1*nt,10*nt);
		RooRealVar *nsig3f  = new RooRealVar("N_{#Upsilon(3S)}","nsig3S",   nt*0.25,-1*nt,10*nt);
		 */
		//use the RATIOs of 2S and 3S as free parameters
		RooRealVar *f2Svs1S = new RooRealVar("N_{2S}/N_{1S}","f2Svs1S",0.21,-0.1,1);
		//RooRealVar *f3Svs1S = new RooRealVar("N_{3S}/N_{1S}","f3Svs1S",0.0,-0.1,0.5);
		RooRealVar *f23vs1S = new RooRealVar("N_{2S+3S}/N_{1S}","f23vs1S",0.45,-0.1,1);
		RooFormulaVar *nsig2f = new RooFormulaVar("nsig2S","@0*@1", RooArgList(*nsig1f,*f2Svs1S));
		//RooFormulaVar *nsig3f = new RooFormulaVar("nsig3S","@0*@1", RooArgList(*nsig1f,*f3Svs1S));
		RooFormulaVar *nsig3f = new RooFormulaVar("nsig3S","@0*@2-@0*@1", RooArgList(*nsig1f,*f2Svs1S,*f23vs1S));

		//f3Svs1S->setConstant(kTRUE);

		//force the ratio to the pp value
		f2Svs1S_pp->setConstant(kTRUE);
		f3Svs1S_pp->setConstant(kTRUE);
		RooFormulaVar *nsig2f_ = new RooFormulaVar("nsig2S_pp","@0*@1", RooArgList(*nsig1f,*f2Svs1S_pp)); 
		RooFormulaVar *nsig3f_ = new RooFormulaVar("nsig3S_pp","@0*@1", RooArgList(*nsig1f,*f3Svs1S_pp)); 

		//only sideband region pdf, using RooPolynomial instead of RooChebychev for multiple ranges fit
		RooAbsPdf  *SB_pdf = new RooAddPdf ("SB_pdf","sideband background pdf",
				RooArgList(*SB_bkgPdf),
				RooArgList(*SB_nbkgd));
		//only signal region pdf, using RooPolynomial instead of RooChebychev for multiple ranges fit
		RooAbsPdf  *S_pdf   = new RooAddPdf ("S_pdf","total signal+background pdf",
				RooArgList(*gauss1S2,*sig2S,*sig3S,*SB_bkgPdf),
				RooArgList(*nsig1f,*nsig2f,*nsig3f,*SB_nbkgd));

		//parameters for likesign
		RooRealVar m0shift("turnOn","turnOn",8.6,0,20.) ;
		RooRealVar width("width","width",2.36,0,20.) ;
		RooRealVar par3("decay","decay",6.8, 0, 20.) ;
		RooGaussian* m0shift_constr;
		RooGaussian* width_constr;
		RooGaussian* par3_constr;

		RooRealVar *nLikesignbkgd = new RooRealVar("NLikesign_{bkg}","nlikesignbkgd",nt*0.75,0,10*nt);
		if (TRKROT) {
			nLikesignbkgd->setVal(TrkRotData->sumEntries());
			nLikesignbkgd->setError(sqrt(TrkRotData->sumEntries()));
		}
		else {
			nLikesignbkgd->setVal(likesignData->sumEntries());
			nLikesignbkgd->setError(sqrt(likesignData->sumEntries()));
		}

		if (LS_constrain) {
			RooGaussian* nLikesignbkgd_constr = new RooGaussian("nLikesignbkgd_constr","nLikesignbkgd_constr",*nLikesignbkgd,RooConst(nLikesignbkgd->getVal()),RooConst(nLikesignbkgd->getError()));
		}
		else nLikesignbkgd->setConstant(kTRUE);

		RooFormulaVar *nResidualbkgd = new RooFormulaVar("NResidual_{bkg}","@0-@1",RooArgList(*nbkgd,*nLikesignbkgd));

		switch (bkgdModel) {
			case 1 :  //use error function to fit the like-sign, then fix the shape and normailization, 
				RooGenericPdf *LikeSignPdf = new  RooGenericPdf("Like-sign","likesign","exp(-@0/decay)*(TMath::Erf((@0-turnOn)/width)+1)",RooArgList(*mass,m0shift,width,par3));
				if (TRKROT) RooFitResult* fit_1st = LikeSignPdf->fitTo(*TrkRotData,Save()) ;
				else RooFitResult* fit_1st = LikeSignPdf->fitTo(*likesignData,Save()) ; // likesign data
				//LikeSignPdf.fitTo(*data) ;       // unlikesign data    
				//fit_1st->Print();
				if (LS_constrain) {
					m0shift_constr = new RooGaussian("m0shift_constr","m0shift_constr",m0shift,RooConst(m0shift.getVal()),RooConst(m0shift.getError()));
					width_constr = new RooGaussian("width_constr","width_constr",width,RooConst(width.getVal()),RooConst(width.getError()));
					par3_constr = new RooGaussian("par3_constr","par3_constr",par3,RooConst(par3.getVal()),RooConst(par3.getError()));
					//m0shift_constr = new RooGaussian("m0shift_constr","m0shift_constr",m0shift,RooConst(7.9),RooConst(0.34*2));
					//width_constr = new RooGaussian("width_constr","width_constr",width,RooConst(2.77),RooConst(0.38*2));
					//par3_constr = new RooGaussian("par3_constr","par3_constr",par3,RooConst(6.3),RooConst(1.0*2));
				}
				else {
					m0shift.setConstant(kTRUE);
					width.setConstant(kTRUE);
					par3.setConstant(kTRUE);
				}
				RooAbsPdf  *pdf_combinedbkgd   = new RooAddPdf ("pdf_combinedbkgd","total combined background pdf",
						RooArgList(*bkgPdf,*LikeSignPdf),
						RooArgList(*nResidualbkgd,*nLikesignbkgd));
				//RooArgList(*LikeSignPdf),
				//RooArgList(*nbkgd));
				break;

			case 2 : //use RooKeysPdf to smooth the like-sign, then fix the shape and normailization
				if (TRKROT) RooKeysPdf *LikeSignPdf = new RooKeysPdf("Like-sign","likesign",*mass,*TrkRotData,3,1.5);
				else RooKeysPdf *LikeSignPdf = new RooKeysPdf("Like-sign","likesign",*mass,*likesignData,3,1.7);
				RooAbsPdf  *pdf_combinedbkgd   = new RooAddPdf ("pdf_combinedbkgd","total combined background pdf",
						RooArgList(*bkgPdf,*LikeSignPdf),
						RooArgList(*nResidualbkgd,*nLikesignbkgd));
				break;

			case 3 : //use error function to fit the unlike-sign directly
				RooGenericPdf *LikeSignPdf = new  RooGenericPdf("Like-sign","likesign","exp(-@0/decay)*(TMath::Erf((@0-turnOn)/width)+1)",RooArgList(*mass,m0shift,width,par3));
				RooAbsPdf  *pdf_combinedbkgd   = new RooAddPdf ("pdf_combinedbkgd","total combined background pdf",
						RooArgList(*LikeSignPdf),
						RooArgList(*nbkgd));
				break;

			case 4 : //use polynomial to fit the unlike-sign directly
				RooAbsPdf  *pdf_combinedbkgd   = new RooAddPdf ("pdf_combinedbkgd","total combined background pdf",
						RooArgList(*bkgPdf),
						RooArgList(*nbkgd));
				break;


			case 5 : //use ( error function + polynomial ) to fit the unlike-sign directly
				RooGenericPdf *LikeSignPdf = new  RooGenericPdf("Like-sign","likesign","exp(-@0/decay)*(TMath::Erf((@0-turnOn)/width)+1)",RooArgList(*mass,m0shift,width,par3));
				RooAbsPdf  *pdf_combinedbkgd   = new RooAddPdf ("pdf_combinedbkgd","total combined background pdf",
						RooArgList(*bkgPdf,*LikeSignPdf),
						RooArgList(*nResidualbkgd,*nLikesignbkgd));
				break;

			default :
				break;
		}

		//pdf with fixed ratio of the pp ratio
		RooAbsPdf  *pdf_pp   = new RooAddPdf ("pdf_pp","total signal+background pdf",
				RooArgList(*gauss1S2,*sig2S,*sig3S,*pdf_combinedbkgd),
				RooArgList(*nsig1f,*nsig2f_,*nsig3f_,*nbkgd));

		//the nominal fit with default pdf 
		if (LS_constrain) {
			RooAbsPdf  *pdf_unconstr   = new RooAddPdf ("pdf_unconstr","total signal+background pdf",
					RooArgList(*gauss1S2,*sig2S,*sig3S,*pdf_combinedbkgd),
					RooArgList(*nsig1f,*nsig2f,*nsig3f,*nbkgd));
			RooProdPdf *pdf  = new RooProdPdf ("pdf","total constr pdf",
					RooArgSet(*pdf_unconstr,*m0shift_constr,*width_constr,*par3_constr,*nLikesignbkgd_constr));
			RooFitResult* fit_2nd = pdf->fitTo(*data,Constrained(),Save(kTRUE),Extended(kTRUE),Minos(doMinos));
		}
		else {
			RooAbsPdf  *pdf   = new RooAddPdf ("pdf","total signal+background pdf",
					RooArgList(*gauss1S2,*sig2S,*sig3S,*pdf_combinedbkgd),
					RooArgList(*nsig1f,*nsig2f,*nsig3f,*nbkgd));
			RooFitResult* fit_2nd = pdf->fitTo(*data,Save(kTRUE),Extended(kTRUE),Minos(doMinos));
		}


		//plot
		TCanvas c; c.cd();
		int nbins = ceil((mmax_-mmin_)/binw_); 
		RooPlot* frame = mass->frame(Bins(nbins),Range(mmin_,mmax_));
		data->plotOn(frame,Name("theData"),MarkerSize(0.8));
		pdf->plotOn(frame,Name("thePdf"));
		if (plotLikeSign) {
			if (TRKROT) TrkRotData->plotOn(frame,Name("theLikeSignData"),MarkerSize(0.8),MarkerColor(kMagenta),MarkerStyle(22));
			else likesignData->plotOn(frame,Name("theLikeSignData"),MarkerSize(0.8),MarkerColor(kRed),MarkerStyle(24));
			//LikeSignPdf->plotOn(frame,Name("theLikeSign"),VisualizeError(*fit_1st,1),FillColor(kOrange));
			//LikeSignPdf->plotOn(frame,Name("theLikeSign"),LineColor(kRed));
		}
		RooArgSet * pars = pdf->getParameters(data);
		//RooArgSet * pars = LikeSignPdf->getParameters(likesignData);

		//calculate chi2 in a mass range
		float bin_Min = (8.2-mmin_)/binw_;
		float bin_Max = (10.8-mmin_)/binw_;
		int binMin = ceil(bin_Min);
		int binMax = ceil(bin_Max);
		int nfloatpars = pars->selectByAttrib("Constant",kFALSE)->getSize();
		float myndof = ceil((10.8-8.2)/binw_) - nfloatpars;
		cout<<binMin<<" "<<binMax<<" "<<nfloatpars<<" "<<myndof<<endl;
		double mychsq = frame->mychiSquare("thePdf","theData",nfloatpars,true,binMin,binMax)*myndof;
		//double mychsq = frame->mychiSquare("theLikeSign","theLikeSignData",nfloatpars,true,binMin,binMax)*myndof;

		/*
		   int nfloatpars = pars->selectByAttrib("Constant",kFALSE)->getSize();
		   float myndof = frame->GetNbinsX() - nfloatpars;
		   double mychsq = frame->chiSquare("theLikeSign","theLikeSignData",nfloatpars)*myndof;
		 */
		//plot parameters
		if(plotpars) {
			paramOn_ = "_paramOn";
			pdf->paramOn(frame,Layout(0.15,0.6,0.4),Layout(0.5,0.935,0.97),Label(Form("#chi^{2}/ndf = %2.1f/%2.0f", mychsq,myndof)));
		}

		/*
		   mass->setRange("R1S",8.8,9.7);
		   mass->setRange("R2S",9.8,10.2);
		//pdf_combinedbkgd->fitTo(*data,Range("R1,R3"),Constrained(),Save(kTRUE),Extended(kTRUE),Minos(doMinos));
		RooAbsReal* integral_1S = pdf_combinedbkgd->createIntegral(*mass,NormSet(*mass),Range("R1S")) ;
		cout << "1S bkgd integral = " << integral_1S->getVal() * (nbkgd->getVal()) << endl ;
		RooAbsReal* integral_2S = pdf_combinedbkgd->createIntegral(*mass,NormSet(*mass),Range("R2S")) ;
		cout << "2S bkgd integral = " << integral_2S->getVal() * (nbkgd->getVal()) << endl ;
		cout << "1S range count: " << data->sumEntries("invariantMass","R1S") <<endl;
		cout << "2S range count: " << data->sumEntries("invariantMass","R2S") <<endl;
		cout << "1S signal yield: " << data->sumEntries("invariantMass","R1S") - integral_1S->getVal() * (nbkgd->getVal()) << endl;
		cout << "2S signal yield: " << data->sumEntries("invariantMass","R2S") - integral_2S->getVal() * (nbkgd->getVal()) << endl;
		 */
		outfile<<"Y(1S) yield  : = "<<nsig1f->getVal()<<" +/- "<<nsig1f->getError()<<endl<<endl;
		outfile<<"free parameter = "<< nfloatpars << ", mychi2 = " << mychsq << ", ndof = " << myndof  << endl << endl;

		//draw the fit lines and save plots
		data->plotOn(frame,Name("theData"),MarkerSize(0.8));
		pdf->plotOn(frame,Components("bkg"),Name("theBkg"),LineStyle(5),LineColor(kGreen));
		pdf->plotOn(frame,Components("pdf_combinedbkgd"),LineStyle(kDashed));
		if (plotLikeSign) {
			if (TRKROT) pdf->plotOn(frame,Components("Like-sign"),Name("theLikeSign"),LineStyle(9),LineColor(kMagenta));
			else  pdf->plotOn(frame,Components("Like-sign"),Name("theLikeSign"),LineStyle(9),LineColor(kRed));
		}
		pdf->plotOn(frame,Name("thePdf"));
		data->plotOn(frame,MarkerSize(0.8));
		if (plotLikeSign) {
			if (TRKROT) TrkRotData->plotOn(frame,Name("theTrkRotData"),MarkerSize(0.8),MarkerColor(kMagenta),MarkerStyle(22));
			else likesignData->plotOn(frame,Name("theLikeSignData"),MarkerSize(0.8),MarkerColor(kRed),MarkerStyle(24));
		}   


		frame->SetTitle( "" );
		frame->GetXaxis()->SetTitle("m_{#mu^{+}#mu^{-}} (GeV/c^{2})");
		frame->GetXaxis()->CenterTitle(kTRUE);
		frame->GetYaxis()->SetTitleOffset(1.3);
		if (PR_plot && RAA) frame->GetYaxis()->SetRangeUser(0,1200);
		//frame->GetYaxis()->SetLabelSize(0.05);
		frame->Draw();


		//plot parameters
		if(!plotpars) {
			paramOn_ = ""; 
			TLatex latex1;
			latex1.SetNDC();
			if (PbPb) {
				latex1.DrawLatex(0.46,1.-0.05*3,"CMS PbPb  #sqrt{s_{NN}} = 2.76 TeV");
				latex1.DrawLatex(0.5,1.-0.05*4.9,"L_{int} = 150 #mub^{-1}"); 
				switch (bin) {  
					case 0: latex1.DrawLatex(0.5,1.-0.05*6.2,"Cent. 0-100%, |y| < 2.4"); break;
					case 3: latex1.DrawLatex(0.5,1.-0.05*6.2,"Cent. 0-5%, |y| < 2.4"); break;
					case 4: latex1.DrawLatex(0.5,1.-0.05*6.2,"Cent. 5-10%, |y| < 2.4"); break;
					case 5: latex1.DrawLatex(0.5,1.-0.05*6.2,"Cent. 10-20%, |y| < 2.4"); break;
					case 6: latex1.DrawLatex(0.5,1.-0.05*6.2,"Cent. 20-30%, |y| < 2.4"); break;
					case 7: latex1.DrawLatex(0.5,1.-0.05*6.2,"Cent. 30-40%, |y| < 2.4"); break;
					case 8: latex1.DrawLatex(0.5,1.-0.05*6.2,"Cent. 40-50%, |y| < 2.4"); break;
					case 9: latex1.DrawLatex(0.5,1.-0.05*6.2,"Cent. 50-100%, |y| < 2.4"); break;
							default; break;
				}   
			}
			else {
				latex1.DrawLatex(0.46,1.-0.05*3,"CMS pp  #sqrt{s_{NN}} = 2.76 TeV");
				latex1.DrawLatex(0.5,1.-0.05*4.9,"L_{int} = 230 nb^{-1}"); 
				latex1.DrawLatex(0.5,1.-0.05*6.2,"|y| < 2.4");
			}
			latex1.DrawLatex(0.5,1.-0.05*7.5,"p_{T}^{#mu} > 4 GeV/c");
			//latex1.DrawLatex(0.7,1.-0.05*8.8,"data");
			latex1.DrawLatex(0.7,1.-0.05*9.8,"total fit");
			latex1.DrawLatex(0.7,1.-0.05*10.8,"background");
			//TMarker M(11.35, 425, 20);
			//M.SetMarkerSize(1);
			//M.DrawMarker(11.35, 425);

			TLine L1; 
			L1.SetLineWidth(2);
			L1.SetLineColor(4);
			L1.DrawLineNDC(0.62, 1. - 0.05*9.55,
					0.68, 1. - 0.05*9.55);

			TLine L2; 
			L2.SetLineWidth(2);
			L2.SetLineColor(4);
			L2.SetLineStyle(2);
			L2.DrawLineNDC(0.62, 1. - 0.05*10.55,
					0.68, 1. - 0.05*10.55);
		}   

		c.SaveAs(figs_+figName_+paramOn_+suffix_+".gif");
		c.SaveAs(figs_+figName_+paramOn_+suffix_+".pdf");

		if (PR_plot) {
			//overlay the pp ratio, calculate the significance of suppression
			m0shift.setConstant(kTRUE);
			width.setConstant(kTRUE);
			par3.setConstant(kTRUE);
			nbkgd->setConstant(kTRUE);
			sigma2->setConstant(kTRUE);
			alpha->setConstant(kTRUE);
			mean->setConstant(kTRUE);
			TrkRotData->plotOn(frame,Name("theTrkRotData"),MarkerSize(0.0),MarkerColor(kWhite),LineColor(kWhite),MarkerStyle(22));
			if (PbPb) suppression(nsig1f, fit_2nd, nfloatpars, pdf, pdf_pp, data, frame);
		}

		//setup the limits
		float baseNll = fit_2nd->minNll();
		//setUpLimits(-0.08, 0.92, pdf, data, f23vs1S, baseNll);
		//setUpLimits(-0.1, 0.9, pdf, data, f2Svs1S, baseNll);

		//calculate the confidence interval with RooStats
		//ConfidencInterval(0.95, f3Svs1S, data, pdf);
		//ConfidencInterval(0.95, f2Svs1S, data, pdf);

		// Print fit results 
		cout << endl << "figure name: "<< figName_ << endl << endl;
		cout << "the nominal fit with the default pdf " << endl ;
		fit_2nd->Print() ;
		cout << "  free parameter = "<< nfloatpars << ", mychi2 = " << mychsq << ", ndof = " << myndof << endl << endl;
	}


//calculate the confidence interval with RooStats
pair<double, double> ConfidencInterval(float CI, RooRealVar *fnll, RooDataSet *data, RooAbsPdf *pdf)  {  
	ProfileLikelihoodCalculator pl(*data,*pdf,*fnll);
	pl.SetConfidenceLevel(CI); // 95% interval
	LikelihoodInterval* interval = pl.GetInterval();
	LikelihoodIntervalPlot plot(interval);
	TCanvas c4; c4.cd(); 
	plot.Draw();
	TString intrvlName = fnll->GetTitle();
	c4.SaveAs(figs_+"nll_"+intrvlName+"_pt4.gif");
	c4.SaveAs(figs_+"nll_"+intrvlName+"_pt4.pdf");
	// print out the iterval on the Parameter of Interest
	cout <<endl<< CI <<"\% interval on " <<fnll->GetName()<<" is : ["<<
		interval->LowerLimit(*fnll) << ", "<<
		interval->UpperLimit(*fnll) << "] "<<endl;
	pair<double, double> CnfdncIntrvl;
	CnfdncIntrvl.first  = interval->LowerLimit(*fnll);
	CnfdncIntrvl.second = interval->UpperLimit(*fnll);
	return CnfdncIntrvl;
}


void suppression(RooRealVar *nsig1f, RooFitResult *fit_2nd, int nfloatpars, RooAbsPdf *pdf, RooAbsPdf *pdf_pp, RooDataSet *data, RooPlot *frame){
	//the layout fit with pp ratio pdf
	//nsig1f->setVal(1380);
	TCanvas c1; c1.cd();
	//pdf->plotOn(frame,Name("thePdf"));
	if (RAA) nsig1f->setVal(2464);//(2352);
	//nsig1f->setConstant(kTRUE);  //fix the 1S yield to the value from the default fit 
	//RooFitResult* fit_3rd = pdf_pp->fitTo(*data,Save(kTRUE),Extended(kTRUE));
	pdf_pp->plotOn(frame,Name("thePdf_pp"),LineStyle(kDashed),LineColor(kRed));
	//pdf_pp->plotOn(frame,Components("pdf_combinedbkgd"),LineColor(kRed),LineStyle(kDashed));
	/*
	   RooArgSet * pars_pp = pdf_pp->getParameters(data);
	   int nfloatpars_pp = pars_pp->selectByAttrib("Constant",kFALSE)->getSize();
	   float nll2 = fit_2nd->minNll();
	   float nll3 = fit_3rd->minNll();
	   double chi = 2.0*(nll3-nll2);
	   int deltaNDOF = nfloatpars-nfloatpars_pp;
	   double cl = 1.0 - TMath::Prob(chi,deltaNDOF)/2;
	   double Significance = -RooStats::PValueToSignificance(cl);
	   outfile<<endl<<"*************************************"<<endl;
	   outfile<<"the delta of S is         : "<<nll3-nll2<<endl;
	   outfile<<"the delta of ndof is      : "<<deltaNDOF<<endl;
	   outfile<<"the C.L. is               : "<<cl<<endl;
	   outfile<<"the significance level is : "<<Significance<<" (one side)"<<endl;
	   outfile<<"*************************************"<<endl<<endl;
	   outfile<<"the C.L. is : "<<cl<<",  the significance level is : "<<Significance<<" (one side)"<<endl<<endl;
	 */	
	//draw and save plots
	data->plotOn(frame,MarkerSize(0.8));
	frame->Draw();
	if(!plotpars) {
		if (RAA) float a=1160;
		else float a=730;
		float delta=a/62*5;
		TLatex latex1;
		latex1.DrawLatex(9.9,a, "CMS PbPb  #sqrt{s_{NN}} = 2.76 TeV");
		a=a-delta/50.0;
		TLatex latex2;
		latex2.DrawLatex(9.9,a-1*delta,"Cent. 0-100%, |y| < 2.4");
		TLatex latex3;
		//^F^F^Flatex3.DrawLatex(9.9,a-2*delta,"p_{T} < 20 GeV/c");
		TLatex latex4;
		latex4.DrawLatex(9.9,a-2*delta, "L_{int} = 150 #mub^{-1}");
		TLatex latex5;
		latex5.DrawLatex(9.9,a-3*delta, "p_{T}^{#mu} > 4 GeV/c");

		if (!RAA) {
			TLatex latex9;
			//  latex9.DrawLatex(7.4,a, "Preliminary");

			latex9.DrawLatex(8,a, "data");  
			TMarker M(7.55,delta/5.0+a,20);
			M.Draw();
			//TLine L0(7.3,delta/4.0+a,7.8,delta/4.0+a);
			//L0.Draw();
			//TLine L1(7.55,a,7.55,a);
			//L1.Draw();

			TLatex latex10;
			latex10.DrawLatex(8,a-1*delta, "PbPb fit");
			TLine L1(7.3,delta/5.0+a-1*delta,7.8,delta/5.0+a-1*delta);
			L1.SetLineColor(kBlue);
			L1.SetLineWidth(2);
			L1.Draw();

			TLatex latex11;
			latex11.DrawLatex(8,a-2*delta, "pp shape");
			TLine L2(7.3,delta/5.0+a-2*delta,7.8,delta/5.0+a-2*delta);
			L2.SetLineColor(kRed);
			L2.SetLineStyle(kDashed);
			L2.SetLineWidth(2);
			L2.Draw();

		}

		else {
			TLatex latex9;
			//  latex9.DrawLatex(7.4,a, "Preliminary");

			latex9.DrawLatex(8+3.5,a-5*delta, "data");
			TMarker M(7.55+3.5,delta/5.0+a-5*delta,20);
			M.Draw();
			//TLine L0(7.3,delta/4.0+a,7.8,delta/4.0+a);
			//L0.Draw();
			//TLine L1(7.55,a,7.55,a);
			//L1.Draw();

			TLatex latex10;
			latex10.DrawLatex(8+3.5,a-6*delta, "PbPb fit");
			TLine L1(7.3+3.5,delta/5.0+a-6*delta,7.8+3.5,delta/5.0+a-6*delta);
			L1.SetLineColor(kBlue);
			L1.SetLineWidth(2);
			L1.Draw();

			TLatex latex11;
			latex11.DrawLatex(8+3.5,a-7*delta, "pp shape");
			latex11.SetTextSize(0.035);
			latex11.DrawLatex(11.7,a-7.75*delta, "(R_{AA} scaled)");
			TLine L2(7.3+3.5,delta/5.0+a-7*delta,7.8+3.5,delta/5.0+a-7*delta);
			L2.SetLineColor(kRed);
			L2.SetLineStyle(kDashed);
			L2.SetLineWidth(2);
			L2.Draw();
		}

	}

	c1.SaveAs(figs_+"overlay1_"+figName_+paramOn_+suffix_+".gif");
	c1.SaveAs(figs_+"overlay1_"+figName_+paramOn_+suffix_+".pdf");
	nsig1f->setConstant(kFALSE);
}


void setUpLimits(float xMin, float xMax, RooAbsPdf *pdf, RooDataSet *data, RooRealVar *param, float baseNll){
	//setting up upper limits
	TCanvas c2; c2.cd();
	int totalBins = 100;
	float BinWidth = (xMax - xMin)/totalBins;
	TH1F *h1 = new TH1F("h1","h1",totalBins,xMin,xMax);
	h1->GetXaxis()->SetTitle(param->getTitle());
	//h1->GetXaxis()->SetRangeUser(-0.1,0.9);
	h1->GetYaxis()->SetTitle("Maximum likelihood");
	TH1F *h2 = new TH1F("h2","h2",totalBins,xMin,xMax);
	gStyle->SetOptStat(kFALSE);
	RooFitResult* fit_nll;
	double MinNll, L, cl;
	for (int i=1; i<=totalBins; i++) {
		param->setVal(xMin + BinWidth*(i-1));
		param->setConstant(kTRUE);
		fit_nll = pdf->fitTo(*data,Save(kTRUE));
		MinNll = fit_nll->minNll()-baseNll;
		L = TMath::Exp(-MinNll);
		cout<<"x = "<<param->getVal()<<", MinNll = "<<MinNll<<", L = "<<L<<endl;
		h1->SetBinContent(i,L);
	}
	for (int i=1; i<=totalBins; i++) {
		cout<<"bin "<<i<<" = "<< h1->GetBinContent(i)<<endl;
	}
	h1->Draw();
	cout<<endl<<"integral = "<<h1->Integral(1,totalBins)<<endl<<endl;
	h1->Scale(1.0/h1->Integral(1,totalBins));
	h1->Draw();
	c2.Update();

	//convoluted with systematic gaussian
	TH1F *h3 = new TH1F("h3","h3",totalBins,xMin,xMax);
	TH1F *h4 = new TH1F("h4","h4",totalBins,xMin,xMax);
	for (int i=1; i<=totalBins; i++) {
		float gausmean = xMin + BinWidth*(i-1);
		cout<<"gausmean = "<<gausmean;
		float gaussigma = 0.00001;
		TH1F *h_syst = new TH1F("h_syst","syst histogram",totalBins,xMin,xMax);
		for (Int_t k=0;k<10000;k++) {h_syst->Fill(gRandom->Gaus(gausmean,gaussigma));}
		double new_nll = 0;
		for (int j=1; j<=totalBins; j++){
			new_nll += (h_syst->GetBinContent(j) * h1->GetBinContent(j));
		}
		cout<<", new value after convolution in bin "<<i<<" = "<<new_nll<<endl;
		h3->SetBinContent(i,new_nll);
		delete h_syst;
	}
	cout<<endl<<"integral = "<<h3->Integral(1,totalBins)<<endl<<endl;
	h3->Scale(1.0/h3->Integral(1,totalBins));
	h3->SetLineColor(kMagenta);
	h3->SetLineWidth(2);
	h3->SetLineStyle(2);
	h3->Draw("same");

	//find out the upper limit
	c2.Update();
	float UpperLimit;
	double CI = 0.842; //0.842; //0.158;
	for (int i=1; i<=totalBins; i++) {
		cl = h1->Integral(1,i);
		cout<<"x = "<< xMin + BinWidth*(i-1) << ", y = " << h1->GetBinContent(i) <<", cl = "<<cl<<endl;
		if (cl<CI) UpperLimit = xMin + BinWidth*(i-1+1);
		h4->SetBinContent(i,cl);
	}   
	float rightmax = 1.1*h4->GetMaximum();
	float y_scale = gPad->GetUymax()/rightmax;
	cout<<gPad->GetUymax()<<" rightmax = "<<rightmax<<", scale = "<<y_scale<<endl;
	h4->SetLineWidth(2);
	h4->SetLineColor(kRed);
	h4->Scale(y_scale);
	h4->Draw("same");
	TGaxis *axis = new TGaxis(gPad->GetUxmax(),gPad->GetUymin(),gPad->GetUxmax(), gPad->GetUymax(),0,rightmax,510,"+L");
	axis->SetLineColor(kRed); axis->SetLabelColor(kRed); 
	axis->SetTitle("confidence level"); axis->SetTitleColor(kRed);
	axis->Draw();

	TLine L1(xMin,y_scale*CI,xMax,y_scale*CI);
	L1.SetLineColor(kBlue);
	c2.SaveAs(figs_+"UpperLimits_"+paramName+"_hi_syst_Extend1.pdf");
	delete h1; delete h2; delete h3; delete h4;
	param->setConstant(kFALSE);
}


Double_t RooPlot::mychiSquare(const char* curvename, const char* histname, Int_t nFitParam, bool chisqRange, int startbin, int stopbin) const
{
	// Calculate and return reduced chi-squared of curve with given name with respect
	// to histogram with given name. If nFitParam is non-zero, it is used to reduce the
	// number of degrees of freedom for a chi^2 for a curve that was fitted to the
	// data with that number of floating parameters

	// Find curve object
	RooCurve* curve = (RooCurve*) findObject(curvename,RooCurve::Class()) ;
	if (!curve) {
		coutE(InputArguments) << "RooPlot::chiSquare(" << GetName() << ") cannot find curve" << endl ;
		return -1. ;
	}

	// Find histogram object
	RooHist* hist = (RooHist*) findObject(histname,RooHist::Class()) ;
	if (!hist) {
		coutE(InputArguments) << "RooPlot::chiSquare(" << GetName() << ") cannot find histogram" << endl ;
		return -1. ;
	}
	return curve->mychiSquare(*hist,nFitParam,chisqRange,startbin,stopbin) ;
}


Double_t RooCurve::mychiSquare(const RooHist& hist, Int_t nFitParam, bool chisqRange, int startbin, int stopbin) const 
{
	// Calculate the chi^2/NDOF of this curve with respect to the histogram
	// 'hist' accounting nFitParam floating parameters in case the curve
	// was the result of a fit

	if (chisqRange) {
		int i = startbin;
		int np = stopbin;
	}
	else {
		Int_t i=0;
		int np = hist.GetN() ;
	}

	Double_t x,y,eyl,eyh,exl,exh ;

	// Find starting and ending bin of histogram based on range of RooCurve
	Double_t xstart,xstop ;

#if ROOT_VERSION_CODE >= ROOT_VERSION(4,0,1)
	GetPoint(0,xstart,y) ;
	GetPoint(GetN()-1,xstop,y) ;
#else
	const_cast<RooCurve*>(this)->GetPoint(0,xstart,y) ;
	const_cast<RooCurve*>(this)->GetPoint(GetN()-1,xstop,y) ;
#endif

	Int_t nbin(0) ;

	Double_t chisq(0) ;
	for (i ; i<np ; i++) {   

		// Retrieve histogram contents
		((RooHist&)hist).GetPoint(i,x,y) ;

		// Check if point is in range of curve
		if (x<xstart || x>xstop) continue ;

		nbin++ ;
		eyl = hist.GetEYlow()[i] ;
		eyh = hist.GetEYhigh()[i] ;
		exl = hist.GetEXlow()[i] ;
		exh = hist.GetEXhigh()[i] ;

		// Integrate function over this bin
		Double_t avg = average(x-exl,x+exh) ;

		// Add pull^2 to chisq
		if (y!=0) {      
			Double_t pull = (y>avg) ? ((y-avg)/eyl) : ((y-avg)/eyh) ;
			chisq += pull*pull ;
		}
	}

	// Return chisq/nDOF 
	return chisq / (nbin-nFitParam) ;
}

