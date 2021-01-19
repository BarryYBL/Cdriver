from Cdriver.common.readConfig import readConfig


class Deploy:
    macChrome: str = readConfig.get_config(key='Deploy', param='macChrome')
    winChrome: str = readConfig.get_config(key='Deploy', param='winChrome')
    url: str = readConfig.get_config(key='Deploy', param='url')


if __name__ == '__main__':
    print(Deploy.url)
    print(Deploy.macChrome)
