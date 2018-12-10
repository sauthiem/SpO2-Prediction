# SpO2-Prediction

## add_age_weight.py
This files add age and weight (join) based on a separate demographic file.

## formatting_1_of_3.py, formatting_2_of_3.py, formatting_3_of_3.py
These files complete missing data after pivoting with forward filling, because the variable is considered constant until a more recent one is received.
List of variable affected:
>'Code', 'storeTime', 'Expiratory Minute Volume', 'Expiratory Tidal Volume', 'IE Ratio', 'Mean Airway Pressure', 'Measured Frequency', 'Peak Airway Pressure', 'Spontaneous Frequency measured', 'O2 Concentration Setting', 'PEEP Setting', 'Tidal Volume Setting', 'FC', 'SpO2', 'Pouls', 'Pressure Support Level Above P', 'Pressure Control Level Above P'

## join_training_files.py
Concatenate dataframes to be used a training file
