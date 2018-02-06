import numpy as np
import pandas as pd

"""
IMPORT
"""
# read data
df = pd.read_csv('../../data/telecom_churn.csv')
df = pd.read_csv('../../data/telecom_churn.csv', usecols=["a", "b"])

# read data + dates
df = pd.read_csv('../../data/telecom_churn.csv', parse_dates=["timestamp"])

dateparse = lambda x: pd.datetime.strptime(x, '%Y-%m-%d %H:%M:%S')
df = pd.read_csv(file_path, parse_dates=['datetime'], date_parser=dateparse)

"""
INFO
"""
df.head()
df.info()
df.describe()
df.describe(include=['object', 'bool'])
df.shape

# For categorial - use value_counts to calc unique values
df['Churn'].value_counts()
df['Area code'].value_counts(normalize=True)

"""
Indexing, Slicing, Transformation
"""
# Convert to type
df['Churn'] = df['Churn'].astype('int64')

# Sort
df.sort_values(by='Total day charge', ascending=False)
df.sort_values(by=['Churn', 'Total day charge'], ascending=[True, False])

# Extract info with conditioning
df[df['Churn'] == 1].mean()
df[df['Churn'] == 1]['Minutes'].mean()
df[(df['Churn'] == 0) & (df['Plan'] == 'No')]['Minutes'].max()

# Loc
df.loc[0:5, 'State':'Area code']

# ILoc
df.iloc[0:5, 0:3]

# First row
df[:1]
df[-1:]

# Will appply function to each column
df.apply(np.max)

# Will appply function to each row
df.apply(np.max, axis=1)

# Each cell
d = {'No': False, 'Yes': True}
df['Plan'] = df['Plan'].map(d)
df = df.replace({'Plan': d})
