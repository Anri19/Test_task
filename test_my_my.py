import pytest
import requests
import json

def test_1():
    a = requests.get('http://127.0.0.1:8000/sequence/elem/13')
    json_res = {"1": 13, "2": 40, "3": 20, "4": 10, "5": 5, "6": 16, "7": 8, "8": 4, "9": 2, "10": 1}
    assert  json_res == a.json()


def test_2():
    a = requests.get('http://127.0.0.1:8000/sequence/longest/13')
    assert  b"Longest sequence is for n = 11 " in a.content


def test_3():
    a = requests.get('http://127.0.0.1:8000/iris/group/sepal_length/max')
    json_res = {"setosa":5.8,"versicolor":7.0,"virginica":7.9}
    assert  json_res == a.json()


def test_4():
    a = requests.get('http://127.0.0.1:8000/iris/describe')
    json_res  = {"sepal_length":{"count":150.0,"mean":5.8433333333,"std":0.828066128,"min":4.3,"25%":5.1,"50%":5.8,"75%":6.4,"max":7.9},
         "sepal_width":{"count":150.0,"mean":3.0573333333,"std":0.4358662849,"min":2.0,"25%":2.8,"50%":3.0,"75%":3.3,"max":4.4},
         "petal_length":{"count":150.0,"mean":3.758,"std":1.7652982333,"min":1.0,"25%":1.6,"50%":4.35,"75%":5.1,"max":6.9},
         "petal_width":{"count":150.0,"mean":1.1993333333,"std":0.762237669,"min":0.1,"25%":0.3,"50%":1.3,"75%":1.8,"max":2.5}}
    assert json_res == a.json()
