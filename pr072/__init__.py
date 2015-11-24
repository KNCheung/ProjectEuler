from pr072 import run as pyRun
from ctypes import CDLL, c_long
from os import path

cRun = CDLL(path.split(path.realpath(__file__))[0] + r'\pr072.dll').run
cRun.argtypes = None
cRun.restype = c_long

#run = cRun
run = pyRun
