import setuptools
import os
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__),os.pardir)))#待理解
with open("README.md","r") as fh:
    long_description=fh.read()

setuptools.setup(
    name="WYC's frist package",
    version="0.0.1",
    author="吴宇晨",
    author_email="2296136694@qq.com",
    description="用来学习发布包的包",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        ],
    )
