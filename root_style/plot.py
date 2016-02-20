import ROOT
#you must open root and compile once and for all ".L rootlogon.C++"                                                                                                          
#Now load the generated library                                                                                                                                                 
ROOT.gSystem.Load("rootlogon_C.so")
#puo' capitare a volte che il .so sia stato compilato con una versione differente di root
#--> cancella rootlogon_C.so (per sicurezza) e ricompila con ++. 
#--> In teoria con ++ i .so vengono cancellati, ma sai mai..., tu cancellalo il .so
ROOT.rootlogon()
#Start plotting 
ROOT.gROOT.SetBatch(ROOT.kTRUE) #Do not show-up canvases
