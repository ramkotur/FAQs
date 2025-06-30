import pandas as pd

a=[1,2,3,4,4]
df = pd.DataFrame(a,columns=['age'])
gc = df.groupby('age').size().reset_index(name='count')
print(gc[gc["count"] > 1])
print(gc)
print (df.groupby('age').size())