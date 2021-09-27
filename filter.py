import pandas as pd
df = pd.read_csv('out_put.csv')

df= df[ (df['col1'] == 'Andhra Pradesh' ) | (df['col1'] == 'Telangana')]
df.to_csv('AP_Telangana.csv')
print(df.shape)