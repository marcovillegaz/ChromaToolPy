"""This script is the processing of peak information stored in singles excel
spreadsheet of single channels. The sample processed here have an unknown
concentration. To know the concentration is needed the use of calibration 
curves."""

import os
from utils import excel


channels = ["CH1", "CH9", "CH10", "CH11", "CH12", "CH13", "CH14", "CH15"]
file_path = r"C:\Users\marco\OneDrive - usach.cl\GWR Analysis\Hojas de calculo\Muestras Henry\Screening_1"
extract_cols = ["Chromatogram Name", "CH", "Peak Name", "Area"]

# Merge single channel data
appended_df = excel.merge(file_path, channels, extract_cols)
# Save data frame in excel
appended_df.to_excel(os.path.join(file_path, "output.xlsx"), index=False)
