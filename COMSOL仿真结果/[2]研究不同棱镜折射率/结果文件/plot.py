# -*- coding: UTF-8 -*-
# @Author   : zhang_z
# @Time     : 2022-05-12

import pandas as pd
import matplotlib.pyplot as plt

# 角度转换部分
import math

N_air = 1.00029
alpha = 0


# 如果存在倾角度 实际的Theta1 可以给一个减去的alpha
def convert_theta2(theta1, n_prism):
    k = (math.sin(math.radians(theta1-alpha))*n_prism)/N_air
    theta2 = math.degrees(math.asin(k))
    return theta2

convert_theta2(27, 1.75)


def getMax(data1, data2):
    end_data = data2[1000]
    top_data = 0
    data1_max = 0
    data2_max = 0
    for x in range(601):
        if x == 0 or x == 600:
            continue
        if data1[x] > data1[x-1] and data1[x] > data1[x+1]:
            if x_data[x] > 33:
                data1_max = x_data[x]

        if data2[x] > data2[x - 1] and data2[x] > data2[x + 1]:
            if x_data[x] > 33:
                data2_max = x_data[x]
                top_data = data2[x]
    change_val = top_data - end_data
    y11.append(change_val)
    rate = change_val/top_data
    print("Changing val = {}".format(rate))
    # print("data1_max = {}, data2_max = {}".format(data1_max, data2_max))
    print("the shifting angle = {}".format(data2_max - data1_max))
    return data2_max - data1_max



# Set Times New Roman
plt.rc("font", family="Times New Roman")

data_dir = pd.read_excel(io="data2.xlsx", sheet_name=None)

# GET DATA
# ===============================================================
# N = 1.33
# data-1
data1 = data_dir["2-1"]
x_data_1 = data1["Column1"]
y_data_1 = data1["Column2"]

# data-2
data2 = data_dir["2-7"]
x_data_2 = data2["Column1"]
y_data_2 = data2["Column2"]
# ===============================================================

# ===============================================================
# N = 1.45
# data-3
data1 = data_dir["2-2"]
x_data_3 = data1["Column1"]
y_data_3 = data1["Column2"]

# data-4
data2 = data_dir["2-8"]
x_data_4 = data2["Column1"]
y_data_4 = data2["Column2"]
# ===============================================================

# ===============================================================
# N = 1.57
# data-5
data1 = data_dir["2-3"]
x_data_5 = data1["Column1"]
y_data_5 = data1["Column2"]

# data-6
data2 = data_dir["2-9"]
x_data_6 = data2["Column1"]
y_data_6 = data2["Column2"]
# ===============================================================

# ===============================================================
# N = 1.68
# data-7
data1 = data_dir["2-4"]
x_data_7 = data1["Column1"]
y_data_7 = data1["Column2"]

# data-8
data2 = data_dir["2-10"]
x_data_8 = data2["Column1"]
y_data_8 = data2["Column2"]
# ===============================================================

# ===============================================================
# N = 1.75
# data-9
data1 = data_dir["2-5"]
x_data_9 = data1["Column1"]
y_data_9 = data1["Column2"]

# data-10
data2 = data_dir["2-11"]
x_data_10 = data2["Column1"]
y_data_10 = data2["Column2"]
# ===============================================================

# ===============================================================
# N = 1.68
# data-11
data1 = data_dir["2-6"]
x_data_11 = data1["Column1"]
y_data_11 = data1["Column2"]

# data-12
data2 = data_dir["2-12"]
x_data_12 = data2["Column1"]
y_data_12 = data2["Column2"]
# ===============================================================

















figure1 = plt.figure()  # create an empty figure
plt.figure(figsize=(10, 8))
# ===============================================================
plt.subplot(2, 3, 1)
plt.xlabel('Incident Angle(deg)')
plt.ylabel('K-Conversion Efficiency')

line1 = plt.plot(x_data_1, y_data_1, c="red", linewidth=3, linestyle=":", label="N = 1.33 0%")
line2 = plt.plot(x_data_2, y_data_2, c="blue", linewidth=3, linestyle="-", label="N = 1.33 4.6%")

# set axis
plt.xlim(25, 70)
plt.ylim(0, 1)

plt.legend(loc="upper left")
# ===============================================================

# ===============================================================
plt.subplot(2, 3, 2)
plt.xlabel('Incident Angle(deg)')
plt.ylabel('K-Conversion Efficiency')

line3 = plt.plot(x_data_3, y_data_3, c="red", linewidth=3, linestyle=":", label="N = 1.45 0%")
line4 = plt.plot(x_data_4, y_data_4, c="blue", linewidth=3, linestyle="-", label="N = 1.45 4.6%")

# set axis
plt.xlim(25, 70)
plt.ylim(0, 1)

plt.legend(loc="lower right")
# ===============================================================

# ===============================================================
plt.subplot(2, 3, 3)
plt.xlabel('Incident Angle(deg)')
plt.ylabel('K-Conversion Efficiency')

line5 = plt.plot(x_data_5, y_data_5, c="red", linewidth=3, linestyle=":", label="N = 1.57 0%")
line6 = plt.plot(x_data_6, y_data_6, c="blue", linewidth=3, linestyle="-", label="N = 1.57 4.6%")

# set axis
plt.xlim(25, 70)
plt.ylim(0, 1)

plt.legend(loc="lower right")
# ===============================================================

# ===============================================================
plt.subplot(2, 3, 4)
plt.xlabel('Incident Angle(deg)')
plt.ylabel('K-Conversion Efficiency')

line7 = plt.plot(x_data_7, y_data_7, c="red", linewidth=3, linestyle=":", label="N = 1.68 0%")
line8 = plt.plot(x_data_8, y_data_8, c="blue", linewidth=3, linestyle="-", label="N = 1.68 4.6%")

# set axis
plt.xlim(25, 70)
plt.ylim(0, 1)

plt.legend(loc="lower right")
# ===============================================================

# ===============================================================
plt.subplot(2, 3, 5)
plt.xlabel('Incident Angle(deg)')
plt.ylabel('K-Conversion Efficiency')

line9 = plt.plot(x_data_9, y_data_9, c="red", linewidth=1.5, linestyle="-", label="N = 1.75 0%")
line10 = plt.plot(x_data_10, y_data_10, c="blue", linewidth=1.5, linestyle="--", label="N = 1.75 4.6%")

# set axis
plt.xlim(25, 75)
plt.ylim(0, 1)

plt.legend(loc="lower right")
# ===============================================================

# ===============================================================
plt.subplot(2, 3, 6)
plt.xlabel('Incident Angle(deg)')
plt.ylabel('K-Conversion Efficiency')

line11 = plt.plot(x_data_11, y_data_11, c="red", linewidth=1.5, linestyle="-", label="N = 1.89 0%")
line12 = plt.plot(x_data_12, y_data_12, c="blue", linewidth=1.5, linestyle="--", label="N = 1.89 4.6%")

# set axis
plt.xlim(25, 75)
plt.ylim(0, 1)

plt.legend(loc="lower right")
# ===============================================================

plt.show()
