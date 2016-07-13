# import ROOT in batch mode
import sys
oldargv = sys.argv[:]
sys.argv = [ '-b-' ]
import ROOT
ROOT.gROOT.SetBatch(True)
sys.argv = oldargv

# load FWLite C++ libraries
ROOT.gSystem.Load("libFWCoreFWLite.so");
ROOT.gSystem.Load("libDataFormatsFWLite.so");
ROOT.FWLiteEnabler.enable()

# load FWlite python libraries
from DataFormats.FWLite import Handle, Events

triggerBits, triggerBitLabel = Handle("edm::TriggerResults"), ("TriggerResults","","HLT")
triggerObjects, triggerObjectLabel  = Handle("std::vector<pat::TriggerObjectStandAlone>"), "selectedPatTrigger"
triggerPrescales, triggerPrescaleLabel  = Handle("pat::PackedTriggerPrescales"), "patTrigger"

# use 'edmFileUtil -d /store/whatever.root' to get the physical file name
#VdM august
#events = Events("root://eoscms.cern.ch//eos/cms/store/data/Run2016B/FSQJets/MINIAOD/PromptReco-v2/000/273/426/00000/E0640C1B-861B-E611-A206-02163E013556.root")
#events = Events("root://eoscms.cern.ch//eos/cms/store/data/Run2015C_25ns/ZeroBias1/MINIAOD/16Dec2015-v1/20000/004E276A-C5B4-E511-BBD5-20CF305B052B.root")
#events = Events("root://eoscms.cern.ch//eos/cms/store/data/Run2015C_25ns/L1MinimumBiasHF1/MINIAOD/16Dec2015-v1/00000/5CC2B5AD-21B6-E511-8902-002590A80E08.root")
events = Events("root://eoscms.cern.ch//eos/cms/store/data/Run2015C_25ns/FSQJets3/MINIAOD/16Dec2015-v1/50000/002FBD2D-AEAF-E511-BB6D-00261894386F.root")

for iev,event in enumerate(events):
    event.getByLabel(triggerBitLabel, triggerBits)
    event.getByLabel(triggerPrescaleLabel, triggerPrescales)

    print "\nEvent %d: run %6d, lumi %4d, event %12d" % (iev,event.eventAuxiliary().run(), event.eventAuxiliary().luminosityBlock(),event.eventAuxiliary().event())
    names = event.object().triggerNames(triggerBits.product())

    for i in xrange(triggerBits.product().size()):
        if iev == 0:
            print "Trigger ", names.triggerName(i) 
        else:
	    if triggerBits.product().accept(i):
	    	print "Trigger ", names.triggerName(i), ", prescale ", triggerPrescales.product().getPrescaleForIndex(i)
    if iev > 10: break
