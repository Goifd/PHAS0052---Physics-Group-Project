import sys
from distutils import filelist
import FWCore.ParameterSet.Config as cms
from RecoMuon.TrackingTools.MuonServiceProxy_cff import *
import FWCore.PythonUtilities.LumiList as LumiList
import FWCore.ParameterSet.Types as CfgTypes
import FWCore.Utilities.FileUtils as FileUtils

name = sys.argv[-1]
begin = '../datasets/MC2011/'
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
process.MessageLogger.cerr.FwkReport.reportEvery = 1000
process.options = cms.untracked.PSet( wantSummary = cms.untracked.bool(True) )

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(max_events) )


# use the following if you want to run over a full index file
files2012data = FileUtils.loadListFromFile (input)
process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(*files2012data    
    )    
)

process.source.skipEvents = cms.untracked.uint32(0)

process.demo = cms.EDAnalyzer('HiggsDemoAnalyzerGit'
)
# ***********************************************************
# output file name                                          *
# default is Higgs4L1file.root                              *
# ***********************************************************
process.TFileService = cms.Service("TFileService",
       fileName = cms.string(output))

process.p = cms.Path(process.demo)