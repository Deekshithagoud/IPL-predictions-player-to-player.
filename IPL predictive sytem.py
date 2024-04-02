# -*- coding: utf-8 -*-
"""
Created on Sun Mar 31 10:08:51 2024

@author: mdeek
"""

import numpy as np
import pickle

# loading the saved model
loaded_model = pickle.load(open('D:/IPL Predictions/ipl_trained_model.sav', 'rb'))

input_data = (1,4,12,8,68,2,243,68,2,23,2,3,6,2,2,1,1,3,23,3,3,1,2,3,9)

# changing the input_data to numpy array
input_data_as_numpy_array = np.asarray(input_data)

# reshape the array as we are predicting for one instance
input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

prediction = loaded_model.predict(input_data_reshaped)
print(prediction ,"Runs")
