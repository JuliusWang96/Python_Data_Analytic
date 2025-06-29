import pandas as pd
from datetime import datetime

# Get today's date and use it as filename
today = datetime.today().date()
today_str = today.strftime('%Y-%m-%d')
file_name = f"{today_str}.xlsx"

# Define your dynamic data (you can populate this dictionary as needed)
sheets = {
    "Summary": pd.DataFrame({'Date': [today], 'Note': ['This is the summary']}),
    "Data2023": pd.DataFrame({'Year': [2023], 'Value': [123]}),
    "Data2024": pd.DataFrame({'Year': [2024], 'Value': [456]}),
    "Notes": pd.DataFrame({'Comment': ['Auto-generated'], 'Checked': [False]})
}

# Write all sheets into the Excel file
with pd.ExcelWriter(file_name, engine='openpyxl') as writer:
    for sheet_name, df in sheets.items():
        df.to_excel(writer, sheet_name=sheet_name, index=False)

print(f"Excel file '{file_name}' with {len(sheets)} sheets created successfully.")
