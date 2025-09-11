"""Process a single batch of data."""

from chroma_tool_py.io import merge_channels, update_xlsx_db

# Important information to be extracted, columns
extract_cols = ["Acquisition Date", "Chromatogram Name", "CH", "Peak Name", "Area"]

RAW_DATA_FOLDER = r"/home/marco/Documentos/GWR Project/peak_info/batch4_01"
DATABASE_PATH = r"/home/marco/Documentos/GWR Project/2025_09_11 - TV_results_database.xlsx"

# Merge peak information into a single dataframe
appended_df = merge_channels(RAW_DATA_FOLDER, extract_cols)

print(appended_df)

# Load information into the database workbook
update_xlsx_db(
    new_df=appended_df,
    workbook_path=DATABASE_PATH,
    sheet_name="TABLE",
    table_name="DataTable",
    batch_name="Batch4_01",
)



