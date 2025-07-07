import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

data = {
    'Hours':[0.5,1.5,2,2.5,3,3.5,4,4.5,5],
    'Pass' :[0,0,0,0,0,1,1,1,1]
}

