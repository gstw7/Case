import matplotlib.pyplot as plt
import seaborn as sns

def plot_bars(df, features, n_rows, n_cols, title, figsize):
   
    fig = plt.figure(figsize=figsize)
    for i, feat in enumerate(features):
        ax = fig.add_subplot(n_rows,n_cols,i+1)
        sns.countplot(data=df, x=feat, ax=ax)
    
    fig.suptitle(title)
    fig.show()

def plot_hists(df, features, n_rows, n_cols, title, figsize):
   
    fig = plt.figure(figsize=figsize)
    for i, feat in enumerate(features):
        ax = fig.add_subplot(n_rows,n_cols,i+1)
        sns.distplot(df[feat], hist=True, bins=20, ax=ax)
    
    fig.suptitle(title)
    fig.show()