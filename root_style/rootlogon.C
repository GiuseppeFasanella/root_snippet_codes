{
  //gSystem->Load("libFWCoreFWLite.so");
  //AutoLibraryLoader::enable();//that was CMSSW

  //By default, rootlogon.C is called only if it exists in the directory you call root from
  //If, however you want rootlogon.C to be called independant of the directory you're in you can:
  //1. Open up the directory root is installed to and open the etc file inside
  //here $ROOTSYS/etc/system.rootrc
  //2. Inside there is a file "system.rootrc" that you need to edit
  //3. Find the line "Rint.Logon: rootlogon.C", now change this line to "Rint.Logon: /path to file/rootlogon.C"

  //Or, if you cannot find the directory,
  //wherever you are, you can call the rootlogon with root -l ~/root_style/rootlogon.C                                                                              

  cout << endl << "Welcome to my rootlogon.C" << endl;
  cout << "reading /home/gfasanel/root/work_dir/root_style/setTDRStyle.C" << endl;
  cout << "and some personal modifications." << endl << endl;

  //  gROOT->ProcessLine(".L ~/setTDRStyle.C");
  gROOT->ProcessLine(".L /home/gfasanel/root/work_dir/root_style/setTDRStyle.C");
  setTDRStyle();
  //All this shit is uneffective!! change setTDRStyle instead
  tdrStyle->SetOptTitle(0);
  tdrStyle->SetPadBottomMargin(0.14);
  tdrStyle->SetPadLeftMargin(0.18);
  tdrStyle->SetPadRightMargin(0.15); // per la paletta !
  tdrStyle->SetTitleXOffset(1.0);
  tdrStyle->SetTitleYOffset(1.3);
  tdrStyle->SetNdivisions(505, "X");
  tdrStyle->SetErrorX(0.5);
  tdrStyle->SetPalette(1,0);

///////// pretty palette ///////////

  int rainbow=0;
  int Red_palette=1;
  if(rainbow){
   const Int_t NRGBs = 5;
   const Int_t NCont = 200;//999 OLD SETTING

  Double_t stops[NRGBs] = { 0.00, 0.34, 0.61, 0.84, 1.00 };
  Double_t red[NRGBs]   = { 0.00, 0.00, 0.87, 1.00, 0.51 };
  Double_t green[NRGBs] = { 0.00, 0.81, 1.00, 0.20, 0.00 };
  Double_t blue[NRGBs]  = { 0.51, 1.00, 0.12, 0.00, 0.00 };
  TColor::CreateGradientColorTable(NRGBs, stops, red, green, blue, NCont);
  tdrStyle->SetNumberContours(NCont);//Questo e' fondamentale!!
  }
  
  if(Red_palette){
  UInt_t Number = 3;
  //Red,Green,Blue
  Double_t Red[Number]    = { 1.00,0.7,0.7};//parto da un quasi bianco (1,1,1)
  Double_t Green[Number]  = { 1.00,0.0,0.0};
  Double_t Blue[Number]   = { 1.00,0.00,0.00};//1,0,1
  Double_t Length[Number] = { 0.00,0.9,1.00};
  Int_t nb=999;
  TColor::CreateGradientColorTable(Number,Length,Red,Green,Blue,nb);
  tdrStyle->SetNumberContours(nb);//Questo e' fondamentale!!
  }
/////////////////////////////////////

  gROOT->ForceStyle();
  //gROOT->SetStyle("tdrStyle");
}
