import re
import zipfile

import requests
import os
from Cdriver.EnvRefer import EnvRefer
from Cdriver.bean.Deploy import Deploy

basedir = os.path.dirname(__file__)
path = os.path.join(basedir, 'BrowserDriver')
if not os.path.exists(path): os.makedirs(path)


def localChromedriver():
    env = EnvRefer
    macChrome = Deploy.macChrome
    winChrome = Deploy.winChrome
    if env == 'macos':
        try:
            localPath = os.listdir(macChrome)[0][0:2]
            return localPath
        except Exception as e:
            return '路径获取失败：\n' + str(e)
    elif env == 'windows':
        try:
            localPath = os.listdir(winChrome)[0][0:2]
            return localPath
        except Exception as e:
            return '路径获取失败：\n' + str(e)


def getVersion(value):
    if value is None:
        value = localChromedriver()
    else:
        pass
    url = Deploy.url
    timeList = []
    versionList = {}
    rather = []
    reponse = requests.get(url).text
    result = re.compile(r'\d.*?/</a>.*?Z').findall(reponse)
    indexKey = 0
    for _ in result:
        indexKey = indexKey + 1
        time = _[-24:-1]
        versionList[indexKey] = re.compile(r'.*?/').findall(_)[0][:-1]
        timeList.append(time)
    for _ in range(1, len(versionList) + 1):
        if versionList[_][0:2] == str(value):
            rather.append(versionList[_])
    return max(rather)


def download(citeValue, OsPath):
    url = Deploy.url
    mac_driver_url = url + getVersion(value=citeValue) + OsPath
    file = requests.get(mac_driver_url, timeout=60)
    with open(path + '/chromedriver.zip', 'wb') as zip_file:
        zip_file.write(file.content)
    file = zipfile.ZipFile(path + r'/chromedriver.zip', 'r')
    for files in file.namelist():
        file.extract(files, path)
    file.close()
    os.remove(path + r'/chromedriver.zip')


# 下载Mac系统下的Chromedriver
def cdriver(version=None):
    env = EnvRefer
    resultMac = path + '/chromedriver'
    resultWin = path + '\chromedriver.exe'

    os.listdir(path)
    if env == 'macos':
        if version is None:
            try:
                SysVer = os.popen(path + r'/chromedriver' + ' --version').read().split(' ')[1][0:2]
                if SysVer != localChromedriver():
                    download(citeValue=None, OsPath='/chromedriver_mac64.zip')
                    os.popen('chmod +x ' + path + '/chromedriver')
                    return resultMac
                else:
                    return resultMac

            except Exception as error:
                print(error)
                download(citeValue=version, OsPath='/chromedriver_mac64.zip')
                os.popen('chmod +x ' + path + '/chromedriver')
                return resultMac
        else:
            download(citeValue=version, OsPath='/chromedriver_mac64.zip')
            os.popen('chmod +x ' + path + '/chromedriver')
            return resultMac

    elif env == 'windows':
        if version is None:
            try:
                SysVer = os.popen(path + r'\chromedriver.exe' + ' --version').read().split(' ')[1][0:2]
                if SysVer != localChromedriver():
                    download(citeValue=None, OsPath='/chromedriver_win32.zip')
                    return resultWin
                else:
                    return resultWin

            except Exception as error:
                print(error)
                download(citeValue=version, OsPath='/chromedriver_win32.zip')
                return resultWin
        else:
            download(citeValue=version, OsPath='/chromedriver_win32.zip')
            return resultWin


if __name__ == '__main__':
    print(cdriver())