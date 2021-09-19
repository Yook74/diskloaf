import os
from math import floor

from progressbar import Bar, AdaptiveETA, progressbar

NUM_CHUNKS = 4096
FILENAME = 'loaf'
BYTE_TO_WRITE = b'\0'

free_space_info = os.statvfs('.')
free_space_gb = (free_space_info.f_bsize * free_space_info.f_bavail) / 2**30
chunk_size_gb = free_space_gb / NUM_CHUNKS

print(f'{free_space_gb:.2} GB free')
print('Mixing the dough')

loaf = open(FILENAME, 'wb')
slice = BYTE_TO_WRITE * floor(chunk_size_gb * 2**30)

print('Baking the loaf')
for chunk_num in progressbar(range(NUM_CHUNKS), widgets=[Bar(), AdaptiveETA()]):
    loaf.write(slice)

loaf.close()

print('Taking it out of the oven')
os.remove(FILENAME)
