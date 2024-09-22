import pyedflib
import pandas as pd
import numpy as np 


file_path = 'chb24_18.edf'  
edf_reader = pyedflib.EdfReader(file_path)

#Extract number of signals and labels
n_signals = edf_reader.signals_in_file
signal_labels = edf_reader.getSignalLabels()

#Define an empty dictionary to store signals
data = {}

for i in range(n_signals):
    signal_data = edf_reader.readSignal(i)
    data[signal_labels[i]] = signal_data

# Convert the dictionary to a DataFrame
df = pd.DataFrame(data)


edf_reader.close()

print(signal_labels)
# print(df.head())

#Save results to csv
df.to_csv('chb24.csv', index=False)
