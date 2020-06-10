# -*- coding: UTF-8 -*-
# Public pack
import pickle
import sys
# Private pack
import ROOT
import headpy.hbes.hfit as hfit


tempfolder = sys.argv[1]
backfunction = sys.argv[2]
signfunction = sys.argv[3]
energy = sys.argv[4]
energy = float(energy)
histpkl = '%s/temphist.pkl' % (tempfolder)
optionpkl = '%s/tempoption.pkl' % (tempfolder)
datasetpkl = '%s/tempdataset.pkl' % (tempfolder)
hfit.dofit(energy,
           histpkl,
           optionpkl,
           datasetpkl,
           backfunction=backfunction,
           signfunction=signfunction)
