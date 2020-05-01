import pandas as pd  
import numpy as np  
import matplotlib.pyplot as plt 
from sklearn.model_selection import train_test_split 
from sklearn.linear_model import LinearRegression
from sklearn import metrics
from flask import Flask, request
from flask import jsonify
import json
from flask import Flask, request, send_file, make_response
import io

def get_data(filename):
    data = pd.read_csv(filename)
    return data

def regression():
    dataset = get_data("jn_code/student-mat.csv")
    X = dataset[['age', 'traveltime', 'studytime', 'goout', 'Dalc','Walc', 'absences', 'G1', 'G2']].values
    y = dataset['G3'].values
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
    regressor = LinearRegression()
    regressor.fit(X_train, y_train)
    y_pred = regressor.predict(X_test)
    df = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred})
    df1 = df.head(50)
    df1_str = pd.DataFrame.to_json(df1)
    return df1_str

def regression_dyn(arg1):
    dataset = get_data("jn_code/student-mat.csv")
    X = dataset[['age', 'traveltime', 'studytime', 'goout', 'Dalc','Walc', 'absences', 'G1', 'G2']].values
    y = dataset['G3'].values
    t_sz = float(arg1)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=t_sz)
    regressor = LinearRegression()  
    regressor.fit(X_train, y_train)
    y_pred = regressor.predict(X_test)
    df = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred})
    df1 = df.head(50)
    df1_str = pd.DataFrame.to_json(df1)
    return df1_str

def plot_pred():
    dataset = get_data("jn_code/student-mat.csv")
    X = dataset[['age', 'traveltime', 'studytime', 'goout', 'Dalc','Walc', 'absences', 'G1', 'G2']].values
    y = dataset['G3'].values
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
    regressor = LinearRegression()
    regressor.fit(X_train, y_train)
    y_pred = regressor.predict(X_test)
    df = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred})
    df1 = df.head(50) 
    df1.plot(kind='bar', figsize=(20,20))
    plt.grid(which='major', linestyle='-', linewidth='0.5', color='green')
    plt.grid(which='minor', linestyle=':', linewidth='0.5', color='black')
    bytes_image = io.BytesIO()
    plt.savefig(bytes_image, format='png')
    bytes_image.seek(0)
    bytes_obj = bytes_image
    return send_file(bytes_obj, attachment_filename='plot.png', mimetype='image/png')

def plot_pred_dyn(arg1):
    dataset = get_data("jn_code/student-mat.csv")
    X = dataset[['age', 'traveltime', 'studytime', 'goout', 'Dalc','Walc', 'absences', 'G1', 'G2']].values
    y = dataset['G3'].values
    t_sz = float(arg1)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=t_sz)
    regressor = LinearRegression()
    regressor.fit(X_train, y_train)
    y_pred = regressor.predict(X_test)
    df = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred})
    df1 = df.head(50)
    df1.plot(kind='bar', figsize=(20,20))
    plt.grid(which='major', linestyle='-', linewidth='0.5', color='green')
    plt.grid(which='minor', linestyle=':', linewidth='0.5', color='black')
    bytes_image = io.BytesIO()
    plt.savefig(bytes_image, format='png')
    bytes_image.seek(0)
    bytes_obj = bytes_image
    return send_file(bytes_obj, attachment_filename='plot.png', mimetype='image/png')
