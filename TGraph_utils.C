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
  
  
