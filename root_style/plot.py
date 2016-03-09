import ROOT
#you must open root and compile once and for all ".L rootlogon.C++"                                                                                                          
#Now load the generated library  
#ROOT.gSystem.Load("rootlogon_C.so")

#####Siccome root e' fesso, a volte non capisce niente tra nuova versione, vecchia versione....
##Percio' compilalo al volo e poi fai il load del rootlogon
import os
os.system("root -l -b -q ~/compile_logon.C") #compile_logon e' definito piu' sotto
ROOT.gSystem.Load("rootlogon_C.so")
#puo' capitare a volte che il .so sia stato compilato con una versione differente di root
#--> cancella rootlogon_C.so (per sicurezza) e ricompila con ++. 
#--> In teoria con ++ i .so vengono cancellati, ma sai mai..., tu cancellalo il .so
ROOT.rootlogon()
#Start plotting 
ROOT.gROOT.SetBatch(ROOT.kTRUE) #Do not show-up canvases


##compile_logon.C e' fatto cosi'
#{
#  gROOT->ProcessLine(".L ~/rootlogon.C++");
#}
