import pandas as pd

path = 'data/'
file_names = ['LCA_Disclosure_Data_FY2023_Q3.csv', 'H-1B_Disclosure_Data_FY2019.csv', 'LCA_Disclosure_Data_FY2020_Q1.csv', 'LCA_Disclosure_Data_FY2020_Q2.csv', 'LCA_Disclosure_Data_FY2020_Q3.csv', 'LCA_Disclosure_Data_FY2020_Q4.csv', 'LCA_Disclosure_Data_FY2021_Q1.csv', 'LCA_Disclosure_Data_FY2021_Q2.csv', 'LCA_Disclosure_Data_FY2021_Q3.csv', 'LCA_Disclosure_Data_FY2021_Q4.csv', 'LCA_Disclosure_Data_FY2022_Q1.csv', 'LCA_Disclosure_Data_FY2022_Q2.csv', 'LCA_Disclosure_Data_FY2022_Q3.csv', 'LCA_Disclosure_Data_FY2022_Q4.csv']

df = pd.read_csv(path + file_names[0], low_memory=False)
columns = set(df.columns.tolist())

all_columns_match = True

for file_name in file_names[1:]:
    df_temp = pd.read_csv(path + file_name, low_memory=False)
    if set(df_temp.columns.tolist()) != columns:
        all_columns_match = False
        print(f"Differences in columns of {file_name}:")
        diff_columns = set(df_temp.columns.tolist()) - columns
        print(f"Extra columns: {diff_columns}")
        diff_columns = columns - set(df_temp.columns.tolist())
        print(f"Missing columns: {diff_columns}")
        print()

if all_columns_match:
    print("All columns match!")
