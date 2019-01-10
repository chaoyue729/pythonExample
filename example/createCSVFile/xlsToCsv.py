import pandas as pd

data_xls = pd.read_excel('/Users/whitexozu/Downloads/lgscript.xlsx', 'Sheet', index_col=None)
# data_xls.to_csv('/Users/whitexozu/dev/project/lgu+/data/lgscript.csv', encoding='utf-8', sep='|')
data_xls.to_csv('/Users/whitexozu/dev/project/LGUplus/data/lgscript.csv', encoding='utf-8', sep='|')
