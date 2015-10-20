cms =ROOT.TLatex(0.12,0.95,"CMS Internal")
cms.SetNDC() # importante cosi' non usi le coordinate assolute, ma le coordinate relative, in percentuale della canvas
cms.SetTextSize(0.04)
cms.Draw()
