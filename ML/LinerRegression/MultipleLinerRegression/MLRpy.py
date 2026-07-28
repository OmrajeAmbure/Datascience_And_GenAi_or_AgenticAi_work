import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 1.Load Dataset
df = pd.read_csv(r"E:/AIandMl project/NIT Course/Python/ML/LinerRegression/MultipleLinerRegression/investment.csv")

# 2.Split Dataset x and y (independent,dependent)
x = df.iloc[:,:-1]
y = df.iloc[:,4]

# 3. Fill Categorical Variable to Numerical
x = pd.get_dummies(
    x,
    drop_first=True,
    dtype=int
)

# 4. Convert The Dataset into training and testing parts
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=0)

# 5. Select The Liner Model and Train
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(x_train,y_train)

y_pred = regressor.predict(x_test)

prediction_df = pd.DataFrame({
    "Actual": y_test,
    "Predicted": y_pred
})

"""
    We want to find the eq -> y = m1*x1 + m2*x2 + m3*x3 + c
        - till now we build ml multiple liner regression model
        - we need find out the best attribute to grow the bussiness
"""
print(prediction_df)

# m1,m2,m3,m4,m5,m6
print(regressor.coef_)

# c 
print(regressor.intercept_) 

# Add Constant(c) Column
x = np.append(arr=np.full((50,1), 8909).astype(int),values=x,axis=1)
# x_sm = sm.add_constant(x)

# Statistical Model
import statsmodels.api as sm

x_opt = x[:,[0,1,2,3,4,5,6,7]]

# OrdinaryLeastSquare
ols_model = sm.OLS(endog=y,exog=x_opt).fit()
ols_model.summary()

"""
                            OLS Regression Results                            
==============================================================================
Dep. Variable:                 Profit   R-squared:                       0.991
Model:                            OLS   Adj. R-squared:                  0.989
Method:                 Least Squares   F-statistic:                     634.7
Date:                Tue, 28 Jul 2026   Prob (F-statistic):           1.83e-40
Time:                        22:51:39   Log-Likelihood:                -524.92
No. Observations:                  50   AIC:                             1066.
Df Residuals:                      42   BIC:                             1081.
Df Model:                           7                                         
Covariance Type:            nonrobust                                         
==============================================================================
                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
const          1.4369      0.630      2.281      0.028       0.165       2.708
x1             0.8145      0.026     31.219      0.000       0.762       0.867
x2             0.5936      0.032     18.604      0.000       0.529       0.658
x3             1.2105      0.021     58.921      0.000       1.169       1.252
x4          3233.5570   4261.253      0.759      0.452   -5366.000    1.18e+04
x5         -3532.3551   6480.341     -0.545      0.589   -1.66e+04    9545.503
x6          -985.2487   4268.007     -0.231      0.819   -9598.435    7627.937
x7          2171.5862   4327.132      0.502      0.618   -6560.920    1.09e+04
==============================================================================
Omnibus:                        0.532   Durbin-Watson:                   1.879
Prob(Omnibus):                  0.766   Jarque-Bera (JB):                0.399
Skew:                           0.214   Prob(JB):                        0.819
Kurtosis:                       2.904   Cond. No.                     1.07e+06
==============================================================================

Notes:
    
    Model Generated Value > p-value (0.05) -- Reject The Null Hypthosis
    this codition we can apply (elimination of attribute)
    --> (backword Elimination or (RFE) recursive feature elimination)
    
    A common guideline is:
        p-value < 0.05 → Statistically significant.
        p-value ≥ 0.05 → Not statistically significant.
    
    if (P>|t| > 0.5) -> it will direct Remove 
    if (P>|t| < 0.5) -> find The Resoins why or first investigate why those variables are not significant.
    if (P>|t| == 0) -> Best Fit Attribute 
    
All About This Table -> https://chatgpt.com/share/6a65acbf-8f40-83ee-8a74-0ad44704ca58

"""

# Statistical Model
import statsmodels.api as sm

x_opt = x[:,[0,1,2,3,4,5,7]]

# OrdinaryLeastSquare
ols_model = sm.OLS(endog=y,exog=x_opt).fit()
ols_model.summary()

"""
                            OLS Regression Results                            
==============================================================================
Dep. Variable:                 Profit   R-squared:                       0.991
Model:                            OLS   Adj. R-squared:                  0.989
Method:                 Least Squares   F-statistic:                     757.2
Date:                Tue, 28 Jul 2026   Prob (F-statistic):           6.50e-42
Time:                        22:54:24   Log-Likelihood:                -524.95
No. Observations:                  50   AIC:                             1064.
Df Residuals:                      43   BIC:                             1077.
Df Model:                           6                                         
Covariance Type:            nonrobust                                         
==============================================================================
                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
const          1.3664      0.545      2.508      0.016       0.268       2.465
x1             0.8152      0.026     31.829      0.000       0.764       0.867
x2             0.5924      0.031     19.048      0.000       0.530       0.655
x3             1.2111      0.020     59.999      0.000       1.170       1.252
x4          3835.0676   3334.421      1.150      0.256   -2889.433    1.06e+04
x5         -2935.7767   5876.951     -0.500      0.620   -1.48e+04    8916.225
x6          2740.6203   3517.011      0.779      0.440   -4352.109    9833.350
==============================================================================
Omnibus:                        0.509   Durbin-Watson:                   1.895
Prob(Omnibus):                  0.775   Jarque-Bera (JB):                0.391
Skew:                           0.210   Prob(JB):                        0.822
Kurtosis:                       2.895   Cond. No.                     8.42e+05
==============================================================================

"""

# Statistical Model
import statsmodels.api as sm

x_opt = x[:,[0,1,2,3,4,7]]

# OrdinaryLeastSquare
ols_model = sm.OLS(endog=y,exog=x_opt).fit()
ols_model.summary()

"""
                            OLS Regression Results                            
==============================================================================
Dep. Variable:                 Profit   R-squared:                       0.991
Model:                            OLS   Adj. R-squared:                  0.989
Method:                 Least Squares   F-statistic:                     924.3
Date:                Tue, 28 Jul 2026   Prob (F-statistic):           2.29e-43
Time:                        22:55:56   Log-Likelihood:                -525.09
No. Observations:                  50   AIC:                             1062.
Df Residuals:                      44   BIC:                             1074.
Df Model:                           5                                         
Covariance Type:            nonrobust                                         
==============================================================================
                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
const          1.3548      0.540      2.510      0.016       0.267       2.443
x1             0.8145      0.025     32.123      0.000       0.763       0.866
x2             0.5906      0.031     19.283      0.000       0.529       0.652
x3             1.2107      0.020     60.544      0.000       1.170       1.251
x4          4199.6700   3225.694      1.302      0.200   -2301.288    1.07e+04
x5          3096.4626   3414.619      0.907      0.369   -3785.251    9978.176
==============================================================================
Omnibus:                        0.549   Durbin-Watson:                   1.935
Prob(Omnibus):                  0.760   Jarque-Bera (JB):                0.465
Skew:                           0.225   Prob(JB):                        0.793
Kurtosis:                       2.860   Cond. No.                     5.39e+05
==============================================================================

"""
# Statistical Model
import statsmodels.api as sm

x_opt = x[:,[0,1,2,3,4]]

# OrdinaryLeastSquare
ols_model = sm.OLS(endog=y,exog=x_opt).fit()
ols_model.summary()

"""
                            OLS Regression Results                            
==============================================================================
Dep. Variable:                 Profit   R-squared:                       0.990
Model:                            OLS   Adj. R-squared:                  0.990
Method:                 Least Squares   F-statistic:                     1160.
Date:                Tue, 28 Jul 2026   Prob (F-statistic):           9.45e-45
Time:                        22:56:53   Log-Likelihood:                -525.55
No. Observations:                  50   AIC:                             1061.
Df Residuals:                      45   BIC:                             1071.
Df Model:                           4                                         
Covariance Type:            nonrobust                                         
==============================================================================
                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
const          1.4619      0.526      2.781      0.008       0.403       2.521
x1             0.8195      0.025     33.170      0.000       0.770       0.869
x2             0.5886      0.030     19.305      0.000       0.527       0.650
x3             1.2085      0.020     61.011      0.000       1.169       1.248
x4          3268.8090   3051.961      1.071      0.290   -2878.155    9415.774
==============================================================================
Omnibus:                        1.930   Durbin-Watson:                   1.979
Prob(Omnibus):                  0.381   Jarque-Bera (JB):                1.284
Skew:                           0.383   Prob(JB):                        0.526
Kurtosis:                       3.176   Cond. No.                     4.31e+05
==============================================================================

"""
# Statistical Model
import statsmodels.api as sm

x_opt = x[:,[0,1,2,3]]

# OrdinaryLeastSquare
ols_model = sm.OLS(endog=y,exog=x_opt).fit()
ols_model.summary()

"""
                            OLS Regression Results                            
==============================================================================
Dep. Variable:                 Profit   R-squared:                       0.990
Model:                            OLS   Adj. R-squared:                  0.990
Method:                 Least Squares   F-statistic:                     1541.
Date:                Tue, 28 Jul 2026   Prob (F-statistic):           3.88e-46
Time:                        22:58:19   Log-Likelihood:                -526.18
No. Observations:                  50   AIC:                             1060.
Df Residuals:                      46   BIC:                             1068.
Df Model:                           3                                         
Covariance Type:            nonrobust                                         
==============================================================================
                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
const          1.5560      0.519      2.998      0.004       0.511       2.601
x1             0.8169      0.025     33.171      0.000       0.767       0.867
x2             0.5923      0.030     19.518      0.000       0.531       0.653
x3             1.2083      0.020     60.907      0.000       1.168       1.248
==============================================================================
Omnibus:                        0.914   Durbin-Watson:                   1.889
Prob(Omnibus):                  0.633   Jarque-Bera (JB):                0.754
Skew:                           0.294   Prob(JB):                        0.686
Kurtosis:                       2.875   Cond. No.                         73.3
==============================================================================

Notes:

    So hear the x1,x2,x3 are the three attribute 
"""

