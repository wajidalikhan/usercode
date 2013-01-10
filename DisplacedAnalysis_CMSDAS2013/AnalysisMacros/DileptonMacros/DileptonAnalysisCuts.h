#ifndef DileptonAnalysisCuts_h
#define DileptonAnalysisCuts_h

#include "AnalysisMacros/CommonMacros/treeAnalyzerBase.h"


//
// DILEPTON ANALYSIS CUTS
//

// This class keeps track of which cuts a candidate has failes/passed
// There is no selection on what type of lepton is in the candidate
// There is no selection on trigger or calo matching

// Set of cuts you want to apply
typedef enum {
  _final, // final selection cuts
  _loose1, // loose set of cuts 1
  _loose2, // loose set of cuts 2
  _veryLoose1, // very loose set of cuts
  _removedLifetime, // invert lifetime cuts
}
analysisCuts;

class DileptonAnalysisCuts {
  public:
    DileptonAnalysisCuts(){};
    DileptonAnalysisCuts( analysisType type, analysisCuts cuts );
    ~DileptonAnalysisCuts() {};

    // Info on which cuts have been passed
    struct PassedWhichCuts
    {
        PassedWhichCuts() :
          passCaloMatch(false),
          passTrackPt(false),
          passSCEt(false),
          passEta(false),
          passLeptonAbsD0(false),
          passIso(false),
          passMinLxySig(false),
          passMaxLxySig(false),
          passOppCharge(false),
          passTriggerMatch(false),
          passVertexChi2(false),
          passHitsBeforeVertex(false),
          passDeltaR(false),
          passCosine(false),
          passDeltaPhi(false),
          passMass(false)
        {}

        bool passCaloMatch;
        bool passTrackPt;
        bool passSCEt;
        bool passEta;
        bool passLeptonAbsD0;
        bool passIso;
        bool passMinLxySig;
        bool passMaxLxySig;
        bool passOppCharge;
        bool passTriggerMatch;
        bool passVertexChi2;
        bool passHitsBeforeVertex;
        bool passDeltaR;
        bool passCosine;
        bool passDeltaPhi;
        bool passMass;
    };

    // Records which cuts have been passed/failed
    PassedWhichCuts whichCuts( TreeDipseudoLeptonCandidate & candidate, TreeLepton & leptonL, TreeLepton & leptonH, analysisType analysis, double lxyScale, double d0Scale );
    // Checks of all cuts have been passed
    bool passAllCuts( PassedWhichCuts cuts );

    // Useful to print to screen cut info
    void printCutValues();

  private:
    // Which set of cuts & analysis
    analysisCuts setOfCuts_;
    analysisType analysisType_;

    // Cut values

    // Individual Leptons
    double minTrackPt_; // lepton pt
    double minSCEt_; // Matched SC Et
    double maxEta_; // lepton eta (track)

    double minAbsD0Sig_; // min value of lepton d0 sig

    double maxIso_; // max sum pt of tracks within isolation cone

    double maxCaloMatchDeltaR_;

    // Dilepton candidate

    double minLxySig_; // min value of vertex Lxy significance
    double maxLxySig_; // max value of vertex Lxy significance

    bool oppositeCharge_; // Require leptons oto have opposite charge

    double maxVertexChi2_; // max vertex chi^2

    // FIXME currently not in tree
    double maxHitsBeforeVertex_; // max number of hits allowed before vertex

    double minDeltaR_; // min deltaR between leptons

    double minCosine_; // min 3D angle between two leptons

    double maxDeltaPhi_; // max value of delta phi between momentum vector of dilepton pair and vector joining primary and displaced vertices

    double minMass_; // min invariant mass of dilepton

};

#endif
