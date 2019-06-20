import pandas as pd

#reading data from a cvs file

df=pd.read_csv('com.csv')
#df1=pd.read_csv('http://13.234.66.67/summer19/datasets/')

df.info()

#to print all the data
df

#top 3 rows
df.head(3)

# particular colum
df['Name']

#for selecting rows ansd colums
df.iloc[0:,[0,3]]

# salary column
df['Salary'].max()
df['Salary'].min()
df['Salary'].mean()

dir(df['Salary'])
df['Salary'].sum()

x=df.values
type(x)

x=df
type(x)

df['Salary'].values
