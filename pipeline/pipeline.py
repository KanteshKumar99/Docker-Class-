import sys
import pandas as pd

args = sys.argv

df=pd.DataFrame({'column-a' : [1,2,3], 'column-b' :['a','b','c']}) 
df['column-3']=args[1]
print(df)
df.to_parquet('output.parquet')
