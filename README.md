# Overview

This package provides some tools for working with specific mathematical models of control systems: [simple motions](https://github.com/shmax3/mmcs/tree/main/mmcs/simple_motions), [Dubins car](https://github.com/shmax3/mmcs/tree/main/mmcs/dubins). The package aims to calculate the following things:
1. The minimum time to reach a given state and the corresponding trajectory.
2. The minimum time to reach a prescribed time-varying state and the corresponding trajectory.
3. The reachable set and its boundary at a given time moment.
4. The distance from a given state to reachable set at a given time moment.


# Installing

You can install the latest version from GitHub:
```bash
$ pip install "git+https://github.com/shmax3/mmcs.git"
```


# Example
Plot the shortest path for Dubins car from the initial state $(x_0, y_0, \varphi_0) = (0, 0, \pi/2)$ to the destination point $(x_\mathrm{dest}, y_\mathrm{dest}) = (2, 1)$.
```python
from mmcs.dubins.path import markov_path
from matplotlib.pyplot import plot, scatter, legend, show


x_dest, y_dest = 2.0, 1.0
t, x, y, phi = markov_path(x=x_dest, y=y_dest)

plot(x, y, label='shortest path to point', color='black')
scatter([0.0], [0.0], label='starting point', color='black')
scatter([x_dest], [y_dest], label='destination point', color='red')
legend(); show()
```
