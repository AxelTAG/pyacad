from setuptools import setup, find_packages

readme = open("./README.md", "r")

setup(name="pyacad",
      packages=["pyacad"],
      version="0.0.3",
      description="A package aimed to simplfy coding of Activex Automation Module of AutoCAD, based on pywin32 library.",
      long_description = readme.read(),
      long_description_content_type="text/markdown",
      author="Kevin Axel Tagliaferri",
      author_email='kevinaxeltagliaferri@hotmail.com',
      url="https://github.com/AxelTAG/pyacad.git",
      install_requires=['pywin32'])
