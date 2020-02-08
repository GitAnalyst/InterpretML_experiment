import pandas as pd

def df_stats(df):
    
    stats = pd.DataFrame(index=list(df))
    stats['DataTypes'] = df.dtypes
    stats['MissingPct'] = df.isnull().sum()/df.shape[0]*100
    stats['NUnique'] = df.nunique().astype(float)
    print(stats)