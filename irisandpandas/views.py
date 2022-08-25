import json
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import pandas as pd


def sepal_length_max(request):
    df = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv')
    js = df.groupby('species')['sepal_length'].max().to_json(orient='columns')
    return HttpResponse(js)

def describe(request):
    df = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv')
    js = df.describe().to_json(orient='columns')
    return HttpResponse(js)
