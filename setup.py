from setuptools import setup, find_packages

setup(name="pyacad",
      packages=["pyacad"],
      version="0.0.1",
      description="A package aimed to simplfy coding of Activex Automation Module of AutoCAD, based on pywin32 library.",
      author="Kevin Axel Tagliaferri",
      author_email='kevinaxeltagliaferri@hotmail.com',
      url="https://github.com/AxelTAG/pyacad.git",
      download_url="https://github.com/AxelTAG/pyacad/tarball/0.0.1"
      packages=find_packages(['pyacad', 'pyacad.*']),
      install_requires=['pywin32'])
