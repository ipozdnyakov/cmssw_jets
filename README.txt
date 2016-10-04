1.INTRODUCTION

This project contains a code  of a CMSSW  analyzer for extracting jets from MINIAOD data.
Analyzer was created by 'mkedanlzr' command and contains one plugin - MyJetAnalyzer.cc
Also crab.py configuration for CRAB3 and JSON files with good lumisections are included.

To start use the code - 
	1) Create CMSSW area 
		>cmsrel CMSSW_8_0_6
		>cd CMSSW_8_0_6/src
	2) Create MyJetAnalyzer (name is essential)
		>mkdir MyJetAnalyzer
		>cd MyJetAnalyzer
		>mkedanlzr MyJetAnalyzer
	3) Compile
		>scramv1 b

2. DATASETS (2016, CMSSW_8_0_6)

One period of 2016 low-pile-up 13 TeV data taking were analysed.

1) ___VdM scan #VdM may (CMSSW_8_0_10_patch1, GT = 80X_dataRun2_Prompt_v8)

!!! Need to be reprocessed with GT 80X_dataRun2_ICHEP16_repro_v0 (or 80X_dataRun2_Prompt_v14), JEC Spring16_25nsV6_DATA.tar.gz, CMSSW_8_0_10

	 Cert_271036-274240_13TeV_PromptReco_Collisions16_JSON_LowPU.txt

		/L1MinimumBias0/Run2016B-PromptReco-v2/MINIAOD
		/L1MinimumBias1/Run2016B-PromptReco-v2/MINIAOD (6 jobs failed)
		/L1MinimumBias2/Run2016B-PromptReco-v2/MINIAOD (8 jobs failed)
		/L1MinimumBias3/Run2016B-PromptReco-v2/MINIAOD (3 jobs failed)
		/L1MinimumBias4/Run2016B-PromptReco-v2/MINIAOD
		/L1MinimumBias5/Run2016B-PromptReco-v2/MINIAOD
		/L1MinimumBias6/Run2016B-PromptReco-v2/MINIAOD (1 job failed)
		/L1MinimumBias7/Run2016B-PromptReco-v2/MINIAOD (1 job failed)
		/L1MinimumBias8/Run2016B-PromptReco-v2/MINIAOD
		/L1MinimumBias9/Run2016B-PromptReco-v2/MINIAOD

		/FSQJets/Run2016B-PromptReco-v2/MINIAOD

For up to date GLOBAL TAGS : https://twiki.cern.ch/twiki/bin/view/CMSPublic/SWGuideFrontierConditions#Global_Tags_for_2016_data_re_rec
For up to dat JEC : https://twiki.cern.ch/twiki/bin/viewauth/CMS/JECDataMC#Recommended_for_Data
