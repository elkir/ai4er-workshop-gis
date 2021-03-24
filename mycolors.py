#mycolors.py

import matplotlib.pyplot as plt
import matplotlib.colors
from matplotlib import cm




### Set Colormaps
def _get_cmap_chm():
    cmap_CHM = plt.cm.get_cmap('viridis',64)
    norm = matplotlib.colors.Normalize(0,70)
    color_mapping_CHM = matplotlib.cm.ScalarMappable(norm=norm,cmap=cmap_CHM)
    return color_mapping_CHM

def _get_cmap_diff():
    top = cm.get_cmap('Greens_r', 128)
    bottom = cm.get_cmap('RdPu', 128)
    newcolors = np.vstack((top(np.linspace(0, 1, 128)),
                           bottom(np.linspace(0, 1, 128))))
    cmap_diff = matplotlib.colors.ListedColormap(newcolors, name='chm_diff')
    norm = matplotlib.colors.TwoSlopeNorm(0,-50,+50)
    color_mapping_diff = matplotlib.cm.ScalarMappable(norm=norm, cmap=cmap_diff)
    return color_mapping_diff


cmap_diff = _get_cmap_diff()
cmap_chm = _get_cmap_chm()



txt_sty ={
    "PURPLE" : '\033[95m',
    "CYAN" : '\033[96m',
    "DARKCYAN" : '\033[36m',
    "BLUE" : '\033[94m',
    "GREEN" : '\033[92m',
    "YELLOW" : '\033[93m',
    "RED" : '\033[91m',
    "BOLD" : '\033[1m',
    "UNDERLINE" : '\033[4m',
    "END" : '\033[0m'
}





def get_rand_cmap(nlabels, type='bright', first_color_black=False, last_color_black=False, verbose=False, f=0.95):
    """
    Creates a random colormap to be used together with matplotlib. Useful for segmentation tasks
    :param nlabels: Number of labels (size of colormap)
    :param type: 'bright' for strong colors, 'soft' for pastel colors
    :param first_color_black: Option to use first color as black, True or False
    :param last_color_black: Option to use last color as black, True or False
    :param verbose: Prints the number of labels and shows the colormap. True or False
    :return: colormap for matplotlib
    """
    from matplotlib.colors import LinearSegmentedColormap
    import colorsys
    import numpy as np


    if type not in ('bright', 'soft'):
        print ('Please choose "bright" or "soft" for type')
        return

    if verbose:
        print('Number of labels: ' + str(nlabels))

    # Generate color map for bright colors, based on hsv
    if type == 'bright':
        randHSVcolors = [(np.random.uniform(low=0.0, high=1),
                          np.random.uniform(low=0.2, high=1),
                          np.random.uniform(low=0.9, high=1)) for i in range(nlabels)]

        # Convert HSV list to RGB
        randRGBcolors = []
        for HSVcolor in randHSVcolors:
            randRGBcolors.append(colorsys.hsv_to_rgb(HSVcolor[0], HSVcolor[1], HSVcolor[2]))

        if first_color_black:
            randRGBcolors[0] = [0, 0, 0]
        if last_color_black:

            randRGBcolors[-1] = [0, 0, 0]

        random_colormap = LinearSegmentedColormap.from_list('new_map', randRGBcolors, N=nlabels)

    # Generate soft pastel colors, by limiting the RGB spectrum
    if type == 'soft':
        low = 0.6
        high = f
        randRGBcolors = [(np.random.uniform(low=low, high=high),
                          np.random.uniform(low=low, high=high),
                          np.random.uniform(low=low, high=high)) for i in range(nlabels)]

        if first_color_black:
            randRGBcolors[0] = [0, 0, 0]

        if last_color_black:
            randRGBcolors[-1] = [0, 0, 0]
        random_colormap = LinearSegmentedColormap.from_list('new_map', randRGBcolors, N=nlabels)

    # Display colorbar
    if verbose:
        from matplotlib import colors, colorbar
        from matplotlib import pyplot as plt
        fig, ax = plt.subplots(1, 1, figsize=(15, 0.5))

        bounds = np.linspace(0, nlabels, nlabels + 1)
        norm = colors.BoundaryNorm(bounds, nlabels)

        cb = colorbar.ColorbarBase(ax, cmap=random_colormap, norm=norm, spacing='proportional', ticks=None,
                                   boundaries=bounds, format='%1i', orientation=u'horizontal')

    return random_colormap