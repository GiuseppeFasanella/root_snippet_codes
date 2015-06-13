//g is a TGraph o TH1
TF1* f=new TF1("f","pol2",0.98,1.03);
g->Fit(f,"OFR+","",0.98,1.03);

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
