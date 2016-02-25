#from setuptools import setup
from distutils.core import setup
import py2exe
import sys

APP = ['bakertool.py']
DATA_FILES = ['locale','icons','breadrecipe.cfg']

sys.path.append("C:\\Windows\\System32")
sys.path.append("C:\\Users\\jredond\PyCharmProjects\\myshell")
#setup(console=['shellconsole.py'])
setup(
    console=APP,
    data_files=DATA_FILES
)