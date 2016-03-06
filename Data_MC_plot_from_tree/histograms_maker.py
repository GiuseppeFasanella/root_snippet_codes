from ROOT import *
import sys
import math
gROOT.SetBatch(kTRUE)
gSystem.Load("~/rootlogon_C.so")
rootlogon()
ratio=1

import os

pu_weights_file=TFile("../pu_weights_0T.root")
pu_weights=pu_weights_file.Get("pu_weights")

pu_reweight_string="("
for i in range(1,pu_weights.GetSize()-3):
   #bin1 means pu 0
   pu_reweight_string+="(truePU=="+str(i-1)+")*"+str(pu_weights.GetBinContent(i))+" + "
   
pu_reweight_string+="(truePU=="+str(pu_weights.GetSize()-3)+")*"+str(pu_weights.GetBinContent(pu_weights.GetSize()-2))+" ) "

#print pu_reweight_string
#pu_reweight_string="(1)"
variables=['probe_Pho_sipip',
           'probe_Pho_sieie',
           'probe_Pho_nTrkSolidCone03',
           'probe_Pho_egPhotonIso',
           'probe_Pho_abseta',       
           'probe_Pho_e',            
           'probe_Pho_et',           
           'probe_Pho_eta',          
           'probe_Pho_full5x5x_r9',  
           'probe_Pho_hoe',          
           'probe_Pho_missingHits',  
           'tag_Pho_abseta',         
           'tag_Pho_e',              
           'tag_Pho_et',             
           'pair_mass',              
           'mass',           
           'event_nPV',
           'PUweight',
           'truePU'
           ]

#Just one variable to test
#variables=['probe_Pho_sipip','probe_Pho_sieie'] #just to test one variable
#variables=['probe_Pho_sieie']
variables=['probe_Pho_missingHits','probe_Pho_et']
#variables=['probe_Pho_full5x5x_r9','probe_Pho_nTrkSolidCone03']
#variables=['mass','probe_Pho_et','probe_Pho_missingHits'] #just to test one variable
#variables=['probe_Pho_abseta','probe_Pho_missingHits']
#variables=['probe_Pho_missingHits','probe_Pho_sieie','probe_Pho_sipip','probe_Pho_nTrkSolidCone03','probe_Pho_full5x5x_r9','probe_Pho_hoe','passingEleVetoSel','mass','pair_mass']

hist={}
hist['probe_Pho_sipip'          ]=dict(name='#sigma_{i#phi i#phi}'     ,unit=''     ,bins=100,xmin=0.,xmax=0.05) 
hist['probe_Pho_sieie'          ]=dict(name='probe_Pho_sieie'          ,unit=''     ,bins=100,xmin=0.,xmax=0.05) 
hist['probe_Pho_nTrkSolidCone03']=dict(name='probe_Pho_nTrkSolidCone03',unit=''     ,bins=5,xmin=0.,xmax=5) 
hist['probe_Pho_egPhotonIso'    ]=dict(name='probe_Pho_egPhotonIso'    ,unit=''     ,bins=100,xmin=0.,xmax=5) 
hist['probe_Pho_abseta'         ]=dict(name='probe_Pho_abseta'         ,unit=''     ,bins=100,xmin=0.,xmax=5) 
hist['probe_Pho_e'              ]=dict(name='probe_Pho_e'              ,unit='[GeV]',bins=150,xmin=0.,xmax=300) 
hist['probe_Pho_et'             ]=dict(name='probe_Pho_et'             ,unit='[GeV]',bins=100,xmin=0.,xmax=200) 
hist['probe_Pho_eta'            ]=dict(name='probe_Pho_eta'            ,unit=''     ,bins=100,xmin=-3,xmax=3) 
hist['probe_Pho_full5x5x_r9'    ]=dict(name='probe_Pho_full5x5x_r9'    ,unit=''     ,bins=80,xmin=0.8,xmax=1) 
hist['probe_Pho_hoe'            ]=dict(name='probe_Pho_hoe'            ,unit=''     ,bins=100,xmin=0.,xmax=0.1) 
hist['probe_Pho_missingHits'    ]=dict(name='probe_Pho_missingHits'    ,unit=''     ,bins=6,xmin=-1,xmax=5) 
hist['tag_Pho_abseta'           ]=dict(name='tag_Pho_abseta'           ,unit=''     ,bins=100,xmin=0.,xmax=3) 
hist['tag_Pho_e'                ]=dict(name='tag_Pho_e'                ,unit='[GeV]',bins=100,xmin=0.,xmax=200) 
hist['tag_Pho_et'               ]=dict(name='tag_Pho_et'               ,unit='[GeV]',bins=100,xmin=0.,xmax=200) 
hist['pair_mass'                ]=dict(name='pair_mass'                ,unit='[GeV]',bins=80,xmin=70.,xmax=110) 
hist['mass'                     ]=dict(name='mass'                     ,unit='[GeV]',bins=40,xmin=70.,xmax=110) 
hist['event_nPV'                ]=dict(name='nPV'                      ,unit=''     ,bins=20,xmin=0.,xmax=20) 
hist['PUweight'                 ]=dict(name='PUweight'                 ,unit=''     ,bins=40,xmin=0.,xmax=4) 
hist['truePU'                   ]=dict(name='truePU  '                 ,unit=''     ,bins=52,xmin=0.,xmax=52) 
hist['passingEleVetoSel'        ]=dict(name='passingEleVetoSel'        ,unit=''     ,bins=2,xmin=0.,xmax=2) 


#file_MC=TFile('root://cmsrm-xrootd02.roma1.infn.it:7070//store/user/gfasanel/crab_jobs_MC/DYToEE_NNPDF30_13TeV-powheg-pythia8/CRAB3_TP_Zeeg/160224_072548/0000/TnPTree_mc_6.root')
#file_MC=TFile.Open('root://xrootd-cms.infn.it//store/user/gfasanel/crab_jobs_MC/DYToEE_NNPDF30_13TeV-powheg-pythia8/CRAB3_TP_Zeeg/160224_072548/0000/TnPTree_mc_6.root')
file_MC=TFile.Open('tp_ntuples/DYToEE_NNPDF30_powheg_76_v2_eeg.root')
tree_MC=file_MC.Get("PhotonToRECO/fitter_tree")
#file_data=TFile.Open('root://cmsrm-xrootd02.roma1.infn.it:7070//store/user/gfasanel/crab_jobs/SingleElectron_0T/CRAB3_TP_Zeeg/160224_071440/0000/TnPTree_data_36.root')
file_data=TFile.Open('tp_ntuples/SingleEle_0T_76_eeg.root')
tree_data=file_data.Get('PhotonToRECO/fitter_tree')

#Cuts####################################

y_scales=['lin','log']
y_factor={}
y_factor['lin']=1.2
y_factor['log']=10

presel="(tag_pt1>30)*(mass + tag_mass <180)*(min_dr>0.2)*(min_dr<0.8)"
probe_barrel="(probe_Pho_abseta<1.442)"
probe_endcap="(probe_Pho_abseta>1.566)*(probe_Pho_abseta<2.5)"
ele_sel="((probe_Pho_missingHits<0) + (probe_Pho_missingHits>1))"
#presel="(probe_Pho_full5x5x_r9>0.8)&&(probe_Pho_hoe<0.1)&&(probe_Pho_egPhotonIso<5)&&(probe_Pho_nTrkSolidCone03<5)"
ptMin=[0,20,40]
ptMax=[20,40,200]
et_20="(probe_Pho_et<20)"
et_20_40="(probe_Pho_et>20)*(probe_Pho_et<40)"
et_40="(probe_Pho_et>40)"

############################################
selection_barrel=presel+"*"+probe_barrel
selection_barrel_ele=presel+"*"+selection_barrel+"*"+ele_sel
selection_endcap=presel+"*"+probe_endcap
selection_endcap_ele=presel+"*"+selection_endcap+"*"+ele_sel

selection_barrel_pt20=selection_barrel+"*"+et_20
selection_barrel_pt20_40=selection_barrel+"*"+et_20_40
selection_barrel_pt40=selection_barrel+"*"+et_40
selection_barrel_ele_pt20=selection_barrel_ele+"*"+et_20
selection_barrel_ele_pt20_40=selection_barrel_ele+"*"+et_20_40
selection_barrel_ele_pt40=selection_barrel_ele+"*"+et_40
selection_endcap_pt20=selection_endcap+"*"+et_20
selection_endcap_pt20_40=selection_endcap+"*"+et_20_40
selection_endcap_pt40=selection_endcap+"*"+et_40
selection_endcap_ele_pt20=selection_endcap_ele+"*"+et_20
selection_endcap_ele_pt20_40=selection_endcap_ele+"*"+et_20_40
selection_endcap_ele_pt40=selection_endcap_ele+"*"+et_40



#sel_names=['barrel','barrel_ele','endcap','endcap_ele']
sel_names=['barrel_ele_pt20','barrel_ele_pt20_40','barrel_ele_pt40','endcap_ele_pt20','endcap_ele_pt20_40','endcap_ele_pt40','barrel_pt20','barrel_pt20_40','barrel_pt40','endcap_pt20','endcap_pt20_40','endcap_pt40']
selection={}

############################################
selection['barrel']=selection_barrel
selection['barrel_ele']=selection_barrel_ele
selection['endcap']=selection_endcap
selection['endcap_ele']=selection_endcap_ele

selection['barrel_ele_pt20']=selection_barrel_ele_pt20
selection['barrel_ele_pt20_40']=selection_barrel_ele_pt20_40
selection['barrel_ele_pt40']=selection_barrel_ele_pt40
selection['endcap_ele_pt20']=selection_endcap_ele_pt20
selection['endcap_ele_pt20_40']=selection_endcap_ele_pt20_40
selection['endcap_ele_pt40']=selection_endcap_ele_pt40
selection['barrel_pt20']=selection_barrel_pt20
selection['barrel_pt20_40']=selection_barrel_pt20_40
selection['barrel_pt40']=selection_barrel_pt40
selection['endcap_pt20']=selection_endcap_pt20
selection['endcap_pt20_40']=selection_endcap_pt20_40
selection['endcap_pt40']=selection_endcap_pt40

#print "[INF0] selection barrel is ",selection['barrel']
#print "[INF0] selection barrel_ele is ",selection['barrel_ele']
#print "[INF0] selection endcap is ",selection['endcap']
#print "[INF0] selection endcap_ele is ",selection['endcap_ele']
print "[INF0] selection barrel_ele_pt20 is ",selection['barrel_ele_pt20']
print "[INF0] selection barrel_ele_pt20_40 is ",selection['barrel_ele_pt20_40']
print "[INF0] selection barrel_ele_pt40 is ",selection['barrel_ele_pt40']

print "[INF0] selection endcap_ele_pt20 is ",selection['endcap_ele_pt20']
print "[INF0] selection endcap_ele_pt20_40 is ",selection['endcap_ele_pt20_40']
print "[INF0] selection endcap_ele_pt40 is ",selection['endcap_ele_pt40']
#file=TFile("Plots/histograms.root","recreate")
file=TFile("Plots/histograms_et.root","recreate")

Histos={}
for variable in variables:
   for sel_name in sel_names:
      Histos['MC_'+str(variable)+'_'+str(sel_name)] = TH1D("h_MC_"+sel_name+"_"+variable,"h_MC_"+sel_name+"_"+variable,hist[variable]['bins'],hist[variable]['xmin'],hist[variable]['xmax'])
      Histos['data_'+str(variable)+'_'+str(sel_name)] = TH1D("h_data_"+sel_name+"_"+variable,"h_data"+sel_name+"_"+variable,hist[variable]['bins'],hist[variable]['xmin'],hist[variable]['xmax'])

#2D plot for efficiency study
for sel_name in sel_names:
   Histos['MC_2D'+'_'+str(sel_name)] = TH2D("h2_MC_"+sel_name+"_eleVeto_pt","h2_MC_"+sel_name+"_eleVeto_pt",2,0,2,4,0,100)
   Histos['data_2D'+'_'+str(sel_name)] = TH2D("h2_data_"+sel_name+"_eleVeto_pt","h2_data"+sel_name+"_eleVeto_pt",2,0,2,4,0,100)

#####################################################################################
types=['data','MC']
tree={}
tree['data']=tree_data
tree['MC']=tree_MC

for type in types:
   tree[type].SetBranchStatus("*",0)
   for variable in variables:
      tree[type].SetBranchStatus(variable,1)
      #Variables used for selection must be actived
      tree[type].SetBranchStatus("tag_pt1",1)
      tree[type].SetBranchStatus("tag_eta1",1)
      tree[type].SetBranchStatus("tag_phi1",1)
      tree[type].SetBranchStatus("tag_pt2",1)
      tree[type].SetBranchStatus("tag_eta2",1)
      tree[type].SetBranchStatus("tag_phi2",1)
      tree[type].SetBranchStatus("probe_Pho_et",1)
      tree[type].SetBranchStatus("probe_Pho_eta",1)
      tree[type].SetBranchStatus("probe_Pho_phi",1)
      tree[type].SetBranchStatus("probe_Pho_e",1)
      tree[type].SetBranchStatus("probe_Pho_abseta",1)
      tree[type].SetBranchStatus("tag_mass",1)
      tree[type].SetBranchStatus("mass",1)

   for i in xrange(0,tree[type].GetEntriesFast()):
      tree[type].GetEntry(i)
      tag_pt1=getattr(tree[type],"tag_pt1")
      tag_eta1=getattr(tree[type],"tag_eta1")
      tag_phi1=getattr(tree[type],"tag_phi1")
      tag_pt2=getattr(tree[type],"tag_pt2")
      tag_eta2=getattr(tree[type],"tag_eta2")
      tag_phi2=getattr(tree[type],"tag_phi2")
      probe_Pho_et=getattr(tree[type],"probe_Pho_et")
      probe_Pho_eta=getattr(tree[type],"probe_Pho_eta")
      probe_Pho_phi=getattr(tree[type],"probe_Pho_phi")
      probe_Pho_e=getattr(tree[type],"probe_Pho_e")
      tag_mass=getattr(tree[type],"tag_mass")
      probe_Pho_abseta=getattr(tree[type],"probe_Pho_abseta")
      mass=getattr(tree[type],"mass")
      probe_Pho_missingHits=getattr(tree[type],"probe_Pho_missingHits")
      passingEleVetoSel=getattr(tree[type],"passingEleVetoSel")
         
      ##selection on dR:
      ele1=TLorentzVector(1.,1.,1.,1.)
      ele2=TLorentzVector(1.,1.,1.,1.)
      probe=TLorentzVector(1.,1.,1.,1.)
      #ele1.SetPtEtaPhiE(tag_pt1,tag_eta1,tag_phi1,tag_pt1*math.cosh(tag_eta1))
      #ele2.SetPtEtaPhiE(tag_pt2,tag_eta2,tag_phi2,tag_pt2*math.cosh(tag_eta2))
      ele1.SetPtEtaPhiM(tag_pt1,tag_eta1,tag_phi1,0)
      ele2.SetPtEtaPhiM(tag_pt2,tag_eta2,tag_phi2,0)
      probe.SetPtEtaPhiE(probe_Pho_et,probe_Pho_eta,probe_Pho_phi,probe_Pho_e)
      dr1=probe.DeltaR(ele1)
      dr2=probe.DeltaR(ele2)
      min_dr=min(dr1,dr2)

      for variable in variables:
         value=getattr(tree[type],variable)
         for sel_name in sel_names:
            Histos[type+'_'+str(variable)+'_'+str(sel_name)].Fill(value,eval(selection[sel_name]))

      
      #2D plots
      for sel_name in sel_names:
         Histos[type+'_2D'+'_'+str(sel_name)].Fill(passingEleVetoSel,probe_Pho_et)         

#After filling, write the histograms
for variable in variables:
   for sel_name in sel_names:
      for type in types:
         Histos[type+'_'+str(variable)+'_'+str(sel_name)].Write()

for sel_name in sel_names:
   Histos['MC_2D'+'_'+str(sel_name)].Write()
   Histos['data_2D'+'_'+str(sel_name)].Write()
   
