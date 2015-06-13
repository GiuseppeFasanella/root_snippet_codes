//Think about a bash alias root = root -l ~/rootlogon.C

//Version \#1 = if it's a macro that you want to compile:
// root -l ~/rootlogon.C
//.L plot.C
//plotter()

#include <TCanvas.h>
void plotter(){
  TCanvas *c=new TCanvas();
  c->Draw();
}

//Version \#2 = if it's a quick macro that you don't want to compile
//root -l plot.C
{
  gROOT->ProcessLine(".L ~/rootlogon.C")
  rootlogon();
  //gROOT->ProcessLine(".L setTDRStyle.cc");
  //setTDRStyle();
  //Plotting
}
