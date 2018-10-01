# -*- coding: utf-8 -*-
"""
Created on Sun Sep 30 21:53:37 2018

@author: angem
"""

import os
from skimage import io, filters
import numpy as np
import time

directory = r'C:\Users\angem\Desktop\VG 3D - R2\01052016 week 2'
print('The current directory is {}'.format(os.path.realpath(os.curdir)))
os.chdir(directory)
print('The current directory has been changed to {}'.format(os.path.realpath(os.curdir)))
for k,fname in enumerate(os.listdir()):
    if fname.rsplit('.')[-1]:
        print('Reading file {}'.format(fname))
        im,a = io.imread(fname)
        io.imshow(im)
        time.sleep(1)
    if k >=1:
        break