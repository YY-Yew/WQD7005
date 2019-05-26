import pandas as pd
import numpy as np
import os
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA




##download and save all the data files in same directory as this script
#read the script path
path = os.path.dirname(os.path.realpath('__file__'))
path = path.replace("\\","/")

#list the file name
arr = []
for file in os.listdir(path):
    if file.endswith(".txt"):
        if file.startswith("Market Watch"):
            arr.append(file)
filenames = [f for f in arr]

#read the 1st file and select useful variables(company name, stock code and last price) 
stock_1stFile = pd.read_csv(filenames[0], sep = '\t', encoding='latin-1')
stock = pd.DataFrame(stock_1stFile.loc[:,['Stock_Code', 'Last']])

#combine the files based on keyID
for data in filenames[1:]:
    stock_remain = pd.read_csv(data, sep = '\t', encoding="latin-1")
    selected_var2 = pd.DataFrame(stock_remain.loc[:,['Stock_Code', 'Last']])
    merge = pd.merge(stock, selected_var2, how = 'left', left_on = 'Stock_Code', right_on = 'Stock_Code')
    stock = merge
stock = stock.replace(np.NaN,0)

#PCA
x = stock.iloc[:,1:].values
x = StandardScaler().fit_transform(x)
pca = PCA(n_components=2)
principalComponents = pca.fit_transform(x)
explained_variance = pca.explained_variance_ratio_ 
print('explained_var =\n\n',explained_variance,'\n')
principalDf = pd.DataFrame(data = principalComponents
                           , columns = ['principal component 1', 'principal component 2'])
print(principalDf.head(5),'\n')
    
#covariance analysis
y = np.array(principalDf).T
covariance = np.cov(y)
variance = np.var(y, axis=1, ddof=1)
print('covariance =\n\n',covariance)