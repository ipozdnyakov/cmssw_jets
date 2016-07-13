import FWCore.ParameterSet.Config as cms
process = cms.Process("USER")
process.load("FWCore.MessageService.MessageLogger_cfi")
process.maxEvents = cms.untracked.PSet(input = cms.untracked.int32(1))

#GLOBAL TAG
process.load('Configuration.StandardSequences.Services_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_condDBv2_cff')
process.GlobalTag.globaltag = '76X_dataRun2_v15'

#INPUT FILE
process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
	#'/store/data/Run2015C_25ns/ZeroBias1/MINIAOD/16Dec2015-v1/20000/0042E935-A7B5-E511-B13D-0025905B860C.root'		#VdM august
        #'/store/data/Run2015C_25ns/L1MinimumBiasHF1/MINIAOD/16Dec2015-v1/00000/5CC2B5AD-21B6-E511-8902-002590A80E08.root'	
	'/store/data/Run2015C_25ns/FSQJets3/MINIAOD/16Dec2015-v1/50000/002FBD2D-AEAF-E511-BB6D-00261894386F.root'
	#'/store/data/Run2016B/FSQJets/MINIAOD/PromptReco-v2/000/273/426/00000/E0640C1B-861B-E611-A206-02163E013556.root'
    )
)

#OUTPUT FILE
process.TFileService = cms.Service("TFileService",
        fileName = cms.string('jets.root'),
        closeFileFast = cms.untracked.bool(True)
)

#ANALYZER
process.JetCollection = cms.EDAnalyzer(
	'MyJetAnalyzer',
	 JetInputTag = cms.InputTag("slimmedJets"),
	 VertexInputTag = cms.InputTag("offlineSlimmedPrimaryVertices"),
	 MinimumPt = cms.double(10),
	 bits = cms.InputTag("TriggerResults","","HLT"),
	 prescales = cms.InputTag("patTrigger")
)
process.p = cms.Path(process.JetCollection)

###################################################
#process.options = cms.untracked.PSet(wantSummary = cms.untracked.bool(True))
#from HLTrigger.HLTfilters.hltHighLevel_cfi import *
#process.triggerSelection = hltHighLevel.clone(
#	TriggerResultsTag = "TriggerResults::HLT",
#	HLTPaths = ["HLT_DiPFJet15_NoCaloMatched_v*","HLT_DiPFJet15_FBEta2_NoCaloMatched_v*"]
#)
