from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.conf import settings
import os

import json
import numpy as np
import pandas as pd

params = {}
with open(os.path.join(settings.BASE_DIR, 'params.json')) as f:
        data = json.load(f)
for key in data:
        params[key] = np.array(data[key])

def sigmoid(z):
    return 1/(1+np.exp(-z))

def relu(z):
    return np.maximum(z,0)

def forward_layer(W, X, b, activation):
    
    Z = np.dot(W, X) + b
    A = np.zeros(Z.shape)
            
    if activation == "sigmoid":
         A = sigmoid(Z)
    elif activation == "relu":
         A = relu(Z)
    cache = np.copy(Z)
    
    assert A.shape == Z.shape
             
    return A,cache

def forward(X, params,printA=False):
    
    cache = {"Z0": X}
    L = len(params)//2 + 1
    y_hat = np.copy(X)
    
    # Hidden layers = relu
    for l in range(1,L-1):
        y_hat,cache_layer = forward_layer(params["W" + str(l)], y_hat, params["b" + str(l)], "relu")
        cache["Z" + str(l)] = np.copy(cache_layer)
                
    # Final layer = sigmoid 
    y_hat,cache_layer = forward_layer(params["W" + str(L-1)], y_hat, params["b" + str(L-1)], "sigmoid")
    cache["Z" + str(L-1)] = np.copy(cache_layer)
        
    return y_hat,cache

def index(request):
    return render(request,'predict/darkLight.html')

def prediction(request):
    red = int(request.GET.get('red'))
    green = int(request.GET.get('green'))
    blue = int(request.GET.get('blue'))

    X = np.array([[red],[green],[blue]])

    out,cac = forward(X,params)

    print(X.shape)
    print(out)

    out = (out > 0.5).astype(int)

    out = out.tolist()

    return JsonResponse({'val': out[0]})