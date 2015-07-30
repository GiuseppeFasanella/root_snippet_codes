Use the functions in TMath like TMath::LocMin, LocMax to find the index
of the min/max element of an array, eg, assuming TGraph *gr;

int n = gr->GetN();
double* y = gr->GetY();
int locmax = TMath::LocMax(n,y);
double tmax = y[locmax];

Min, max tra 2 elementi e tra elementi di un array
  double range_min=TMath::Max(TMath::MinElement(g->GetN(),g->GetX()),rangeLimMin);
  double range_max=TMath::Min(TMath::MaxElement(g->GetN(),g->GetX()),rangeLimMax);
