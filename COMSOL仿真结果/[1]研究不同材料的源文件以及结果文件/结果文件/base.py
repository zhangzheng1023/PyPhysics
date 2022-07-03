# -*- coding: UTF-8 -*-
# @Author   : zhang_z
# @Time     : 2022-06-02

import matplotlib.pyplot as plt

# plot in axes
fig, ax = plt.subplots()
fig2, axs = plt.subplots(2, 2)
ax.plot([1, 2, 3], [3, 4, 3])
fig2.show()
plt.show()
