import pyedflib
import numpy as np
import os

# file_name = os.path.join(pyedflib.util.test_data_path(),
# import pyedflib as pyedflib
# 'test_generator.edf')
f = pyedflib.EdfReader('Subject00_1.edf')
n = f.signals_in_file
signal_labels = f.getSignalLabels()
sigbufs = np.zeros((n, f.getNSamples()[0]))
for i in np.arange(n):
    sigbufs[i, :] = f.readSignal(i)

print(f)
