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

lt = st.number_input("Luas Tanah")
lb = st.number_input("Luas Bangunan")
jkt = st.number_input("Jumlah Kamar Tidur")
jkm = st.number_input("Jumlah Kamar Mandi")
st.write('Garasi')

col1, col2 = st.columns((1,6))

with col1 :
    ada_grs = st.button('Ada')
with col2 :
    tidak_ada_grs = st.button('Tidak ada')
    
if(ada_grs) :
    grs = 1
if(tidak_ada_grs) :
    grs = 0

predict_button = st.button('Predict')

if(predict_button) :
    st.write(f'Harga rumah impianmu adalah Rp{prediksi(lt,lb,jkt,jkm,grs)}')
