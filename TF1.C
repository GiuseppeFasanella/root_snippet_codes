#Esempio semplice semplice
root -l ~/rootlogon.C 
TCanvas *c=new TCanvas()
c->SetLogx()
TH1F* h=new TH1F("h","h",100,1,20000)
h->GetXaxis()->SetTitle("Number of data events")
h->GetYaxis()->SetTitle("Statistical error on scale [%]")
h->Draw()
TF1 *f=new TF1("f","4/sqrt(x)",1,20000)
f->Draw("same")
TLatex *label=new TLatex(0.5,0.85,"Err=#sigma_{intr}/#sqrt{N}")
label->SetNDC()
label->Draw("same")
TLatex *sigma=new TLatex(0.5,0.75,"#sigma_{intr}=4%")
sigma->SetNDC()
sigma->Draw("same")
c->SaveAs("~/scratch1/www/RUN2_ECAL_Calibration/expected_error.png")
.q
####################################################################

tf1->Eval(x)
tf1->GetMinimumX()
