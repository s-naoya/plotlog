import copy
import argparse
from glob import glob
from os.path import splitext, basename, isfile, isdir

from src.datacut import DataCut
from src.setting import Setting


def main():
    args = arg_parser()
    print(args)
    st = Setting("src/default.yml", args.setting[0])
    st.configure()
    log_file_paths = get_log_file_paths(args, st.setting)

    for log_file_path in log_file_paths:
        data = setup_data_frame(args, st.setting, log_file_path)
        data.dispose()

    st.dispose()


def get_log_file_paths(args, st):
    paths = list()
    if args.input:
        paths = copy.copy(args.input)
    elif args.all:
        paths = glob(st["put_log_dir"]+"*")
    elif args.after:
        paths = [path for path in glob(st["put_log_dir"]+"*") if splitext(basename(path))[0] >= args.after[0]]
    elif args.select:
        paths = [path for path in [st["put_log_dir"]+date+"."+st["log_extension"] for date in args.select] if isfile(path)]
    elif args.new:
        paths = [path for path in glob(st["put_log_dir"]+"*") if not isdir(st["graph_save_dir"] + "/" + splitext(basename(path))[0][0:8] + "/" + splitext(basename(path))[0])]
    return paths


def setup_data_frame(args, st, path):
    data = DataCut(path)
    data.import_file(st["header_row"], st["log_separate_type"])
    data.set_x_axis(st["xaxis_col"])
    if args.shift:
        data.shift(st["shift_trig_col"], st["shift_trig_val"])
    if args.slice:
        data.slice(args.slice)
    return data


def arg_parser():
    parser = argparse.ArgumentParser()
    group1 = parser.add_mutually_exclusive_group()
    group1.add_argument("--all",
                        help="plot graph by all log data",
                        action="store_true")
    group1.add_argument("--after",
                        help="plot graph after DATE. DATE is yyyymmddhhmm.",
                        action="store",
                        nargs=1,
                        metavar="DATE")
    group1.add_argument("--select",
                        help="plot graph only <DATE...>. DATE is yyyymmddhhmm.",
                        action="store",
                        nargs="+",
                        metavar="DATE")
    group1.add_argument("--new",
                        help="DEFAULT: plot graph which has not plotted.",
                        action="store_true",
                        default=True)
    group1.add_argument("--input",
                        help="plot graph which you input log file path",
                        action="store",
                        nargs="+",
                        metavar="LOG_FILE_PATH")
    parser.add_argument("--setting",
                        help="setting file path. default is 'user.yml'",
                        action="store",
                        nargs=1,
                        default="user.yml",
                        metavar="SETTING_FILE_PATH")
    parser.add_argument("--slice",
                        help="sliced data by start and finish time",
                        action="store",
                        nargs=2,
                        metavar=("BEGIN", "END"))
    parser.add_argument("--shift",
                        help="shift plot start time and x-axis",
                        action="store_true")
    return parser.parse_args()


if __name__ == '__main__':
    main()
