import ROOT
import math

# TRandom3 is the best one: you should not use the other ones in "real" codes

rand=ROOT.TRandom3()
rn=rand.Uniform(0,2) # rn is uniform between o and 2

rand_gauss=ROOT.TRandom3()
rn_gauss=rand_gauss.Gaus(0.5,0.1) # rn is gaussian with mean 0.5 and sigma 0.1

