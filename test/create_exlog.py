from os import makedirs
from os.path import isdir
from shutil import rmtree
import numpy as np
import pandas as pd

default_files = [("20170101000000", "log/"),
                 ("20170101120000", "log/"),
                 ("20170102000000", "log/"),
                 ("20170102180000", "log/test1/"),
                 ("20170102200000", "log/test1/"),
                 ("20170103000000", "log/test2/"),
                 ("20170103100000", "log/test2/")]


# log_date_type: 0 or 1 or 2 or 3
def create_exlog(log_date_type=0, files=default_files):
    if isdir("./log"):
        rmtree("./log")
    x = np.linspace(0, 20, 2001)

    for i in range(len(files)):
        df = pd.DataFrame()
        k = (i+1)/3
        df["x"] = x
        df["sin"] = k*np.sin(x)
        df["cos"] = k*np.cos(x)
        df["log"] = k*np.log(x+1)
        df["trig"] = x*0.1
        df.loc[:1000, "trig"] = 0
        df.loc[1001:, "trig"] -= 1

        if log_date_type == 0:
            name = files[i][0][2:]
        elif log_date_type == 1:
            name = files[i][0][2:-2]
        elif log_date_type == 2:
            name = files[i][0]
        elif log_date_type == 3:
            name = files[i][0][:-2]
        else:
            name = ""

        if not isdir(files[i][1]):
            makedirs(files[i][1])

        path = files[i][1]+name+".csv"
        df.to_csv(path, index=False)


if __name__ == '__main__':
    create_exlog()
