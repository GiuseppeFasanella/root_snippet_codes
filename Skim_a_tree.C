TTree* addBranch_class::AddBranch_R9Eleprime(TChain* originalChain, TString treename, bool isMC){
  //to have a branch with r9prime                                                                                                                                                
  //From the original tree take R9 and eta                                                                                                                                       
  Float_t         R9Ele[3];
  Float_t         etaEle[3];

  originalChain->SetBranchStatus("*",0);
  originalChain->SetBranchStatus("etaEle",1);
  originalChain->SetBranchStatus("R9Ele",1);
  originalChain->SetBranchAddress("etaEle", etaEle);
  originalChain->SetBranchAddress("R9Ele", R9Ele);

  TTree* newtree = new TTree(treename, treename);
  Float_t R9Eleprime[3];
  newtree->Branch("R9Eleprime", R9Eleprime, "R9Eleprime[3]/F");

  Long64_t nentries= originalChain->GetEntries();
  for(Long64_t ientry = 0; ientry< nentries; ientry++){
    originalChain->GetEntry(ientry);
    R9Eleprime[0]=1;
    R9Eleprime[1]=1;
    R9Eleprime[2]=-999;
    newtree->Fill();
  }

  originalChain->SetBranchStatus("*",1);
  originalChain->ResetBranchAddresses();
  return newtree;
}
