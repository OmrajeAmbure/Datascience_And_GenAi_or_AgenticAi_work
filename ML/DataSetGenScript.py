import pandas as pd
import numpy as np

df = pd.DataFrame({
    "state" : ['Mumbai','Bangalore','Hyderbad','Bangalore','Hyderbad','Mumbai','Bangalore','Mumbai','Hyderabad','Mumbai'],
    "age" : [44,27,30,38,40,35,np.nan,48,50,37],
    "salary" : [72000,48000,54000,61000,np.nan,58000,52000,79000,83000,67000],
    "purchased" : ['No','Yes','No','No','Yes','Yes','No','Yes','No','Yes'],
    })
print(df)
df.to_csv("data.csv",index=False)

"""
Heare,
    - state,age,salary --> Independent Variable
    - purchased --> Dependent Variable [Yes| No]
    it means the user home purcesed or not purchsed 
    it totlay depend on the [state,age,salary]
    
    - Use Classification
"""

