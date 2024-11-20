#! usr/bin/python3

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import sys
import argparse
from io import StringIO

def main(args):
    train_data = pd.read_csv('../train_data.csv')

    if sys.stdin.isatty() == 0:
        if (len(args) > 1):
            print("arguments and stdin are provided")
            sys.exit(1)
        else:
            csv_data = sys.stdin.read()
            df = pd.read_csv(StringIO(csv_data))
    else:
        if (len(args) > 2):
            print("Too many arguments")
            sys.exit(1)
        elif (len(args) == 1):
            print("No input file provided and no data in stdin.")
            sys.exit(1)
        else:
            csv_data = args[1]
            df = pd.read_csv(csv_data)

    # %%
    # fonts
    #plt.rcParams['font.family'] = 'Arial' # English
    #plt.rcParams['font.family'] = 'Yu Gothic' # Japanese
    plt.rcParams['mathtext.fontset'] = 'stix'
    plt.rcParams['font.size'] = 18 # overall
    plt.rcParams['xtick.labelsize'] = 15 # x axis
    plt.rcParams['ytick.labelsize'] = 15 # y axis
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
    plt.rcParams['axes.linewidth'] = 1.8 # axis line width
    # legend
    plt.rcParams['legend.fancybox'] = False
    plt.rcParams['legend.framealpha'] = 0
    plt.rcParams['legend.edgecolor'] = 'black'
    plt.rcParams['legend.handlelength'] = 1
    plt.rcParams['legend.labelspacing'] = 0.6
    plt.rcParams['legend.handletextpad'] = 0.8
    plt.rcParams['legend.markerscale'] = 1.2
    plt.rcParams['legend.loc'] = 'best'  # upper right lower left best


    pivot = df.pivot(index='b', columns='a', values='lap')
    x = pivot.columns.values
    y = pivot.index.values
    Z = pivot.values
    X, Y = np.meshgrid(x, y)

    fig = plt.figure()
    fig = plt.figure()
    aa = plt.pcolormesh(X, Y, Z, cmap='plasma')


    plt.savefig('heatmap.png', bbox_inches='tight', pad_inches=0.05)

if __name__ == "__main__":
    args = sys.argv
    main(args)
