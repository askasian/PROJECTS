# %%
import pandas as pd
import numpy as np
import cufflinks as cf

from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot

# %%
# init_notebook_mode(connected=True)
cf.go_offline()

df = pd.DataFrame(np.random.randn(100, 4), columns='A B C D'.split())
print('\n', df.head())

# %%
df2 = pd.DataFrame({'Category': ['A', 'B', 'C'], 'Values': [32, 43, 50]})
df2

# %%
df.plot()

# %%
df.iplot()

# %%
df.iplot(kind='scatter', x='A', y='B')

# %%
df.iplot(kind='scatter', x='A', y='B', mode='markers', size=20)


# %%
df2.iplot(kind='bar', x='Category', y='Values')
# %%
df.sum().iplot(kind='bar')
# %%
df.iplot(kind='box')
# %%
