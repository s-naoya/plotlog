import pandas as pd


class DataCut:
    __log_file_path = None
    df = None

    def __init__(self, log_file_path):
        self.__log_file_path = log_file_path

    def dispose(self):
        self.__log_file_path = None

    def import_file(self, header, sep):
        self.df = pd.read_csv(self.__log_file_path, header=header, sep=sep)
