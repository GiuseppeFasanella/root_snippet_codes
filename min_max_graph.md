Use the functions in TMath like TMath::LocMin, LocMax to find the index
of the min/max element of an array, eg, assuming TGraph *gr;

int n = gr->GetN();
double* y = gr->GetY();
int locmax = TMath::LocMax(n,y);
double tmax = y[locmax];
