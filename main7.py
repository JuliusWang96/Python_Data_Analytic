import pandas as pd

# --- SETTINGS ---
file_path = 'test_1.xlsx'      # Input Excel file
output_path = 'Output1.xlsx'   # Output Excel file

# Values to filter by
search_values_col3 = ['17', '18', '19']
search_values_col4 = ['SDL', 'SDL', 'sDL']

# Load Excel file
df = pd.read_excel(file_path)

# Convert columns 3 and 4 to string for filtering
col3 = df.iloc[:, 2].astype(str)
col4 = df.iloc[:, 3].astype(str)

# Prepare Excel writer for output
with pd.ExcelWriter(output_path, engine='openpyxl') as writer:
    # Loop through all combinations
    for val3 in search_values_col3:
        for val4 in search_values_col4:
            # Filter for the current combination
            filtered = df[(col3 == val3) & (col4 == val4)]
            
            if not filtered.empty:
                # Extract columns 5 to 17 (index 4 to 16), clipped to max columns available
                start_col = 4
                end_col = 17
                max_col = df.shape[1]
                filtered_subset = filtered.iloc[:, start_col:min(end_col, max_col)]
                
                # Sheet name is combination e.g. "17-SDL"
                sheet_name = f"{val3}-{val4}"
                
                # Excel sheet names max length is 31, truncate if necessary
                sheet_name = sheet_name[:31]
                
                # Write to the sheet
                filtered_subset.to_excel(writer, sheet_name=sheet_name, index=False)

print(f"✅ Created '{output_path}' with sheets for all filtered combinations.")
