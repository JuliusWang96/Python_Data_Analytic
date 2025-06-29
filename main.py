import pandas as pd

excel_file = 'books.xlsx'
csv_file = 'books.csv'

df = pd.read_excel(excel_file, usecols=['title', 'authors'])
#df_csv = pd.read_csv(csv_file)

print(df)


