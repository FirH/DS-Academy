import pickle
import numpy as np
import pandas as pd
import streamlit as st

with open ("prediksi_harga_rumah.pkl", "rb") as f:
     model = pickle.load(f)

def prediksi(LT,LB,JKT,JKM,GRS):
    predict = pd.DataFrame()
    predict['LT'] = [LT]
    predict['LB'] = [LB]
    predict['JKT'] = [JKT]
    predict['JKM'] = [JKM]
    predict['GRS'] = [GRS]
    return(model.predict(predict)[0])

lt = st.number_input("Input LT")
lb = st.number_input("Input LB")
jkt = st.number_input("Input JKT")
jkm = st.number_input("Input JKM")
grs = st.number_input("Input GRS")

st.write(prediksi(lt,lb,jkt,jkm,grs))
