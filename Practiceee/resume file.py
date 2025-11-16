import pandas as pd

# From dict
data = {'name': ['Amey', 'John','Amey'], 'score': [90, 85,75]}
df = pd.DataFrame(data)

df['scorealter'] = df.apply(lambda x: x['score']*.2,axis=1)
df['map']=df['scorealter'].map(lambda x:int(x)*3)

df.groupby('name')['score'].sum().sort_values(by='name',ascending=True).reset_index()


