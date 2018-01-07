import pandas as pd


class DataCut:
    df = None
    x_axis = None
    __log_file_path = None

    def __init__(self, log_file_path):
        self.__log_file_path = log_file_path

    def dispose(self):
        self.__log_file_path = None
        self.df = None

    def import_file(self, header, sep):
        self.df = pd.read_csv(self.__log_file_path, header=header, sep=sep)

    def set_x_axis(self, x_col):
        self.x_axis = self.df[x_col]
