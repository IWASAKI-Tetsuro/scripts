import matplotlib as mpl
import matplotlib.pyplot as plt

mpl.rcParams['font.family'] = 'DejaVu Sans'
mpl.rcParams['mathtext.fontset'] = 'stix'
mpl.rcParams['font.size'] = 16  # 適宜変更

class Plotter:
    def __init__(
        self,
        figsize=(8, 6),
        dpi=100,
        xlabel="xlabel",
        ylabel="ylabel",
        xscale='linear',
        yscale='linear'
    ):
        """
        figsize: tuple (width, height) in inches
        dpi: resolution
        xlabel, ylabel: デフォルト軸ラベル
        xscale, yscale: デフォルトスケール
        """
        self.fig = plt.figure(figsize=figsize, dpi=dpi)
        self.ax_list = []

        self.xlabel = xlabel
        self.ylabel = ylabel
        self.xscale = xscale
        self.yscale = yscale

    def setup(self, ax):
        ax.minorticks_on()
        ax.tick_params(axis='x', labelsize=15, direction='in',
                       top=True, bottom=True, width=1.5, length=5.5)
        ax.tick_params(axis='y', labelsize=15, direction='in',
                       left=True, right=True, width=1.5, length=5.5)
        ax.tick_params(axis='x', which='minor', direction='in',
                       top=True, bottom=True, width=1.0, length=3.5)
        ax.tick_params(axis='y', which='minor', direction='in',
                       left=True, right=True, width=1.0, length=3.5)
        ax.spines['top'].set_linewidth(1.8)
        ax.spines['bottom'].set_linewidth(1.8)
        ax.spines['right'].set_linewidth(1.8)
        ax.spines['left'].set_linewidth(1.8)
        ax.margins(0.03)

    def add_subplot(self, position=111, xlabel=None, ylabel=None,
                    xscale=None, yscale=None):
        ax = self.fig.add_subplot(position)

        xlabel = xlabel if xlabel else self.xlabel
        ylabel = ylabel if ylabel else self.ylabel
        xscale = xscale if xscale else self.xscale
        yscale = yscale if yscale else self.yscale

        ax.set_xlabel(xlabel, fontsize=20)
        ax.set_ylabel(ylabel, fontsize=20)
        ax.set_xscale(xscale)
        ax.set_yscale(yscale)

        self.setup(ax)
        self.ax_list.append(ax)
        return ax

    def plot_2D(self, x, y, label=None, style='b-', linewidth=2, ax=None,
                xlim=None, ylim=None, margin=None):
        if ax is None:
            if not self.ax_list:
                raise RuntimeError("No Axes available. Call add_subplot() first.")
            ax = self.ax_list[-1]

        ax.plot(x, y, style, label=label, linewidth=linewidth)

        if xlim is not None:
            ax.set_xlim(xlim)
        if ylim is not None:
            ax.set_ylim(ylim)
        if margin is not None:
            ax.margins(margin)

    def scatter_2D(self, x, y, label=None, color='b', marker='o', ax=None):
        if ax is None:
            if not self.ax_list:
                raise RuntimeError("No Axes available. Call add_subplot() first.")
            ax = self.ax_list[-1]
        ax.scatter(x, y, label=label, c=color, marker=marker)

    def stacked_bar(
        self,
        x,
        y_stacks,
        labels=None,
        colors=None,
        width=0.6,
        ax=None,
        xlim=None,
        ylim=None,
        margin=None
    ):
        """
        積み上げ棒グラフを描画するメソッド

        Parameters
        ----------
        x : array-like
            棒グラフのx軸位置
        y_stacks : list of array-like
            積み上げる各系列のyデータをまとめたリスト
            例えば3つ系列を積み上げる場合 [y1, y2, y3] のように渡す
        labels : list of str or None
            それぞれの系列に対応する凡例用ラベル
        colors : list of str or None
            それぞれの系列に対応する色指定
        width : float
            棒グラフの幅
        ax : matplotlib.axes.Axes or None
            描画先のAxes。Noneなら最後に追加したAxesを利用
        xlim, ylim : tuple or list or None
            x軸, y軸の表示範囲
        margin : float or None
            軸方向の空白余白 (0.05 なら5%余白)
        """
        if ax is None:
            if not self.ax_list:
                raise RuntimeError("No Axes available. Call add_subplot() first.")
            ax = self.ax_list[-1]
        # 系列数
        n_stacks = len(y_stacks)
        if labels is None:
            labels = [None] * n_stacks
        if colors is None:
            colors = [None] * n_stacks

        bottom = None  # 初回はNoneとして bar() に渡し、以降は積み上げを反映
        for i in range(n_stacks):
            ax.bar(
                x,
                y_stacks[i],
                width=width,
                label=labels[i],
                color=colors[i],
                bottom=bottom
            )
            # 次系列のために bottom を更新
            if bottom is None:
                bottom = y_stacks[i]
            else:
                bottom = [b + y for b, y in zip(bottom, y_stacks[i])]

        if xlim is not None:
            ax.set_xlim(xlim)
        if ylim is not None:
            ax.set_ylim(ylim)
        if margin is not None:
            ax.margins(margin)

    def add_legend(self, ax=None, fontsize=14, facecolor='white', framealpha=1.0):
        if ax is None:
            if not self.ax_list:
                raise RuntimeError("No Axes available. Call add_subplot() first.")
            ax = self.ax_list[-1]

        legend_obj = ax.legend(fontsize=fontsize)
        if legend_obj is not None:
            frame = legend_obj.get_frame()
            frame.set_facecolor(facecolor)
            frame.set_alpha(framealpha)

    def enable_grid(self, ax=None, major=True, minor=True):
        if ax is None:
            if not self.ax_list:
                raise RuntimeError("No Axes available. Call add_subplot() first.")
            ax = self.ax_list[-1]
        ax.grid(major, which='major', linestyle='--', linewidth=0.8, alpha=0.6)
        if minor:
            ax.grid(True, which='minor', linestyle=':', linewidth=0.5, alpha=0.4)

    def show(self, only_self=False, block=True):
        if only_self:
            for fignum in plt.get_fignums():
                fig_candidate = plt.figure(fignum)
                if fig_candidate != self.fig:
                    plt.close(fig_candidate)
        plt.show(block=block)

    def save(self, filename, transparent=True):
        if transparent:
            self.fig.patch.set_alpha(0)
        self.fig.savefig(filename, bbox_inches='tight', pad_inches=0.05, transparent=transparent)

