import numpy as np
import pandas as pd
import statsmodels.api as sm
import statsmodels.formula.api as smf

df = pd.DataFrame({"A": [10,20,30,40,50],
                   "B": [20, 30, 10, 40, 50],
                   "C": [32, 234, 23, 23, 42523]})
				   
df1 = pd.DataFrame({"Id": [1,2,3,4,5]})
res = pd.concat([df, df1], axis=1)

result = sm.ols(formula="A ~B + C", data=res).fit()
df['predicted'] = result.predict(df) 