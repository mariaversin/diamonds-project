import pandas as pd
import numpy as np
import seaborn as sns

def col_objects(data):
    
    replace_cut = {'Ideal': 1, 'Premium': 2, 'Very Good': 3, 'Good': 4,'Fair': 5 }
    for k, v in replace_cut.items():
        data['cut']= data['cut'].apply(lambda x:v if x == k else x )    
        
    replace_color = {'J': 1,'I': 2,'H': 3,'G': 4,'F': 5,'E': 6,'D': 7}
    for k, v in replace_color.tems():
        data['color']= data['color'].apply(lambda x:v if x == k else x ) 
       
    replace_clarity = {'I1': 1, 'SI2': 2, 'SI1': 3 , 'VS2': 4, 'VS1': 5, 'VVS2': 6, 'VVS1': 7, 'IF': 8}
    for k,v in replace_clarity.items():    
         data['clarity']= data['clarity'].apply(lambda x:v if x == k else x ) 
    

    # Calculamos la correlacion    
    corr = data.corr()
    corr.style.background_gradient(cmap='coolwarm')
    sns.heatmap(corr, linewidths=0.5, annot=True)


    features_norm = ['carat','table','depth']
    xyz = ['x','y','z']
    numerics = features_norm + xyz

    for col in numerics:
        mean = np.mean(data[col])
        std = np.std(data[col])
        data[col] = (data[col] - mean) / std 
    upper = corr.where(np.triu(np.ones(corr.shape), k=1).astype(np.bool))
    to_drop = [column for column in upper.columns if any(upper[column] > 0.95)]

