import pandas as pd
import os

# Read the CSV file
data_path = os.path.join('..', 'data', 'PRISM_ppt_tmean_tmax_vpdmin_vpdmax_stable_4km_1919_2019.csv')
df = pd.read_csv(data_path, skiprows=10)  # Skip the first 10 rows of metadata

# Calculate means for each county
county_means = df.groupby('Name').agg({
    'ppt (inches)': 'mean',
    'tmean (degrees F)': 'mean',
    'tmax (degrees F)': 'mean',
    'vpdmin (hPa)': 'mean',
    'vpdmax (hPa)': 'mean'
}).round(2)

# Save to Excel
output_path = 'county_means.xlsx'
county_means.to_excel(output_path)

print(f"Excel file '{output_path}' has been created with the mean values for each county.")