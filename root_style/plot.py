import ROOT
#you must compile ".L setTDRStyle.cc" and load the generated library
gROOT.gSystem.Load("setTDRStyle.so")
setTDRStyle()
#Now you can plot (needs to be checked)
