// system include files
#include <memory>
#include <vector>
#include <cmath>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDAnalyzer.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/Common/interface/TriggerNames.h"
#include "DataFormats/Common/interface/TriggerResults.h"
#include "DataFormats/JetReco/interface/PFJet.h"
#include "DataFormats/JetReco/interface/PFJetCollection.h"
#include "DataFormats/PatCandidates/interface/Jet.h"
#include "DataFormats/Math/interface/deltaR.h"
#include "DataFormats/PatCandidates/interface/TriggerObjectStandAlone.h"
#include "DataFormats/PatCandidates/interface/PackedTriggerPrescales.h"

#include <TROOT.h>
#include <TSystem.h>
#include "TFile.h"
#include "TMath.h"
#include "TTree.h"

//TFile Service
#include "FWCore/ServiceRegistry/interface/Service.h"
#include "CommonTools/UtilAlgos/interface/TFileService.h"

using namespace cms;
using namespace edm;
using namespace std;
using namespace pat;
using namespace reco;

//
// class declaration
//

class MyJetAnalyzer : public edm::EDAnalyzer {
   public:
      explicit MyJetAnalyzer(const edm::ParameterSet&);
      ~MyJetAnalyzer();
      static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);
   private:
      virtual void beginJob() override;
      virtual void analyze(const edm::Event&, const edm::EventSetup&) override;
      virtual void endJob() override;

      TTree *jet_tree;
      double pt_min_;
      int iRun = -1, iEvt = -1, nPV = -1;
      int CNTR = -1, FWD2 = -1, FWD3 = -1;
      double pt = 0, phi = 0, eta = 0, rap = 0, cor = 0, unc = 0;

      edm::EDGetTokenT<edm::TriggerResults> triggerBits_;
      edm::EDGetTokenT<pat::PackedTriggerPrescales> triggerPrescales_;
      edm::EDGetTokenT<pat::JetCollection> jet_label_;
      edm::EDGetTokenT<reco::VertexCollection> vertex_label_;
};

MyJetAnalyzer::MyJetAnalyzer(const edm::ParameterSet& iConfig):
    triggerBits_(consumes<edm::TriggerResults>(iConfig.getParameter<edm::InputTag>("bits"))),
    triggerPrescales_(consumes<pat::PackedTriggerPrescales>(iConfig.getParameter<edm::InputTag>("prescales"))),
    jet_label_(consumes<pat::JetCollection>(iConfig.getParameter<edm::InputTag>("JetInputTag"))),
    vertex_label_(consumes<reco::VertexCollection>(iConfig.getParameter<edm::InputTag>("VertexInputTag")))
{
  pt_min_    	= iConfig.getParameter<double>("MinimumPt");

  edm::Service<TFileService> fs;
  jet_tree = fs->make<TTree>("jet_tree","jet_tree");

  jet_tree->Branch("iEvt",&iEvt,"iEvt/I");
  jet_tree->Branch("iRun",&iRun,"iRun/I");
  jet_tree->Branch("nPV",&nPV,"nPV/I");
  jet_tree->Branch("CNTR",&CNTR,"CNTR/I");
  jet_tree->Branch("FWD2",&FWD2,"FWD2/I");
  jet_tree->Branch("FWD3",&FWD3,"FWD3/I");
  jet_tree->Branch("pt",&pt,"pt/D");
  jet_tree->Branch("phi",&phi,"phi/D");
  jet_tree->Branch("eta",&eta,"eta/D");
  jet_tree->Branch("rap",&rap,"rap/D");
  jet_tree->Branch("cor",&cor,"cor/D");
  jet_tree->Branch("unc",&unc,"unc/D");
}

MyJetAnalyzer::~MyJetAnalyzer(){
}

// ------------ method called for each event  ------------
void
MyJetAnalyzer::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup)
{
    using namespace edm;
//EVENT
    iEvt=iEvent.eventAuxiliary().event();
    iRun=iEvent.eventAuxiliary().run();
//VERTICES
    edm::Handle<reco::VertexCollection> vtx;
    iEvent.getByToken(vertex_label_, vtx);
    nPV = (*vtx).size();
//TRIGGERS
    edm::Handle<edm::TriggerResults> triggerBits;
    edm::Handle<pat::PackedTriggerPrescales> triggerPrescales;

    iEvent.getByToken(triggerBits_, triggerBits);
    iEvent.getByToken(triggerPrescales_, triggerPrescales);

    const edm::TriggerNames &names = iEvent.triggerNames(*triggerBits);
    CNTR = -1;
    FWD2 = -1;
    FWD3 = -1;
    for (unsigned int i = 0, n = triggerBits->size(); i < n; ++i) {
	if(names.triggerName(i) == "HLT_DiPFJet15_NoCaloMatched_v2"){
		if(triggerBits->accept(i)) CNTR = triggerPrescales->getPrescaleForIndex(i);
	}
	if(names.triggerName(i) == "HLT_DiPFJet15_FBEta2_NoCaloMatched_v2"){
		if(triggerBits->accept(i)) FWD2 = triggerPrescales->getPrescaleForIndex(i);
	}
	if(names.triggerName(i) == "HLT_DiPFJet15_FBEta3_NoCaloMatched_v2"){
		if(triggerBits->accept(i)) FWD3 = triggerPrescales->getPrescaleForIndex(i);
	}
    }
//JETS
  edm::Handle<pat::JetCollection> jets;
  iEvent.getByToken(jet_label_, jets);
  for (const pat::Jet &j : *jets) {
    if (j.pt() < pt_min_) continue;
    pt = j.pt();
    phi = j.phi();
    eta = j.eta();
    rap = j.rapidity();
    cor = j.jecFactor("Uncorrected");
    jet_tree->Fill();
  }
}

void MyJetAnalyzer::beginJob(){}
void MyJetAnalyzer::endJob(){}

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void MyJetAnalyzer::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  //The following says we do not know what parameters are allowed so do no validation
  // Please change this to state exactly what you do use, even if it is no parameters
  edm::ParameterSetDescription desc;
  desc.setUnknown();
  descriptions.addDefault(desc);
}

//define this as a plug-in
DEFINE_FWK_MODULE(MyJetAnalyzer);
