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


rate = 5
r, c, d = colored_image.shape
new_image = np.zeros((r * rate, c * rate, d))
print(new_image.shape)
print(new_image.dtype)
new_image = new_image.astype('uint8')
imshow(new_image)

for rr in range(r):
    for cc in range(c):
        for dd in range(d):
            new_image[rate*rr, rate*cc, dd] = colored_image[rr, cc, dd]
            new_image[rate*rr, rate*cc+1, dd] = colored_image[rr, cc, dd]
            new_image[rate*rr+1, rate*cc, dd] = colored_image[rr, cc, dd]
            new_image[rate*rr+1, rate*cc+1, dd] = colored_image[rr, cc, dd]

imshow(new_image)
imsave('.\\01_2.jpg', new_image)
