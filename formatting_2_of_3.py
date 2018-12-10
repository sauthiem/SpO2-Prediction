import csv
from datetime import datetime as dt
from datetime import *
import pandas as pd
import sys
import numpy as np
from os.path import join, dirname, abspath, isfile
import os
from csv import DictReader
import matplotlib.pyplot as plt
import math

File = input("Enter file number:")

d = pd.read_csv("NEW_DATA/p_" + File + "_com.csv", sep=',')

with open("NEW_DATA/p_" + File + "_com.csv") as f:
    O2 = [row["O2 Concentration Setting"] for row in DictReader(f)]
with open("NEW_DATA/p_" + File + "_com.csv") as f:
    PEEP_set = [row["PEEP Setting"] for row in DictReader(f)]
with open("NEW_DATA/p_" + File + "_com.csv") as f:
    TV_set = [row["Tidal Volume Setting"] for row in DictReader(f)]
with open("NEW_DATA/p_" + File + "_com.csv") as f:
    ST_min = [row["storeTime"] for row in DictReader(f)]
with open("NEW_DATA/p_" + File + "_com.csv") as f:
    EMV = [row["Expiratory Minute Volume"] for row in DictReader(f)]
with open("NEW_DATA/p_" + File + "_com.csv") as f:
    ETV = [row["Expiratory Tidal Volume"] for row in DictReader(f)]
with open("NEW_DATA/p_" + File + "_com.csv") as f:
    IE = [row["IE Ratio"] for row in DictReader(f)]    
with open("NEW_DATA/p_" + File + "_com.csv") as f:
    MAP = [row["Mean Airway Pressure"] for row in DictReader(f)] 
with open("NEW_DATA/p_" + File + "_com.csv") as f:
    MF = [row["Measured Frequency"] for row in DictReader(f)]    
with open("NEW_DATA/p_" + File + "_com.csv") as f:
    PAP = [row["Peak Airway Pressure"] for row in DictReader(f)] 
with open("NEW_DATA/p_" + File + "_com.csv") as f:
    SFM = [row["Spontaneous Frequency measured"] for row in DictReader(f)] 
with open("NEW_DATA/p_" + File + "_com.csv") as f:
    FC = [row["FC"] for row in DictReader(f)]    
with open("NEW_DATA/p_" + File + "_com.csv") as f:
    P = [row["Pouls"] for row in DictReader(f)]
with open("NEW_DATA/p_" + File + "_com.csv") as f:
    SpO2 = [row["SpO2"] for row in DictReader(f)]
with open("NEW_DATA/p_" + File + "_com.csv") as f:
    Code = [row["Code"] for row in DictReader(f)]
with open("NEW_DATA/p_" + File + "_com.csv") as f:
    PSP = [row["Pressure Support Level Above P"] for row in DictReader(f)]
with open("NEW_DATA/p_" + File + "_com.csv") as f:
    PCP = [row["Pressure Control Level Above P"] for row in DictReader(f)]
###################################################################

###########################################################
L_STmin = []
L_O2 = []
L_PEEP_set = []
L_TV_set = []
L_ST = []
L_EMV = []
L_ETV = []
L_IE = []
L_MAP = []
L_MF = []
L_PAP = []
L_SFM = []
L_FC = []
L_P = []
L_SP = []
L_SPbin = []
L_dt = []
L_PSP = []
L_PCP = []

L_delta_O2 = []
L_delta_PEEP = []
L_delta_TV_set = []

L_r = []
L_x = []
L_c = []

L_delST = []
L_Code = []
L_dt_min =[]

L_totdelST = []
#################################################################
for r in range(len(O2)):
    O2[r] = float(O2[r])
    PEEP_set[r] = float(PEEP_set[r])
    TV_set[r] = float(TV_set[r])
    EMV[r] = float(EMV[r])
    ETV[r] = float(ETV[r])
    MAP[r] = float(MAP[r])
    MF[r] = float(MF[r])
    PAP[r] = float(PAP[r])
    SFM[r] = float(SFM[r])
    FC[r] = float(FC[r])
    P[r] = float(P[r])
    SpO2[r] = float(SpO2[r])
    PSP[r] = float(PSP[r])
    PCP[r] = float(PCP[r])
####################################################################
for r in range(len(d.storeTime)):
    L_dt.append(dt.strptime(d.storeTime[r], "%Y-%m-%d %H:%M:%S.%f"))
    

L_ts = []    

cnt=0
for r in range(len(O2)):

    
    if (r < len(O2)-5) and (r > 1) and ((O2[r] != O2[r-1]) or (PEEP_set[r] != PEEP_set[r-1]) or (TV_set[r] != TV_set[r-1])):


        c = r
        delta_ST = 0
        tot_delST = 0
        Ts=0
        while Ts < 300:   
            b = c
            c += 1
            if Code[c] == Code[r]:
                L_c.append(c)

                """d1 = L_dt[b].year*365*24*60*60 + L_dt[b].month*30*24*60*60 + L_dt[b].day*24*60*60 + L_dt[b].hour*60*60 + L_dt[b].minute*60 + L_dt[b].second
                d2 = L_dt[c].year*365*24*60*60 + L_dt[c].month*30*24*60*60 + L_dt[c].day*24*60*60 + L_dt[c].hour*60*60 + L_dt[c].minute*60 + L_dt[c].second
                delta_ST = d2 - d1
                L_delST.append(delta_ST)
                tot_delST += delta_ST"""
                
                s=L_dt[c]-L_dt[b]
                ts=s.total_seconds()
                Ts += ts
                L_ts.append(ts)
                
            elif (Code[c] != Code[r]) or (c == len(O2)-1):
                cnt += 1
                break
        
        L_totdelST.append(tot_delST)       
        L_r.append(r)
   
         
        t1 = L_dt[r-1].year*365*24*60*60 + L_dt[r-1].month*30*24*60*60 + L_dt[r-1].day*24*60*60 + L_dt[r-1].hour*60*60 + L_dt[r-1].minute*60 + L_dt[r-1].second
                
        t2 = L_dt[r].year*365*24*60*60 + L_dt[r].month*30*24*60*60 + L_dt[r].day*24*60*60 + L_dt[r].hour*60*60 + L_dt[r].minute*60 + L_dt[r].second
      
        del_t = t1 + t2
        
        
        L_delta_O2.append(O2[r] - O2[r-1]) 
        L_delta_PEEP.append(PEEP_set[r] - PEEP_set[r-1])
        L_delta_TV_set.append(TV_set[r] - TV_set[r-1])
        L_O2.append(O2[r])
        L_ST.append(ST_min[r])
        L_EMV.append(EMV[r])
        L_ETV.append(ETV[r])
        L_IE.append(IE[r])
        L_MAP.append(MAP[r])
        L_MF.append(MF[r])
        L_PAP.append(PAP[r])
        L_SFM.append(SFM[r])
        L_FC.append(FC[r])
        L_P.append(P[r])
        L_Code.append(Code[r])
        L_PSP.append(PSP[r])
        L_PCP.append(PCP[r])
        

        
        if Code[c] == Code[r]:
            L_SP.append(SpO2[c])
        elif (Code[c] != Code[r]) or ((abs(O2[r] - O2[r-1]) <= 0.2*O2[r]) and del_t < 300):
            L_SP.append(10000)
            
        L_PEEP_set.append(PEEP_set[r])
        L_TV_set.append(TV_set[r])
        
        delta_ST = 0
        
        if SpO2[c] < 81:
            L_SPbin.append(1)
        if 81 <= SpO2[c] <= 83:
            L_SPbin.append(2)
        if 84 <= SpO2[c] <= 85:
            L_SPbin.append(3)   
        if 86 <= SpO2[c] <= 87:
            L_SPbin.append(4)
        if 88 <= SpO2[c] <= 89:
            L_SPbin.append(5)
        if 90 <= SpO2[c] <= 91:
            L_SPbin.append(6)
        if 92 <= SpO2[c] <= 93:
            L_SPbin.append(7)
        if 94 <= SpO2[c] <= 95:
            L_SPbin.append(8)
        if 96 <= SpO2[c] <= 97:
            L_SPbin.append(9)
        if SpO2[c] > 97:
            L_SPbin.append(10)
            
    O2[r] = float(O2[r])
    PEEP_set[r] = float(PEEP_set[r])
    TV_set[r] = float(TV_set[r])
    Code[r] = float(Code[r])


df = pd.DataFrame({'Code': L_Code, 'storeTime': L_ST, 'Expiratory Minute Volume': L_EMV, 'Expiratory Tidal Volume': L_ETV, 'IE Ratio': L_IE, 'Mean Airway Pressure': L_MAP, 'Measured Frequency': L_MF, 'Peak Airway Pressure': L_PAP, 'Spontaneous Frequency measured': L_SFM, 'FC': L_FC, 'Pulse': L_P, 'FiO2 Setting': L_O2, 'PEEP Setting': L_PEEP_set, 'Tidal Volume Setting': L_TV_set, 'delta FiO2 Setting': L_delta_O2, 'delta PEEP Setting': L_delta_PEEP, 'delta Tidal Volume Setting': L_delta_TV_set, 'Pressure Support Level Above P': L_PSP, 'Pressure Control Level Above P': L_PCP, 'SpO2_in_5_min': L_SP, 'Binned SpO2': L_SPbin})

df1 = df[['Code', 'storeTime', 'Expiratory Minute Volume', 'Expiratory Tidal Volume', 'IE Ratio', 'Mean Airway Pressure', 'Measured Frequency', 'Peak Airway Pressure', 'Spontaneous Frequency measured', 'FC', 'Pulse', 'FiO2 Setting', 'PEEP Setting', 'Tidal Volume Setting', 'delta FiO2 Setting', 'delta PEEP Setting', 'delta Tidal Volume Setting', 'Pressure Support Level Above P', 'Pressure Control Level Above P', 'SpO2_in_5_min', 'Binned SpO2']]



df2 = df1[df1.SpO2_in_5_min != 10000]
        


df2.to_csv("NEW_DATA/p_" + File + "_settings.csv", sep=',', index=None) 
df2.to_csv("NEW_DATA/p_" + File + "_settings_tab.csv", sep='\t', index=None) 

