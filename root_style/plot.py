import ROOT
#you must open root and compile once and for all ".L rootlogon.C++"                                                                                                          
#Now load the generated library                                                                                                                                                 
ROOT.gSystem.Load("rootlogon_C.so")
ROOT.rootlogon()
#Start plotting 

