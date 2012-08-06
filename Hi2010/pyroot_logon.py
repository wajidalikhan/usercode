from ROOT import gROOT, gStyle, gSystem, TLatex
import subprocess

def cmsPrelimHI(canvas, lumi):
    l = TLatex();
    l.SetNDC();
    l.SetTextFont(42);
    l.SetTextAlign(31);
    l.SetTextSize(0.03);

    canvas.cd()
    l.DrawLatex(1. - canvas.GetRightMargin(), 1. - canvas.GetTopMargin() + 0.01,
                'CMS preliminary, #font[52]{L} = %0.0f #mub^{-1}, #sqrt{s_{NN}} = 2.76 TeV' % (lumi)
                )
    canvas.Update()

def cmsPrelimPP(canvas, lumi):
    l = TLatex();
    l.SetNDC();
    l.SetTextFont(42);
    l.SetTextAlign(31);
    l.SetTextSize(0.03);

    canvas.cd()
    l.DrawLatex(1. - canvas.GetRightMargin(), 1. - canvas.GetTopMargin() + 0.01,
                'CMS preliminary, #font[52]{L} = %0.0f nb^{-1}, #sqrt{s} = 2.76 TeV' % (lumi)
                )
    canvas.Update()

gROOT.SetStyle('Plain')
gStyle.SetPadTickX(1)
gStyle.SetPadTickY(1)
gStyle.SetOptStat("iouRMe")
gStyle.SetPalette(1)
gStyle.SetOptFit(1112)
gStyle.SetOptTitle(0)

gStyle.SetCanvasDefH(600) ## Height of canvas
gStyle.SetCanvasDefW(600) ## Width of canvas
gStyle.SetErrorX(0.)

gStyle.SetMarkerStyle(20)

## For the fit/function:
gStyle.SetFuncColor(2)
gStyle.SetFuncStyle(1)
gStyle.SetFuncWidth(1)

##  Margins:
gStyle.SetPadTopMargin(0.05)
gStyle.SetPadBottomMargin(0.13)
gStyle.SetPadLeftMargin(0.175) ## was 0.16
gStyle.SetPadRightMargin(0.05)## was 0.02

gStyle.SetTitleColor(1, "XYZ")
gStyle.SetTitleFont(42, "XYZ")
gStyle.SetTitleSize(0.06, "XYZ")
gStyle.SetTitleXOffset(0.9)
gStyle.SetTitleYOffset(1.5) ## was 1.25

##  For the axis labels:
gStyle.SetLabelColor(1, "XYZ")
gStyle.SetLabelFont(42, "XYZ")
gStyle.SetLabelOffset(0.007, "XYZ")
gStyle.SetLabelSize(0.05, "XYZ")

if (gSystem.DynamicPathName("libFWCoreFWLite.so",True)):
    print "adding RooFit ...",
    scramCmd = ['scram','tool','info','roofitcore']
    grepCmd = ['grep', 'INCLUDE']
    pscram = subprocess.Popen(scramCmd, stdout = subprocess.PIPE)
    pgrep = subprocess.Popen(grepCmd, stdin=pscram.stdout,
                             stdout=subprocess.PIPE)
    pscram.stdout.close()
    output = pgrep.communicate()[0]
    if (pgrep.returncode == 0):
        roofitinc = output.split("=")[1].rstrip()
        ## print roofitinc
        gROOT.GetInterpreter().AddIncludePath(roofitinc)
        roofitinc = '-I"' + roofitinc + '"'
        gSystem.AddIncludePath(roofitinc)
        print "done"
    else:
        print "failed"
        print 'scram returned:',pscram.returncode,'grep:',pgrep.returncode

print 'end of pyroot_logon'
