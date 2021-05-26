from numpy.core.arrayprint import printoptions
from numpy.lib.function_base import extract
import scipy.io
import numpy as np
import pandas as pd
import os

class m2c:
    def __init__(self) -> None:
        pass

    def extract_list(x):
        if(type(x[0]) == list and len(x[0]) == 1):
            return m2c.extract_list(x[0])
        return x[0]

    def splitcsvjson(x):
        aux = []
        js = "{\n"
        for name, typ in x.dtype.fields.items():
            if name == 'X':
                # print((x[name][0][0]).shape)
                # print(x[name][0][0])
                df = pd.DataFrame(x[name][0][0])
            else:
                #region Correct data
                # Base numpy arrays
                aux = [i.tolist() for i in x[name].tolist()[0]]

                # Lists on lists
                aux = m2c.extract_list(aux)
                # Numpy.array elements
                try:
                    if (type(aux[0]) != str):
                        aux = [i.tolist()[0] for i in aux]
                except:
                    pass
                
                # String type
                if type(aux) == str:
                    aux = '"'+aux+'"'
                
                #endregion Correct data
                js += f'\t"{name}": {aux},\n'
        js += "}"
        js = js.replace("'", '"')
        return df, js[:-3]+js[-2:]

    def read_matfile(filename):
        data = scipy.io.loadmat(filename)
        cols=[]
        for i in data:
            if '__' not in i :
                cols.append(i)
        df=pd.DataFrame(columns=cols)
        for i in data:
            if '__' not in i :
                df[i]=(data[i]).ravel()

        return df

    def convert_mat(file):
        df = m2c.read_matfile(file)
        os.mkdir(file.split(".")[0])
        for i in range(len(df['data'])):
            df_1, metadata = m2c.splitcsvjson(df['data'][i])
            direction = file.split('.')[0]
            df_1.to_csv(direction+'/register'+str(i)+'.csv')
            with open(direction+"/metadata"+str(i)+".json","w") as f:
                f.write(metadata)

m2c.convert_mat("file.mat")
