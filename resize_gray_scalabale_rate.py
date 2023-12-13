# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 15:20:42 2023

@author: Amin
"""

from skimage.io import imread, imsave, imshow
from skimage.color import rgb2gray
import numpy as np


colored_image = imread('.\\01.jpg')
print(colored_image.shape)
print(colored_image.dtype)
imshow(colored_image)

grayed_image = rgb2gray(colored_image)
print(grayed_image.shape)
print(grayed_image.dtype)
grayed_image *= 255 
grayed_image = grayed_image.astype('uint8')
print(grayed_image.shape)
print(grayed_image.dtype)
imshow(grayed_image)

rate = 10
c , r = grayed_image.shape
new_image = np.ones((c * rate, r * rate))
print(new_image.shape)
print(new_image.dtype)
new_image *= 128
new_image = new_image.astype('uint8')
imshow(new_image)


for rr in range(r):
    for cc in range(c):
        for idxC in range(rate):
            for idxR in range(rate):
                new_image[cc*rate+idxC, rr*rate+idxR] = grayed_image[cc, rr]


imshow(new_image)
imsave('.\\01_10.jpg', new_image)
