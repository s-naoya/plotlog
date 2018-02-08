import re
import sys
import copy
from glob import glob
from os.path import splitext, basename, isdir


class SelectLog:
    def __init__(self):
        pass

    def get_logfile_paths(self, args, put_log_dir, graph_save_dir, log_date_type):
        paths = list()
        if args.input:
            paths = copy.copy(args.input)
        elif args.all:
            paths = self.__all_logfile_path(put_log_dir)
        elif args.after:
            paths = self.__get_paths_of_after(args.after[0], put_log_dir, log_date_type)
        elif args.select:
            paths = self.__get_paths_of_select(args.select, put_log_dir)
        elif args.new:
            paths = self.__get_paths_of_new(put_log_dir, graph_save_dir, log_date_type)

        return paths

    def __get_paths_of_after(self, date, put_log_dir, log_date_type):
        all_paths = self.__all_logfile_path(put_log_dir)
        paths = list()
        for path in all_paths:
            fn = splitext(basename(path))[0]
            if self.__is_fn_in_date(fn, log_date_type) and fn >= date:
                paths.append(path)
        return paths

    def __get_paths_of_new(self, put_log_dir, graph_save_dir, log_date_type):
        paths = list()
        for path in self.__all_logfile_path(put_log_dir):
            date_time, date = self.__get_date(path, log_date_type)
            if not isdir(graph_save_dir + date + "/" + date_time):
                paths.append(path)
        return paths

    @staticmethod
    def __get_paths_of_select(dates, put_log_dir):
        paths = list()
        for date in dates:
            path = glob(put_log_dir + "**/" + date + ".*", recursive=True)
            if len(path) == 1:
                paths.append(path[0])
            elif len(path) == 0:
                print("error:", date, "logfile is not found")
            else:
                print("error: found several", date, "logfile")
        return paths

    @staticmethod
    def __all_logfile_path(put_log_dir):
        return glob(put_log_dir + "**/*.*", recursive=True)

    @staticmethod
    def __is_fn_in_date(s, f_type):
        if f_type == 0:
            return re.search("[%s]" % s, "[0-9]{2}[0-1][0-9][0-3][0-9]"
                                         "[0-2][0-9][0-5][0-9][0-5][0-9]")
        elif f_type == 1:
            return re.search("[%s]" % s, "[0-9]{2}[0-1][0-9][0-3][0-9]"
                                         "[0-2][0-9][0-5][0-9]")
        elif f_type == 2:
            return re.search("[%s]" % s, "[0-9]{4}[0-1][0-9][0-3][0-9]"
                                         "[0-2][0-9][0-5][0-9][0-5][0-9]")
        elif f_type == 3:
            return re.search("[%s]" % s, "[0-9]{4}[0-1][0-9][0-3][0-9]"
                                         "[0-2][0-9][0-5][0-9]")
        else:
            print("error: log_date_type is 0 or 1 or 2 or 3")
            sys.exit()

    @staticmethod
    def __get_date(path, f_type):
        date_time = splitext(basename(path))[0]
        date = date_time[0:6] if f_type == 0 or f_type == 1 else date_time[0:8]
        return date_time, date
