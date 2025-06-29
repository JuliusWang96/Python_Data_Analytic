# Initialize libraries

import pandas as pd
from datetime import datetime

# Input

file_name = "Load_Ouput.xlsx"
search_value_col3 = '17'        # Value to search in Column 3
search_value_col4 = 'SDL'        # Value to search in Column 4

# Create Sheets
num_sheets = 5

# Generate dynamic sheets with sample data
sheets = {}
for i in range(1, num_sheets + 1):
    sheet_name = f"Sheet{i}"  # You can also use any custom naming logic
    df = pd.DataFrame({
        'Sheet Name': [sheet_name],
        'Value': [i * 10]  # Just sample data
    })
    sheets[sheet_name] = df

# Write all dynamic sheets to Excel
with pd.ExcelWriter(file_name, engine='openpyxl') as writer:
    for sheet_name, df in sheets.items():
        df.to_excel(writer, sheet_name=sheet_name, index=False)