import numpy as np
import pandas as pd


class Chromatogram:
    # This is a class attribute
    all = []

    def __init__(self, NAME, INFO, PDA_DATA=None, FL_DATA=None):
        # Run validation to reacive arguments
        assert type(NAME) is str, f"{NAME} must be a string!"

        # Assign to self object (instance attributes)
        self.NAME = NAME
        self.INFO = INFO
        self.PDA_DATA = PDA_DATA
        self.FL_DATA = {}

        # Action to execute
        Chromatogram.all.append(self)

    # Return an unambiguous string representation of the object
    def __repr__(self) -> str:
        return f"Chromatogram('{self.NAME}')\n\tPDA:'{self.INFO})"

    @classmethod
    def from_file(cls, file_path):
        """Create an instance using the name of the data file"""

        # Extract chromatogram name from filename
        path_list = file_path.split("\\")
        filename = path_list[-1].split(".")

        # Create the instance (important to return)
        return cls(name=filename[0])

    # @classmethod
    # def create from FL() Develop this method.

    @classmethod
    def create_from_pda(cls, file_path, detector=None):
        """This method open the data obtained in a Diode Array Detector (DAD) as
        a text file and create an instance of Chromatogram class"""

        print("Openning DAD file...")

        # Open the .txt file
        with open(file_path, "r") as file:
            lines = file.readlines()

        # "Data comprises raw, unprocessed facts that need context to become
        #  useful, while information is data that has been processed, organized,
        #  and interpreted to add meaning and value."

        # Extract PDA information and data in .txt file (depend of HPLC software)
        data = []
        info = []
        for i, line in enumerate(lines):
            if i < 11:
                info.append(line)
            elif i > 11:
                row = list(map(int, line.split()))
                data.append(row)

        # PDA data
        data = np.array(data)

        # PDA information
        info_dict = {}
        for item in info:
            item = item.replace("\n", "").replace(",", ".")
            key, value = item.split("\t")
            info_dict[key] = value

        # Chromatogram name
        path_list = file_path.split("\\")
        name_list = path_list[-1].split(".")

        # Instanciate object
        return cls(
            NAME=name_list[0],
            INFO=info_dict,
            PDA_DATA=data,
        )

    def add_FL(self, file_path, channel):
        """This method add the data obtained in a fluorescence detector, which
        is stored in csv file (time vs intensity)

        params:
        file_path(str): path of the csv file contianign data point.
        channel(str): channel name to store in FL attribute. In ChromNAV, FL
        data points are exported by single channels."""

        # Read csv file
        df = pd.read_csv(file_path, sep=";", decimal=",")
        # Define FL dictionary
        FL_dict = {}
        FL_dict["time"] = df["min"].to_numpy()
        FL_dict[channel] = df["Intensity"].to_numpy()
        # Assignt to FL_data attribute
        self.FL_DATA = FL_dict

    # def add_PDA()  (DEVELOP THIS METHOD)
