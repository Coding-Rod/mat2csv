from numpy.core.arrayprint import printoptions
from numpy.lib.function_base import extract
import scipy.io
import numpy as np
import pandas as pd
import os
import json

def extract_list(x):
    if(type(x[0]) == list and len(x[0]) == 1):
        return extract_list(x[0])
    return x[0]

def dict_work(x):
    keys = list(x.keys())
    for i in keys:
        if "_" in i:
            del x[i]
    temp = {}
    for i,j in x.items():
        temp[i] = [float(k) for k in list(extract_list(j))]
    return temp
    

def splitcsvjson2(x):
    df = pd.DataFrame(x['data'])
    df = df.set_index(0)
    del x['data']
    x = dict_work(x)
    js = json.dumps(x, indent = 4)
    return df, js
    

def convert_mat2(file):
    data = scipy.io.loadmat(file)
    df, metadata = splitcsvjson2(data)
    direction = file.split('.')[0]
    os.mkdir(direction)
    df.to_csv(direction+'/data.csv')
    with open(direction+"/metadata.json","w") as f:
        f.write(metadata)

# splitcsvjson2(scipy.io.loadmat('eeg_200605191428_epochs.mat'))
convert_mat2('eeg_200605191428_epochs.mat')
# x, js = splitcsvjson2(x)
# print(js)