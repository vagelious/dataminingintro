# importing pandas package 
import pandas as pd 
import numpy as np
import heapq
from collections import Counter
from sklearn.metrics.pairwise import cosine_similarity
from sklearn import datasets, model_selection
from sklearn.metrics import classification_report	

# making data frame from csv file 
gros_data = pd.read_csv("groceries.csv",sep=";") 
gros_data.head(600)