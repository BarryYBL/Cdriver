# coding=utf-8
import re
import ast
from setuptools import setup, find_packages

_version_re = re.compile(r'__version__\s+=\s+(.*)')

with open('Cdriver/__init__.py', 'rb') as f:
    version = str(ast.literal_eval(_version_re.search(
        f.read().decode('utf-8')).group(1)))

setup(
    name='Cdriver',
    version=version,
    license='BSD',
    url='https://github.com/BarryYBL/Cdriver',
    author='Barry',
    author_email='YBL2652612315@126.com',
    description='Automatically download the browser drivers',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'certifi==2020.12.5',
        'chardet==4.0.0',
        'idna==2.10',
        'requests==2.25.1',
        'urllib3==1.26.2',
    ],
    classifiers=[
        'Intended Audience :: Developers',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        "Topic :: Software Development :: Testing",
    ],
    py_modules=['whyteboard'],
    scripts=[
        'Cdriver/chromePath.ini',
    ],
)
