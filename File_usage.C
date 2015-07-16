TFile *f = new TFile("tmp/outside_init.root", "recreate");
f->Print();
f->cd();
//histo->Write();
f->Write();                                                                                                                                                
f->Close();
