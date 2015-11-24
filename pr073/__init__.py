﻿from pr073 import run as pyRun
from ctypes import CDLL, c_long
from os.path import split, realpath

cRun = CDLL(split(realpath(__file__))[0] + r'\pr073.dll').run
cRun.argtypes = None
cRun.restype = c_long


#run = pyRun
run = cRun
