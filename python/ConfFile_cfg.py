import FWCore.ParameterSet.Config as cms
process = cms.Process("USER")
process.load("FWCore.MessageService.MessageLogger_cfi")
process.load("Configuration.StandardSequences.Services_cff")

process.MessageLogger.cerr.FwkReport.reportEvery = 10000
process.MessageLogger.cerr.default.limit = 10
process.options = cms.untracked.PSet(wantSummary = cms.untracked.bool(True))



process.maxEvents = cms.untracked.PSet(input = cms.untracked.int32(100))

#GLOBAL TAG
process.load('Configuration.StandardSequences.Services_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_condDBv2_cff')
process.GlobalTag.globaltag = '80X_dataRun2_Prompt_v8'

#INPUT FILE
process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
	#'/store/data/Run2016B/FSQJets/MINIAOD/PromptReco-v2/000/273/150/00000/E099BFE2-D719-E611-8E71-02163E014476.root' #VdM May2016
	'/store/data/Run2016B/FSQJets/MINIAOD/PromptReco-v2/000/273/426/00000/E0640C1B-861B-E611-A206-02163E013556.root'
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
