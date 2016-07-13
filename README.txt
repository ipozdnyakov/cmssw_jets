1.INTRODUCTION

This project contains a code  of a CMSSW  analyzer for extracting jets from MINIAOD data.
Analyzer was created by 'mkedanlzr' command and contains one plugin - MyJetAnalyzer.cc
Also crab.py configuration for CRAB3 and JSON files with good lumisections are included.

2. DATASETS

Three periods of low-pile-up 13 TeV data taking were analysed.

1) ___VdM scan #VdM august (CMSSW_7_4_14, GT 74X_dataRun2_v4  --> CMSSW_7_6_3, GT 76X_dataRun2_v15)
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

3) ___VdM scan #VdM may (CMSSW_8_0_10_patch1, GT = 80X_dataRun2_Prompt_v8)
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

3. BRANCHES

Branches contains differen code and configurations for 2015 and 2016 data

/CMSSW_7_6_3 - for 2015 data
/CMSSW_8_0_6 - for 2016 data
