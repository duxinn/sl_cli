from setuptools import setup, find_packages
import os

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="sl_cli",
    version="0.1",
    author="duxin",
    author_email="chenqin_1990@foxmail.com",
    description="",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/duxinn/sl_cli",
    packages=find_packages(),
    install_requires=[
        "Click",
        "xlwt",
        "pycrypto",
        "chardet",
        "fabric"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    data_files=[
        (os.path.expanduser('~'), ['skeleton_configs/surfing.conf.example.json'])
    ],
    entry_points='''
        [console_scripts]
        sl_cli=cli.entry:cli
        sl_ser=cli.entry:ftp_server_cli
    '''
)
