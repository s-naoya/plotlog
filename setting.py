import yaml


class Setting:
    default = None

    def __init__(self):
        pass

    def configure(self):
        with open("default.yml") as f:
            self.default = yaml.load(f)
