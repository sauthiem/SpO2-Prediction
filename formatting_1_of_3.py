import csv
from datetime import datetime as dt
import pandas as pd
import sys
import numpy as np
from os.path import join, dirname, abspath, isfile
import os
from csv import DictReader
import matplotlib.pyplot as plt

##############################################
File = input("Enter file number:")


d = pd.read_csv("NEW_DATA/patients_file_" + File + ".csv", header=None, sep=';')    

d.columns = ['Code', 'storeTime', 'eqt', 'label', 'num_val']
d1 = d[['Code', 'storeTime', 'label', 'num_val']]
d2 = d1.drop(d1.index[0])




d2_piv = d2.pivot_table(index=['Code','storeTime'], columns='label', values='num_val', aggfunc='first')

d2_piv.reset_index(level=0, inplace=True)
d2_piv.reset_index(level=0, inplace=True)




d2_piv.to_csv("NEW_DATA/pivoted_patients_" + File + ".csv", sep='\t', index=None)


################################################################################

F = d2_piv.FC.fillna(method='bfill')
F1 = F.fillna(method='ffill')

Sp = d2_piv.SpO2.fillna(method='bfill')
Sp1 = Sp.fillna(method='ffill')

Pulse = d2_piv.Pouls.fillna(method='bfill')
Pulse1 = Pulse.fillna(method='ffill')

PSL = d2_piv["Pressure Support Level Above P"].fillna(method='bfill')
PSL1 = PSL.fillna(method='ffill')

PCL = d2_piv["Pressure Control Level Above P"].fillna(method='bfill')
PCL1 = PCL.fillna(method='ffill')


A = d2_piv.drop("FC", axis = 1)  
B = A.drop("SpO2", axis = 1)
C = B.drop("Pouls", axis = 1)
D = C.drop("Pressure Support Level Above P", axis = 1)
E = D.drop("Pressure Control Level Above P", axis = 1)


frames = [E, F1, Sp1, Pulse1, PSL1, PCL1]

df = pd.concat(frames, axis=1)


df.reset_index(level=0, inplace=True)


df1 = df[['Code', 'storeTime', 'Expiratory Minute Volume', 'Expiratory Tidal Volume', 'IE Ratio', 'Mean Airway Pressure', 'Measured Frequency', 'Peak Airway Pressure', 'Spontaneous Frequency measured', 'O2 Concentration Setting', 'PEEP Setting', 'Tidal Volume Setting', 'FC', 'SpO2', 'Pouls', 'Pressure Support Level Above P', 'Pressure Control Level Above P']]



df3 = df1.dropna()

df3.to_csv("NEW_DATA/p_" + File + "_com.csv", sep=',', index=None)
df3.to_csv("NEW_DATA/p_" + File + "_tab.csv", sep='\t', index=None)



