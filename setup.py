
from setuptools import setup, find_packages
importe codecs
import os



VERSION = '0.0.1'
DESCRIPTION = "A python kivy package for creating Data tables"


# Settig up
setup(name = 'DataTables',
      vertion = VERSION,
      author = "Mengistu Getie (sgetme)",
      author_email = "sgetme@outlook.com",
      description = DESCRIPTION,
      packages = find_packages(),
      install_requures =[],
      keywords = ['python', 'kivy', 'DataTables'],
      classifieres = [
        "Development Status :: 1 - planning",
        "Intendeed Audience:: Developers",
        "Programming Language:: Python ::3",
        "Operating System :: Unix",
        "Operating System :: MacOS:: MacOS X",
        "Operating System :: Microsoft :: Windows",
      ])
