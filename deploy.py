import pickle
import numpy as np
import pandas as pd
import streamlit as st

with open ("prediksi_harga_rumah.pkl", "rb") as f:
    model = pickle.load(f)

def prediksi(LT,LB,JKT,JKM,GRS):
    predict = pd.DataFrame()
    predict['Luas Tanah'] = [LT]
    predict['Luas Bangunan'] = [LB]
    predict['Jumlah Kamar Tidur'] = [JKT]
    predict['Jumlah Kamar Mandi'] = [JKM]
    predict['Garasi'] = [GRS]
    return(model.predict(predict)[0])   

lt = st.number_input("Input LT")
lb = st.number_input("Input LB")
jkt = st.number_input("Input JKT")
jkm = st.number_input("Input JKM")
grs = st.number_input("Input GRS")

predict_button = st.button('Predict')

if(predict_button) :
    st.write(f'Harga rumah impianmu adalah : Rp{prediksi(lt,lb,jkt,jkm,grs)}')
