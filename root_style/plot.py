import ROOT
#you must open root and compile once and for all ".L setTDRStyle.cc++"
#Now load the generated library
ROOT.gSystem.Load("setTDRStyle_cc.so")
ROOT.setTDRStyle()
#Start plotting

