import os
import copy
import argparse
from glob import glob
from os.path import splitext, basename, isfile, isdir


from src.datacut import DataCut
from src.plotgraph import PlotGraph
from src.setting import Setting


def main():
    args = arg_parser()
    st = Setting("src/default.yml", args.setting[0])
    st.configure()
    log_file_paths = get_log_file_paths(args, st.setting)
    pg = PlotGraph()

    for log_file_path in log_file_paths:
        data, memo = setup_data_frame(args, st.setting, log_file_path)
        log_file_name = splitext(basename(log_file_path))[0]

        if args.input:
            save_dir = st.setting["graph_save_dir"] + "other/" + log_file_name
            if not isdir(save_dir):
                os.makedirs(save_dir)
        else:
            date_time, date = get_date(log_file_path, st.setting["log_date_length"])
            save_dir = st.setting["graph_save_dir"] + date + "/" + date_time
            if not isdir(save_dir):
                os.makedirs(save_dir)
        for stg in st.graph:
            graph_path = save_dir + "/" + log_file_name + "_" + stg["name"] \
                         + memo + "." + st.setting["graph_extension"]
            pg.plot(graph_path, st.setting, stg, data.x_axis, data.df)
        print("Complete", log_file_name)

        data.dispose()
    st.dispose()


def get_log_file_paths(args, st):
    paths = []
    if args.input:
        paths = copy.copy(args.input)
    elif args.all:
        paths = glob(st["put_log_dir"]+"*")
    elif args.after:
        for path in glob(st["put_log_dir"] + "*"):
            if splitext(basename(path))[0] >= args.after[0]:
                paths.append(path)
    elif args.select:
        select_paths = []
        for date in args.select:
            select_path = st["put_log_dir"] + date + "." + st["log_extension"]
            select_paths.append(select_path)
        for path in select_paths:
            if isfile(path):
                paths.append(path)
    elif args.new:
        for path in glob(st["put_log_dir"] + "*"):
            date_time, date = get_date(path, st["log_date_length"])
            if not isdir(st["graph_save_dir"] + date + "/" + date_time):
                paths.append(path)
    return paths


def setup_data_frame(args, st, path):
    data = DataCut(path)
    data.import_file(st["header_row"], st["log_separate_char"])
    data.set_x_axis(st["xaxis_col"])
    memo = ""
    if args.noshift:
        memo += "_noshift"
    else:
        data.shift(st["shift_trig_col"], st["shift_trig_val"])
    if args.slice:
        data.slice(args.slice)
        st["xlim"] = [float(args.slice[0]), float(args.slice[1])]
        memo += "_slice_" + args.slice[0] + "_" + args.slice[1]
    return data, memo


def get_date(path, length):
    date_time = splitext(basename(path))[0]
    return date_time, date_time[0:length-4]  # 4 = length of hhmm


def arg_parser():
    parser = argparse.ArgumentParser(
        description='Plot graph for many log file that is managed by DATE')
    group1 = parser.add_mutually_exclusive_group()
    group1.add_argument("--new",
                        help="DEFAULT: output graphs that has not been output yet",
                        action="store_true",
                        default=True)
    group1.add_argument("--all",
                        help="output graphs for all data",
                        action="store_true")
    group1.add_argument("--after",
                        help="output graphs after the selected DATE(yyyymmddhhmm)",
                        action="store",
                        nargs=1,
                        metavar="DATE")
    group1.add_argument("--select",
                        help="output graphs only selected DATEs",
                        action="store",
                        nargs="+",
                        metavar="DATE")
    group1.add_argument("--input",
                        help="output graphs for selected log file",
                        action="store",
                        nargs="+",
                        metavar="LOG_FILE_PATH")
    parser.add_argument("--setting",
                        help="select setting file (default:'user.yml')",
                        action="store",
                        nargs=1,
                        default="user.yml",
                        metavar="SETTING_FILE_PATH")
    parser.add_argument("--slice",
                        help="sliced data by begin and end x-axis value",
                        action="store",
                        nargs=2,
                        metavar=("BEGIN", "END"))
    parser.add_argument("--noshift",
                        help="don't shift plot start time and x-axis",
                        action="store_true")
    return parser.parse_args()


if __name__ == '__main__':
    main()
