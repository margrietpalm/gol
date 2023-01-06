import numpy as np
from PIL import Image

def draw_grid(grid, num, scale=1):
    print(grid.shape)
    im = Image.fromarray(255*(1-grid.astype(np.uint8)))
    im = im.resize((scale * grid.shape[0], scale * grid.shape[0]), Image.Resampling.LANCZOS)
    print(im.size)
    im.save(f'/home/mpalm/temp/step_{num:03d}.png')