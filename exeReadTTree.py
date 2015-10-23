# Name: execute.py
#
# CMS Open Data
#
# Description: 
#
# Returns: 

import ROOT
from readTTree import readTTree
import time

start_time = time.time()

# CMS data:

data_files = [
        'root://eospublic.cern.ch//eos/opendata/cms/Run2010B/Mu/PATtuples/Mu_PAT_data_500files_1.root',
]

maxEv = 100 #number of processed events. maxEvents = -1 runs over all of them


t=readTTree()
tree=t.process()

t.plotter()

print("--- %s seconds ---" % (time.time() - start_time))


