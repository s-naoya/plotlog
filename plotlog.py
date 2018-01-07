import argparse


def main():
    args = arg_parser()
    print(args)


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
                        metavar="FILENAME",
                        nargs="*")
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
