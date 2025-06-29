import pandas as pd
from datetime import datetime

# Get today's date
today = datetime.today().date()
today_str = today.strftime('%Y-%m-%d')

# Create DataFrame with today's date
df = pd.DataFrame({'Date': [today]})

# Define filename with today's date
file_name = f"{today_str}.xlsx"

# Write to new Excel file and sheet
with pd.ExcelWriter(file_name, engine='openpyxl') as writer:
    df.to_excel(writer, sheet_name='Julius', index=False)

print(f"Excel file '{file_name}' created successfully.")
