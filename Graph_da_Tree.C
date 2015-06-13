//data is the TTree
data->Draw("branch>>histo", "selection");                                                                                            
TGraph *gr_data = new TGraph(data->GetSelectedRows(),data->GetV2(), data->GetV1());   
gr_data->Draw("ap");                                                                                                                                  
