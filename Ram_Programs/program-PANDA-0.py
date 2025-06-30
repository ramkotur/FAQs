import pandas as pd

data = {
    'name':['aa','bb','cc', 'dd'],
    'age':[10,20,30,30]
}

df =pd.DataFrame(data)

print (df)

print(df.groupby('age').size().reset_index(name='Count'))