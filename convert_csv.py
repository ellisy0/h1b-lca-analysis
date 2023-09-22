import os
import pandas as pd

src_dir = 'src_data/'
output_dir = 'data/'

# Create the output directory if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

# Get a list of all .xlsx files in the source directory
files = [f for f in os.listdir(src_dir) if f.endswith('.xlsx')]

# Iterate over the files and convert them to CSV
for file in files:
    print(f'Converting {file} to CSV...')

    # Load the Excel file into a pandas DataFrame
    df = pd.read_excel(os.path.join(src_dir, file))
    
    # Construct the output file path by replacing the extension with .csv
    output_file = os.path.join(output_dir, os.path.splitext(file)[0] + '.csv')
    
    # Convert the DataFrame to CSV and save it
    df.to_csv(output_file, index=False)

print('All files converted to CSV successfully!')
