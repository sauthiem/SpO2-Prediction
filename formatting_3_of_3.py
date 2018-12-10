import csv
from datetime import datetime as dt
import pandas as pd
import sys
import numpy as np
from os.path import join, dirname, abspath, isfile
import os
from csv import DictReader


File = input("Enter file number:")


with open("NEW_DATA/p_" + File + "_settings.csv", 'r', encoding='utf-8') as inFile, open("NEW_DATA/p_" + File + "_settings_new_header.csv", 'w', encoding='utf-8') as outfile:
    r = csv.reader(inFile)
    w = csv.writer(outfile)
                                                                                    
    next(r, None)  # skip the first row from the reader, the old header
    # write new header
    w.writerow(['Code', 'storeTime', 'Expiratory Minute Volume', 'Expiratory Tidal Volume', 'IE Ratio', 'Mean Airway Pressure', 'Measured Frequency', 'PeakAirwayPres', 'Spontaneous Frequency measured', 'FC', 'Pulse', 'FiO2_setting', 'PEEP_setting', 'TV_setting', 'Pr_Supp_Level_Above_P', 'Pr_Ctrl_Level_Above_P', 'deltaFiO2', 'deltaPEEP', 'deltaTV', 'SpO2 in 5 min.', 'Binned SpO2'])

    # copy the rest
    for row in r:
        w.writerow(row)
###############################################################

d = pd.read_csv("NEW_DATA/p_" + File + "_settings_new_header.csv", encoding='utf-8', sep=',')
################################################################################
a=0
L1 = []
FC_ind = d.columns.get_loc("FC")
for r in range(len(d.FC)):
    if (d.FC[r] > (d.Pulse[r] + 10)) or (d.FC[r] < (d.Pulse[r] - 10)):
        d.iat[r,FC_ind] = 10000
        a=a+1
        L1.append(r)
        
df = d.drop( d[ (d.FC==10000)].index )
        
df.to_csv("NEW_DATA/p_" + File + "_settings_01.csv", sep='\t', index=False) 
d1 = pd.read_csv("NEW_DATA/p_" + File + "_settings_01.csv", sep='\t')
#############################################################
for r in range(len(d1.PeakAirwayPres)):  
    if d1.PeakAirwayPres[r] <= 5:
        d1.PeakAirwayPres[r] = 100000
            
########################################### 
d2 = d1.drop( d1[ (d1.deltaFiO2==100000)].index )
d3 = d2.drop( d2[ (d2.PeakAirwayPres==100000)].index )


##################################################################
d3.to_csv("NEW_DATA/p_" + File + "_settings_temp.csv", encoding='utf-8', sep=',', index=None)

d4 = pd.read_csv("NEW_DATA/p_" + File + "_settings_temp.csv", encoding='utf-8', sep=',')
##################################################################
def myround(x, base=5):
    return int(base * round(float(x)/base))

for r in range(len(d4.deltaFiO2)):
    d4.deltaFiO2[r] = myround(d4.deltaFiO2[r])



d4.to_csv("NEW_DATA/p_" + File + "_Training_DS_01.csv", sep='\t', encoding='utf-8', index=None)
