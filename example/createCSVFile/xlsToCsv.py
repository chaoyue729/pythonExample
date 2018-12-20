import pandas as pd

data_xls = pd.read_excel('/Users/whitexozu/Downloads/lgscript.xlsx', 'Sheet1', index_col=None)
data_xls.to_csv('/Users/whitexozu/Downloads/lgscript.xlsx', encoding='utf-8')