def aux(df):


    '''
    in: DataFrame;
    out: DataFrame auxiliar'''

    df_aux = pd.DataFrame({'colunas' : df.columns,
                    'tipo': df.dtypes,
                    'missing' : df.isna().sum(),
                    'size' : df.shape[0],
                    'unicos': df.nunique()})
    df_aux['percentual'] = round(df_aux['missing'] / df_aux['size'],3)

return df_aux