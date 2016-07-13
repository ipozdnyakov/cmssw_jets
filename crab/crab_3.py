from WMCore.Configuration import Configuration
config = Configuration()

config.section_("General")
config.General.requestName	= 'MinBias0'
config.General.workArea         = 'MinBias_2016B_VdMmay' #config.General.requestName

config.General.transferLogs     = True

config.section_("JobType")
config.JobType.psetName 	= '../python/ConfFile_cfg.py'
config.JobType.pluginName	= 'Analysis'
config.JobType.outputFiles 	= ['jets.root']

config.section_("Data")
config.Data.inputDataset 	= '/L1MinimumBias0/Run2016B-PromptReco-v2/MINIAOD' #VdM May 2016
#config.Data.inputDataset 	= '/FSQJets/Run2016B-PromptReco-v2/MINIAOD' #VdM May 2016

config.Data.lumiMask 		= 'Cert_271036-274240_13TeV_PromptReco_Collisions16_JSON_LowPU.txt' #VdM May 2016
config.Data.unitsPerJob 	= 15
config.Data.splitting 		= 'LumiBased'

config.section_('User')

config.section_("Site")
config.Site.storageSite 	= 'T2_RU_ITEP'
#config.Site.blacklist 		= ['T2_US_Wisconsin', 'T2_US_Caltech']

