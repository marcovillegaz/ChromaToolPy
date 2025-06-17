"""Process a single batch of data."""

import os
import shutil

from src.io.merge_channels import *
from src.io.update_excel_db import *


# Important information to be extracted, columns
extract_cols = ["Acquisition Date", "Chromatogram Name", "CH", "Peak Name", "Area"]

raw_data_folder = r"C:\Users\marco\OneDrive - usach.cl\GWR Analysis\2_Analysis\Thais_Vargas\Raw\batch1_02"
database_path = r"C:\Users\marco\OneDrive - usach.cl\GWR Analysis\2_Analysis\Thais_Vargas\TV_results_database.xlsx"

# Merge peak information into a single dataframe
appended_df = merge_files(raw_data_folder, extract_cols)

print(appended_df)

# Load information into the database workbook
load_data(
    new_df=appended_df,
    workbook_path=database_path,
    sheet_name="TABLE",
    table_name="DataTable",
    batch_name="Batch1_02",
)
