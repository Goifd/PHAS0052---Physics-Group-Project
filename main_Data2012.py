import os
import sys

fileList = ['CMS_Run2012B_DoubleElectron_AOD_22Jan2013-v1_20000_file_index',
                'CMS_Run2012B_DoubleElectron_AOD_22Jan2013-v1_20001_file_index',
                'CMS_Run2012B_DoubleElectron_AOD_22Jan2013-v1_30000_file_index',
                'CMS_Run2012B_DoubleMuParked_AOD_22Jan2013-v1_10000_file_index',
                'CMS_Run2012B_DoubleMuParked_AOD_22Jan2013-v1_20000_file_index',
                'CMS_Run2012B_DoubleMuParked_AOD_22Jan2013-v1_20001_file_index',
                'CMS_Run2012B_DoubleMuParked_AOD_22Jan2013-v1_20002_file_index',
                'CMS_Run2012B_DoubleMuParked_AOD_22Jan2013-v1_210000_file_index',
                'CMS_Run2012B_DoubleMuParked_AOD_22Jan2013-v1_30000_file_index',
                'CMS_Run2012B_DoubleMuParked_AOD_22Jan2013-v1_310000_file_index',
                'CMS_Run2012C_DoubleElectron_AOD_22Jan2013-v1_20000_file_index',
                'CMS_Run2012C_DoubleElectron_AOD_22Jan2013-v1_20001_file_index',
                'CMS_Run2012C_DoubleElectron_AOD_22Jan2013-v1_20002_file_index',
                'CMS_Run2012C_DoubleElectron_AOD_22Jan2013-v1_20003_file_index',
                'CMS_Run2012C_DoubleElectron_AOD_22Jan2013-v1_20011_file_index',
                'CMS_Run2012C_DoubleMuParked_AOD_22Jan2013-v1_10000_file_index',
                'CMS_Run2012C_DoubleMuParked_AOD_22Jan2013-v1_10001_file_index',
                'CMS_Run2012C_DoubleMuParked_AOD_22Jan2013-v1_10002_file_index',
                'CMS_Run2012C_DoubleMuParked_AOD_22Jan2013-v1_10003_file_index',
                'CMS_Run2012C_DoubleMuParked_AOD_22Jan2013-v1_10010_file_index',
                'CMS_Run2012C_DoubleMuParked_AOD_22Jan2013-v1_10011_file_index',
                'CMS_Run2012C_DoubleMuParked_AOD_22Jan2013-v1_10013_file_index',
                'CMS_Run2012C_DoubleMuParked_AOD_22Jan2013-v1_10016_file_index',
                'CMS_Run2012C_DoubleMuParked_AOD_22Jan2013-v1_10018_file_index',
                'CMS_Run2012C_DoubleMuParked_AOD_22Jan2013-v1_10021_file_index',
                'CMS_Run2012C_DoubleMuParked_AOD_22Jan2013-v1_10022_file_index',
                'CMS_Run2012C_DoubleMuParked_AOD_22Jan2013-v1_10024_file_index',
                'CMS_Run2012C_DoubleMuParked_AOD_22Jan2013-v1_20000_file_index']

min = int(sys.argv[-2])
max = int(sys.argv[-1])+1

for i in range(min,max):
    name = fileList[i]
    nohup = str(i) + '_Data2012nohup.log'
    command = 'nohup cmsRun 2012_Data.py ' + name + ' > '+ nohup + '&'
    os.system(command)
    print("File " + str(i) + " is now running")