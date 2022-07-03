# -*- coding: UTF-8 -*-
# @Author   : zhang_z
# @Time     : 2022-05-26
import math
import numpy as np

import pandas as pd
import matplotlib.pyplot as plt

# Set Times New Roman
plt.rc("font", family="Times New Roman")

data_dir = pd.read_excel(io="data7.xlsx", sheet_name=None)

# GET DATA
# ===============================================================
data = data_dir["7-1"]
x_data = data["Column1"]
y_1 = data["Column2"]

data = data_dir["7-2"]
y_2 = data["Column2"]

data = data_dir["7-3"]
y_3 = data["Column2"]

data = data_dir["7-4"]
y_4 = data["Column2"]

data = data_dir["7-5"]
y_5 = data["Column2"]


# ===============================================================
# Get Max len 0-600

x1 = [0, 1.15, 2.3, 3.45, 4.6]
y1 = []  # y1 记录峰值之间的差值

def convert_theta2(theta1, n_prism):
    k = (math.sin(math.radians(theta1-15))*n_prism)/1.00029
    theta2 = math.degrees(math.asin(k))
    return theta2

def getMax(data1, data2):
    end_data = data2[600]
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

    rate = change_val/top_data
    print("Changing val = {}".format(rate))
    # print("data1_max = {}, data2_max = {}".format(data1_max, data2_max))
    print("the shifting angle = {}".format(data2_max - data1_max))
    return data2_max - data1_max



plt.figure(figsize=(14, 10))
font_size = 10
plt.subplot(221)
plt.xlabel('Incident Angle(deg)', fontsize=font_size)
plt.ylabel('Conversion Efficiency', fontsize=font_size)
width = 2
ll1 = plt.plot(x_data, y_1, c="black", linewidth=width, linestyle="-", label="0%")
ll2 = plt.plot(x_data, y_2, c="blue", linewidth=width, linestyle="-", label="1.15%")
ll3 = plt.plot(x_data, y_3, c="red", linewidth=width, linestyle="-", label="2.3%")
ll4 = plt.plot(x_data, y_4, c="green", linewidth=width, linestyle="-", label="3.45%")
ll5 = plt.plot(x_data, y_5, c="orange", linewidth=width, linestyle="-", label="4.60%")
plt.xticks(rotation=0, size=font_size)
plt.yticks([0, 0.2, 0.4, 0.6, 0.8, 1.0], rotation=0, size=font_size)
ax = plt.gca()
plt.text(0.03, 0.875, "(a)", fontsize=font_size + 10, weight="bold", transform=ax.transAxes)
plt.legend(loc="lower right", ncol=1, fontsize=font_size)
plt.title("Conversion Efficiency under different hydrogen concentrations", fontsize=font_size)

plt.subplot(222)
plt.xlabel('Incident Angle(deg)', fontsize=font_size)
plt.ylabel('Conversion Efficiency', fontsize=font_size)
ll7 = plt.plot(x_data, y_1, c="black", linewidth=width, linestyle="-", label="0%")
ll8 = plt.plot(x_data, y_2, c="blue", linewidth=width, linestyle="-", label="1.15%")
ll9 = plt.plot(x_data, y_3, c="red", linewidth=width, linestyle="-", label="2.3%")
ll10 = plt.plot(x_data, y_4, c="green", linewidth=width, linestyle="-", label="3.45%")
ll11 = plt.plot(x_data, y_5, c="orange", linewidth=width, linestyle="-", label="4.60%")
plt.xticks(rotation=0, size=font_size)
plt.yticks([0.70, 0.75, 0.80, 0.85, 0.90, 0.95, 1.00], rotation=0, size=font_size)
plt.xlim(33.5, 41.5)
plt.ylim(0.7, 1.05)
ax = plt.gca()
plt.text(0.03, 0.875, "(b)", fontsize=font_size + 10, weight="bold", transform=ax.transAxes)
plt.legend(loc="lower right", ncol=1, fontsize=font_size)
plt.title("Partial magnification of Fig3.6.(a)", fontsize=font_size)


# 直线拟合
temp_x = np.arange(0, 4.65, 0.1)
a = 35.604
b = 0.754782608695654
temp_y1 = a+b*temp_x
a = 41.5875977661076
b = 1.9097175415989
temp_y2 = a+b*temp_x

plt.subplot(223)
xx = [0, 1.15, 2.3, 3.45, 4.6]
y = [35.76, 36.4, 37.18, 38.12, 39.24]
y2 = []
for i in range(5):
    y2.append(convert_theta2(y[i], 1.89))
    print(y2[i])

print(y2[4]-y2[0])
plt.xlabel('Hydrogen concentration', fontsize=font_size)
plt.ylabel('Peak Angle[°]', fontsize=font_size)
plt.plot(temp_x, temp_y1, color="red", linewidth=2, linestyle="--", label="Linear Fit")
_ll1 = plt.scatter(xx, y, c="blue", marker="v", s=80, label="Peak Angle")


ax = plt.gca()
plt.text(0.03, 0.875, "(c)", fontsize=font_size + 10, weight="bold", transform=ax.transAxes)
plt.legend(loc="lower right", ncol=1, fontsize=font_size)
plt.title("Peak Angle under Different Hydrogen concentration", fontsize=font_size)

plt.xticks([0, 1.15, 2.3, 3.45, 4.6], rotation=0, size=font_size)
plt.yticks(rotation=0, size=font_size)

############################################################
plt.subplot(224)

plt.xlabel('Hydrogen concentration', fontsize=font_size)
plt.ylabel('Peak Angle[°]', fontsize=font_size)
_ll3 = plt.scatter(xx, y2, c="blue", marker="v", s=80, label="Peak Angle")
plt.plot(temp_x, temp_y2, color="red", linewidth=2, linestyle="--", label="Linear Fit")



ax = plt.gca()
plt.text(0.03, 0.875, "(d)", fontsize=font_size + 10, weight="bold", transform=ax.transAxes)
plt.legend(loc="lower right", ncol=1, fontsize=font_size)
plt.title("After Magnification by the Prism", fontsize=font_size)

plt.xticks([0, 1.15, 2.3, 3.45, 4.6], rotation=0, size=font_size)
plt.yticks(rotation=0, size=font_size)

plt.savefig("Figure3-6.pdf")
plt.close()

# 需要找出最佳的D1值 根据前文的情况
# 我们认为为了在一定程度上的取得




