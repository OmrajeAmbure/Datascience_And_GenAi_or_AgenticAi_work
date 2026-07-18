import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


dataset = pd.read_csv('data.csv')

x = dataset.iloc[:,:-1].values
y = dataset.iloc[:,3].values

from sklearn.impute import SimpleImputer
imputer = SimpleImputer(strategy='median');
"""
Univariate imputer for completing missing values with simple strategies.
Replace missing values using a descriptive statistic (e.g. mean, median, or most frequent) along each column, or using a constant value.

Definition : SimpleImputer(*, missing_values=np.nan, strategy="mean",
fill_value=None, copy=True, add_indicator=False,keep_empty_features=False)

strategystr or Callable, default='mean'
    > The imputation strategy.
        - If "mean", then replace missing values using the mean along each column. Can only be used with numeric data.
        
        - If "median", then replace missing values using the median along each column. Can only be used with numeric data.
        
        - If "most_frequent", then replace missing using the most frequent value along each column. 
          Can be used with strings or numeric data. If there is more than one such value, only the smallest is returned.
        
        - If "constant", then replace missing values with fill_value. Can be used with strings or numeric data.
        
        - If an instance of Callable, then replace missing values using the scalar statistic returned by running 
          the callable over a dense 1d array containing non-missing values of each column.
"""

imputer = imputer.fit(x[:,1:3])
x[:,1:3] = imputer.transform(x[:,1:3])

from sklearn.preprocessing import LabelEncoder
"""
Encode target labels with value between 0 and n_classes-1.
This transformer should be used to encode target values, i.e. y, and not the input X.
"""
labelEncoder_x = LabelEncoder()
x[:,0] = labelEncoder_x.fit_transform(x[:,0])

labelEncoder_y = LabelEncoder()
y = labelEncoder_y.fit_transform(y)

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test = train_test_split(x,y,train_size=0.8,test_size=0.2)

"""
-> Split arrays or matrices into random train and test subsets.
-> Quick utility that wraps input validation, next(ShuffleSplit().split(X, y)), and application to input data into a single call for splitting (and optionally subsampling) data into a one-liner.
Definition : train_test_split(*iterables, test_size=None, train_size=None, random_state=None,
shuffle=True, stratify=None, **kwargs: Any)

By diffult it will always suffel the Record on the random state --> Result the model accuracy always change 
so , we use the random_state=0. it will give the proper result

"""
