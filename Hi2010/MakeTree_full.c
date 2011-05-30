#include <vector>
#include "TClonesArray.h"

pair<double, double> GetAngles_CS( TLorentzVector a,  TLorentzVector b) const;
pair<double, double> GetAngles_HX( TLorentzVector a,  TLorentzVector b) const;

void MakeTree_full(){
	//gROOT->LoadMacro("setTDRStyle_modified.C");
	//setTDRStyle();

	//TFile *f = TFile::Open("/castor/cern.ch/cms/store/user/tdahms/HeavyIons/Onia/Data2010/v13/Histos/ReReco/Histos_OniaSkim_ReReco_v13_h3_sum.root");
	TFile *f = TFile::Open("/castor/cern.ch/cms/store/user/tdahms/pp2760/Onia/Data2011/v5/Histos/HiReReco/Histos_OniaSkim_HiReReco_pp2760_v5h0_sum.root");

	//TFile *f = TFile::Open("/castor/cern.ch/cms/store/user/tdahms/pp2760/Onia/Data2011/v1/Histos/Prompt/Histos_OniaSkim_pp2760_v1h1_sum.root");
	//TFile *f = TFile::Open("/castor/cern.ch/cms/store/user/tdahms/pp2760/Onia/Data2011/v1/Histos/Prompt/Histos_OniaSkim_pp2760_v1h3_ZhensHiCuts_test.root");
	//TFile *f = new TFile("Histos_OniaSkim_ReReco_v7h0_sum.root");
	//TFile *f = new TFile("GlbMuon_OniaSkim_ReReco_pp.root");
	TTree *t = (TTree*)f->Get("myTree");
	Long64_t nentries = t->GetEntries();

	const int NMAX=100;
	UInt_t eventNb;
	UInt_t runNb;
	Int_t Centrality;
	Int_t HLTriggers;
	Int_t Reco_QQ_size;
	Int_t Reco_QQ_trig[NMAX];
	Int_t Reco_QQ_type[NMAX];
	Int_t Reco_QQ_sign[NMAX];
	Float_t Reco_QQ_VtxProb[NMAX];
	TClonesArray *Reco_QQ_4mom;
	TClonesArray *Reco_QQ_mupl_4mom;
	TClonesArray *Reco_QQ_mumi_4mom;
	Int_t Reco_mu_size;
	Int_t Reco_mu_type[NMAX];
	Int_t Reco_mu_charge[NMAX];
	TClonesArray *Reco_mu_4mom = 0;
	//Int_t nReco_QQ;
	Float_t invariantMass;
	Int_t QQtrig;
	Int_t QQsign;
	Float_t upsPt;
	Float_t upsEta;
	Float_t upsRapidity;	
	Float_t vProb;
	Float_t muPlusPt;
	Float_t muMinusPt;
	Float_t muPlusEta;
	Float_t muMinusEta;
	Float_t muPlusPhi;
	Float_t muMinusPhi;
	float theta_HX;
	float phi_HX;
	float theta_CS;
	float phi_CS;

	float QQmuPlusDxy[100];
	float QQmuPlusDz[100];
	int QQmuPlusNhits[100];
	int QQmuPlusNPixelhits[100];
	int QQmuPlusNPxlLayers[100];
	float QQmuPlusInnerChi[100];
	float QQmuPlusGlobalChi[100];
	int QQmuPlusNMuonhits[100];
	float QQmuPlusDB[100];

	float QQmuMinusDxy[100];
	float QQmuMinusDz[100];
	int QQmuMinusNhits[100];
	int QQmuMinusNPixelhits[100];
	int QQmuMinusNPxlLayers[100];
	float QQmuMinusInnerChi[100];
	float QQmuMinusGlobalChi[100];
	int QQmuMinusNMuonhits[100];
	float QQmuMinusDB[100];

	float muPlusDxy;
	float muPlusDz;
	int muPlusNhits;
	int muPlusNPixelhits;
	int muPlusNPxlLayers;
	float muPlusInnerChi;
	float muPlusGlobalChi;
	int muPlusNMuonhits;
	float muPlusDB;

	float muMinusDxy;
	float muMinusDz;
	int muMinusNhits;
	int muMinusNPixelhits;
	int muMinusNPxlLayers;
	float muMinusInnerChi;
	float muMinusGlobalChi;
	int muMinusNMuonhits;
	float muMinusDB;

	t->SetBranchAddress("Centrality",    &Centrality    );
	t->SetBranchAddress("eventNb",    &eventNb    );
	t->SetBranchAddress("runNb",    &runNb    );
	t->SetBranchAddress("HLTriggers",    &HLTriggers    );
	t->SetBranchAddress("Reco_QQ_size",  &Reco_QQ_size  );
	t->SetBranchAddress("Reco_QQ_trig",  &Reco_QQ_trig  );
	t->SetBranchAddress("Reco_QQ_type",  Reco_QQ_type   );
	t->SetBranchAddress("Reco_QQ_sign",  Reco_QQ_sign   );
	t->SetBranchAddress("Reco_QQ_VtxProb",  Reco_QQ_VtxProb);
	t->SetBranchAddress("Reco_QQ_4mom",  &Reco_QQ_4mom  );
	t->SetBranchAddress("Reco_QQ_mupl_4mom", &Reco_QQ_mupl_4mom);
	t->SetBranchAddress("Reco_QQ_mumi_4mom", &Reco_QQ_mumi_4mom);

	t->SetBranchAddress("muPlusDxy",QQmuPlusDxy);
	t->SetBranchAddress("muPlusDz",QQmuPlusDz);
	t->SetBranchAddress("muPlusNhits",QQmuPlusNhits);
	t->SetBranchAddress("muPlusNPixelhits",QQmuPlusNPixelhits);
	t->SetBranchAddress("muPlusNPxlLayers",QQmuPlusNPxlLayers);
	t->SetBranchAddress("muPlusInnerChi",QQmuPlusInnerChi);
	t->SetBranchAddress("muPlusGlobalChi",QQmuPlusGlobalChi);
	t->SetBranchAddress("muPlusNMuonhits",QQmuPlusNMuonhits);
	t->SetBranchAddress("muPlusDB",QQmuPlusDB);

	t->SetBranchAddress("muMinusDxy",QQmuMinusDxy);
	t->SetBranchAddress("muMinusDz",QQmuMinusDz);
	t->SetBranchAddress("muMinusNhits",QQmuMinusNhits);
	t->SetBranchAddress("muMinusNPixelhits",QQmuMinusNPixelhits);
	t->SetBranchAddress("muMinusNPxlLayers",QQmuMinusNPxlLayers);
	t->SetBranchAddress("muMinusInnerChi",QQmuMinusInnerChi);
	t->SetBranchAddress("muMinusGlobalChi",QQmuMinusGlobalChi);
	t->SetBranchAddress("muMinusNMuonhits",QQmuMinusNMuonhits);
	t->SetBranchAddress("muMinusDB",QQmuMinusDB);

	t->SetBranchAddress("Reco_mu_size",  &Reco_mu_size  );
	t->SetBranchAddress("Reco_mu_type",  Reco_mu_type   );
	t->SetBranchAddress("Reco_mu_charge",Reco_mu_charge );
	t->SetBranchAddress("Reco_mu_4mom",  &Reco_mu_4mom);

	TH1F *h_QQ_mass = new TH1F("h_QQ_mass","",70,7,14);
	TH1F *h_QQ_mass_1 = new TH1F("h_QQ_mass_1","",70,7,14);
	TH1F *h_QQ_mass_2 = new TH1F("h_QQ_mass_2","",70,7,14);	

	TFile *f1 = new TFile("MassTree_NewCuts_pp_HIrereco.root","RECREATE");
	//TFile *f1 = new TFile("MassTree_NewCuts_hi.root","RECREATE");

	TTree *UpsilonTree = new TTree("UpsilonTree","UpsilonTree");
	TTree *UpsilonTree_allsign = new TTree("UpsilonTree_allsign","UpsilonTree_allsign");
	
	//UpsilonTree->Branch("nReco_QQ", &nReco_QQ, "nReco_QQ/I");
	UpsilonTree->Branch("Centrality",    &Centrality,    "Centrality/I");
	UpsilonTree->Branch("HLTriggers",    &HLTriggers,    "HLTriggers/I");
	UpsilonTree->Branch("QQtrig",   &QQtrig,    "QQtrig/I");
	UpsilonTree->Branch("QQsign",   &QQsign,    "QQsign/I");
	UpsilonTree->Branch("vProb",    &vProb,     "vProb/F");
	UpsilonTree->Branch("eventNb",    &eventNb,     "eventNb/I");
	UpsilonTree->Branch("runNb",    &runNb,     "runNb/I");
	UpsilonTree->Branch("invariantMass", &invariantMass, "invariantMass/F");
	UpsilonTree->Branch("upsPt", &upsPt, "upsPt/F");
	UpsilonTree->Branch("upsEta", &upsEta, "upsEta/F");
	UpsilonTree->Branch("upsRapidity", &upsRapidity, "upsRapidity/F");
	UpsilonTree->Branch("muPlusPt", &muPlusPt, "muPlusPt/F");
	UpsilonTree->Branch("muMinusPt", &muMinusPt, "muMinusPt/F");
	UpsilonTree->Branch("muPlusEta", &muPlusEta, "muPlusEta/F");
	UpsilonTree->Branch("muMinusEta", &muMinusEta, "muMinusEta/F");
	UpsilonTree->Branch("muPlusPhi", &muPlusPhi, "muPlusPhi/F");
	UpsilonTree->Branch("muMinusPhi", &muMinusPhi, "muMinusPhi/F");
	UpsilonTree->Branch("theta_HX", &theta_HX, "theta_HX/F");
	UpsilonTree->Branch("phi_HX", &phi_HX, "phi_HX/F");
	UpsilonTree->Branch("theta_CS", &theta_CS, "theta_CS/F");
	UpsilonTree->Branch("phi_CS", &phi_CS, "phi_CS/F");

	UpsilonTree->Branch("muPlusDxy", &muPlusDxy,"muPlusDxy/F");
	UpsilonTree->Branch("muPlusDz", &muPlusDz,"muPlusDz/F");
	UpsilonTree->Branch("muPlusNhits", &muPlusNhits,"muPlusNhits/I");
	UpsilonTree->Branch("muPlusNPixelhits", &muPlusNPixelhits,"muPlusNPixelhits/I");
	UpsilonTree->Branch("muPlusNPxlLayers", &muPlusNPxlLayers,"muPlusNPxlLayers/I");
	UpsilonTree->Branch("muPlusInnerChi", &muPlusInnerChi,"muPlusInnerChi/F");
	UpsilonTree->Branch("muPlusGlobalChi", &muPlusGlobalChi,"muPlusGlobalChi/F");
	UpsilonTree->Branch("muPlusNMuonhits", &muPlusNMuonhits,"muPlusNMuonhits/I");
	UpsilonTree->Branch("muPlusDB", &muPlusDB,"muPlusDB/F");

	UpsilonTree->Branch("muMinusDxy", &muMinusDxy,"muMinusDxy/F");
	UpsilonTree->Branch("muMinusDz", &muMinusDz,"muMinusDz/F");
	UpsilonTree->Branch("muMinusNhits", &muMinusNhits,"muMinusNhits/I");
	UpsilonTree->Branch("muMinusNPixelhits", &muMinusNPixelhits,"muMinusNPixelhits/I");
	UpsilonTree->Branch("muMinusNPxlLayers", &muMinusNPxlLayers,"muMinusNPxlLayers/I");
	UpsilonTree->Branch("muMinusInnerChi", &muMinusInnerChi,"muMinusInnerChi/F");
	UpsilonTree->Branch("muMinusGlobalChi", &muMinusGlobalChi,"muMinusGlobalChi/F");
	UpsilonTree->Branch("muMinusNMuonhits", &muMinusNMuonhits,"muMinusNMuonhits/I");
	UpsilonTree->Branch("muMinusDB", &muMinusDB,"muMinusDB/F");

	UpsilonTree_allsign->Branch("Centrality",    &Centrality,    "Centrality/I");
	UpsilonTree_allsign->Branch("HLTriggers",    &HLTriggers,    "HLTriggers/I");
	UpsilonTree_allsign->Branch("QQtrig",   &QQtrig,    "QQtrig/I");
	UpsilonTree_allsign->Branch("QQsign",   &QQsign,    "QQsign/I");
	UpsilonTree_allsign->Branch("vProb",    &vProb,     "vProb/F");
	UpsilonTree_allsign->Branch("eventNb",    &eventNb,     "eventNb/I");
	UpsilonTree_allsign->Branch("runNb",    &runNb,     "runNb/I");
	UpsilonTree_allsign->Branch("invariantMass", &invariantMass, "invariantMass/F");
	UpsilonTree_allsign->Branch("upsPt", &upsPt, "upsPt/F");
	UpsilonTree_allsign->Branch("upsEta", &upsEta, "upsEta/F");
	UpsilonTree_allsign->Branch("upsRapidity", &upsRapidity, "upsRapidity/F");
	UpsilonTree_allsign->Branch("muPlusPt", &muPlusPt, "muPlusPt/F");
	UpsilonTree_allsign->Branch("muMinusPt", &muMinusPt, "muMinusPt/F");
	UpsilonTree_allsign->Branch("muPlusEta", &muPlusEta, "muPlusEta/F");
	UpsilonTree_allsign->Branch("muMinusEta", &muMinusEta, "muMinusEta/F");
	UpsilonTree_allsign->Branch("muPlusPhi", &muPlusPhi, "muPlusPhi/F");
	UpsilonTree_allsign->Branch("muMinusPhi", &muMinusPhi, "muMinusPhi/F");
	UpsilonTree_allsign->Branch("theta_HX", &theta_HX, "theta_HX/F");
	UpsilonTree_allsign->Branch("phi_HX", &phi_HX, "phi_HX/F");
	UpsilonTree_allsign->Branch("theta_CS", &theta_CS, "theta_CS/F");
	UpsilonTree_allsign->Branch("phi_CS", &phi_CS, "phi_CS/F");


	for (int i=0; i<nentries; i++) {
		t->GetEntry(i);
		//nReco_QQ=0;
		if (i%1000==0) cout<<i<<endl;
		for(int iQQ = 0; iQQ < Reco_QQ_size; iQQ++){
			//cout<<iQQ<<endl;
			//eventNb=eventNb[iQQ];
			//runNb=runNb[iQQ];
			vProb = Reco_QQ_VtxProb[iQQ];
			QQtrig = Reco_QQ_trig[iQQ];
			QQsign = Reco_QQ_sign[iQQ];
			TLorentzVector *Reco_QQ = (TLorentzVector *) Reco_QQ_4mom->At(iQQ);
			TLorentzVector *Reco_QQ_mupl = (TLorentzVector *) Reco_QQ_mupl_4mom->At(iQQ);
			TLorentzVector *Reco_QQ_mumi = (TLorentzVector *) Reco_QQ_mumi_4mom->At(iQQ);
			invariantMass=Reco_QQ->M();
			upsPt=Reco_QQ->Pt();
			upsEta=Reco_QQ->Eta();
			upsRapidity=Reco_QQ->Rapidity();
			muMinusPt=Reco_QQ_mumi->Pt();
			muMinusEta=Reco_QQ_mumi->Eta();
			muMinusPhi=Reco_QQ_mumi->Phi();
			muPlusPt=Reco_QQ_mupl->Pt();
			muPlusEta=Reco_QQ_mupl->Eta();
			muPlusPhi=Reco_QQ_mupl->Phi();
			theta_HX = GetAngles_HX(*Reco_QQ_mupl,*Reco_QQ_mumi).first;
			phi_HX = GetAngles_HX(*Reco_QQ_mupl,*Reco_QQ_mumi).second;
			theta_CS = GetAngles_CS(*Reco_QQ_mupl,*Reco_QQ_mumi).first;
			phi_CS = GetAngles_CS(*Reco_QQ_mupl,*Reco_QQ_mumi).second;

			muPlusDxy=QQmuPlusDxy[iQQ];
			muPlusDz=QQmuPlusDz[iQQ];
			muPlusNhits=QQmuPlusNhits[iQQ];
			muPlusNPixelhits=QQmuPlusNPixelhits[iQQ];
			muPlusNPxlLayers=QQmuPlusNPxlLayers[iQQ];
			muPlusInnerChi=QQmuPlusInnerChi[iQQ];
			muPlusGlobalChi=QQmuPlusGlobalChi[iQQ];
			muPlusNMuonhits=QQmuPlusNMuonhits[iQQ];
			muPlusDB=QQmuPlusDB[iQQ];

			muMinusDxy=QQmuMinusDxy[iQQ];
			muMinusDz=QQmuMinusDz[iQQ];
			muMinusNhits=QQmuMinusNhits[iQQ];
			muMinusNPixelhits=QQmuMinusNPixelhits[iQQ];
			muMinusNPxlLayers=QQmuMinusNPxlLayers[iQQ];
			muMinusInnerChi=QQmuMinusInnerChi[iQQ];
			muMinusGlobalChi=QQmuMinusGlobalChi[iQQ];
			muMinusNMuonhits=QQmuMinusNMuonhits[iQQ];
			muMinusDB=QQmuMinusDB[iQQ];

			/*
			   if (fabs(muPlusDxy)<3 && fabs(muPlusDz)<15 
			   && muPlusNhits>10 && muPlusNPxlLayers>0 && muPlusNMuonhits>6 
			   && muPlusInnerChi<4 && muPlusGlobalChi<6
			   && fabs(muMinusDxy)<3 && fabs(muMinusDz)<15 
			   && muMinusNhits>10 && muMinusNPxlLayers>0 && muMinusNMuonhits>6 
			   && muMinusInnerChi<4 && muMinusGlobalChi<6 
			   && vProb>0.01) 

			   if (fabs(muPlusDxy)<3 && fabs(muPlusDz)<15 
			   && muPlusNhits>10 && muPlusNPxlLayers>0 && muPlusNMuonhits>12 
			   && muPlusInnerChi<2.1 && muPlusGlobalChi<2.7
			   && fabs(muMinusDxy)<3 && fabs(muMinusDz)<15 
			   && muMinusNhits>10 && muMinusNPxlLayers>0 && muMinusNMuonhits>12 
			   && muMinusInnerChi<2.1 && muMinusGlobalChi<2.7 
			   && vProb>0.19) 
			 */
			if (HLTriggers&1==1 && Reco_QQ_trig[iQQ]&1==1 && (Reco_QQ_type[iQQ]==0) 
			   )
			{
				UpsilonTree_allsign->Fill();
				if (Reco_QQ_sign[iQQ]==0) {
					UpsilonTree->Fill();

					if (Reco_QQ->M()>7 && Reco_QQ->M()<14) {
						h_QQ_mass->Fill(Reco_QQ->M());
					}
					if (Reco_QQ_mupl->Pt()>=4 && Reco_QQ_mumi->Pt()>=4 && Reco_QQ->M()>7 && Reco_QQ->M()<14) {
						h_QQ_mass_1->Fill(Reco_QQ->M());
					}
				}
				else if (Reco_QQ_mupl->Pt()>=4 && Reco_QQ_mumi->Pt()>=4 && Reco_QQ->M()>7 && Reco_QQ->M()<14) {
					h_QQ_mass_2->Fill(Reco_QQ->M());
				}

			}
			//nReco_QQ++;
		}
		//	UpsilonTree->Fill();
	}

	gROOT->SetStyle("Plain");
	gStyle->SetPalette(1);
	gStyle->SetFrameBorderMode(0);
	gStyle->SetFrameFillColor(0);
	gStyle->SetCanvasColor(0);
	gStyle->SetTitleFillColor(0);
	gStyle->SetStatColor(0);
	gStyle->SetPadBorderSize(0);
	gStyle->SetCanvasBorderSize(0);
	gStyle->SetOptTitle(0); // at least most of the time
	gStyle->SetOptStat(0); // most of the time, sometimes "nemriou" might be useful to display name, number of entries, mean, rms, integral, overflow and underflow
	gStyle->SetOptFit(0); // set to 1 only if you want to display fit results

	TCanvas *c1 = new TCanvas("c1","c1");
	//h_QQ_mass->GetYaxis()->SetRangeUser(0,180);
	h_QQ_mass->SetMarkerColor(kRed);
	h_QQ_mass->SetMarkerStyle(22);
	h_QQ_mass->SetXTitle("#mu#mu invariant mass [GeV/c^{2}]");
	h_QQ_mass->SetYTitle("Events/(0.1 GeV/c^{2})");
	//h_QQ_mass->Draw("PE");

	h_QQ_mass_1->SetMarkerColor(kBlue);
	h_QQ_mass_1->SetMarkerStyle(20);
	h_QQ_mass_1->SetXTitle("#mu#mu invariant mass [GeV/c^{2}]");
	h_QQ_mass_1->SetYTitle("Events/(0.1 GeV/c^{2})");
	h_QQ_mass_1->Draw("PE");

	h_QQ_mass_2->SetMarkerColor(kRed);
	h_QQ_mass_2->SetMarkerStyle(24);
	h_QQ_mass_2->Draw("samePE");

	TLegend *legend = new TLegend(.45,.75,.99,.99);
	//legend->AddEntry(h_QQ_mass,"#mu^{+}#mu^{-} pairs, acceptance cut","P");
	legend->AddEntry(h_QQ_mass_1,"#mu^{+}#mu^{-} pairs, #mu p_{T} > 4 GeV/c","P");
	legend->AddEntry(h_QQ_mass_2,"same sign #mu pairs, #mu p_{T} > 4 GeV/c","P");
	legend->Draw();

	//h_QQ_mass->Write();
	//h_QQ_mass_1->Write();
	//h_QQ_mass_2->Write();
	//c1->SaveAs("paperPlots/ups_invmass_hi.pdf");
	//c1->SaveAs("paperPlots/ups_invmass_hi.gif");
	c1->Write();
	f1->Write();

}


////////////////////////////////////////////////////////////////////////
// Calculates theta and phi in CS frame
////////////////////////////////////////////////////////////////////////
pair<double, double> GetAngles_CS( TLorentzVector a,  TLorentzVector b) const {
	TLorentzVector c = a+b;                   // JPsi momentum in lab frame
	TVector3 bv = c.BoostVector();
	TLorentzVector p1(0., 0.,  1380., 1380.); // beam momentum in lab frame
	TLorentzVector p2(0., 0., -1380., 1380.); // beam momentum in lab frame
	p1.Boost(-bv);
	p2.Boost(-bv);
	TVector3 beam1 = p1.Vect().Unit();        // beam direction in JPsi rest frame
	TVector3 beam2 = p2.Vect().Unit();        // beam direction in JPsi rest frame

	TVector3 Z = ( beam1 - beam2 ).Unit();    // bisector of 2 beam direction in JPsi rest frame
	TVector3 Y = beam1.Cross( beam2 ).Unit(); // the production plane normal
	TVector3 X = Y.Cross(Z).Unit();           // completes the right-handed coordinate

	a.Boost(-bv);                             // muon+ momentum in JPsi rest frame
	TVector3 mu(a.Vect().Dot(X), a.Vect().Dot(Y), a.Vect().Dot(Z)); // transform to new coordinate
	pair<double, double> angles;
	angles.first = mu.Theta();
	angles.second = mu.Phi()>0. ? mu.Phi() : mu.Phi()+2.*TMath::Pi();
	return angles;
}

////////////////////////////////////////////////////////////////////////
// Calculates theta and phi in HX frame
////////////////////////////////////////////////////////////////////////
pair<double, double> GetAngles_HX( TLorentzVector a,  TLorentzVector b) const {
	TLorentzVector c = a+b;                   // JPsi momentum in lab frame
	TVector3 bv = c.BoostVector();
	TLorentzVector p1(0., 0.,  1380., 1380.); // beam momentum in lab frame
	TLorentzVector p2(0., 0., -1380., 1380.); // beam momentum in lab frame
	p1.Boost(-bv);
	p2.Boost(-bv);
	TVector3 beam1 = p1.Vect().Unit();        // beam direction in JPsi rest frame
	TVector3 beam2 = p2.Vect().Unit();        // beam direction in JPsi rest frame

	TVector3 Z = c.Vect().Unit();             // JPsi direction in lab frame
	TVector3 Y = beam1.Cross( beam2 ).Unit(); // the production plane normal
	TVector3 X = Y.Cross(Z).Unit();           // completes the right-handed coordinate

	a.Boost(-bv);                             // muon+ momentum in JPsi rest frame
	TVector3 mu(a.Vect().Dot(X), a.Vect().Dot(Y), a.Vect().Dot(Z)); // transform to new coordinate
	pair<double, double> angles;
	angles.first = mu.Theta();
	angles.second = mu.Phi()>0. ? mu.Phi() : mu.Phi()+2.*TMath::Pi();
	return angles;
}



