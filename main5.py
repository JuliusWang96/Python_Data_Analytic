import pandas as pd

# --- SETTINGS ---
file_path = 'test_1.xlsx'        # Input Excel file
output_path = 'Output1.xlsx'     # Output Excel file
search_value_col3 = '17'        # Value to search in Column 3
search_value_col4 = 'SDL'        # Value to search in Column 4

# --- LOAD EXCEL FILE ---
df = pd.read_excel(file_path)

# --- CHECK COLUMN COUNT ---
if df.shape[1] < 17:
    raise ValueError("The Excel file must contain at least 17 columns.")

# --- CONVERT COLUMNS TO STRING FOR RELIABLE COMPARISON ---
col3 = df.iloc[:, 2].astype(str)
col4 = df.iloc[:, 3].astype(str)
val3 = str(search_value_col3)
val4 = str(search_value_col4)

# --- FILTER BASED ON COLUMN 3 AND 4 ---
filtered_df = df[(col3 == val3) & (col4 == val4)]

# --- EXTRACT COLUMNS 5 TO 17 (index 4 to 16) ---
result_df = filtered_df.iloc[:, 4:17].copy()

# --- FIND MAX ROWS FROM COLUMN 9 TO 14 (index 8 to 13) ---
max_rows = pd.DataFrame()

for i in range(8, 14):  # Column indices 8 to 13 (Col 9 to Col 14)
    col = result_df.columns[i]
    max_val = result_df[col].max()
    rows_with_max = result_df[result_df[col] == max_val]
    max_rows = pd.concat([max_rows, rows_with_max])

# --- REMOVE DUPLICATE ROWS IF SAME ROW IS MAX IN MULTIPLE COLUMNS ---
max_rows = max_rows.drop_duplicates()

# --- WRITE TO EXCEL ---
max_rows.to_excel(output_path, index=False)

print(f"✅ Filtered rows with max values saved to: {output_path}")
