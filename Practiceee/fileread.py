import pandas as pd

df=pd.read_excel('test.xlsx')

for i,j in df.iterrows():
    dob=j[dob]
    with open("sample.sql","w") as f:
        f="""
        update q2_user  set dob={r[dob]} where userid= {r[userid]}  """
        f.write('Update q2_user set dob={r[dob] where userid={r[userid]}')
