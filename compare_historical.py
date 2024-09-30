import pandas as pd
import os

# Read the historical means from the existing Excel file
historical_means_path = 'county_means.xlsx'
historical_means = pd.read_excel(historical_means_path, index_col=0)

# Read the July 2020 data
july_2020_path = r"C:\Users\addis\OneDrive\COLLEGE\!Fall 2024\572\lab1\data\PRISM_ppt_tmean_tmax_vpdmin_vpdmax_stable_4km_2020_2020.csv"
july_2020_df = pd.read_csv(july_2020_path, skiprows=10)

# Set the 'Name' column as the index for the July 2020 data
july_2020_df = july_2020_df.set_index('Name')

# Ensure both DataFrames have the same index
common_counties = historical_means.index.intersection(july_2020_df.index)
historical_means = historical_means.loc[common_counties]
july_2020_df = july_2020_df.loc[common_counties]

# Calculate the absolute differences
differences = july_2020_df[['ppt (inches)', 'tmean (degrees F)', 'tmax (degrees F)', 'vpdmin (hPa)', 'vpdmax (hPa)']] - historical_means

# Round the differences to 2 decimal places
differences = differences.round(2)

# Save the absolute differences to a new Excel file
output_path_abs = 'county_differences_2020_vs_historical_absolute.xlsx'
differences.to_excel(output_path_abs)

print(f"Excel file '{output_path_abs}' has been created with the absolute differences between July 2020 and historical averages.")

# Calculate the percentage changes
percentage_changes = ((july_2020_df[['ppt (inches)', 'tmean (degrees F)', 'tmax (degrees F)', 'vpdmin (hPa)', 'vpdmax (hPa)']] - historical_means) / historical_means) * 100

# Round the percentage changes to 2 decimal places
percentage_changes = percentage_changes.round(2)

# Save the percentage changes to a new Excel file
output_path_pct = 'county_differences_2020_vs_historical_percentage.xlsx'
percentage_changes.to_excel(output_path_pct)

print(f"Excel file '{output_path_pct}' has been created with the percentage changes between July 2020 and historical averages.")