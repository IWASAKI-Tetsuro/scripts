import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ptick

# fonts
#plt.rcParams['font.family'] = 'Arial' # Ubuntu22 server does't have Arial fonts. so this option is not activated
plt.rcParams['mathtext.fontset'] = 'stix'
plt.rcParams['font.size'] = 18
plt.rcParams['xtick.labelsize'] = 15
plt.rcParams['ytick.labelsize'] = 15
plt.rcParams['legend.fontsize'] = 15
plt.rcParams['svg.fonttype'] = 'none'

# axis
## major tick
plt.rcParams['xtick.direction'] = 'in'
plt.rcParams['ytick.direction'] = 'in'
plt.rcParams['xtick.top'] = True
plt.rcParams['xtick.bottom'] = True
plt.rcParams['ytick.left'] = True
plt.rcParams['ytick.right'] = True
plt.rcParams['xtick.major.size'] = 5.5
plt.rcParams['ytick.major.size'] = 5.5
plt.rcParams['xtick.major.width' ] = 1.5
plt.rcParams['ytick.major.width'] = 1.5

## minor tick
plt.rcParams['xtick.minor.visible'] = True
plt.rcParams['ytick.minor.visible'] = True
plt.rcParams['xtick.minor.size'] = 3.0
plt.rcParams['ytick.minor.size'] = 3.0
plt.rcParams['xtick.minor.width'] = 1.5
plt.rcParams['ytick.minor.width'] = 1.5
plt.rcParams['axes.linewidth'] = 1.8 

# legend
plt.rcParams['legend.fancybox'] = False
plt.rcParams['legend.framealpha'] = 0
plt.rcParams['legend.edgecolor'] = 'black'
plt.rcParams['legend.handlelength'] = 1
plt.rcParams['legend.labelspacing'] = 0.6
plt.rcParams['legend.handletextpad'] = 0.8
plt.rcParams['legend.markerscale'] = 1.2
plt.rcParams['legend.loc'] = 'best'  # upper right lower left

# 
plt.subplot().yaxis.set_major_formatter(ptick.ScalarFormatter(useMathText=True)) 
plt.subplot().yaxis.offsetText.set_fontsize(10)
plt.subplot().ticklabel_format(style='sci',axis='y',scilimits=(0,0))

# log scale
#plt.xscale('log')
#plt.yscale('log')
