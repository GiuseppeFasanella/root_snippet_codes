variables={}
variables["pt"]=dict(name="pt", var="comesichiamailpt")
...

regions={}
region["sel1"]=dict(name="selection1", cut="bla>x && bla<y")

for variable in variable.keys():
    for region in region.keys():
        tree->Draw(str(variables[variable]['name']),   regions[region]['cut'])

hists={}
for variable in variable.keys():
    for region in region.keys():
        hist[str(region)+'_'+str(variable)] = TH1D(....)
e poi lo riprendi col nome

cmq per non farlo entry per entry
ti fai una funzione
che fa il calcolo col tlorentzvector
la compili
e la chiami nel draw del tree
