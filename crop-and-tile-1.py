# -*- coding: utf-8 -*-
"""
Created on Sun Sep 30 21:53:37 2018

@author: angem
"""

import os
from skimage import io, filters
import numpy as np
import matplotlib.pyplot as plt
import time
#io.use_plugin('matplotlib')

directory = r'C:\Users\angem\Desktop\VG 3D - R2\01052016 week 2'
print(                                                                         #Print prints strings to the console
      'The current directory is {}'.format(os.path.realpath(os.curdir)) #the format method (function) for strings inserts the input argument in teh string at the curly brackets. You can insert many arguments
      )
os.chdir(directory)
print('The current directory has been changed to {}'.format(os.path.realpath(os.curdir)))
for k,fname in enumerate(os.listdir()):
    if fname.rsplit('.')[-1]: #rsplit splits the string into separate strings at the given delimiter
        print('Reading file {}'.format(fname))
        im= io.imread(fname)
        plt.figure((k+1)*1000)
        print('Show pictures as they were read in')
        io.imshow(im)
        print('now lets show each color channel')
        for k2 in np.arange(np.size(im,axis=2)):
            plt.figure(k*1000+k2+1)
            io.imshow(im[k2])
        
        #time.sleep(1)
    if k >=1:
        break