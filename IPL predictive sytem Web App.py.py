# -*- coding: utf-8 -*-
"""
Created on Sun Mar 31 10:08:51 2024

@author: mdeek
"""

import numpy as np
import pickle
import streamlit as st

# loading the saved model
loaded_model = pickle.load(open('D:/IPL Predictions/ipl_trained_model.sav', 'rb'))

#creating a function for prediction

def ipl_runs_prediction(input_data):
    

    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction, "Runs")


  
    
def main():
    
    #giving a title 
    st.title("IPL RUNS prediction Web app")
    
    #getting the input data from the user
    
    "Venue" == st.text_input("Venue stadium")
    "Batsman Team" == st.text_input("Batsman Team")
    "Bowlers Team" == st.text_input("Bowlers Team")
    "Batsman" == st.text_input("Skin Thickness")
    'Bowler' == st.text_input("Insulin Level")
    'Runs Previous Performance' == st.text_input("BMI value")
    'Batsman Overall Performance' == st.text_input("Batsman Overall Performance")
    'Strike Rate' == st.text_input("Strike Rate")
    'Avg. Runs/Inning' == st.text_input("Avg. Runs/Inning")
    'Batsman Batting Order'== st.text_input("Batsman Batting Order")
    'Batsman Age'== st.text_input("Batsman Age")
    'Batsman Experience'== st.text_input("Batsman Experience")
    'Batsman Fitness'== st.text_input("Batsman Fitness")
    'Batsman Preferred Shots' == st.text_input("Batsman Preferred Shots")
    'Batsman Strengths'== st.text_input("Batsman Strengths")
    'Batsman Ability Pace'== st.text_input("Batsman Ability Pace")
    'Batsman Ability Spin'== st.text_input("Batsman Ability Spin")
    'Bowler Recent Wickets'== st.text_input("Bowler Recent Wickets")
    'Bowler Overall Performance' == st.text_input("Bowler Overall Performance")
    'Bowler Last season Wickets' == st.text_input("Bowler Last season Wickets")
    'Bowler Accuracy' == st.text_input("Bowler Accuracy")
    'Bowlers Work load' == st.text_input("Bowlers Work load")
    'Match Weather Conditions' == st.text_input("Match Weather Conditions")
    'Bowler Fitness' == st.text_input("Bowler Fitness")
    'Fielding Positions' == st.text_input("Fielding Positions")
    'Economy Rate'== st.text_input("Economy Rate")
   
    
    #code for prediction 
    RUNS = ''
    
    #creating a button for prediction
    
    if st.button("GET RUNS PREDICTION"):
        RUNS = ipl_runs_prediction_prediction(['Venue', 'Batsman Team', 'Bowlers Team','Batsman','Bowler','Runs Previous Performance' , 'Batsman Overall Performance','Strike Rate', 'Avg. Runs/Inning' ,'Batsman Batting Order', 'Batsman Age','Batsman Experience','Batsman Fitness','Batsman Preferred Shots','Batsman Strengths','Batsman Ability Pace','Batsman Ability Spin','Bowler Recent Wickets','Bowler Overall Performance','Bowler Last season Wickets','Bowler Accuracy','Bowlers Work load','Match Weather Conditions','Bowler Fitness','Fielding Positions','Economy Rate'])
    
    st.success(RUNS)
    
    
    
    
    
if __name__ == '__main__':
    main()
    
    