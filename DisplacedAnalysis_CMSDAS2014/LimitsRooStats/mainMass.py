from GetWorkspaceMass import *
from GetLimitBayesian import *
import ROOT as r
import sys,os.path

if len(sys.argv)<3:
	sys.exit('usage python main.py massValue LeptonType')

r.RooMsgService.instance().deleteStream(1)

M = float(sys.argv[1])
LeptonType = sys.argv[2]


w = GetWorkspaceMass(M,LeptonType)
GetLimitBayesian(w,LeptonType,str(M))
