import pandas as pd

# --- SETTINGS ---
file_path = 'test_1.xlsx'       # Input Excel file
output_path = 'Output1.xlsx'    # Output Excel file
search_value = '17'             # Can be a number or string

# --- LOAD EXCEL FILE ---
df = pd.read_excel(file_path)

# --- CHECK COLUMN COUNT ---
if df.shape[1] < 17:
    raise ValueError("The Excel file must contain at least 17 columns.")

# --- CONVERT COLUMN 3 AND SEARCH VALUE TO STRING FOR COMPARISON ---
column_3_as_str = df.iloc[:, 2].astype(str)
search_value_str = str(search_value)

# --- FILTER ROWS WHERE COLUMN 3 MATCHES THE SEARCH VALUE ---
filtered_df = df[column_3_as_str == search_value_str]

# --- EXTRACT COLUMNS 4 TO 17 (index 3 to 16) ---
result_df = filtered_df.iloc[:, 3:17]

# --- WRITE TO NEW EXCEL FILE ---
result_df.to_excel(output_path, index=False)

print(f"✅ Filtered data saved to: {output_path}")
