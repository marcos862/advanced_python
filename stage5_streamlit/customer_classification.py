import os
import pdb
import base64
import pickle
import numpy as np
import pandas as pd
import streamlit as st

from sklearn import svm
from sklearn.decomposition import PCA

BASE_PATH = r"C:\Projects\avst\advanced_python\proyecto_integrador"

pickle_file_pca = 'pca_model_integrador.plk'
full_path = os.path.join(BASE_PATH, pickle_file_pca)
with open(full_path,'rb') as file:
    pickle_pca = pickle.load(file)

pickle_file_svm = 'svm_model_integrador.plk'
full_path = os.path.join(BASE_PATH, pickle_file_svm)
with open(full_path,'rb') as file:
    pickle_svm = pickle.load(file)


app_mode = st.sidebar.selectbox('Select Page', ['Home', 'Prediction'])
if app_mode=='Home':
    st.title('Customer Classifier :')
    # st.image('hipster_loan-1.jpg')
    st.write('App realised by : Marcos Bolaños')
    st.write('(leveraged from Nadia Mhadhbi App)')

elif app_mode =='Prediction':

    # csv=pd.read_csv("informations.csv")
    # st.write(csv)

    # st.image('slider-short-3.jpg')

    st.subheader('Please fill up all details to know what type of customers you are !')
    st.sidebar.header("Informations about the customer : ")
    dict_education = {'Graduation': 0, 'PhD': 1, 'Master': 2, 'Basic': 3, '2n Cycle': 4}
    dict_marital_status = {'Single': 0, 'Together': 1, 'Married': 2, 'Divorced': 3,
                           'Widow': 4}
    YearBirth = st.sidebar.slider('Yearh Birth', 1920, 2020, 1970)
    Married = st.sidebar.radio('Married', tuple(dict_marital_status.keys()))
    Education = st.sidebar.radio('Education', tuple(dict_education.keys()))
    kidshome = st.sidebar.radio('Kids',options=['0', '1', '2', '3+'])
    teenhome = st.sidebar.radio('Teens',options=['0', '1', '2', '3+'])
    ApplicantIncome = st.sidebar.slider('Income', 0, 200000, 50000)
    MntWines = st.sidebar.slider('Spent on Wines', 0, 2000, 0)
    MntFruits = st.sidebar.slider('Spent on Fruits', 0, 2000, 0)
    MntMeatProducts = st.sidebar.slider('Spent on Meat', 0, 2000, 0)
    MntFishProducts = st.sidebar.slider('Spent on Fish', 0, 2000, 0)
    MntSweetProducts = st.sidebar.slider('Spent on Sweets', 0, 2000, 0)
    MntGoldProds = st.sidebar.slider('Spent on Gold', 0, 2000, 0)

    data1={
        'Income': ApplicantIncome,
        'Kidhome': kidshome,
        'Teenhome': teenhome,
        'Recency': 0,
        'MntWines' : MntWines,
        'MntFruits' : MntFruits,
        'MntMeatProducts' : MntMeatProducts,
        'MntFishProducts' : MntFishProducts,
        'MntSweetProducts' : MntSweetProducts,
        'MntGoldProds' : MntGoldProds,
        'NumDealsPurchases': 0,
        'NumWebPurchases': 0,
        'NumCatalogPurchases': 0,
        'NumStorePurchases': 0,
        'NumWebVisitsMonth': 0,
        'AcceptedCmp3': 0,
        'AcceptedCmp4': 0,
        'AcceptedCmp5': 0,
        'AcceptedCmp1': 0,
        'AcceptedCmp2': 0,
        'Complain': 0,
        'Response': 0,
        'Age': 2023 - int(YearBirth),
        'Education_encoded': dict_education[Education],
        'Marital_Status_encoded': dict_marital_status[Married],        
    }
    customer_type = {
        0: "Mid-High", 
        1: "Mid-Low", 
        2: "Rich",
        3: "Poor"
    }

    df_for_prediction = pd.DataFrame(data1, index=[0])

    if st.button("Predict"):
        X_PCA = pickle_pca.transform(df_for_prediction)
        X_SVM = pickle_svm.predict(X_PCA)
        # file_ = open("6m-rain.gif", "rb")
        # contents = file_.read()
        # data_url = base64.b64encode(contents).decode("utf-8")
        # file_.close()

        # file = open("green-cola-no.gif", "rb")
        # contents = file.read()
        # data_url_no = base64.b64encode(contents).decode("utf-8")
        # file.close()

        st.success(
            f'According to your inputs, you are {customer_type[X_SVM[0]]}')
            # st.markdown(
    # f'<img src="data:image/gif;base64,{data_url_no}" alt="cat gif">',
    # unsafe_allow_html=True,)
            # st.markdown(
    # f'<img src="data:image/gif;base64,{data_url}" alt="cat gif">',
    # unsafe_allow_html=True,
    # )