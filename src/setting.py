import copy
import yaml


class Setting:
    default = None
    __user = None

    setting = None
    graph = list()

    __default_file_path = None
    __user_file_path = None

    def __init__(self, default_file_path, user_file_path):
        self.__default_file_path = default_file_path
        self.__user_file_path = user_file_path

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
                    for key2 in default["legend"]:
                        dd[key2] = f[key][key2] if key2 in f[key] \
                                                else default[key][key2]
                    d[key] = dd
                else:
                    d[key] = f[key] if key in f else default[key]
            to.append(d)

    def __input_yaml(self):
        with open(self.__default_file_path) as f:
            self.default = yaml.load(f)
        with open(self.__user_file_path) as f:
            self.__user = yaml.load(f)
