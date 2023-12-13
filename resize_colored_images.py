# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 15:20:42 2023

@author: Amin
"""

from skimage.io import imread, imsave, imshow
import numpy as np
from tqdm import tqdm


colored_image = imread('.\\grass.jpg')
print(colored_image.shape)
print(colored_image.dtype)
imshow(colored_image)

rate = 4

c, r, d = colored_image.shape
new_image = np.ones((c * rate, r * rate, d))
print(new_image.shape)
print(new_image.dtype)
new_image *= 128
new_image = new_image.astype('uint8')
imshow(new_image)


for rr in tqdm(range(r)):
    for cc in range(c):
        for idxC in range(rate):
            for idxR in range(rate):
                for idxD in range(d):
                    new_image[cc*rate+idxC, rr*rate+idxR, idxD] = colored_image[cc, rr, idxD]


imshow(new_image)
imsave('.\\grass2.jpg', new_image)
