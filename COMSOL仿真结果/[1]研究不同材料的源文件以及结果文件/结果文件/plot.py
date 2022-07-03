# -*- coding: UTF-8 -*-
# @Author   : zhang_z
# @Time     : 2022-05-05

import pandas as pd
import matplotlib.pyplot as plt

# Set Times New Roman
plt.rc("font", family="Times New Roman")

data_dir = pd.read_excel(io="data1.xlsx", sheet_name=None)

# GET DATA
# ===============================================================
# Ag
# data-1
data1 = data_dir["1-1"]
x_data_1 = data1["Column1"]
y_data_1 = data1["Column2"]

# data-2
data2 = data_dir["1-2"]
x_data_2 = data2["Column1"]
y_data_2 = data2["Column2"]
# ===============================================================

# ===============================================================
# Au
# data-3
data1 = data_dir["1-3"]
x_data_3 = data1["Column1"]
y_data_3 = data1["Column2"]

# data-4
data2 = data_dir["1-4"]
x_data_4 = data2["Column1"]
y_data_4 = data2["Column2"]
# ===============================================================

# ===============================================================
# Al
# data-5
data1 = data_dir["1-5"]
x_data_5 = data1["Column1"]
y_data_5 = data1["Column2"]

# data-6
data2 = data_dir["1-6"]
x_data_6 = data2["Column1"]
y_data_6 = data2["Column2"]
# ===============================================================

# ===============================================================
# None
# data-7
data1 = data_dir["1-7"]
x_data_7 = data1["Column1"]
y_data_7 = data1["Column2"]

# data-8
data2 = data_dir["1-8"]
x_data_8 = data2["Column1"]
y_data_8 = data2["Column2"]
# ===============================================================

# ===============================================================
# ITO
# data-9
data1 = data_dir["1-9"]
x_data_9 = data1["Column1"]
y_data_9 = data1["Column2"]

# data-10
data2 = data_dir["1-10"]
x_data_10 = data2["Column1"]
y_data_10 = data2["Column2"]
# ===============================================================


plt.figure(figsize=(9, 8))
plt.subplot(3, 2, 1)

line1 = plt.plot(x_data_1, y_data_1, c="red", linewidth=4, linestyle="-")
line2 = plt.plot(x_data_2, y_data_2, c="blue", linewidth=4, linestyle="--")

# set axis
plt.xlim(20, 50)
plt.ylim(0, 1)


# ===============================================================
plt.subplot(3, 2, 2)


line3 = plt.plot(x_data_3, y_data_3, c="red", linewidth=4, linestyle="-")
line4 = plt.plot(x_data_4, y_data_4, c="blue", linewidth=4, linestyle="--")
plt.xlim(20, 50)
plt.ylim(0, 1)


# ===============================================================
plt.subplot(3, 2, 3)


line5 = plt.plot(x_data_5, y_data_5, c="red", linewidth=4, linestyle="-")
line6 = plt.plot(x_data_6, y_data_6, c="blue", linewidth=4, linestyle="--")
plt.xlim(20, 50)
plt.ylim(0, 1)


# ===============================================================
plt.subplot(3, 2, 4)


line7 = plt.plot(x_data_7, y_data_7, c="red", linewidth=4, linestyle="-")
line8 = plt.plot(x_data_8, y_data_8, c="blue", linewidth=4, linestyle="--")
plt.xlim(20, 50)
plt.ylim(0, 1)


# ===============================================================
plt.subplot(3, 2, 5)


line9 = plt.plot(x_data_9, y_data_9, c="red", linewidth=4, linestyle="-")
line10 = plt.plot(x_data_10, y_data_10, c="blue", linewidth=4, linestyle="--")
plt.xlim(20, 50)
plt.ylim(0, 1)

# ===============================================================
plt.subplot(3, 2, 6)





line11 = plt.plot(x_data_7, y_data_7, c="black", linewidth=4, linestyle="-")
line12 = plt.plot(x_data_8, y_data_8, c="black", linewidth=4, linestyle="--")
plt.xlim(20, 50)
plt.ylim(0, 1)

plt.show()

