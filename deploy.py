import pickle
import numpy as np
import pandas as pd

with open ("./prediksi_harga_rumah.pkl", "rb") as f:
    model = pickle.load(f)

def prediksi(LT,LB,JKT,JKM,GRS):
    predict = pd.DataFrame()
    predict['LT'] = [LT]
    predict['LB'] = [LB]
    predict['JKT'] = [JKT]
    predict['JKM'] = [JKM]
    predict['GRS'] = [GRS]
    print(model.predict(predict)[0])


prediksi(100,100,2,2,1)