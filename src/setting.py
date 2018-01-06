import yaml
import copy


class Setting:
    default = None
    user = None

    setting = None
    graph = None

    __default_file_path = "src/default.yml"
    __user_file_path = None

    def __init__(self, user_file_path):
        self.__user_file_path = user_file_path

    def configure(self):
        self.input_yaml()
        self.setting = copy.deepcopy(self.default)
        del self.setting["graph"]
        self.update_setting(self.user, self.setting)

    def update_setting(self, from_, to):
        for key in to:
            if key in from_:
                if isinstance(to[key], dict):
                    self.update_setting(from_[key], to[key])
                else:
                    to[key] = from_[key]

    def input_yaml(self):
        with open(self.__default_file_path) as f:
            self.default = yaml.load(f)
        with open(self.__user_file_path) as f:
            self.user = yaml.load(f)
