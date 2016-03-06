gr->Draw("A"); //fino a che non disegni l'asse non puoi accedere agli assi
gr->GetXaxis()->SetRangeUser(0.2,0.4);
gr->GetXaxis()->SetLimits(0.2,0.4);//SetLimits e' meglio: e' piu' potente
gr->SetMinimum(0.);//dell'asse y
gr->SetMaximum(2.);//dell'asse y
gr->Draw("AP*")//senza A non disegna l'asse e non vedi proprio niente

//Questo in C
  Double_t y[n]  = {    1.00687590075,0.943667243719,1.03375527426 };
  Double_t ey[n] = {  0.0621014822419, 0.129975570451,0.294470567649};
  Double_t x[n]  = {15.,30.,70.};
  Double_t ex[n] = {5.,10.,30.};
  gr = new TGraphErrors(n,x,y,ex,ey);
  
//questo in python

import ROOT
import numpy as np

#Il trucco con i TGraph e' usa le liste di python fino all'ultimo perche' sono molto flessibili,                                                                                
#e all'ultimo momento le casti ad array perche' i TGraph non sanno gestire le list                                                                                              
list_x=[1.,2.,3.,4.]
list_y=[1.,2.,3.,4.]
graph=ROOT.TGraph(len(list_x),np.asarray(list_x),np.asarray(list_y))
graph.Draw("AP*") #Mi raccomando Draw("A....") perche' senza la A non disegna l'asse e non vedi niente 
  
