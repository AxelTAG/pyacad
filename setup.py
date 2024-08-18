import platform
from setuptools import setup, find_packages

install_requires = []

if platform.system() == "Windows":
      install_requires.append("pywin32")

readme = open("./README.md", "r")

setup(name="pyacad",
      packages=["pyacad"],
      version="0.0.5",
      description="A package aimed to simplfy coding of Activex Automation Module of AutoCAD, based on pywin32 library.",
      long_description = readme.read(),
      long_description_content_type="text/markdown",
      author="Kevin Axel Tagliaferri",
      author_email='kevinaxeltagliaferri@hotmail.com',
      url="https://github.com/AxelTAG/pyacad.git",
      install_requires=install_requires)
