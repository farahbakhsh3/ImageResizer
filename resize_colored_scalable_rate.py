# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 15:20:42 2023

@author: Amin
"""

from skimage.io import imread, imsave, imshow
from skimage.color import rgb2gray
import numpy as np
from tqdm import tqdm

colored_image = imread('.\\gl.jpg')
print(colored_image.shape)
print(colored_image.dtype)
imshow(colored_image)


rate = 2
r, c, d = colored_image.shape
new_image = np.zeros((r * rate, c * rate, d))
print(new_image.shape)
print(new_image.dtype)
new_image = new_image.astype('uint8')
imshow(new_image)

for rr in tqdm(range(r)):
    for cc in range(c):
        for win_rr in range(rate):
            for win_cc in range(rate):
                for dd in range(d):
                    new_image[rate*rr+win_rr, rate*cc+win_cc, dd] = colored_image[rr, cc, dd]


imshow(new_image)
imsave('.\\gl_2.jpg', new_image)
