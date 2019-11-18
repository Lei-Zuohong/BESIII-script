# Public pack
import pickle
import sys
# Private pack
import ROOT

with open('%s/temphist.pkl' % (sys.argv[1]), 'rb') as infile:
    hist = pickle.load(infile)
with open('%s/tempdataset.pkl' % (sys.argv[1]), 'rb') as infile:
    dataset = pickle.load(infile)
with open('%s/tempoption2.pkl' % (sys.argv[1]), 'rb') as infile:
    option_list = pickle.load(infile)
# 2.start roofit
ROOT.gSystem.Load('libRooFit')
# 2.build momega
mass = ROOT.RooRealVar('mass', 'mass',
                       dataset['m']-dataset['c'],
                       dataset['m']+dataset['c'])
# 2.build pdf for mc
gmean = ROOT.RooRealVar('gmean', 'gmean',
                        option_list['gmean'][0],
                        option_list['gmean'][1],
                        option_list['gmean'][2])
gsigm = ROOT.RooRealVar('gsigm', 'gsigm',
                        option_list['gsigm'][0],
                        option_list['gsigm'][1],
                        option_list['gsigm'][2])
gauss = ROOT.RooGaussian('gauss', 'gauss', mass, gmean, gsigm)
datam = ROOT.RooDataHist(
    'datam', 'datam', ROOT.RooArgList(mass), hist['m'])
pdfmc = ROOT.RooHistPdf('pdfmc', 'pdfmc', ROOT.RooArgSet(mass), datam, 0)
pdfsi = ROOT.RooFFTConvPdf('pdfsi', 'pdfsi', mass, pdfmc, gauss)
# 2.build pdf for back
p0 = ROOT.RooRealVar('p0', 'p0',
                     option_list['p0'][0],
                     option_list['p0'][1],
                     option_list['p0'][2])
p1 = ROOT.RooRealVar('p1', 'p1',
                     option_list['p1'][0],
                     option_list['p1'][1],
                     option_list['p1'][2])
p2 = ROOT.RooRealVar('p2', 'p2',
                     option_list['p2'][0],
                     option_list['p2'][1],
                     option_list['p2'][2])
pdfba = ROOT.RooPolynomial(
    'pdfba', 'pdfba', mass, ROOT.RooArgList(p0, p1, p2))
# 2.conbine gauss1+gauss2
npdf1 = ROOT.RooRealVar('npdf1', 'npdf1',
                        option_list['npdf1'][0],
                        option_list['npdf1'][1],
                        option_list['npdf1'][2])
npdf2 = ROOT.RooRealVar('npdf2', 'npdf2',
                        option_list['npdf2'][0],
                        option_list['npdf2'][1],
                        option_list['npdf2'][2])
pdf12 = ROOT.RooAddPdf('pdf12', 'pdf12', ROOT.RooArgList(
    pdfsi, pdfba), ROOT.RooArgList(npdf1, npdf2))
# 3.import data
datar = ROOT.RooDataHist(
    'datar', 'datar', ROOT.RooArgList(mass), hist['r'])
# 3.fit
a = pdf12.fitTo(datar)
# 4.output
output = {}
output['nevent'] = npdf1.getVal()
output['enevent'] = npdf1.getError()
nmc = hist['m'].GetEntries()
n = 500000
output['e'] = e = nmc / n
output['ee'] = pow(e*(1-e)/n, 0.5)
with open('%s/%s' % (sys.argv[1], sys.argv[2]), 'wb') as outfile:
    pickle.dump(output, outfile)
