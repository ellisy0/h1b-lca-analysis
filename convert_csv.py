import os
import pandas as pd

src_dir = 'src_data/'
output_dir = 'data/'

os.makedirs(output_dir, exist_ok=True)
files = [f for f in os.listdir(src_dir) if f.endswith('.xlsx')]

for file in files:
    print(f'Converting {file} to CSV...')
    df = pd.read_excel(os.path.join(src_dir, file))
    output_file = os.path.join(output_dir, os.path.splitext(file)[0] + '.csv')
    df.to_csv(output_file, index=False)

print('All files converted to CSV successfully!')
