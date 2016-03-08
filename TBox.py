    box=TBox(0.1,-1,18,1) #x1,y1, x2, y2
    #Colore trasparente (credo si veda solo nel pdf perche' il png non gestisce le trasparenze)
    #shadedYellow=TColor.GetColorTransparent(kYellow,0.35)                                                                                                                      
    #box.SetFillColor(shadedYellow)    
    #Colore pieno, ma giallo chiaro chiaro
    box.SetFillColor(kYellow-9)
    box.SetFillStyle(3001)
    box.SetLineColor(kYellow-9)
    #Tratteggio grigio di qualita' accettabile
    #box.SetFillColor(12)                                                                                                                                                       
    #box.SetFillStyle(3004)                                                                                                                                                     
    box.Draw("same")
