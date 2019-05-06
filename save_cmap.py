# -*- coding: utf-8 -*-
"""
Created on Mon May  6 16:00:00 2019

@author: Shengjie Liu, liushengjie0756@gmail.com
"""

from matplotlib.pyplot import plt
import numpy as np

def save_cmap(img, cmap, fname):
   
    sizes = np.shape(img)
    height = float(sizes[0])
    width = float(sizes[1])
     
    fig = plt.figure()
    fig.set_size_inches(width/height, 1, forward=False)
    ax = plt.Axes(fig, [0., 0., 1., 1.])
    ax.set_axis_off()
    fig.add_axes(ax)
 
    ax.imshow(img, cmap=cmap)
    plt.savefig(fname, dpi = height) 
    plt.close()