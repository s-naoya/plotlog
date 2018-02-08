from os import makedirs
from os.path import isdir
import numpy as np
import pandas as pd

log_date_type = 0  # or 1 or 2 or 3
names = ["20170101000000", "20170101120000", "20170102000000", "20170102180000", "20170103000000"]
dirs = ["log/", "log/", "log/", "log/test1/", "log/test2/"]
x = np.linspace(0, 20, 2001)

for i in range(len(names)):
    df = pd.DataFrame()
    k = (i+1)/3
    df["x"] = x
    df["sin"] = k*np.sin(x)
    df["cos"] = k*np.cos(x)
    df["log"] = k*np.log(x+1)
    df["trig"] = x*0.1
    df.loc[:1000, "trig"] = 0
    df.loc[1001:, "trig"] -= 1

    name = None
    if log_date_type == 0:
        name = names[i][2:]
    elif log_date_type == 1:
        name = names[i][2:-2]
    elif log_date_type == 2:
        name = names[i]
    elif log_date_type == 3:
        name = names[i][:-2]

    if not isdir(dirs[i]):
        makedirs(dirs[i])

    df.to_csv(dirs[i]+name+".csv", index=False)
