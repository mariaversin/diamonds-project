import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets, svm, metrics
from sklearn.model_selection import train_test_split
from sklearn.svm import LinearSVC
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import GridSearchCV, cross_val_score, train_test_split, KFold
from sklearn.linear_model import Ridge
import sklearn.ensemble as skens
from sklearn.metrics import accuracy_score

data = pd.read_csv('../data.csv/data.csv')
test = pd.read_csv('../test.csv')