import re
import sys
import copy
from glob import glob
from os.path import splitext, basename


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
            pass
        elif args.new:
            pass

        return paths

    def __get_paths_of_after(self, date, put_log_dir, log_date_type):
        all_paths = self.__all_logfile_path(put_log_dir)
        paths = list()
        for path in all_paths:
            fn = splitext(basename(path))[0]
            if self.is_fn_in_date(fn, log_date_type) and fn >= date:
                paths.append(path)
        return paths

    @staticmethod
    def __all_logfile_path(put_log_dir):
        return glob(put_log_dir + "**/*.*", recursive=True)

    @staticmethod
    def is_fn_in_date(s, f_type):
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
