import ROOT
import numpy as np

#Il trucco con i TGraph e' usa le liste di python fino all'ultimo perche' sono molto flessibili,                                                                                
#e all'ultimo momento le casti ad array perche' i TGraph non sanno gestire le list                                                                                              
list_x=[1.,2.,3.,4.]
list_y=[1.,2.,3.,4.]
graph=ROOT.TGraph(len(list_x),np.asarray(list_x),np.asarray(list_y))
graph.Draw("AP*") #Mi raccomando Draw("A....") perche' senza la A non disegna l'asse e non vedi niente  
