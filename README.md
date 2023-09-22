# H-1B LCA Visa Data Analysis

Not sure if your H1-B [Labor Condition Application (LCA)](https://en.wikipedia.org/wiki/Labor_Condition_Application) statistics on your favorite visa info website is up-to-date? Too slow and tedious to look up each company's LCA data on your favorite visa info website? This project aims to solve these problems by providing a local, simple, easy-to-use, and up-to-date H1-B LCA data analysis tool. You decide if the data is up-to-date, by comparing the data in `src_data/` (listed below) to the current disclosure data from the [United States Department of Labor (DOL)](https://www.dol.gov/agencies/eta/foreign-labor/performance#dis) source files.

- `src_data_urls.txt`: The download links for the DOL data source files. Run `wget -P src_data/ -i src_data_urls.txt` to download all files to `src_data/`.
- `src_data/`: All downloaded disclosure data source files from the DOL website are stored in this directory. Filenames and formats are kept as-is. All files prior to 2020 (e.g. `H-1B_Disclosure_Data_FY2019.xlsx`) are not considered because they are sufficiently outdated & have completely different fields in the xlsx file. Current files in this directory are listed below:
  - `LCA_Disclosure_Data_FY2023_Q3.xlsx`: Decision date from 2022-10-01 to 2023-06-30, in order.
  - `LCA_Disclosure_Data_FY2022_Q4.xlsx`: Decision date from 2022-07-01 to 2022-09-30, in order.
  - `LCA_Disclosure_Data_FY2022_Q3.xlsx`: Decision date from 2022-04-01 to 2022-06-30, in order.
  - `LCA_Disclosure_Data_FY2022_Q2.xlsx`: Decision date from 2022-01-01 to 2022-03-31, in order.
  - `LCA_Disclosure_Data_FY2022_Q1.xlsx`: Decision date from 2021-10-01 to 2021-12-31, in order.
  - `LCA_Disclosure_Data_FY2021_Q4.xlsx`: Decision date from 2021-07-01 to 2021-09-30, in order.
  - `LCA_Disclosure_Data_FY2021_Q3.xlsx`: Decision date from 2021-04-01 to 2021-06-30, in order.
  - `LCA_Disclosure_Data_FY2021_Q2.xlsx`: Decision date from 2021-01-01 to 2021-03-31, in order.
  - `LCA_Disclosure_Data_FY2021_Q1.xlsx`: Decision date from 2020-10-01 to 2020-12-31, in order.
  - `LCA_Disclosure_Data_FY2020_Q4.xlsx`: Decision date from 2020-07-01 to 2020-09-30, in order.
  - `LCA_Disclosure_Data_FY2020_Q3.xlsx`: Decision date from 2020-04-01 to 2020-06-30, in order.
  - `LCA_Disclosure_Data_FY2020_Q2.xlsx`: Decision date from 2020-01-01 to 2020-03-31, in order.
  - `LCA_Disclosure_Data_FY2020_Q1.xlsx`: Decision date from 2019-10-01 to 2019-12-31, in order.
- `convert_csv.py`: Converts all files in `src_data/` to CSV format and stores them in `data/`, for faster processing down the line.
- `check_fields_match`: Checks if all CSV files in `data/` have the same fields. If not, it will print out the fields that are different.
- `column_name_fix.py`: Fixes mismatched column names, found out by `check_fields_match.py`, in all CSV files in `data/`. Currently converts all mismatches to the latest format in `data/LCA_Disclosure_Data_FY2023_Q3.csv`.
