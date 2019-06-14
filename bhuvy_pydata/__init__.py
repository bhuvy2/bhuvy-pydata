import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import os
import matplotlib.font_manager
from collections import OrderedDict

def find_custom_fonts():
    fonts = matplotlib.font_manager.findSystemFonts(fontpaths=None, fontext='ttf')
  
    ideal_fonts = [
      "merriweather",
      "roboto",
    ]

    ret = []

    for i_font in ideal_fonts:
        for font in fonts:
            lower_font = font.lower()
            if i_font in lower_font and ('light' not in lower_font) and ('bold' not in lower_font):
                fname = matplotlib.font_manager.FontProperties(fname=font).get_name()  
                ret.append(fname)

    dups_removed = list(OrderedDict.fromkeys(ret))
    return ', '.join(dups_removed + ['sans-serif'])

def register_style():
    '''
    Write all goose-styles to the relevant matplotlib configuration directory.
    '''

    import os
    import matplotlib
  
    styles = dict()
  
    styles['bhuvy.mplstyle'] = '''

# Main Grids  
figure.facecolor: F0F8FF

patch.antialiased: True

# Lines
lines.linewidth: 2.0
lines.solid_capstyle: butt

# Axes
axes.titlesize: 16
axes.labelsize: 12
axes.labelcolor: 657b83
axes.facecolor: 9EBBD4
axes.edgecolor: 00000
axes.axisbelow: True
axes.prop_cycle: cycler('color', ['268BD2', '2AA198', '859900', 'B58900', 'CB4B16', 'DC322F', 'D33682', '6C71C4'])
axes.spines.top: False
axes.spines.right: False

axes.grid: True
grid.color: fdf6e3

grid.linestyle: -
grid.linewidth: 1

xtick.color: 000000
xtick.direction: out

ytick.color: 000000
ytick.direction: out

# Font

font.family: sans-serif
font.sans-serif: {}
'''.format(find_custom_fonts())

    dirname = os.path.abspath(os.path.join(matplotlib.get_configdir(), 'stylelib'))
  
    if not os.path.isdir(dirname): os.makedirs(dirname)
  
    for fname, style in styles.items():
        open(os.path.join(dirname, fname),'w').write(style)


