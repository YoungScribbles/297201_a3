#Streamlit application for the knn model
import streamlit as st
import plate_model as pm
import pandas as pd

@st.cache_resource
def load_model():
    return pm.PlateModel('./data/applications.csv')

mod = load_model()

# Styles
st.markdown("""
    <style>
        .title {
            font-size: 50px;
            font-weight: bold;
            color: green;
            text-align: center;
        }
        .success {
            color: green;
            font-weight: bold;
        }
        
        .declined {
            color: red;
            font-weight: bold;
        }
 
        .container {
            padding: 20px;
            border-radius: 5px;
            background-color: #f9f9f9;
            margin-bottom: 20px;
        }
    </style>
""", unsafe_allow_html=True)


#Application
st.markdown('<div class="title">Custom License Plate Approval Predictor 🚗</div>', unsafe_allow_html=True)

st.markdown('Wondering if your custom license plate will get the green light? Enter your desired plate below and find out!')

st.write('')

plate = st.text_input('Enter your custom license plate here:', '')

if st.button('Predict'):
    if plate:
        knn_prediction = mod.predict_approved(plate)
        
        if knn_prediction == 1:
            st.markdown('<div class="container"><div class="success">✅ Congratulations! Your license plate is likely to be approved!</div></div>', unsafe_allow_html=True)
        else:
            st.markdown('<div class="container"><div class="declined">🙅‍♀ Sorry, your license plate is likely to be declined.</div></div>', unsafe_allow_html=True)
    else:
        st.error('Please enter a license plate.')

st.markdown("""
    <div style="text-align: center;">
        <hr>
        <p>Disclaimer: This tool is powered by a prediction model and results may vary. For official confirmation, please consult the DMV.</p>
        <p style="color: #777;">© 2024 - Brought to you by Matt P, Johnny W, and Fiona C.</p>
    </div>
""", unsafe_allow_html=True)
