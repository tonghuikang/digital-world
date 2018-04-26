#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
*** DW Final Exam 2018 Question 1 ****
This file is provided solely for your convenience. 
Should there be any discrepancies, the final version of the code is printed in the question paper. 
'''
'''
*** Import Statements ***
'''

import numpy as np
from sklearn import linear_model, datasets
from sklearn.model_selection import train_test_split 
from sklearn.metrics import mean_squared_error

'''
*** Load the dataset ***
'''
bunchobject = datasets.load_diabetes() 

'''
*** Select the independent variable(s) / dependent variables ***
'''

data = bunchobject.data
feature_index = 2
x = data[:, np.newaxis, feature_index] 
y = bunchobject.target 

'''
*** Carry out the multiple linear regression ***
'''
x_train, x_test, y_train, y_test = train_test_split( x , y , test_size = 0.4, random_state = 10009 )
    
regr = linear_model.LinearRegression()
a = regr.fit(x_train, y_train)
y_pred = regr.predict(x_test)
    
mse = mean_squared_error(y_pred, y_test)
    
results = {'coefficients': regr.coef_ ,
            'intercept': regr.intercept_,
            'mean squared error': mse}
print(results)


