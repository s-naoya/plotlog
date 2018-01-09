plotlog
===
Output graph script by log file.
In addition to a single file,
you can easily process a large number of identical format log files.



## System requirements
- language : After Python 3.6.3
- necessary package
    - matplotlib
        - `pip3 install matplotlib`
    - pandas
        - `pip3 install pandas`
    - pyyaml
        - `pip3 install yaml`


## Usage
```
plotlog [-h]
        [--new | --all | --after DATE | --select DATE [DATE ...] |
        --input LOG_FILE_PATH [LOG_FILE_PATH ...]]
        [--setting SETTING_FILE_PATH] [--slice BEGIN END] [--noshift]


optional arguments:
  -h, --help            show this help message and exit
  --new                 DEFAULT: output graphs that has not been output yet
  --all                 output graphs for all data
  --after DATE          output graphs after the selected DATE(yyyymmddhhmm)
  --select DATE [DATE ...]
                        output graphs only selected DATEs
  --input LOG_FILE_PATH [LOG_FILE_PATH ...]
                        output graphs for selected log file
  --setting SETTING_FILE_PATH
                        select setting file (default:'user.yml')
  --slice BEGIN END     sliced data by begin and end x-axis value
  --noshift             don't shift plot start time and x-axis
```


## Setting
### item
Confirm [src/default.yml](https://github.com/s-naoya/plotlog/blob/master/src/default.yml)

### way
It is reflected by editing user.yml.
Also, this is reflected by creating a new yaml file and reading it with the `--setting` argument.


## Log file condition
- File name: recommend "yyyymmddhhmm.csv" or "yymmddhhmm.csv" used date.
    - ex.) 201712302359.csv
    - Extension and separate charcter can change setting file.
- All column equal all row
- Put on the directory specified in the setting file (except when using --input)


## LICENCE
This script is licenced under the MIT License. (See [link](https://github.com/s-naoya/plotlog/blob/master/LICENSE))
