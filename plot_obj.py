#! /bin/python3

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import sys
import argparse
from io import StringIO

def df_from_arg_or_stdin(args):
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
    df = df_from_arg_or_stdin(args)
    #plot_2data(df)
    #plot_3data(df)

if __name__ == "__main__":
    args = sys.argv
    main(args)
