# -*- coding: utf-8 -*-
"""
Created on Sun Sep 11 23:16:12 2022

@author: visha
"""

import pickle
import numpy as np
import streamlit as st
from PIL import Image
  
# loading in the model to predict on the data
pickle_in = open(r'C:\Users\visha\Downloads\trained_model.sav', 'rb')
classifier = pickle.load(pickle_in)
  
def welcome():
    return 'Welcome All!'
  
# defining the function which will make the prediction using 
# the data which the user inputs
def prediction(income, age, experience, current_job_years, current_house_years, married_single, car_ownership_yes,
               house_ownership_owned, house_ownership_rented):  
   
    prediction = classifier.predict(
        [[income, age, experience, current_job_years, current_house_years, married_single, car_ownership_yes,
               house_ownership_owned, house_ownership_rented]])
    print(prediction)
    return prediction
      
  
# this is the main function in which we define our webpage 
def main():
      # giving the webpage a title
    st.title("Credit Default Prediction")
      
    # here we define some of the front end elements of the web page like 
    # the font and background color, the padding and the text to be displayed
    html_temp = """
    <div style ="padding:13px">
    <h1 style ="color:black;text-align:center;">DEFAULT CLASSIFIER PREDICTION</h1>
    </div>
    """
      
    # this line allows us to display the front end aspects we have 
    # defined in the above code
    st.markdown(html_temp, unsafe_allow_html = True)
      
    # the following lines create text boxes in which the user can enter 
    # the data required to make the prediction
    income = st.text_input("Annual Income in Rupees", "")
    age = st.text_input("Age", "")
    experience = st.text_input("Experience", "")
    current_job_years = st.text_input("Current Job Years", "")
    current_house_years = st.text_input("Current House Years", "")
    married_single = st.radio("Married/Single [0 = Married and 1 = Single]", ["0","1"])
    car_ownership_yes = st.radio("Do you own a car? [0 = Doesn't own a car and 1 = Owns a car]", ["0","1"])
    house_ownership_owned = st.radio("House ownership? [0 = Doesn't own a house and 1 = Owns a house]", ["0","1"])
    house_ownership_rented = st.radio("House Rented? [0 = Doesn't live on rent and 1 = Lives in a rented house]", ["0","1"])
    result = ""

    if st.button("Predict"):
        result = prediction(income, age, experience, current_job_years, current_house_years, married_single, car_ownership_yes,
               house_ownership_owned, house_ownership_rented)
    st.success('The output is {}'.format(result))
    st.text_input("0 = Won't Default '/n' 1 = Will Default") 
if __name__=='__main__':
    main()