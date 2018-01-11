import copy
import yaml


class Setting:
    default = None
    default_strings = None
    __user = None

    setting = None
    graph = list()

    __default_file_path = None
    __user_file_path = None

    def __init__(self, user_file_path):
        self.__user_file_path = user_file_path
        self.set_default_setting()

    def configure(self):
        self.__input_yaml()

        self.setting = copy.deepcopy(self.default)
        del self.setting["graph"]
        self.__update_setting(self.__user, self.setting)

        self.__update_graph(copy.deepcopy(self.default["graph"][0]),
                            self.__user["graph"], self.graph)

    def dispose(self):
        self.default.clear()
        self.__user.clear()
        self.setting.clear()
        self.graph.clear()

    def __update_setting(self, from_, to):
        for key in to:
            if key in from_:
                if isinstance(to[key], dict):
                    self.__update_setting(from_[key], to[key])
                else:
                    to[key] = from_[key]

    def __update_graph(self, default, from_, to):
        for f in from_:
            d = dict()
            for key in default:
                if key == "plot":
                    ll = list()
                    self.__update_graph(default[key][0], f[key], ll)
                    d[key] = ll
                elif key == "legend":
                    dd = dict()
                    if key in f:
                        for key2 in default["legend"]:
                            dd[key2] = f[key][key2] if key2 in f[key] \
                                                    else default[key][key2]
                    else:
                        dd = default["legend"]
                    d[key] = dd
                else:
                    d[key] = f[key] if key in f else default[key]
            to.append(d)

    def __input_yaml(self):
        self.set_default_setting()
        with open(self.__user_file_path) as f:
            self.__user = yaml.load(f)

    def set_default_setting(self):
        self.default_strings = """
# log file separate character
log_separate_char: ","

# log file extension
log_extension: "csv"

# used date of log file name type. 0 or 1 or 2 or 3.
# yymmddhhmmss -> 0, yymmddhhmm -> 1, yyyymmddhhmmss -> 2, yyyymmddhhmm -> 3
log_date_type: 0

# output graph extension.
graph_extension: "png"

# log file directory path.
put_log_dir: "log/"

# graph output directory path.
graph_save_dir: "graph/"

# graph size.
# [ x[px], y[px] ]
graph_size: [800, 600]

# header row. If you don't use header, input "null".
header_row: 0

# graph x axis column.
# line number or header name.
xaxis_col: 0

# data shift trigger column.
shift_trig_col: 1

# data shift trigger value.
# do shift if shift_trig_val[0] < shift_trig_col < shift_trig_val[1]
shift_trig_val: [-0.00001, 0.00001]

# graph x axis limiter.
# [ min[s], max[s] ]
xlim: [null, null]

# graph kind array
graph:
  - name: ""  # use file name
    xlabel: ""  # x axis label
    ylabel: ""  # y axis label
    ylim: [null, null]  # y axis limiter
    plot:  # plot line array
      - {col: 1, label: null, color: null, style: "order", width: 1}
    plotfp: false  # which is plot footprint
    legend: {loc: "best", bbox_to_anchor: null, ncol: 1}  # legend setting
        """
        self.default = yaml.load(self.default_strings)
