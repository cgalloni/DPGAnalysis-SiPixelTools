from WMCore.Configuration import Configuration
config = Configuration()

config.section_('General')
config.General.transferOutputs = True
config.General.transferLogs = True
config.General.requestName = 'Run300780_BPix_FPix'

config.section_('JobType')
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'pxl_BPIX_FPIX.py'
#config.JobType.pyCfgParams = []
#config.JobType.inputFiles = []
#config.JobType.disableAutomaticOutputCollection = True
#config.JobType.outputFiles = ['Resolution.root']

config.section_('Data')
config.Data.inputDataset = '/SingleMuon/Run2017C-PromptReco-v3/RECO'
config.Data.runRange = '300780'
config.Data.splitting = 'EventAwareLumiBased'
config.Data.unitsPerJob = 1000
config.Data.outLFNDirBase = '/store/group/dpg_tracker_pixel/comm_pixel/Resolution/Phase1'
config.Data.outputDatasetTag = 'Run300780-CMSSW_9_2_7-92X_dataRun2_Prompt_v8'
config.Data.ignoreLocality = True

config.section_('Site')
config.Site.storageSite = 'T2_CH_CERN'
