import sys
import FWCore.ParameterSet.Config as cms
from RecoMuon.TrackingTools.MuonServiceProxy_cff import *
import FWCore.PythonUtilities.LumiList as LumiList
import FWCore.ParameterSet.Types as CfgTypes
import FWCore.Utilities.FileUtils as FileUtils

name = sys.argv[-1]
begin = '../datasets/Data2012/'
end_txt = '.txt'
end_root = '.root'
max_events = -1

input = begin + name + end_txt
output = name + end_root


process = cms.Process("Demo")

# intialize MessageLogger and output report
process.load("FWCore.MessageLogger.MessageLogger_cfi")
process.MessageLogger.cerr.threshold = 'INFO'
process.MessageLogger.categories.append('Demo')
process.MessageLogger.cerr.INFO = cms.untracked.PSet(
        limit = cms.untracked.int32(-1)
        )
process.options = cms.untracked.PSet( wantSummary = cms.untracked.bool(True) )

# set the maximum number of events to be processed   
process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(max_events) )

# define JSON file for 2012 data
goodJSON = '../datasets/Data2012/Cert_190456-208686_8TeV_22Jan2013ReReco_Collisions12_JSON.txt'
myLumis = LumiList.LumiList(filename = goodJSON).getCMSSWString().split(',')

# use the following if you want to run over a full index file
files2012data = FileUtils.loadListFromFile (input)
process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(*files2012data    
    )    
)

# apply JSON file
process.source.lumisToProcess = CfgTypes.untracked(CfgTypes.VLuminosityBlockRange())
process.source.lumisToProcess.extend(myLumis)

# number of events to be skipped (0 by default) 
process.source.skipEvents = cms.untracked.uint32(0)

process.demo = cms.EDAnalyzer('HiggsDemoAnalyzerGit')

# output file name                                          
process.TFileService = cms.Service("TFileService",
    fileName = cms.string(output))

process.p = cms.Path(process.demo)
