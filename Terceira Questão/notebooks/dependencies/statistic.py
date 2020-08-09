import pandas as pd
from scipy.stats import chi2, chi2_contingency

def chisquare(data, target, alpha = 0.05):
    
    features_cat = df_train.select_dtypes(exclude=['float', 'int']).columns
    for feat in features_cat:
        data_crosstab = pd.crosstab (data[feat], data[target], margins = False)
        #Chi-square
        _, p, _, _ = chi2_contingency (data_crosstab)

        #Results    
        if p <= alpha:
            print(f'Há dependencia entre {feat} e {target}. P-valor: {p}')
        else:
            print(f'Não há dependencia entre {feat} e {target}. P-valor: {p}')

def corr_2_cols(Col1, Col2):
    res = df_train.groupby([Col1, Col2]).size().unstack()
    res['frequencia(%)'] = (res[res.columns[1]]/(res[res.columns[0]] + res[res.columns[1]]))
    return res