import os
import sys
fileList = ['CMS_MonteCarlo2012_Summer12_DR53X_DYJetsToLL_M-10to50_HT-200to400_TuneZ2star_8TeV-madgraph-tauola_AODSIM_PU_S10_START53_V19-v1_00000_file_index',
                'CMS_MonteCarlo2012_Summer12_DR53X_DYJetsToLL_M-10to50_HT-200to400_TuneZ2star_8TeV-madgraph-tauola_AODSIM_PU_S10_START53_V19-v1_30000_file_index',
                'CMS_MonteCarlo2012_Summer12_DR53X_DYJetsToLL_M-10to50_HT-400toInf_TuneZ2star_8TeV-madgraph-tauola_AODSIM_PU_S10_START53_V19-v1_00000_file_index',
                'CMS_MonteCarlo2012_Summer12_DR53X_DYJetsToLL_M-10to50_HT-400toInf_TuneZ2star_8TeV-madgraph-tauola_AODSIM_PU_S10_START53_V19-v1_30000_file_index',
                'CMS_MonteCarlo2012_Summer12_DR53X_DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-tauola-tauPolarOff_AODSIM_PU_S10_START53_V19-v1_00000_file_index',
                'CMS_MonteCarlo2012_Summer12_DR53X_DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-tauola-tauPolarOff_AODSIM_PU_S10_START53_V19-v1_00001_file_index',
                'CMS_MonteCarlo2012_Summer12_DR53X_SMHiggsToZZTo4L_M-125_8TeV-powheg15-JHUgenV3-pythia6_AODSIM_PU_S10_START53_V19-v1_10000_file_index',
                'CMS_MonteCarlo2012_Summer12_DR53X_TTbar_8TeV-Madspin_aMCatNLO-herwig_AODSIM_PU_S10_START53_V19-v2_00000_file_index',
                'CMS_MonteCarlo2012_Summer12_DR53X_TTbar_8TeV-Madspin_aMCatNLO-herwig_AODSIM_PU_S10_START53_V19-v2_20000_file_index',
                'CMS_MonteCarlo2012_Summer12_DR53X_ZZTo2e2mu_8TeV-powheg-pythia6_AODSIM_PU_RD1_START53_V7N-v2_10000_file_index',
                'CMS_MonteCarlo2012_Summer12_DR53X_ZZTo4e_8TeV-powheg-pythia6_AODSIM_PU_RD1_START53_V7N-v2_20000_file_index',
                'CMS_MonteCarlo2012_Summer12_DR53X_ZZTo4mu_8TeV-powheg-pythia6_AODSIM_PU_RD1_START53_V7N-v1_20000_file_index']
min = int(sys.argv[-2])
max = int(sys.argv[-1])+1
for i in range(min,max):
    name = fileList[i]
    nohup = str(i) + '_MC2012nohup.log'
    command = 'nohup cmsRun 2012_MC.py ' + name + ' > '+ nohup + '&'
    os.system(command)
    print("File " + str(i) + " is now running")