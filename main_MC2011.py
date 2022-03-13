import os
import sys
fileList = ['CMS_MonteCarlo2011_Summer11LegDR_DYJetsToLL_M-10To50_TuneZ2_7TeV-pythia6_AODSIM_PU_S13_START53_LV6-v1_00000_file_index',
                'CMS_MonteCarlo2011_Summer11LegDR_DYJetsToLL_M-50_7TeV-madgraph-pythia6-tauola_AODSIM_PU_S13_START53_LV6-v1_00000_file_index',
                'CMS_MonteCarlo2011_Summer11LegDR_DYJetsToLL_M-50_7TeV-madgraph-pythia6-tauola_AODSIM_PU_S13_START53_LV6-v1_00001_file_index',
                'CMS_MonteCarlo2011_Summer11LegDR_DYJetsToLL_M-50_7TeV-madgraph-pythia6-tauola_AODSIM_PU_S13_START53_LV6-v1_00002_file_index',
                'CMS_MonteCarlo2011_Summer11LegDR_DYJetsToLL_M-50_7TeV-madgraph-pythia6-tauola_AODSIM_PU_S13_START53_LV6-v1_010000_file_index',
                'CMS_MonteCarlo2011_Summer11LegDR_DYJetsToLL_M-50_7TeV-madgraph-pythia6-tauola_AODSIM_PU_S13_START53_LV6-v1_010001_file_index',
                'CMS_MonteCarlo2011_Summer11LegDR_DYJetsToLL_M-50_7TeV-madgraph-pythia6-tauola_AODSIM_PU_S13_START53_LV6-v1_010002_file_index',
                'CMS_MonteCarlo2011_Summer11LegDR_DYJetsToLL_M-50_7TeV-madgraph-pythia6-tauola_AODSIM_PU_S13_START53_LV6-v1_010003_file_index',
                'CMS_MonteCarlo2011_Summer11LegDR_DYJetsToLL_M-50_7TeV-madgraph-pythia6-tauola_AODSIM_PU_S13_START53_LV6-v1_010004_file_index',
                'CMS_MonteCarlo2011_Summer11LegDR_DYJetsToLL_M-50_7TeV-madgraph-pythia6-tauola_AODSIM_PU_S13_START53_LV6-v1_010005_file_index',
                'CMS_MonteCarlo2011_Summer11LegDR_SMHiggsToZZTo4L_M-125_7TeV-powheg15-JHUgenV3-pythia6_AODSIM_PU_S13_START53_LV6-v1_20000_file_index',
                'CMS_MonteCarlo2011_Summer11LegDR_TTTo2L2Nu2B_7TeV-powheg-pythia6_AODSIM_PU_S13_START53_LV6-v1_00000_file_index',
                'CMS_MonteCarlo2011_Summer11LegDR_ZZTo2e2mu_mll4_7TeV-powheg-pythia6_AODSIM_PU_S13_START53_LV6-v1_00000_file_index',
                'CMS_MonteCarlo2011_Summer11LegDR_ZZTo2e2mu_mll4_7TeV-powheg-pythia6_AODSIM_PU_S13_START53_LV6-v1_20000_file_index',
                'CMS_MonteCarlo2011_Summer11LegDR_ZZTo2e2mu_mll4_7TeV-powheg-pythia6_AODSIM_PU_S13_START53_LV6-v1_40000_file_index',
                'CMS_MonteCarlo2011_Summer11LegDR_ZZTo4e_mll4_7TeV-powheg-pythia6_AODSIM_PU_S13_START53_LV6-v1_00000_file_index',
                'CMS_MonteCarlo2011_Summer11LegDR_ZZTo4e_mll4_7TeV-powheg-pythia6_AODSIM_PU_S13_START53_LV6-v1_10000_file_index',
                'CMS_MonteCarlo2011_Summer11LegDR_ZZTo4e_mll4_7TeV-powheg-pythia6_AODSIM_PU_S13_START53_LV6-v1_20000_file_index',
                'CMS_MonteCarlo2011_Summer11LegDR_ZZTo4e_mll4_7TeV-powheg-pythia6_AODSIM_PU_S13_START53_LV6-v1_30000_file_index',
                'CMS_MonteCarlo2011_Summer11LegDR_ZZTo4e_mll4_7TeV-powheg-pythia6_AODSIM_PU_S13_START53_LV6-v1_40000_file_index',
                'CMS_MonteCarlo2011_Summer11LegDR_ZZTo4e_mll4_7TeV-powheg-pythia6_AODSIM_PU_S13_START53_LV6-v1_420000_file_index',
                'CMS_MonteCarlo2011_Summer11LegDR_ZZTo4mu_mll4_7TeV-powheg-pythia6_AODSIM_PU_S13_START53_LV6-v1_10000_file_index',
                'CMS_MonteCarlo2011_Summer11LegDR_ZZTo4mu_mll4_7TeV-powheg-pythia6_AODSIM_PU_S13_START53_LV6-v1_40000_file_index']
min = int(sys.argv[-2])
max = int(sys.argv[-1])+1
for i in range(min,max):
    name = fileList[i]
    nohup = str(i) + '_MC2011nohup.log'
    command = 'nohup cmsRun 2011_MC.py ' + name + ' > '+ nohup + '&'
    os.system(command)
    print("File " + str(i) + " is now running")