import csv
from datetime import datetime as dt
from datetime import *
import pandas as pd
import sys
import numpy as np
from os.path import join, dirname, abspath, isfile
import os
from csv import DictReader

d1 = pd.read_csv("CHU_DATA/init_data_files/p_1150_Training_DS_01.csv", encoding='utf-8', sep='\t')
d2 = pd.read_csv("CHU_DATA/init_data_files/p_151300_Training_DS_01.csv", encoding='utf-8', sep='\t')
d3 = pd.read_csv("CHU_DATA/init_data_files/p_301450_Training_DS_01.csv", encoding='utf-8', sep='\t')
d4 = pd.read_csv("CHU_DATA/init_data_files/p_451650_Training_DS_01.csv", encoding='utf-8', sep='\t')


frames = [d1, d2, d3, d4]

df = pd.concat(frames, axis=0)

df.to_csv("CHU_DATA/init_data_files/Final_Training_DS.csv", sep='\t', encoding='utf-8', index=None)
