import pandas as pd
from datetime import datetime

# Get today's date and format for filename
today = datetime.today().date()
today_str = today.strftime('%Y-%m-%d')
file_name = f"{today_str}.xlsx"

# Example data for multiple sheets
df1 = pd.DataFrame({'Date': [today], 'Sheet': ['Sheet1']})
df2 = pd.DataFrame({'Date': [today], 'Sheet': ['Sheet2']})
df3 = pd.DataFrame({'Date': [today], 'Sheet': ['Sheet3']})

# Write all sheets into one Excel file
with pd.ExcelWriter(file_name, engine='openpyxl') as writer:
    df1.to_excel(writer, sheet_name='Sheet1', index=False)
    df2.to_excel(writer, sheet_name='Sheet2', index=False)
    df3.to_excel(writer, sheet_name='Sheet3', index=False)

print(f"Excel file '{file_name}' with multiple sheets created successfully.")
