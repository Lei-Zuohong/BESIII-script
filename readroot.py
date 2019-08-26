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


rootfile = sys.argv[1]
pklfile = sys.argv[2]
treename = sys.argv[3]
branchlist = sys.argv[4:]

'''
roottopkl(rootfile, pklfile, treename, branchlist)
'''
print(branchlist)
print('done root to pkl')
