from numpy.core.arrayprint import printoptions
from numpy.lib.function_base import extract
import scipy.io
import numpy as np
import pandas as pd
import os

data = scipy.io.loadmat('s1.mat')
print(data['s1'])




