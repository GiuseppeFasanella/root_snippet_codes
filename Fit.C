//The Minuit package acts on Fortran Function FCN. for TH1 this FNC is the chisquare

//g is a TGraph o TH1
TF1* f=new TF1("f","pol2",0.98,1.03); //gaus, expo, polN
//f->SetParName(0,"c0");
//f->SetParameter(1,minX); //initialization for parameter 1
//f->SetParLimits(0,-1,1); //Set bounds for parameter 0
//f->FixParameter(2,1.60); //Parameter 2 is fixed
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

 *fname: The name of the fitted function (the model) is passed as the first parameter. This
 name may be one of ROOT pre-defined function names or a user-defined function.
 The functions below are predefined, and can be used with the TH1::Fit method:
o "gaus" Gaussian function with 3 parameters:
 f(x) = p0*exp(-0.5*((x-p1)/p2)^2))
o "expo" An Exponential with 2 parameters: f(x) = exp(p0+p1*x)
o "polN" A polynomial of degree N: f(x) = p0 + p1*x + p2*x2
 +...
o "landau" Landau function with mean and sigma. This function has been adapted
 from the CERNLIB routine G110 denlan.
 *option: The second parameter is the fitting option. Here is the list of fitting options:
o "W" Set all weights to 1 for non empty bins; ignore error bars
o "WW" Set all weights to 1 including empty bins; ignore error bars
o "I" Use integral of function in bin instead of value at bin center
o "L" Use log likelihood method (default is chi-square method)
o "U" Use a user specified fitting algorithm
o "Q" Quiet mode (minimum printing)
o "V" Verbose mode (default is between Q and V)
o "E" Perform better errors estimation using the Minos technique
o "M" Improve fit results
o "R" Use the range specified in the function range
o "N" Do not store the graphics function, do not draw
o "0" Do not plot the result of the fit. By default the fitted function is drawn unless
 the option "N" above is specified.
o "+" Add this new fitted function to the list of fitted functions (by default, the
 previous function is deleted and only the last one is kept)
o "B" Use this option when you want to fix one or more parameters and the fitting
 function is like polN, expo, landau, gaus.
o “LL” An improved Log Likelihood fit in case of very low statistics and when bin
 contents are not integers. Do not use this option if bin contents are large
 (greater than 100).
o “C” In case of linear fitting, don't calculate the chisquare (saves time).
o “F” If fitting a polN, switch to Minu
