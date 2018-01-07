import copy
import pandas as pd


class DataCut:
    df = None
    x_axis = None

    __log_file_path = list()
    __x_col = None

    def __init__(self, log_file_path_list):
        for path in log_file_path_list:
            self.__log_file_path.append(path)

    def dispose(self):
        self.__log_file_path.clear()
        self.df = None

    def import_file(self, header, sep):
        for path in self.__log_file_path:
            self.df = pd.read_csv(path, header=header, sep=sep)

    def set_x_axis(self, x_col):
        self.x_axis = self.df[x_col]
        self.__x_col = x_col

    def shift(self, trig_col, trig_val):
        trig_df = self.df[trig_col]
        idx = [0, None]
        while abs(float(trig_df[idx[0]])) < trig_val:
            idx[0] += 1
        shift_start_time = self.x_axis[idx[0]]
        shift_df = self.df.iloc[idx[0]:idx[1], :]
        shift_df[self.__x_col] = shift_df[self.__x_col] - shift_start_time
        self.df = shift_df.reset_index(drop=True)
        self.set_x_axis(self.__x_col)

    def slice(self, begin, end):
        idx = [0, None]
        while float(self.x_axis[idx[0]]) < begin:
            idx[0] += 1
        idx[1] = idx[0]
        while float(self.x_axis[idx[1]]) <= end:
            idx[1] += 1
        slice_df = self.df.iloc[idx[0]:idx[1], :]
        self.df = slice_df.reset_index(drop=True)
        self.set_x_axis(self.__x_col)
