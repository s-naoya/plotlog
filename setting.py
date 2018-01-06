import yaml


class Setting:
    default = None
    setting = None
    __default_file_path = "default.yml"
    __setting_file_path = None

    def __init__(self, setting_file_path):
        self.__setting_file_path = setting_file_path

    def configure(self):
        with open(self.__default_file_path) as f:
            self.default = yaml.load(f)
        with open(self.__setting_file_path) as f:
            self.setting = yaml.load(f)
