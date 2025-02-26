# サンプルデータ
from plotter import Plotter
import numpy as np

categories = ['Apple', 'Banana', 'Cherry']
y1 = [3, 2, 5]
y2 = [2, 3, 1]
y3 = [1, 2, 2]

plotter = Plotter(xlabel="Fruits", ylabel="Quantity")
ax = plotter.add_subplot()

# x軸用に [0, 1, 2] のような数値インデックスを作る
x_index = range(len(categories))

# 積み上げ棒グラフを描画 (x_indexを使う)
plotter.stacked_bar(
    x=x_index,
    y_stacks=[y1, y2, y3],
    labels=["Series1", "Series2", "Series3"],
    colors=["red", "green", "blue"],
    ax=ax
)

# 目盛位置・ラベルを設定
ax.set_xticks(x_index)
ax.set_xticklabels(categories)

plotter.add_legend(ax)
plotter.enable_grid(ax)

plotter.save("test.png", transparent=0)

