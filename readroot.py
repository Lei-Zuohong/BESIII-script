from ROOT import TFile, TTree
import os
import re
import sys
import pickle


def roottopkl(rootfile, pklfile, treename, branchlist):
    infile = TFile(rootfile)
    intree = infile.Get(treename)
    innum = intree.GetEntries()
    output = []
    for i1 in range(innum):
        intree.GetEntry(i1)
        output.append({})
        for i2 in branchlist:
            exec('indata = intree.%s' % (i2))
            output[i1][i2] = indata
    with open(pklfile, 'wb') as outfile:
        pickle.dump(output, outfile)


rootfile = '/scratchfs/bes/leizh/opp_data/simr/omega_2.0.root'
pklfile = 'test.pkl'
treename = 'fit4c'
branchlist = ['momega']


roottopkl(rootfile, pklfile, treename, branchlist)
