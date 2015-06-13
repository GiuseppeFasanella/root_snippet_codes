{
  TF1 *f=new TF1("my_func","cosh(x)",-5,5);
  f->GetXaxis()->SetTitle("#eta");
  f->GetYaxis()->SetTitle("cosh(#eta)");
  f->Draw();

  TLine *line1 = new TLine(-5,1,5,1);
  line1->SetLineWidth(2);
  line1->Draw();

}
