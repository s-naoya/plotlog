import copy
from os.path import splitext, basename
import argparse
from glob import glob


from src.setting import Setting


def main():
    args = arg_parser()
    print(args)
    st = Setting("src/default.yml", args.setting[0])
    st.configure()
    set_log_file_paths(args, st.setting)


def set_log_file_paths(args, st):
    paths = list()
    if args.all:
        paths = glob(st["put_log_dir"]+"*")
    elif args.after:
        paths = [path for path in glob(st["put_log_dir"]+"*") if splitext(basename(path))[0] >= args.after[0]]
    elif args.select:
        pass
    elif args.input:
        paths = copy.copy(args.input)
    elif args.new:
        pass

    print(paths)
    return paths


def arg_parser():
    parser = argparse.ArgumentParser()
    group1 = parser.add_mutually_exclusive_group()
    group1.add_argument("--all",
                        help="plot graph by all log data.",
                        action="store_true")
    group1.add_argument("--after",
                        help="plot graph after DATE. DATE is yyyymmddhhmm.",
                        action="store",
                        metavar="DATE",
                        nargs=1)
    group1.add_argument("--select",
                        help="plot graph only <DATE...>. DATE is yyyymmddhhmm.",
                        action="store",
                        metavar="DATE",
                        nargs="+")
    group1.add_argument("--new",
                        help="plot graph which has not plotted.",
                        action="store_true",
                        default=True)
    group1.add_argument("--input",
                        help="plot graph which you input log file path.",
                        action="store",
                        metavar="LOG_FILE_PATH",
                        nargs="+")
    parser.add_argument("--setting",
                        help="setting file path. default is 'user.yml'.",
                        action="store",
                        metavar="SETTING_FILE_PATH",
                        nargs=1,
                        default="user.yml")
    parser.add_argument("--slice",
                        help="sliced data by start and finish time",
                        action="store",
                        metavar=("BEGIN", "END"),
                        nargs=2)
    parser.add_argument("--shift",
                        help="shift plot start time and x-axis",
                        action="store_true")

    return parser.parse_args()


if __name__ == '__main__':
    main()
