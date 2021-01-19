
"""
 pip3 install Cdriver==0.0.5
"""

from Cdriver import cdriver

if __name__ == '__main__':
    cdriver()  # 自动匹配系统客户端Chrome版本
    cdriver(78)  # 也可以自定义Chromedriver版本
