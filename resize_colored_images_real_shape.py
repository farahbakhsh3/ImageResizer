# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 15:20:42 2023

@author: Amin
"""

from skimage.io import imread, imsave, imshow
import numpy as np
from tqdm import tqdm
import matplotlib.pyplot as plt


path = 'D:\\My Prog\\Class Python\\Resize\\'
filename = 'gl'
ext = 'jpg'

original_image = imread(f'{path}{filename}.{ext}')
rO, cO, dO = original_image.shape
print(f'Original_image ::  {original_image.shape}')
print(f'Original_image ::  {original_image.dtype}')

shape = {'Row': 2000, 'Col': 2500}
rate = {'R': shape['Row']/rO, 'C': shape['Col']/cO}
print(f'Shape ::  {shape}')
print(f'Rate ::  {rate}')

new_image = np.zeros((int(rO * rate['R']), int(cO * rate['C']), dO))
new_image = new_image.astype('uint8')
rN, cN, dN = new_image.shape
print(f'New_image ::  {new_image.shape}')
print(f'New_image ::  {new_image.dtype}')

for idxR in tqdm(range(rN)):
    for idxC in range(cN):
        for idxD in range(dN):
            new_image[idxR, idxC, idxD] = original_image[int(
                idxR/rate['R']), int(idxC/rate['C']), idxD]

imsave(f'{path}{filename}_New.{ext}', new_image)

fig, axs = plt.subplots(1, 2, sharey='all', sharex='all')
axs[0].imshow(original_image)
axs[1].imshow(new_image)
fig.savefig(f'{path}{filename}_Plot.{ext}')
