# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 15:20:42 2023

@author: Amin
"""

from skimage.io import imread, imsave, imshow
import numpy as np
from tqdm import tqdm


original_image = imread('.\\01.jpg')
rO, cO, dO = original_image.shape
print(f'Original_image ::  {original_image.shape}')
print(f'Original_image ::  {original_image.dtype}')
imshow(original_image)

rate = 0.2
print(f'Rate ::  {rate}')

new_image = np.zeros((int(rO * rate), int(cO * rate), dO))
new_image = new_image.astype('uint8')
rN, cN, dN = new_image.shape
print(f'New_image ::  {new_image.shape}')
print(f'New_image ::  {new_image.dtype}')
imshow(new_image)

for idxR in tqdm(range(rN)):
    for idxC in range(cN):
        for idxD in range(dN):
            new_image[idxR, idxC, idxD] = original_image[int(idxR/rate), int(idxC/rate), idxD]

imshow(new_image)
imsave('.\\02.jpg', new_image)
