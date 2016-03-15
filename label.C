const TString lumiString = "CMS #font[50]{Preliminary}";
#font[[50] serve per fare il corsivo (carattere inclinato)
#font[40]{text} serve per farlo NON grassetto
//const TString lumiString2 = "0.6 fb^{-1} (#sqrt{s}=13 TeV, B=0T)";                                                                                                             
const TString lumiString2 = "0.6 fb^{-1} (13 TeV, 0T)";

    TLatex *latLumi = new TLatex(0, 1.11, lumiString);
    TLatex *latLumi2 = new TLatex(320, 1.11, lumiString2);
