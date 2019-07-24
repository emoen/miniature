# pip install yfinance
import yfinance as yf
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
from keras.layers import Dropout



pho=yf.Ticker("pho.ol")
pho.info
hist = pho.history(period="max")

scaler = MinMaxScaler(feature_range = (0, 1))
close = hist.Close.values
close = close.reshape(-1,1)
norm_close = scaler.fit_transform(close)


num_records = len(norm_close)
features_set = []
labels = []
for i in range(60, num_records):
    features_set.append(norm_close[i-60:i])
    labels.append(norm_close[i])
    
features_set, labels = np.array(features_set), np.array(labels)

features_set = np.reshape(features_set, (features_set.shape[0], features_set.shape[1], 1)) 

model = Sequential()
model.add(LSTM(units=50, return_sequences=True, input_shape=(features_set.shape[1], 1)))
model.add(Dropout(0.2))
model.add(LSTM(units=50, return_sequences=True))
model.add(Dropout(0.2))

model.add(LSTM(units=50, return_sequences=True))
model.add(Dropout(0.2))

model.add(LSTM(units=50))
model.add(Dropout(0.2))
model.add(Dense(units = 1))
model.compile(optimizer = 'adam', loss = 'mean_squared_error')
model.fit(features_set, labels, epochs = 100, batch_size = 32)  


test_features = []
for i in range(num_records-60, num_records):
    test_features.append(norm_close[i-60:i, 0])
    
test_features = np.array(test_features)
test_features = np.reshape(test_features, (test_features.shape[0], test_features.shape[1], 1))
predictions = model.predict(test_features) 
predictions = scaler.inverse_transform(predictions)