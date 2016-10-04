1.INTRODUCTION

This project contains a code  of a CMSSW  analyzer for extracting jets from MINIAOD data.
Analyzer was created by 'mkedanlzr' command and contains one plugin - MyJetAnalyzer.cc, so
code should be used from CMSSW_X_X_X/src/analyzer/analyzer/>
Also crab.py configuration for CRAB3 and JSON files with good lumisections are included.

To start use the code - 
	1) Create CMSSW area 
		>cmsrel CMSSW_7_6_3
		>cd CMSSW_7_6_3/src
	2) Create MyJetAnalyzer (name is essential)
		>mkdir MyJetAnalyzer
		>cd MyJetAnalyzer
		>mkedanlzr MyJetAnalyzer
	3) Compile
		>scramv1 b

2. DATASETS (2015, CMSSW_7_6_3)

Three periods of low-pile-up 13 TeV data taking were analysed.

1) ___VdM scan #VdM august (CMSSW_7_4_14, GT 74X_dataRun2_v4  --> CMSSW_7_6_3, GT 76X_dataRun2_v15)

!!! Need to be reprocessed with GT 76X_dataRun2_16Dec2015_v0 (JEC Fall15_25nsV2_DATA.tar.gz) CMSSW_7_6_3

   Cert_254986-255031_13TeV_PromptReco_Collisions15_LOWPU_25ns_JSON.txt

		/L1MinimumBiasHF1/Run2015C_25ns-16Dec2015-v1/MINIAOD
		/L1MinimumBiasHF2/Run2015C_25ns-16Dec2015-v1/MINIAOD (2 jobs failed)
		/L1MinimumBiasHF3/Run2015C_25ns-16Dec2015-v1/MINIAOD (2 jobs failed)
		/L1MinimumBiasHF4/Run2015C_25ns-16Dec2015-v1/MINIAOD
		/L1MinimumBiasHF5/Run2015C_25ns-16Dec2015-v1/MINIAOD
		/L1MinimumBiasHF6/Run2015C_25ns-16Dec2015-v1/MINIAOD
		/L1MinimumBiasHF7/Run2015C_25ns-16Dec2015-v1/MINIAOD
		/L1MinimumBiasHF8/Run2015C_25ns-16Dec2015-v1/MINIAOD

		/FSQJets3/Run2015C_25ns-16Dec2015-v1/MINIAOD

2) ___CMS Totem Run #CMS totem (CMSSW_7_4_15, GT 74X_dataRun2_Prompt_v4  --> CMSSW_7_6_3, GT 76X_dataRun2_v15)

!!! Need to be reprocessed with GT 76X_dataRun2_16Dec2015_v0 (JEC Fall15_25nsV2_DATA.tar.gz) CMSSW_7_6_3

	 Cert_259152-259431_13TeV_PromptReco_Collisions15_25ns_Totem_JSON.txt

    /L1MinimumBiasHF1/Run2015D-16Dec2015-v1/MINIAOD
		/L1MinimumBiasHF2/Run2015D-16Dec2015-v1/MINIAOD	(2 jobs failed)
		/L1MinimumBiasHF3/Run2015D-16Dec2015-v1/MINIAOD
		/L1MinimumBiasHF4/Run2015D-16Dec2015-v1/MINIAOD
		/L1MinimumBiasHF5/Run2015D-16Dec2015-v1/MINIAOD
		/L1MinimumBiasHF6/Run2015D-16Dec2015-v1/MINIAOD
		/L1MinimumBiasHF7/Run2015D-16Dec2015-v1/MINIAOD
		/L1MinimumBiasHF8/Run2015D-16Dec2015-v1/MINIAOD

    /FSQJets3/Run2015D-16Dec2015-v1/MINIAOD

3. MC datasets (DR76 - RECO with CMSSW76)

https://cms-pdmv.cern.ch/mcm/requests?prepid=FSQ-RunIIFall15MiniAODv2-0002*&page=0&shown=536871039

/MinBias_Pt-10to35_fwdJet_bwdJet_TuneCUETP8M1_13TeV-pythia8/RunIIFall15MiniAODv2-PU25nsData2015v1_castor_76X_mcRun2_asymptotic_v12-v1/MINIAODSIM
/QCD_Pt-35toInf_TuneCUETP8M1_13TeV-pythia8/RunIIFall15MiniAODv2-PU25nsData2015v1_castor_76X_mcRun2_asymptotic_v12-v1/MINIAODSIM
/MinBias_Pt-35toInf_fwdJet_bwdJet_TuneCUETP8M1_13TeV-pythia8/RunIIFall15MiniAODv2-PU25nsData2015v1_castor_76X_mcRun2_asymptotic_v12-v1/MINIAODSIM
/MinBias_Pt-35toInf_fwdJet_bwdJet_TuneCUETP8M1_13TeV-pythia8/RunIIFall15MiniAODv2-PU25nsData2015v1_castor_76X_mcRun2_asymptotic_v12_ext1-v1/MINIAODSIM
/MinBias_TuneCUETP8M1_13TeV_PYTHIA8/RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/MINIAODSIM


/QCD_Pt-10to35_TuneCUETHS1_13TeV-herwigpp/RunIIFall15MiniAODv2-PU25nsData2015v1_castor_76X_mcRun2_asymptotic_v12-v1/MINIAODSIM
/QCD_Pt-10to35_fwdJet_bwdJet_TuneCUETHS1_13TeV-herwigpp/RunIIFall15MiniAODv2-PU25nsData2015v1_castor_76X_mcRun2_asymptotic_v12-v1/MINIAODSIM
/QCD_Pt-35toInf_TuneCUETHS1_13TeV-herwigpp/RunIIFall15MiniAODv2-PU25nsData2015v1_castor_76X_mcRun2_asymptotic_v12-v1/MINIAODSIM
/QCD_Pt-35toInf_fwdJet_bwdJet_TuneCUETHS1_13TeV-herwigpp/RunIIFall15MiniAODv2-PU25nsData2015v1_castor_76X_mcRun2_asymptotic_v12-v1/MINIAODSIM
/MinBias_TuneCUETHS1-13TeV-herwigpp/RunIIFall15MiniAODv2-PU25nsData2015v1_castor_76X_mcRun2_asymptotic_v12-v1/MINIAODSIM

GLOBAL TAG (from https://twiki.cern.ch/twiki/bin/view/CMSPublic/SWGuideFrontierConditions#Global_Tags_for_RunIIFall15DR76)
	--- 76X_mcRun2_asymptotic_RunIIFall15DR76_v1

JEC (from https://twiki.cern.ch/twiki/bin/viewauth/CMS/JECDataMC#Recommended_for_MC)
	--- Fall15_25nsV2_MC.tar.gz

Further information about other GLOBAL TAG record (e.g. HLT)
	- https://cms-conddb.cern.ch/cmsDbBrowser/diff/Prod/gts/76X_mcRun2_asymptotic_RunIIFall15DR76_v1/76X_mcRun2_asymptotic_v12
