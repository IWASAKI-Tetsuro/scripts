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
        # Figureのみ先に生成。Axesはまだ作らない
        self.fig = plt.figure(figsize=figsize, dpi=dpi)
        self.ax_list = []  # Axesをまとめて管理するリスト

        # ユーザが何も指定しない場合のラベル/スケール設定
        self.xlabel = xlabel
        self.ylabel = ylabel
        self.xscale = xscale
        self.yscale = yscale

    def setup(self, ax):
        """
        描画スタイルの設定のみを行う。軸ラベル・スケールは別メソッドで設定
        """
        ax.minorticks_on()
        ax.tick_params(axis='x', labelsize=15, direction='in',
                       top=True, bottom=True, width=1.5, length=5.5)
        ax.tick_params(axis='y', labelsize=15, direction='in',
                       left=True, right=True, width=1.5, length=5.5)
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
        """
        新しいAxesを追加して返す。
        例: add_subplot(221) -> 2行×2列レイアウトの1番目
            add_subplot(2,2,1) というタプル形式でも指定可。
        """
        ax = self.fig.add_subplot(position)

        # ラベル・スケールを個別指定できる
        xlabel = xlabel if xlabel else self.xlabel
        ylabel = ylabel if ylabel else self.ylabel
        xscale = xscale if xscale else self.xscale
        yscale = yscale if yscale else self.yscale

        # 軸ラベルやスケールを設定
        ax.set_xlabel(xlabel, fontsize=15)
        ax.set_ylabel(ylabel, fontsize=15)
        ax.set_xscale(xscale)
        ax.set_yscale(yscale)

        # 見た目調整
        self.setup(ax)

        self.ax_list.append(ax)
        return ax

    def plot_2D(self, x, y, label=None, style='b-', linewidth=2, ax=None,
                xlim=None, ylim=None, margin=None):
        """
        2Dラインプロット

        Parameters
        ----------
        x, y : array-like
            プロットするデータ
        label : str or None
            凡例表示用のラベル (デフォルト: None)
        style : str
            matplotlibのラインスタイル指定 (例: 'r--', 'g:', etc.)
        ax : matplotlib.axes.Axes or None
            描画先のAxes。Noneなら最後に追加したAxesを使う
        xlim : tuple or list or None
            X軸の表示範囲 (min, max)
        ylim : tuple or list or None
            Y軸の表示範囲 (min, max)
        margin : float or None
            軸方向の空白余白 (0.05 なら5%余白)。
            xlim, ylim を指定すると通常は margin が無視される点に注意。
        """
        if ax is None:
            if not self.ax_list:

                raise RuntimeError("No Axes available. Call add_subplot() first.")
            ax = self.ax_list[-1]

        # プロット描画
        ax.plot(x, y, style, label=label, linewidth=linewidth)

        # xlim, ylim が与えられた場合は適用
        if xlim is not None:
            ax.set_xlim(xlim)
        if ylim is not None:
            ax.set_ylim(ylim)

        # margin が指定されていれば設定
        # ただし xlim/ylim が既に指定されていると margin の効果は薄い
        if margin is not None:
            ax.margins(margin)

    def scatter_2D(self, x, y, label=None, color='b', marker='o', ax=None):
        """
        2D散布図
        """
        if ax is None:
            if not self.ax_list:
                raise RuntimeError("No Axes available. Call add_subplot() first.")
            ax = self.ax_list[-1]
        ax.scatter(x, y, label=label, c=color, marker=marker)

    def add_legend(self, ax=None, fontsize=12, facecolor='white', framealpha=1.0):
        """
        Axesに凡例を追加し、背景色・透過度を調整可能にする
        """
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
        """
        Axesに格子線を追加
        major, minorのどちらの目盛りにグリッドを適用するか
        """
        if ax is None:
            if not self.ax_list:
                raise RuntimeError("No Axes available. Call add_subplot() first.")
            ax = self.ax_list[-1]
        ax.grid(major, which='major', linestyle='--', linewidth=0.8, alpha=0.6)
        if minor:
            ax.grid(True, which='minor', linestyle=':', linewidth=0.5, alpha=0.4)

    def show(self, only_self=False, block=True):
        """
        プロット表示
        only_self=True: このインスタンスのFigure以外を閉じてから表示
        """
        if only_self:
            for fignum in plt.get_fignums():
                fig_candidate = plt.figure(fignum)
                if fig_candidate != self.fig:
                    plt.close(fig_candidate)
        plt.show(block=block)

    def save(self, filename, transparent=True):
        """
        画像をファイルとして保存
        transparent=Trueのとき背景を透明化
        """
        if transparent:
            self.fig.patch.set_alpha(0)
        self.fig.savefig(filename, bbox_inches='tight', pad_inches=0.05, transparent=transparent)

