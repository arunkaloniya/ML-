import pandas as pd 
import numpy as np 
import sklearn as sk
import matplotlib.pyplot as plt
import seaborn as sn



# Reading Input dataset 

# Comments being added on 1st Nov 

input_data=pd.read_csv(r'C:\Users\Arun\gitlib\ml-2\CarPrice_Assignment.csv')

input_data.columns

input_data.dtypes

input_data.isnull().sum()


plt.scatter(x=input_data['symboling'],y=input_data['price'])
plt.show()

# Creating heatmap for the input dataset 
corr_matrix=input_data.corr()

sn.heatmap(corr_matrix, annot=True)
plt.show()

# col_type=input_data.dtypes.to_frame(name='Data_type').reset_index()




# col_num=col_type[((col_type['Data_type']=='int64' )| (col_type['Data_type']=='float64'))]
# col_char=col_type[(col_type['Data_type']=='int64' )| (col_type['Data_type']=='float64')]




