  TString x = "a-complex-thing";
  TObjArray *tx = x.Tokenize("-");
  tx->Print();
  token1=((TObjString *)(tx->At(0)))->String();
  token2=((TObjString *)(tx->At(1)))->String();
  //for (Int_t i = 0; i < tx->GetEntries(); i++){std::cout << ((TObjString *)(tx->At(i)))->String() << std::endl;} 
  
  //Funziona perfettamente
