import pickle
import pandas as pd
import streamlit as st
from extract_transform import (load_data, clean_data, remove_outlier,
 keep_flat, add_delta_days, keep_paris)

data = pd.DataFrame()
for year in range(2017,2023):
    data_year = load_data.load_data(year)
    data = pd.concat([data,data_year])

data = clean_data.clean_data(data)
Bounds = {
    "Built surface min": 9,
    "Built surface max": 1000,
    "Ground surface max": 100000,
    "Transaction cost min": 1000,
    "Transaction cost max": 10000000}
Nsigma = 1.5 # any data superior to 1.5 times its standard deviation will be removed
data = remove_outlier.remove_outlier(data, Nsigma, Bounds)
data = keep_flat.keep_flat(data)
data = add_delta_days.add_delta_days(data)
file1 = open('dset/test.pkl','wb')
pickle.dump(data,file1)
data = keep_paris.keep_paris(data) #keep only usefull data and create a column District

# we save the data in a pickle file
file = open('dset/data.pkl', 'wb')
pickle.dump(data, file)
