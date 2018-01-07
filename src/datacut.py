import pandas as pd


class DataCut:
    df = None
    x_axis = None

    __log_file_path = None
    __x_col = None

    def __init__(self, log_file_path):
        self.__log_file_path = log_file_path

    def dispose(self):
        self.__log_file_path = None
        self.df = None

    def import_file(self, header, sep):
        self.df = pd.read_csv(self.__log_file_path, header=header, sep=sep)

    def set_x_axis(self, x_col):
        self.x_axis = self.df[x_col]
        self.__x_col = x_col

    def slice(self, trig_col, trig_val):
        arr = self.df.as_matrix()
        trig_arr = self.df[trig_col].as_matrix()
        idx = [0, None]
        while abs(float(trig_arr[idx[0]])) < trig_val:
            idx[0] += 1
        shift_time = arr[idx[0], 0]
        shift_arr = arr[idx[0]:idx[1], :]
        shift_arr[:, 0] = shift_arr[:, 0] - shift_time
        shift_df = pd.DataFrame(shift_arr)
        shift_df.columns = self.df.columns
        self.df = shift_df
        self.set_x_axis(self.__x_col)
