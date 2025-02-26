from plotter import Plotter
import numpy as np
plotter = Plotter(figsize=(8,6))
ax = plotter.add_subplot(position=111, xlabel="X0", ylabel="Y0")

x_data = np.arange(0,6.28,0.1)
y_data0 = np.sin(x_data)
y_data1 = np.cos(x_data)

plotter.plot_2D(x_data, y_data0, label="Line0", style="b-", ax=ax, linewidth=5)
plotter.scatter_2D(x_data, y_data1, label="Line1", color="r", marker=".", ax=ax)
plotter.add_legend(ax=ax)
plotter.add_legend(ax=ax)

plotter.save("test.png", transparent=False)
