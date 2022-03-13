import os
import sys

fileList = ['CMS_Run2011A_DoubleElectron_AOD_12Oct2013-v1_20000_file_index',
            'CMS_Run2011A_DoubleElectron_AOD_12Oct2013-v1_20001_file_index',
            'CMS_Run2011A_DoubleMu_AOD_12Oct2013-v1_10000_file_index',
            'CMS_Run2011A_DoubleMu_AOD_12Oct2013-v1_10001_file_index',
            'CMS_Run2011A_DoubleMu_AOD_12Oct2013-v1_20000_file_index']

min = int(sys.argv[-2])
max = int(sys.argv[-1])+1

for i in range(min,max):
    name = fileList[i]
    nohup = str(i) + '_Data2011nohup.log'
    command = 'nohup cmsRun 2011_Data.py ' + name + ' > '+ nohup + '&'
    os.system(command)
    print("File " + str(i) + " is now running")