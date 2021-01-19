import platform


def _EnvRefer():
    os_system = platform.system()
    if os_system == 'Windows':
        return 'windows'
    elif os_system == 'Darwin' or \
            os_system == 'darwin' or \
            os_system == 'Mac' or \
            os_system == 'mac' or \
            os_system == 'OS X':
        return 'macos'


EnvRefer = _EnvRefer()
