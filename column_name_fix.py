import fileinput
import glob

path = 'data/'
h1b_dep_fix_list = ['LCA_Disclosure_Data_FY2020_Q1.csv', 'LCA_Disclosure_Data_FY2020_Q2.csv', 'LCA_Disclosure_Data_FY2020_Q3.csv', 'LCA_Disclosure_Data_FY2020_Q4.csv', 'LCA_Disclosure_Data_FY2021_Q2.csv', 'LCA_Disclosure_Data_FY2021_Q4.csv']
employer_poc_fix_list = ['LCA_Disclosure_Data_FY2021_Q1.csv', 'LCA_Disclosure_Data_FY2021_Q3.csv']

def find_replace_columns(filepath, replace_dict):
    with fileinput.input(filepath, inplace=True) as file:
        for line in file:
            for old_column, new_column in replace_dict.items():
                if file.filelineno() == 1:
                    line = line.replace(old_column, new_column)
            print(line, end='')

replace_dict_h1b = {'H-1B_DEPENDENT': 'H_1B_DEPENDENT'}
replace_dict_employer_poc = {'EMPLOYER_POC_ADDRESS_1': 'EMPLOYER_POC_ADDRESS1', 'EMPLOYER_POC_ADDRESS_2': 'EMPLOYER_POC_ADDRESS2', 'H1B_DEPENDENT': 'H_1B_DEPENDENT'}

for file_name in h1b_dep_fix_list:
    fullpath = path + file_name
    find_replace_columns(fullpath, replace_dict_h1b)

for file_name in employer_poc_fix_list:
    fullpath = path + file_name
    find_replace_columns(fullpath, replace_dict_employer_poc)
