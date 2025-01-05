"""This script is to create surface plot from PDA data for J. Vidal"""

from classes.chromatogram import Chromatogram
from chroma_display import chroma_plot

file_path = r"C:\Users\marco\python-projects\HPLC-signal\orders\client_data\0103 IMI 5 mg OPW FE 10 ppm_003.txt"


print(file_path)

# Chromatogram instance
chroma1 = Chromatogram.create_from_pda(file_path)

print(chroma1.NAME)

chroma_plot.pda_contour(
    chroma1,
    y_max=400,
    z_min=-1000,
    z_max=20000,
    save_path=f"orders\client_data",
)

chroma_plot.pda_2d(chroma1, [250, 300])

""" chroma_plot.pda_surface(
    chroma1,
    y_max=400,
    # z_min=-1000,
    # z_max=20000,
    save_path="orders\client_data",
) """
