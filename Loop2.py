import pandas as pd
from datetime import datetime

# Get today's date and file name
today = datetime.today().date()
today_str = today.strftime('%Y-%m-%d')
file_name = f"{today_str}.xlsx"

# Let's say we want to create 5 sheets dynamically
num_sheets = 5

# Generate dynamic sheets with sample data
sheets = {}
for i in range(1, num_sheets + 1):
    sheet_name = f"Sheet{i}"  # You can also use any custom naming logic
    df = pd.DataFrame({
        'Sheet Name': [sheet_name],
        'Date Created': [today],
        'Value': [i * 10]  # Just sample data
    })
    sheets[sheet_name] = df

# Write all dynamic sheets to Excel
with pd.ExcelWriter(file_name, engine='openpyxl') as writer:
    for sheet_name, df in sheets.items():
        df.to_excel(writer, sheet_name=sheet_name, index=False)

print(f"Excel file '{file_name}' with {num_sheets} dynamically named sheets created.")
