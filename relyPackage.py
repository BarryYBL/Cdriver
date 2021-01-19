import os
import sys
import platform
import logging


class packageExport:
    # 导出到哪个文件下，默认为项目名更目录
    root: str = 'git/Cdriver'

    # 找到当前目录
    basedir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    path = os.path.join(basedir, root)
    logging.debug('当前目录：' + path)

    # 找到解释器，虚拟环境目录
    python_root = sys.executable
    logging.debug('虚拟环境目录：' + python_root)

    # 拼接生成requirements命令
    if platform.system() == 'Darwin' or 'darwin':
        command = python_root + ' -m pip freeze > ' + path + '/requirements.txt'
        os.system(command)
        logging.debug('导出成功：' + command)
    if platform.system() == 'Linux' or 'linux':
        command = python_root + ' -m pip freeze > ' + path + '/requirements.txt'
        os.system(command)
        logging.debug('导出成功：' + command)
    if platform.system() == 'Windows' or 'windows':
        command = '"' + python_root + '"' + ' -m pip freeze > "' + path + '\\requirements.txt"'
        os.system(command)
        logging.debug('导出成功：' + command)


package = packageExport
