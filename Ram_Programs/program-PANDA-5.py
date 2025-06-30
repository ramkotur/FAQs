import pandas as pd

data = {'name': ['aa', 'bb', 'cc'],
        'age': [10, 20, 10]}

df = pd.DataFrame(data)

# -------- Process -1 --------------
# Find duplicate ages
duplicate_ages = df[df.duplicated(['age'], keep=False)]

print(duplicate_ages)

# -------- Process -2 --------------

duplicate_ages = df.groupby('age').filter(lambda x: len(x) > 1)

print(duplicate_ages)
