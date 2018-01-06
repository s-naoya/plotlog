import copy
import yaml


class Setting:
    default = None
    user = None

    setting = None
    graph = list()

    __default_file_path = "src/default.yml"
    __user_file_path = None

    def __init__(self, user_file_path):
        self.__user_file_path = user_file_path

    def configure(self):
        self.input_yaml()

        self.setting = copy.deepcopy(self.default)
        del self.setting["graph"]
        self.__update_setting(self.user, self.setting)

        self.__update_graph(copy.deepcopy(self.default["graph"][0]),
                            self.user["graph"], self.graph)

    def __update_setting(self, from_, to):
        for key in to:
            if key in from_:
                if isinstance(to[key], dict):
                    self.__update_setting(from_[key], to[key])
                else:
                    to[key] = from_[key]

    @staticmethod
    def __update_graph(default, from_, to):
        for f in from_:
            d = dict()
            for key in default:
                if key == "plot":
                    ll = list()
                    for ff in f[key]:
                        dd = dict()
                        for key2 in default["plot"][0]:
                            if key2 in ff:
                                dd[key2] = ff[key2]
                            else:
                                dd[key2] = default[key][0][key2]
                        ll.append(dd)
                    d[key] = ll
                elif key == "legend":
                    dd = dict()
                    for key2 in default["legend"]:
                        if key2 in f[key]:
                            dd[key2] = f[key][key2]
                        else:
                            dd[key2] = default[key][key2]
                    d[key] = dd
                else:
                    d[key] = f[key] if key in f else default[key]
            to.append(d)

    def input_yaml(self):
        with open(self.__default_file_path) as f:
            self.default = yaml.load(f)
        with open(self.__user_file_path) as f:
            self.user = yaml.load(f)
