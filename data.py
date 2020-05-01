import requests
import io
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.externals.joblib import Memory
from sklearn.datasets import load_svmlight_file
from sklearn.svm import SVC
from os import listdir
from flask import Flask, request, send_file, make_response


code_dir = os.path.dirname(__file__)

def get_url():
    input_path = code_dir+'/input/input.txt'
    input_file = open(input_path, "rt")
    contents = input_file.read()
    url = contents.rstrip()
    input_file.close()
    return str(url)

def download(output):
    data_dir = code_dir+'/data/'
    output_file = data_dir+output
    url = get_url()
    r = requests.get(url, allow_redirects=True)
    open(output_file, 'wb').write(r.content)
    return  str(output) + " Downloaded" + " to" + str(code_dir) + "/data"
