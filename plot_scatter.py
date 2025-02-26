# サンプルデータ
from plotter import Plotter
import numpy as np
x = np.arange(0,6.28,0.1)
y1 = np.sin(x)
y2 = np.cos(x)

plotter = Plotter(figsize=(16,6))
ax  = plotter.add_subplot(position=121,xlabel="X0", ylabel="Y0")
ax1 = plotter.add_subplot(position=122,xlabel="X0", ylabel="Y0")
plotter.plot_2D(x,y1, ax=ax,label="aaa")
plotter.scatter_2D(x,y2, ax=ax1, label="bbb")
plotter.enable_grid(ax=ax)
plotter.enable_grid(ax=ax1)
plotter.add_legend(ax=ax)
plotter.add_legend(ax=ax1)

plotter.save("test.png", transparent=0)

