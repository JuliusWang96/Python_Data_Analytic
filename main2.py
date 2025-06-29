import pandas as pd

# --- SETTINGS ---
file_path = 'test_1.xlsx' # Input Excel file
output_path = 'Output1.xlsx' # Output Excel file
search_value = 'A2'     # Value to search in Column 3

# --- LOAD EXCEL FILE ---
df = pd.read_excel(file_path)

# --- CHECK COLUMN COUNT ---
if df.shape[1] < 17:
    raise ValueError("The Excel file must contain at least 17 columns.")

# --- FILTER ROWS WHERE COLUMN 3 MATCHES THE SEARCH VALUE ---
filtered_df = df[df.iloc[:, 2] == search_value]  # Column 3 is index 2

# --- EXTRACT COLUMNS 4 TO 17 (index 3 to 17) ---
result_df = filtered_df.iloc[:, 3:17]

# --- WRITE TO NEW EXCEL FILE ---
result_df.to_excel(output_path, index=False)

print(f"Filtered data saved to: {output_path}")
