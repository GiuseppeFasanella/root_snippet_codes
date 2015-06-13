#include <TFile.h>
#include <TList.h>
#include <TKey.h>
#include <TObject.h>
#include <TString.h>
#include <TGraph.h>
#include <fstream>

void taker(TString my_root_file){
  TFile f_in(my_root_file);
  f_in.cd();
  TList *KeyList = f_in.GetListOfKeys();
  for(int i =0; i <  KeyList->GetEntries(); i++){
    TKey *currentKey=(TKey *)KeyList->At(i);
    TString className=currentKey->GetClassName();
    // se non e' un TGraph passa oltre                                                                                                                                          
    if (! (className.CompareTo("TGraph")==0)) continue;
    TGraph *g = (TGraph *)currentKey->ReadObj();
    //graph preso, ora ci puoi lavorare
  
    if(((TString)currentKey->GetName()).Contains("constTerm")){
      g->GetXaxis()->SetTitle("#sigma");
    }
  
  }
  
}

