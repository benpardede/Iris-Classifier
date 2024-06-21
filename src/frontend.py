import streamlit as st
import requests
import time

st.image('asstess/header-iris.png')
st.title('Iris Classifier App')
st.markdown('*Created by Max - Pacmann Batch 14*')
st.divider()

st.markdown('Just type the value, and get the result :sunglasses:')

with st.form(key='iris-form'):
    sepal_length = st.number_input('Sepal Length', min_value = 0, help = "Input the numerical Sepal Length")
    sepal_width = st.number_input('Sepal width', min_value = 0, help = "Input the numerical Sepal width")
    petal_length = st.number_input('Petal Length', min_value = 0, help = "Input the numerical Petal Length")
    Petal_width = st.number_input('Petal width', min_value = 0, help = "Input the numerical Petal width")

    submit_button = st.form_submit_button('predict')

    if submit_button:
        #do something
        data = {
            'sepal_length' : sepal_length,
            'sepal_width' : sepal_width,
            'petal_length' : petal_length,
            'petal_width' : Petal_width,
        }
        
        #with spinner
        with st.spinner('Wait for it...'):
            #do something
            response = requests.post('http://backend:8000/predict', json=data)
            result = response.json()
            
            if response.status_code == 200:
                st.success(result['result'])
                st.balloons()
            else:
                st.error(result['detail_error'])
            