import copy
from glob import glob

class SelectLog:
    def __init__(self):
        pass

    def get_logfile_paths(self, args, put_log_dir, graph_save_dir, log_date_type):
        paths = list()
        if args.input:
            paths = copy.copy(args.input)
        elif args.all:
            paths = glob(put_log_dir + "*")
        elif args.after:
            pass
        elif args.select:
            pass
        elif args.new:
            pass

        return paths
