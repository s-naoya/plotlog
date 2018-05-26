import re
import sys
import copy
from glob import glob
from os import makedirs
from os.path import splitext, basename, isdir, isfile


class SelectLog:
    def __init__(self, put_log_dir, graph_save_dir, log_date_format):
        self.put_log_dir = put_log_dir
        self.graph_save_dir = graph_save_dir
        self.log_date_format = log_date_format
        self.date_len = len(re.sub(r"[^YMDhms]", "", self.log_date_format))

    def get_logfile_paths(self, args, log_date_type):
        if args.input:
            paths = copy.copy(args.input)
        elif args.all:
            paths = self.get_paths_of_all()
        elif args.after:
            paths = self.get_paths_of_after(args.after[0], log_date_type)
        elif args.select:
            paths = self.get_paths_of_select(args.select)
        elif args.new:
            paths = self.get_paths_of_new(log_date_type)
        else:
            print("Error: Please select input log file.")
            sys.exit()

        for path in paths:
            if not isfile(path):
                print(path, "is not exits.")
                paths.remove(path)
        if len(paths) == 0:
            print("There is no target log file.")
            sys.exit()

        return paths

    def setup_save_dir(self, logfile_name, log_date_type, graph_save_dir):
        if self.__is_fn_in_date(logfile_name, log_date_type) is None:
            save_dir = graph_save_dir + "other/" + logfile_name
        else:
            date_time, date = self.__get_date(logfile_name, log_date_type)
            save_dir = graph_save_dir + date + "/" + date_time

        if not isdir(save_dir):
            makedirs(save_dir)
        return save_dir

    def get_paths_of_after(self, date, log_date_type):
        all_paths = self.get_paths_of_all()
        paths = list()
        for path in all_paths:
            fn = splitext(basename(path))[0]
            if self.__is_fn_in_date(fn, log_date_type) and fn >= date:
                paths.append(path)
        return paths

    def get_paths_of_new(self, log_date_type):
        paths = list()
        for path in self.get_paths_of_all():
            date_time, date = self.__get_date(self.get_fn(path), log_date_type)
            if not isdir(self.graph_save_dir + date + "/" + date_time):
                paths.append(path)
        return paths

    def get_paths_of_select(self, dates):
        paths = list()
        for date in dates:
            path = glob(self.put_log_dir + "**/" + date + ".*", recursive=True)
            if len(path) == 1:
                paths.append(path[0])
            elif len(path) == 0:
                print("Error:", date, "log file is not found")
            else:
                print("Error: found several", date, "log file")
        return paths

    def get_paths_of_all(self):
        return glob(self.put_log_dir + "**/*.*", recursive=True)

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
            print("Error: log_date_type is 0 or 1 or 2 or 3")
            sys.exit()

    # filename to date (To remove a non-numeric from a string)
    @staticmethod
    def fn_to_date(log_file_name):
        return re.sub(r"[^0-9]", "", log_file_name)

    @staticmethod
    def __get_date(date_time, f_type):
        date = date_time[0:6] if f_type == 0 or f_type == 1 else date_time[0:8]
        return date_time, date

    @staticmethod
    def get_fn(path):
        return splitext(basename(path))[0]
