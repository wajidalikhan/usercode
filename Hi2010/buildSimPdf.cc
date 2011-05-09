#include "RooSimWSTool.h"
#include "RooArgSet.h"
#include "RooArgList.h"
#include "RooRealVar.h"
#include "RooConstVar.h"
#include "RooCategory.h"
#include "RooWorkspace.h"
#include "RooFormulaVar.h"
#include "RooCBShape.h"
#include "RooChebychev.h"
#include "RooAddPdf.h"
#include "RooDataSet.h"
#include "RooExtendPdf.h"

#include "TTree.h"
#include "TFile.h"

float mmin = 8.0, mmax = 14.0;
TString dirname_ = "";
TString treeName = "UpsilonTree";

bool buildPdf(RooWorkspace &ws) {

  double const M1S(9.460);
  double const M2S(10.023);
  double const M3S(10.355);
  RooRealVar * mass = ws.var("invariantMass");
  if (!mass) {
    mass = new RooRealVar("invariantMass", "#mu#mu mass", mmin, mmax, 
			  "GeV/c^{2}");
  }
  
  RooRealVar mean("mean", "mean", M1S, M1S-0.3, M1S+0.3, "GeV/c^{2}");

  RooConstVar rat2("rat2", "rat2", M2S/M1S);
  RooConstVar rat3("rat3", "rat3", M3S/M1S);

  RooFormulaVar mean1S("mean1S", "@0", RooArgList(mean));
  RooFormulaVar mean2S("mean2S", "@0*@1", RooArgList(mean,rat2));
  RooFormulaVar mean3S("mean3S", "@0*@1", RooArgList(mean,rat3));

  RooRealVar sigma1("sigma1", "#sigma_{1}", 0.092, 0.01, 0.3);
  sigma1.setConstant();
  RooFormulaVar sigma1S("sigma1S", "@0", RooArgList(sigma1));
  RooFormulaVar sigma2S("sigma2S", "@0*@1", RooArgList(sigma1,rat2));
  RooFormulaVar sigma3S("sigma3S", "@0*@1", RooArgList(sigma1,rat3));

  RooRealVar alpha("alpha", "#alpha", 1.6, 0.1, 10.);
  alpha.setConstant();
  RooRealVar npow("npow", "n_{CB}", 2.3, 0.1, 10.);
  npow.setConstant();

  RooCBShape sig1S("sig1S", "sig1S", *mass, mean1S, sigma1S, alpha, npow);
  RooCBShape sig2S("sig2S", "sig2S", *mass, mean2S, sigma2S, alpha, npow);
  RooCBShape sig3S("sig3S", "sig3S", *mass, mean3S, sigma3S, alpha, npow);

  RooRealVar bkg_a1("bkg_a1", "a_{1,bkg}", 0., -2., 2.);
  RooRealVar bkg_a2("bkg_a2", "a_{2,bkg}", 0., -2., 2.);
  RooChebychev bkg("bkg", "bkg", *mass, RooArgList(bkg_a1, bkg_a2));

  RooRealVar nsig1("nsig1", "N_{1S}", 100, -1000, 1e6);
  RooRealVar f23("f23", "(2S+3S)/1S", 0.5);
  f23.setConstant(false);
  // RooRealVar f2("f2", "2S/1S", 0.2);
  RooRealVar f2("f2", "3S/2S", 0.6);
  f2.setConstant(false);
  RooRealVar nbkg("nbkg", "N_{bkg}", 300., -1000., 1e6);

  // RooFormulaVar nsig2("nsig2", "@0*@1", RooArgList(nsig1,f2));
  // RooFormulaVar nsig3("nsig3", "@0*(@1-@2)", RooArgList(nsig1, f23, f2));

  RooFormulaVar nsig2("nsig2", "@0*@1/(1+@2)", RooArgList(nsig1, f23, f2));
  RooFormulaVar nsig3("nsig3", "@0*@1*@2/(1+@2)", RooArgList(nsig1, f23, f2));

  RooExtendPdf sig1SN("sig1SN", "sig1SN", sig1SN, nsig1);
  RooExtendPdf sig2SN("sig2SN", "sig2SN", sig2SN, nsig2);
  RooExtendPdf sig3SN("sig3SN", "sig3SN", sig3SN, nsig3);
  RooExtendPdf bkgN("bkgN", "bkgN", bkgN, nbkg);

  // RooAddPdf pdf("pdf", "pdf", RooArgList(sig1SN, sig2SN, sig3SN, bkgN));
  RooAddPdf pdf("pdf", "pdf", RooArgList(sig1S, sig2S, sig3S, bkg),
		RooArgList(nsig1, nsig2, nsig3, nbkg));

  //pdf.Print("v");
  return ws.import(pdf, RooFit::RecycleConflictNodes(), RooFit::Silence());
}

void buildSimPdf(RooWorkspace &ws, RooCategory const &dataCat) {

  if (!ws.pdf("pdf") && buildPdf(ws)) {
    std::cout << "cannot get pdf.\n";
  }

  RooSimWSTool simTool(ws);
  simTool.build("simPdf", "pdf", RooFit::SplitParam("f23", dataCat.GetName()),
		RooFit::SplitParam("f23,f2,nsig1,nbkg", dataCat.GetName()),
		RooFit::SplitParam("bkg_a1,bkg_a2", dataCat.GetName()));

}

bool readData(RooWorkspace &ws, TString HIfilename, TString ppFilename,
	      TString extraCut = "") {
  TFile hifile(HIfilename, "read");
  TTree * tree;
  TString dirTree = treeName;
  if (dirname_.Length() > 0)
    dirTree = dirname_ + "/" + treeName;
  hifile.GetObject(dirTree, tree);
  assert(tree);
  if (extraCut.Length() > 0) {
    TTree * tree2 = tree->CopyTree(extraCut);
    tree = tree2;
  }

  RooRealVar * mass = ws.var("invariantMass");
  if (!mass) {
    mass = new RooRealVar("invariantMass", "#mu#mu mass", mmin, mmax, 
			  "GeV/c^{2}");
  }
  RooRealVar muppt("muPlusPt" ,"#mu+ pt",2,20,"GeV/c"); 
  RooRealVar mumpt("muMinusPt","#mu- pt",2,20,"GeV/c"); 
  RooRealVar upsPt("upsPt","p_{T}(#Upsilon)",0.,"GeV");
  RooRealVar upsRapidity("upsRapidity", "upsRapidity", 0.);

  RooArgSet cols(*mass, muppt, mumpt, upsPt, upsRapidity);
  RooDataSet hidata("hidata", "hidata", tree, cols);

  TFile ppfile(ppFilename, "read");
  tree = 0;
  ppfile.GetObject(dirTree, tree);
  if (extraCut.Length() > 0) {
    TTree * tree2 = tree->CopyTree(extraCut);
    tree = tree2;
  }

  RooDataSet ppdata("ppdata", "ppdata", tree, cols);

  RooCategory dataCat("dataCat", "dataCat");
  dataCat.defineType("hi");
  dataCat.defineType("pp");

  RooDataSet data("data", "data", cols, RooFit::Index(dataCat),
		  RooFit::Import("hi", hidata), RooFit::Import("pp", ppdata));

  return ws.import(data/*, RooFit::RecycleConflictNodes(), RooFit::Silence()*/);  
}

double computeRatio(RooRealVar const &x, RooRealVar const &y) {
  assert(y.getVal() != 0);
  return x.getVal()/y.getVal();
}

double computeRatioError(RooRealVar const &x, RooRealVar const &y) {
  double err = x.getError()*x.getError()/x.getVal()/x.getVal() +
    y.getError()*y.getError()/y.getVal()/y.getVal();

  return computeRatio(x,y)*sqrt(err);
}