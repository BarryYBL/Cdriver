import configparser
import os


class ReadConfig:
    def __init__(self):
        __basedir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        # 具体到那个路径
        __path = os.path.join(__basedir, 'chromePath.ini')
        self.cf = configparser.ConfigParser()
        self.cf.read(__path)

    def get_config(self, key, param):
        value = self.cf.get(key, param)
        return value


readConfig = ReadConfig()
if __name__ == '__main__':
    test = ReadConfig()
    t = readConfig.get_config(key='Deploy', param="macChrome")
    print(t)
