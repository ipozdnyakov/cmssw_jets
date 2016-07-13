from WMCore.Configuration import Configuration
config = Configuration()

config.section_("General")
config.General.requestName	= 'MinBiasHF8'
#config.General.requestName	= 'FSQJets3_2015C_VdMaugust'
#config.General.requestName	= 'FSQJets3_2015D_CMSTotem'
#config.General.workArea         = 'MinBias_2015C_VdMaugust' #config.General.requestName
config.General.workArea         = 'MinBias_2015D_CMSTotem' #config.General.requestName
config.General.transferLogs     = True

config.section_("JobType")
config.JobType.psetName 	= '../python/ConfFile_cfg.py'
config.JobType.pluginName	= 'Analysis'
config.JobType.outputFiles 	= ['jets.root']

config.section_("Data")
#config.Data.inputDataset 	= '/L1MinimumBiasHF8/Run2015C_25ns-16Dec2015-v1/MINIAOD' #VdM august
config.Data.inputDataset 	= '/L1MinimumBiasHF8/Run2015D-16Dec2015-v1/MINIAOD' #CMS Totem
#config.Data.inputDataset 	= '/FSQJets3/Run2015D-16Dec2015-v1/MINIAOD' #CMS Totem
#config.Data.inputDataset 	= '/FSQJets3/Run2015C_25ns-16Dec2015-v1/MINIAOD' #VdM august

config.Data.lumiMask 		= 'Cert_259152-259431_13TeV_PromptReco_Collisions15_25ns_Totem_JSON.txt' #CMS Totem
#config.Data.lumiMask 		= 'Cert_254986-255031_13TeV_PromptReco_Collisions15_LOWPU_25ns_JSON.txt' #VdM august
config.Data.unitsPerJob 	= 15
config.Data.splitting 		= 'LumiBased'

config.section_('User')

config.section_("Site")
config.Site.storageSite 	= 'T2_RU_ITEP'
#config.Site.blacklist 		= ['T2_US_Wisconsin', 'T2_US_Caltech']

