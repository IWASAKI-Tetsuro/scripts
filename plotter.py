#! /bin/python3

import sys
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def DataFrameFromStdinOrArgs(file=None, delimiter=',', index=True):
    ignore_index = not index

    if(file is not None):
        df = pd.read(file, delimiter=delimiter, ignore_index=ignore_index)
    else:
    return df


def plot_2data(df):
    x = df.iloc[:,0].values
    y = df.iloc[:,1].values

    fig, ax = plt.subplots()
    ax.plot(x, y, label='hoge')

    #ax.set_xlim(0, 1)
    #ax.set_ylim(0, 1)

    ax.set_xlabel('x_label', fontsize=15)
    ax.set_ylabel('y_label', fontsize=15)

    #ax.set_xscale('log')
    #ax.set_yscale('log')

    ax.tick_params(axis='x', labelsize=15, direction='in', top=True, bottom=True, width=1.5, length=5.5)
    ax.tick_params(axis='y', labelsize=15, direction='in', left=True, right=True, width=1.5, length=5.5)

    ax.minorticks_on()
    ax.tick_params(axis='x', which='minor', labelsize=15, direction='in', top=True, bottom=True, width=1.5, length=3)
    ax.tick_params(axis='y', which='minor', labelsize=15, direction='in', left=True, right=True, width=1.5, length=3)

    ax.spines['top'].set_linewidth(1.8)
    ax.spines['bottom'].set_linewidth(1.8)
    ax.spines['right'].set_linewidth(1.8)
    ax.spines['left'].set_linewidth(1.8)

    legend = ax.legend(fontsize=15, fancybox=False, framealpha=0, edgecolor='black',
                        handlelength=1, labelspacing=0.6, handletextpad=0.8, markerscale=1.2, loc='best')

    plt.savefig('output_2data.svg', bbox_inches='tight', pad_inches=0.05)

def plot_3data(df):
    keys = df.iloc[:,0].values
    keys = np.unique(keys)

    fig, ax = plt.subplots()

    for key in keys:
        x_key = df[df.iloc[:,0] == key].iloc[:,1]
        y_key = df[df.iloc[:,0] == key].iloc[:,2]
        ax.plot(x_key, y_key)

    #ax.set_xlim(0, 1)
    #ax.set_ylim(0, 1)

    ax.set_xlabel('x_label', fontsize=15)
    ax.set_ylabel('y_label', fontsize=15)

    #ax.set_xscale('log')
    #ax.set_yscale('log')

    ax.tick_params(axis='x', labelsize=15, direction='in', top=True, bottom=True, width=1.5, length=5.5)
    ax.tick_params(axis='y', labelsize=15, direction='in', left=True, right=True, width=1.5, length=5.5)

    ax.minorticks_on()
    ax.tick_params(axis='x', which='minor', labelsize=15, direction='in', top=True, bottom=True, width=1.5, length=3)
    ax.tick_params(axis='y', which='minor', labelsize=15, direction='in', left=True, right=True, width=1.5, length=3)

    ax.spines['top'].set_linewidth(1.8)
    ax.spines['bottom'].set_linewidth(1.8)
    ax.spines['right'].set_linewidth(1.8)
    ax.spines['left'].set_linewidth(1.8)

    legend = ax.legend(fontsize=15, fancybox=False, framealpha=0, edgecolor='black',
                        handlelength=1, labelspacing=0.6, handletextpad=0.8, markerscale=1.2, loc='best')

    plt.savefig('output_3data.svg', bbox_inches='tight', pad_inches=0.05)

def main(args):
    args = sys.argv
    df = DataFrameFromStdinOrArgs(file=None, delimiter=',', index=True)
    #plot_2data(df)
    #plot_3data(df)

if __name__ == "__main__":
    main()

    
