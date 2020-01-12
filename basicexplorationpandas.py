import pandas as pd
import numpy as np
titanic=pd.read_csv('C:\\Users\\chand\\Documents\\general_functions\\titanic.csv')
titanic.describe()
titanic.shape
titanic.info()
titanic.isnull().sum()
titanic.describe(include='all')
df = pd.DataFrame(titanic)
df=pd.DataFrame(titanic.describe(include=['int','float']))
for column in df:
    upper=np.nanpercentile(df[column],75)
    lower=np.nanpercentile(df[column],25)
    IQR=upper-lower
    print(IQR)
    upperresult=upper+(1.5*IQR)
    lowerresult=lower-(1.5*IQR)
    print(upperresult)
    print(lowerresult)
    resultlist=[]
    for y in df['Age'].values:
        if y>upperresult or y<lowerresult:
            resultlist.append(y)
        print(resultlist)


df_num=df.select_dtypes(exclude=[object])
df_num_cols=df_num.columns
print(df_num_cols)
for c in df_num_cols:
    print(c)


def dataframeExplor(df):
    print("ROWS: {} COLUMNS: {}".format(str(df.shape[0]),str(df.shape[1])))
    null_df = pd.DataFrame(df.isnull().sum())
    null_df.columns = ['counts']
    null_df[null_df['counts']>0]
    df_num = df.select_dtypes(exclude='object')
    for i in df_num.columns:
        print(i)
        print(outlier_Fun(df_num[i]))