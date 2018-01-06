import yaml


class Setting:
    default = None
    user = None
    setting = None
    __default_file_path = "src/default.yml"
    __user_file_path = None

    def __init__(self, user_file_path):
        self.__user_file_path = user_file_path

    # configure setting dictionary
    def configure(self):
        with open(self.__default_file_path) as f:
            self.default = yaml.load(f)
        with open(self.__user_file_path) as f:
            self.user = yaml.load(f)
        self.setting = dict(self.default)
        self.setting["log_extension"] = "dat"
