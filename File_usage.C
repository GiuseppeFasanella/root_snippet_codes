TFile *f = new TFile("tmp/outside_init.root", "recreate");
TFile *_file0 = TFile::Open("file.root"); //credo che per eos e' l'unico modo ammesso
f->Print();
f->cd();
//histo->Write();
f->Write();                                                                                                                                                
f->Close();

 If option = NEW or CREATE   create a new file and open it for writing,
                             if the file already exists the file is
                             not opened.
           = RECREATE        create a new file, if the file already
                             exists it will be overwritten.
           = UPDATE          open an existing file for writing.
                             if no file exists, it is created.
           = READ            open an existing file for reading (default)
