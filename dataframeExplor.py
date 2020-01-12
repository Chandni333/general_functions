def dataframeExplor(df):
    print("ROWS: {} COLUMNS: {}".format(str(df.shape[0]),str(df.shape[1])))
    null_df = pd.DataFrame(df.isnull().sum())
    null_df.columns = ['counts']
    null_df[null_df['counts']>0]
    df_num = df.select_dtypes(exclude='object')
    for i in df_num.columns:
        print(i)
        print(outlier_Fun(df_num[i]))