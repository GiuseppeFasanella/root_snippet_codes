//The Minuit package acts on Fortran Function FCN. for TH1 this FNC is the chisquare

//g is a TGraph o TH1
TF1* f=new TF1("f","pol2",0.98,1.03); //gaus, expo, polN
//f->SetParName(0,"c0");
//f->SetParLimits(0,-1,1); //Set bounds for parameters
g->Fit(f,"OFR+","",0.98,1.03);

//After the fit, access the fit parameters
TF1 * fit=g->GetFunction("f");
double chi2=fit->GetChisquare(); //This is NOT normalized (I think)
double p1 = fit->GetParameter(1);//Remember that parameters start from 0
double e1= fit->GetParError(1);

*************User defined functions*****************************************
//Definisci una tua funzione e poi usala per fittare
Double_t asymmetricParabola(Double_t* x,Double_t* par); //Dichiarazione della funzione
Double_t asymmetricParabola(Double_t* x,Double_t* par) // Definizione
{
  Double_t value=0.;
  if (x[0]<=par[1])
    value=par[2]*(x[0]-par[1])*(x[0]-par[1]);
  else
    value=par[3]*(x[0]-par[1])*(x[0]-par[1]);
  return value+par[0];
}

TF1* fun=new TF1("fun",asymmetricParabola,0.98,1.02,4); 
//4 e' il numero di parametri della della tua funzione                                                                                                         
fun->SetParameter(0,0);//If you need to initialize                                                                                                                                               
g->Fit(fun,"OFR+","",0.98,1.02);                                                                                                                                        
cout<<"minimum is "<<fun->GetMinimumX() <<endl;
