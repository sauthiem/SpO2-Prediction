import csv
from datetime import datetime as dt
import time
import pandas as pd
import sys
import numpy as np
from os.path import join, dirname, abspath, isfile
import os
from csv import DictReader
import seaborn as sns
from multiprocessing import Pool
from concurrent.futures import ThreadPoolExecutor
from functools import partial



d = pd.read_csv("CHU_DATA/init_data_files/Demog.csv", sep='\t')    
d02 = pd.read_csv("CHU_DATA/init_data_files/Joined_Files_1850.csv", sep='\t', encoding='utf-8')    


ds = d.sort_values(by=['Code'], ascending=True)
d1 = ds.reset_index(drop=True)

d2s = d02.sort(['Code', 'storeTime'], ascending=True)
d2 = d2s.reset_index(drop=True)

d1.to_csv("CHU_DATA/init_data_files/Demog_sorted.csv", sep='\t', encoding='utf-8', index=None)

###############################################################
d2['Age'] = ""
d2['Weight'] = ""
####################################################################
L_dt = []
L_BD = []
L_P = []
L_delTime = []
LL_delT = [[]]
L_n = []
L_C = []
L_A = []
L_W = []


L_adm = list(d1.Date_admission)
L_bdt = list(d1.Date_naissance)
L_Code_d1 = list(d1.Code)
L_wgt = list(d1.Poids)

L_ST = list(d2.storeTime)
########################################################################

def fn1(L_adm,L_bdt,L_ST):
    for r in range(len(L_adm)):
        L_adm[r] = L_adm[r].split(" ")
        L_adm[r][-1] = L_adm[r][-1][:5]
        L_adm[r] = " ".join(L_adm[r])
    
        L_bdt[r] = L_bdt[r].split(" ")
        L_bdt[r][-1] = L_bdt[r][-1][:5]
        L_bdt[r] = " ".join(L_bdt[r])
    
    for r in range(len(L_ST)):
        L_ST[r] = L_ST[r].split(" ")
        L_ST[r][-1] = L_ST[r][-1][:5]
        L_ST[r] = " ".join(L_ST[r])

    for r in range(len(L_ST)):
        L_ST[r] = dt.strptime(L_ST[r], "%Y-%m-%d %H:%M")

    for r in range(len(L_bdt)):
        L_bdt[r] = dt.strptime(L_bdt[r], "%Y-%m-%d %H:%M")
    
    for r in range(len(L_adm)):
        L_adm[r] = dt.strptime(L_adm[r], "%Y-%m-%d %H:%M")
################################################################     
fn1(L_adm,L_bdt,L_ST)
####################################################################
d3 = pd.DataFrame({'Code': L_Code_d1, 'Adm_date': L_adm, 'Bdate': L_bdt, 'Weight': L_wgt})
###################################################################
    
d2['storeTime'] = d2['storeTime'].map(lambda storeTime: dt.strptime(storeTime,"%Y-%m-%d %H:%M:%S"))

#########################################################################
g = d3.groupby(['Code'])
code_keys = g.groups.keys()
L_code_keys = list(code_keys)

g1 = d2.groupby(['Code'])
d2_code_keys = g1.groups.keys()
d2_code_keys = list(d2_code_keys)


AdmL = []
BDL = []
KL = []
L_age = []

LL_ST = []
L_t1 = []
LL_t1 = []
L_t2 = []
LL_codes = []
LL_C = []
LL_A = []
LL_BD = []
####################################################################


def age_wgt(L_BD,L_delTime,L_n,L_C,L_A,d2,g,L_code_keys,g1,d2_code_keys,AdmL,BDL,KL,L_age,LL_ST,L_t1,LL_t1,L_t2,LL_C,LL_A,LL_BD):
    for e in range(len(L_code_keys)):
        L_code_keys[e] = int(L_code_keys[e])
    
        adm_by_grp = g.get_group(L_code_keys[e])
        adm_by_grp_ind_arr = adm_by_grp.index.values
    
        KL.append(L_code_keys[e])
    
        AdmL.append(list(adm_by_grp.Adm_date))
        BDL.append(list(adm_by_grp.Bdate))
        
    
        for r in range(len(d2_code_keys)):
            d2_code_keys[r] = int(d2_code_keys[r])
        
            d2_by_grp = g1.get_group(d2_code_keys[r])
            d2_grp_ind_arr = d2_by_grp.index.values
        
            LL_ST.append(list(d2_by_grp.storeTime))

            
            if d2_code_keys[r] == L_code_keys[e]:


                t1 = d2_by_grp.storeTime[d2_grp_ind_arr[0]]
                L_t1.append(t1)
                
                for x in range(len(adm_by_grp.Code)):

                
                    t2 = AdmL[e][x]

                    L_t2.append(t2)

                    L_delTime.append(abs((t2-t1).total_seconds()))
            
                    n = L_delTime.index(min(L_delTime))
                    L_n.append(n)
                    

                    L_C.append(adm_by_grp.Code[adm_by_grp_ind_arr[n]])
                    L_A.append(adm_by_grp.Adm_date[adm_by_grp_ind_arr[n]])
                    L_BD.append(adm_by_grp.Bdate[adm_by_grp_ind_arr[n]])
            
        
                now=dt.now()
                age = now.year - L_BD[n].year
                L_age.append(age)
    
                wgt = adm_by_grp.Weight[adm_by_grp_ind_arr[n]]
    

                c = d2_grp_ind_arr[0]

                while c < (d2_grp_ind_arr[0] + len(d2_grp_ind_arr)):
                    (d2.Age)[c] = age
                    (d2.Weight)[c] = wgt
                    c += 1
                
                LL_t1.append(L_t1)
                LL_C.append(L_C)
                LL_A.append(L_A)
                LL_BD.append(L_BD)
                del L_t1[:]
                del L_delTime[:]
                del L_A[:]
                del L_BD[:]
                del L_C[:]
            
      



age_wgt(L_BD,L_delTime,L_n,L_C,L_A,d2,g,L_code_keys,g1,d2_code_keys,AdmL,BDL,KL,L_age,LL_ST,L_t1,LL_t1,L_t2,LL_C,LL_A,LL_BD)


d2.to_csv("CHU_DATA/init_data_files/Training_File.csv", sep='\t', index=None)
 
df2 = pd.read_csv("CHU_DATA/init_data_files/Training_File.csv", sep='\t')    

df2["Tidal_Vol_per_weight"] = ""
#############################################################
def fn2(df2):
    TVSW = df2.TV_setting/df2.Weight
    return TVSW

df2.Tidal_Vol_per_weight = df2.apply(fn2, axis=1)
###############################################################
df2.to_csv("CHU_DATA/init_data_files/Training_File_01.csv", sep='\t', index=None)
df3 = df2[np.isfinite(df2['Age'])]
df3.to_csv("CHU_DATA/init_data_files/Training_File_02.csv", sep='\t', index=None)

