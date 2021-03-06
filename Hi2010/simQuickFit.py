#! /usr/bin/env python

from optparse import OptionParser

parser = OptionParser()
parser.add_option('--pt', dest='pt', default=4.0, type='float',
                  help='pt to cut at')
parser.add_option('--params', '-p', default='', dest='paramfile',
                  help='initial parameters file')
parser.add_option('--keys', action="store_true",default=False, dest='keys',
                  help='use keys pdf for background')
parser.add_option('-b', action='store_true', default=False, dest='b',
                  help='no x windows')
(opts, args) = parser.parse_args()

import pyroot_logon
from ROOT import gROOT
gROOT.ProcessLine('.L buildSimPdf.cc+')

from ROOT import readData,computeRatio,computeRatioError,buildPdf,\
     computeSumError,\
     RooWorkspace,RooFit,TCanvas,kRed,kGreen,kDashed,buildSimPdf,RooArgSet,\
     RooRealVar,RooMsgService, TMath, TFile, RooAbsReal
from math import sqrt

RooMsgService.instance().setGlobalKillBelow(RooFit.ERROR)

hidatafile = 'data/dimuonTree_150mub.root'
ppdatafile = 'data/dimuonTree_2011_pp.root'

mmin = 7.
mmax = 14.


cuts = '(muPlusPt > %0.1f) && (muMinusPt > %0.1f) && (abs(upsRapidity)<2.4) && (vProb > 0.05)' \
       % (opts.pt, opts.pt)
simparamfile = opts.paramfile
useKeys = opts.keys
## cuts = '(muPlusPt > 3.5) && (muMinusPt > 3.5) && (abs(upsRapidity)<2.4)'
## simparamfile = 'nom3.5SimFit.txt'

ws = RooWorkspace("ws","ws")

readData(ws, hidatafile, ppdatafile, cuts, mmin, mmax)

mass = ws.var('invariantMass')

ppBkgModel = 1
bkgModel = 0
if useKeys:
    bkgModel = 2

buildPdf(ws, False, ppBkgModel, True)
buildPdf(ws, True, bkgModel, True)
simPdf = buildSimPdf(ws, ws.cat('dataCat'))

#ws.Print()

data = ws.data('data').reduce('(QQsign==QQsign::PlusMinus)')
pars = simPdf.getParameters(data)
ws.var('nsig1_pp').setVal(90)
ws.var('nsig1_pp').setError(10)
ws.var('nsig1_hi').setVal(1200)
ws.var('nsig1_hi').setError(40)

ws.var('nbkg_pp').setVal(335*(mmax-mmin)/7.)
ws.var('nbkg_pp').setError(12)
ws.var('nbkg_hi').setVal(10000*(mmax-mmin)/7.)
ws.var('nbkg_hi').setError(100)

if len(simparamfile) > 0:
    pars.readFromFile(simparamfile)

ws.Print()
data.Print()

pars.Print('v')

#assert(False)
fr = simPdf.fitTo(data, RooFit.Extended(),
                  RooFit.Minos(False),
                  RooFit.NumCPU(2),
                  RooFit.Save(True))

pars.writeToFile('lastSimFit.txt')

#assert(False)

dataCat = ws.cat('dataCat')
catSet = RooArgSet(dataCat)

Nexp = simPdf.expectedEvents(data.get())
print 'Nexp:', Nexp

hican = TCanvas("hi", "hi")
dataCat.setLabel('hi')
mf_hi = mass.frame(mmin, mmax, int((mmax-mmin)*10))
data.plotOn(mf_hi, RooFit.Invisible(),
            RooFit.Cut('(dataCat==dataCat::hi)'),
            RooFit.Name('data_norm'))
simPdf.plotOn(mf_hi, RooFit.Slice(catSet),
##               RooFit.Normalization(Nexp, RooAbsReal.NumEvent),
              RooFit.ProjWData(catSet,data),
              RooFit.Name('fullFit')
              )
simPdf.plotOn(mf_hi, RooFit.Components('bkg*'),
##               RooFit.Normalization(Nexp, RooAbsReal.NumEvent),
              RooFit.Slice(catSet),
              RooFit.ProjWData(catSet,data),
              RooFit.LineColor(kRed+2),
              RooFit.LineStyle(kDashed))
## simPdf.plotOn(mf_hi, RooFit.Components('bkgPoly*'),
##               RooFit.Normalization(Nexp, RooAbsReal.NumEvent),
##               RooFit.Slice(catSet),
##               RooFit.ProjWData(catSet,data),
##               RooFit.LineColor(kGreen+2),
##               RooFit.LineStyle(kDashed))
data.plotOn(mf_hi,
            RooFit.Cut('(dataCat==dataCat::hi)'),
            RooFit.Name('data_hi'))
mf_hi.Draw()
pyroot_logon.cmsPrelimHI(hican, 150)
hican.Update()

ppcan = TCanvas("pp", "pp")
dataCat.setLabel('pp')
mf_pp = mass.frame(mmin, mmax, int((mmax-mmin)*10))
data.plotOn(mf_pp, RooFit.Invisible(),
            RooFit.Cut('(dataCat==dataCat::pp)'),
            RooFit.Name('data_norm'))
simPdf.plotOn(mf_pp, RooFit.Slice(catSet),
##               RooFit.Normalization(Nexp, RooAbsReal.NumEvent),
              RooFit.ProjWData(catSet,data),
              RooFit.Name('fullFit')
              )
simPdf.plotOn(mf_pp, RooFit.Components('bkg*'),
##               RooFit.Normalization(Nexp, RooAbsReal.NumEvent),
              RooFit.Slice(catSet),
              RooFit.ProjWData(catSet,data),
              RooFit.LineColor(kRed+2),
              RooFit.LineStyle(kDashed))
## simPdf.plotOn(mf_pp, RooFit.Components('bkgPoly*'),
##               RooFit.Normalization(Nexp, RooAbsReal.NumEvent),
##               RooFit.Slice(catSet),
##               RooFit.ProjWData(catSet,data),
##               RooFit.LineColor(kGreen+2),
##               RooFit.LineStyle(kDashed))
data.plotOn(mf_pp,
            RooFit.Cut('(dataCat==dataCat::pp)'),
            RooFit.Name('data_pp'))
mf_pp.Draw()
pyroot_logon.cmsPrelimPP(ppcan, 225)
ppcan.Update()

hican.Print('hiFitPt%0.1f.pdf' % (opts.pt))
hican.Print('hiFitPt%0.1f.png' % (opts.pt))
ppcan.Print('ppFitPt%0.1f.pdf' % (opts.pt))
ppcan.Print('ppFitPt%0.1f.png' % (opts.pt))

fr.Print('v')

if (ws.var('f2_hi')) or (ws.var('f3_hi')):
    if (ws.var('f23_hi')):
        x23Error = computeRatioError(ws.var('f23_hi'), ws.var('f23_pp'),
                                     fr.correlation('f23_hi','f23_pp'))
        x23 = computeRatio(ws.var('f23_hi'), ws.var('f23_pp'))
    if (ws.var('f2_hi')):
        x2Error = computeRatioError(ws.var('f2_hi'), ws.var('f2_pp'),
                                    fr.correlation('f2_hi','f2_pp'))
        x2 = computeRatio(ws.var('f2_hi'), ws.var('f2_pp'))
    if (ws.var('f3_hi')):
        x3Error = computeRatioError(ws.var('f3_hi'), ws.var('f3_pp'),
                                    fr.correlation('f3_hi','f3_pp'))
        x3 = computeRatio(ws.var('f3_hi'), ws.var('f3_pp'))
    print
    print 'double ratios (hi/pp)'
    print '---------------------'
    if (x2):
        print 'chi_2 : %0.3f +/- %0.3f' % (x2, x2Error)
    if (x3):
        print 'chi_3 : %0.3f +/- %0.3f' % (x3, x3Error)        
    if (x23):
        print 'chi_23 : %0.3f +/- %0.3f' % (x23, x23Error)
    print '---------------------'
    print

## diff = ws.var('f23_pp').getVal() - ws.var('f23_hi').getVal()
## err2 = ws.var('f23_hi').getError()**2 + ws.var('f23_pp').getError()**2  - \
##        fr.correlation('f23_hi','f23_pp')*ws.var('f23_hi').getError()*ws.var('f23_pp').getError()

## print 'back of the envelope significance of double ratio two methods'
## print '-------------------------------------------------------------'
## print '(2S+3S)/1S : (%0.3f - %0.3f)/%0.3f = %0.2f'%(ws.var('f23_pp').getVal(),
##                                                     ws.var('f23_hi').getVal(),
##                                                     sqrt(err2),
##                                                     diff/sqrt(err2))
## print '-------------------------------------------------------------'
## print

chi2_hi = mf_hi.chiSquare('fullFit', 'data_hi', 0)*int((mmax-mmin)*10)
chi2_pp = mf_pp.chiSquare('fullFit', 'data_pp', 0)*int((mmax-mmin)*10)

chi2 = chi2_hi+chi2_pp
ndf = 2*int((mmax-mmin)*10) - fr.floatParsFinal().getSize()
print 'chi2/ndf = (%0.3f + %0.3f)/%i = %0.3f' % (chi2_hi, chi2_pp,
                                                 ndf, chi2/ndf)
print 'chi2 prob = %0.4g' % (TMath.Prob(chi2, ndf))

resultFile = TFile("lastSimFit.root", "recreate")
fr.Write("nll")
resultFile.Close()
