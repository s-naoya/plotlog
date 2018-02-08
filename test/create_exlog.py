import numpy as np
import pandas as pd

# log_date_type = 0
names = ["170101000000", "170101120000", "170102000000"]
# log_date_type = 1
# names = ["1701010000", "1701011200", "1701020000", "1707001400"]
# log_date_type = 2
# names = ["20170101000000", "20170101120000", "20170102000000", "20170700140000"]
# log_date_type = 3
# names = ["201701010000", "201701011200", "201701020000", "201707001400"]
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
    df.to_csv("log/"+names[i]+".csv", index=False)
