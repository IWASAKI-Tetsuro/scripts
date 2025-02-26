#! /bin/python3
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

class Plotter:
    def __init__(self, position=111, xlabel="xlabel", ylabel="ylabel", xscale='linear', yscale='linear'):
        self.xlabel = xlabel
        self.ylabel = ylabel
        self.xscale = xscale
        self.yscale = yscale
        self.fig = plt.figure()
        self.ax_list = []  # 追加のAxesを管理するリスト
        self.fig, self.ax = plt.subplots()  # メインのAxes
        self.ax = self.add_subplot(position, xlabel=self.xlabel, ylabel=self.ylabel, xscale=self.xscale, yscale=self.yscale)

    def setup(self, ax):
        """ Axes の基本設定を適用 """
        ax.minorticks_on()
        ax.set_xlabel(self.xlabel, fontsize=15)
        ax.set_ylabel(self.ylabel, fontsize=15)
        ax.tick_params(axis='x', labelsize=15, direction='in', top=True, bottom=True, width=1.5, length=5.5)
        ax.tick_params(axis='y', labelsize=15, direction='in', left=True, right=True, width=1.5, length=5.5)
        ax.set_xscale(self.xscale)
        ax.set_yscale(self.yscale)
        ax.spines['top'].set_linewidth(1.8)
        ax.spines['bottom'].set_linewidth(1.8)
        ax.spines['right'].set_linewidth(1.8)
        ax.spines['left'].set_linewidth(1.8)
        ax.margins(0.05)

    def add_subplot(self, position=111, xlabel=None, ylabel=None, xscale=None, yscale=None):
        """ 新しいAxesを追加 """
        ax = self.fig.add_subplot(position)
        self.ax_list.append(ax)  # 新しいAxesをリストに追加
        xlabel = xlabel if xlabel else self.xlabel
        ylabel = ylabel if ylabel else self.ylabel
        xscale = xscale if xscale else self.xscale
        yscale = yscale if yscale else self.yscale
        ax.set_xlabel(xlabel, fontsize=15)
        ax.set_ylabel(ylabel, fontsize=15)
        ax.set_xscale(xscale)
        ax.set_yscale(yscale)
        self.setup(ax)  # 設定を適用
        return ax  # 追加したAxesを直接返す

    def plot_2D(self, x, y, label=None, style='b-', ax=None):
        """ 指定した Axes に 2D プロットを描画 """
        if ax is None:
            ax = self.ax  # デフォルトはメインのax
        ax.plot(x, y, style, label=label)

    def scatter_2D(self, x, y, label=None, style='b-', ax=None):
        """ 指定した Axes に散布図を描画 """
        if ax is None:
            ax = self.ax
        ax.scatter(x, y, label=label)

    def add_legend(self, ax=None):
        """ 指定した Axes に凡例を追加 """
        if ax is None:
            ax = self.ax
        ax.legend(fontsize=12)

    def enable_grid(self, ax=None, major=True, minor=True):
        """ 指定した Axes にグリッドを有効化 """
        if ax is None:
            ax = self.ax
        ax.grid(major, which='major', linestyle='--', linewidth=0.8, alpha=0.6)
        if minor:
            ax.grid(True, which='minor', linestyle=':', linewidth=0.5, alpha=0.4)

    def show(self):
        """ すべてのプロットを表示 """
        plt.show()

    def save(self, name):
        """ 透過画像を保存 """
        self.fig.patch.set_alpha(0)  # 保存時のみ透明化
        self.fig.savefig(name, bbox_inches='tight', pad_inches=0.05, transparent=True)

