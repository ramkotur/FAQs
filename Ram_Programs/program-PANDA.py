import pandas as pd

data1={'key':['a','b','c'],
     'value':[1,2,3]}
data2 ={'key':['a','b','d'],
      'value':[10,20,30]
        }

df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)

df3 = pd.merge(df1,df2, on='key', how='inner', suffiexs=('_df1','_df2'))

df3.show()
