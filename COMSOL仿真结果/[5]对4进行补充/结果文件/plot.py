# -*- coding: UTF-8 -*-
# @Author   : zhang_z
# @Time     : 2022-05-17

import pandas as pd
import twisy
import matplotlib.pyplot as plt

# Set Times New Roman
data_dir = pd.read_excel(io="data4.xlsx", sheet_name=None)
data_dir2 = pd.read_excel(io="data5.xlsx", sheet_name=None)

# xx yy 表示5中的数据
# GET DATA
# ===============================================================
data = data_dir2["5-1-1"]
xx = data["Column1"]
yy_1_1 = data["Column2"]

data = data_dir2["5-1-2"]
yy_1_2 = data["Column2"]

data = data_dir2["5-1-3"]
yy_1_3 = data["Column2"]

data = data_dir2["5-1-4"]
yy_1_4 = data["Column2"]

data = data_dir2["5-1-5"]
yy_1_5 = data["Column2"]

data = data_dir2["5-1-6"]
yy_1_6 = data["Column2"]

data = data_dir2["5-1-7"]
yy_1_7 = data["Column2"]


data = data_dir2["5-2-1"]
yy_2_1 = data["Column2"]

data = data_dir2["5-2-2"]
yy_2_2 = data["Column2"]

data = data_dir2["5-2-3"]
yy_2_3 = data["Column2"]

data = data_dir2["5-2-4"]
yy_2_4 = data["Column2"]

data = data_dir2["5-2-5"]
yy_2_5 = data["Column2"]

data = data_dir2["5-2-6"]
yy_2_6 = data["Column2"]

data = data_dir2["5-2-7"]
yy_2_7 = data["Column2"]


# GET DATA
# ===============================================================
data = data_dir["4-1-1"]
x_data = data["Column1"]
y_1_1 = data["Column2"]

data = data_dir["4-1-2"]
y_1_2 = data["Column2"]

data = data_dir["4-1-3"]
y_1_3 = data["Column2"]

data = data_dir["4-1-4"]
y_1_4 = data["Column2"]

data = data_dir["4-1-5"]
y_1_5 = data["Column2"]

data = data_dir["4-1-6"]
y_1_6 = data["Column2"]

data = data_dir["4-1-7"]
y_1_7 = data["Column2"]

data = data_dir["4-2-1"]
y_2_1 = data["Column2"]

data = data_dir["4-2-2"]
y_2_2 = data["Column2"]

data = data_dir["4-2-3"]
y_2_3 = data["Column2"]

data = data_dir["4-2-4"]
y_2_4 = data["Column2"]

data = data_dir["4-2-5"]
y_2_5 = data["Column2"]

data = data_dir["4-2-6"]
y_2_6 = data["Column2"]

data = data_dir["4-2-7"]
y_2_7 = data["Column2"]

data = data_dir["4-3-1"]
y_3_1 = data["Column2"]

data = data_dir["4-3-2"]
y_3_2 = data["Column2"]

data = data_dir["4-3-3"]
y_3_3 = data["Column2"]

data = data_dir["4-3-4"]
y_3_4 = data["Column2"]

data = data_dir["4-3-5"]
y_3_5 = data["Column2"]

data = data_dir["4-3-6"]
y_3_6 = data["Column2"]

data = data_dir["4-3-7"]
y_3_7 = data["Column2"]

data = data_dir["4-3-8"]
y_3_8 = data["Column2"]

data = data_dir["4-4-1"]
y_4_1 = data["Column2"]

data = data_dir["4-4-2"]
y_4_2 = data["Column2"]

data = data_dir["4-4-3"]
y_4_3 = data["Column2"]

data = data_dir["4-4-4"]
y_4_4 = data["Column2"]

data = data_dir["4-4-5"]
y_4_5 = data["Column2"]

data = data_dir["4-4-6"]
y_4_6 = data["Column2"]

data = data_dir["4-4-7"]
y_4_7 = data["Column2"]

data = data_dir["4-4-8"]
y_4_8 = data["Column2"]
# ===============================================================
# Get Max len 0-600

x1 = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]
x2 = [3, 4, 5, 6, 7, 8, 9, 10]
y1 = []  # y1 记录峰值之间的差值
y11 = []  # y11 记录data2的尖锐程度
y2 = []

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
    y11.append(change_val)
    rate = change_val/top_data
    print("Changing val = {}".format(rate))
    # print("data1_max = {}, data2_max = {}".format(data1_max, data2_max))
    print("the shifting angle = {}".format(data2_max - data1_max))
    return data2_max - data1_max


def getMax2(data1, data2):
    end_data = data2[1500]
    top_data = 0
    data1_max = 0
    data2_max = 0
    for x in range(1501):
        if x == 0 or x == 1500:
            continue
        if data1[x] > data1[x-1] and data1[x] > data1[x+1]:
            if xx[x] > 33:
                data1_max = xx[x]

        if data2[x] > data2[x - 1] and data2[x] > data2[x + 1]:
            if xx[x] > 33:
                data2_max = xx[x]
                top_data = data2[x]
    change_val = top_data - end_data
    y11.append(change_val)
    rate = change_val/top_data
    print("Changing val = {}".format(rate))
    # print("data1_max = {}, data2_max = {}".format(data1_max, data2_max))
    print("the shifting angle = {}".format(data2_max - data1_max))
    return data2_max - data1_max





print("D1 = 5nm")
y1.append(getMax2(yy_1_1, yy_2_1))
print("D1 = 6nm")
y1.append(getMax2(yy_1_2, yy_2_2))
print("D1 = 7nm")
y1.append(getMax2(yy_1_3, yy_2_3))
print("D1 = 8nm")
y1.append(getMax2(yy_1_4, yy_2_4))
print("D1 = 9nm")
y1.append(getMax2(yy_1_5, yy_2_5))
print("D1 = 10nm")
y1.append(getMax2(yy_1_6, yy_2_6))
print("D1 = 11nm")
y1.append(getMax2(yy_1_7, yy_2_7))


print("D1 = 12nm")
y1.append(getMax(y_1_1, y_2_1))
print("D1 = 13nm")
y1.append(getMax(y_1_2, y_2_2))
print("D1 = 14nm")
y1.append(getMax(y_1_3, y_2_3))
print("D1 = 15nm")
y1.append(getMax(y_1_4, y_2_4))
print("D1 = 16nm")
y1.append(getMax(y_1_5, y_2_5))
print("D1 = 17nm")
y1.append(getMax(y_1_6, y_2_6))
print("D1 = 18nm")
y1.append(getMax(y_1_7, y_2_7))


# ===============================================================
font_size = 10
plt.figure(figsize=(14, 5))
plt.subplot(121)

plt.xlabel('Incident Angle[°]', fontsize=font_size)
plt.ylabel('Conversion Efficiency', fontsize=font_size)
width = 1.2
ll1 = plt.plot(xx, yy_1_1, c="black", linewidth=width, linestyle="-", label="D1 = 5nm 0%")
ll2 = plt.plot(xx, yy_2_1, c="black", linewidth=width, linestyle="--", label="D1 = 5nm 4.6%")

ll3 = plt.plot(xx, yy_1_2, c="brown", linewidth=width, linestyle="-", label="D1 = 6nm 0%")
ll4 = plt.plot(xx, yy_2_2, c="brown", linewidth=width, linestyle="--", label="D1 = 6nm 4.6%")

ll5 = plt.plot(xx, yy_1_3, c="darkred", linewidth=width, linestyle="-", label="D1 = 7nm 0%")
ll6 = plt.plot(xx, yy_2_3, c="darkred", linewidth=width, linestyle="--", label="D1 = 7nm 4.6%")

ll7 = plt.plot(xx, yy_1_4, c="red", linewidth=width, linestyle="-", label="D1 = 8nm 0%")
ll8 = plt.plot(xx, yy_2_4, c="red", linewidth=width, linestyle="--", label="D1 = 8nm 4.6%")

ll9 = plt.plot(xx, yy_1_5, c="saddlebrown", linewidth=width, linestyle="-", label="D1 = 9nm 0%")
ll10 = plt.plot(xx, yy_2_5, c="saddlebrown", linewidth=width, linestyle="--", label="D1 = 9nm 4.6%")

ll11 = plt.plot(xx, yy_1_6, c="darkolivegreen", linewidth=width, linestyle="-", label="D1 = 10nm 0%")
ll12 = plt.plot(xx, yy_2_6, c="darkolivegreen", linewidth=width, linestyle="--", label="D1 = 10nm 4.6%")

ll13 = plt.plot(xx, yy_1_7, c="green", linewidth=width, linestyle="-", label="D1 = 11nm 0%")
ll14 = plt.plot(xx, yy_2_7, c="green", linewidth=width, linestyle="--", label="D1 = 11nm 4.6%")

line1 = plt.plot(x_data, y_1_1, c="dimgray", linewidth=width, linestyle="-", label="D1 = 12nm 0%")
line2 = plt.plot(x_data, y_2_1, c="dimgray", linewidth=width, linestyle="--", label="D1 = 12nm 4.6%")
line3 = plt.plot(x_data, y_1_2, c="orange", linewidth=width, linestyle="-", label="D1 = 13nm 0%")
line4 = plt.plot(x_data, y_2_2, c="orange", linewidth=width, linestyle="--", label="D1 = 13nm 4.6%")
line5 = plt.plot(x_data, y_1_3, c="lightslategrey", linewidth=width, linestyle="-", label="D1 = 14nm 0%")
line6 = plt.plot(x_data, y_2_3, c="lightslategrey", linewidth=width, linestyle="--", label="D1 = 14nm 4.6%")
line7 = plt.plot(x_data, y_1_4, c="midnightblue", linewidth=width, linestyle="-", label="D1 = 15nm 0%")
line8 = plt.plot(x_data, y_2_4, c="midnightblue", linewidth=width, linestyle="--", label="D1 = 15nm 4.6%")
line9 = plt.plot(x_data, y_1_5, c="blue", linewidth=width, linestyle="-", label="D1 = 16nm 0%")
line10 = plt.plot(x_data, y_2_5, c="blue", linewidth=width, linestyle="--", label="D1 = 16nm 4.6%")
line11 = plt.plot(x_data, y_1_6, c="indigo", linewidth=width, linestyle="-", label="D1 = 17nm 0%")
line12 = plt.plot(x_data, y_2_6, c="indigo", linewidth=width, linestyle="--", label="D1 = 17nm 4.6%")
line13 = plt.plot(x_data, y_1_7, c="crimson", linewidth=width, linestyle="-", label="D1 = 18nm 0%")
line14 = plt.plot(x_data, y_2_7, c="crimson", linewidth=width, linestyle="--", label="D1 = 18nm 4.6%")


# set axis
plt.xlim(20, 50)
plt.xticks(rotation=0, size=font_size)
plt.yticks([0, 0.2, 0.4, 0.6, 0.8, 1.0], rotation=0, size=font_size)
plt.ylim(0, 1)

ax = plt.gca()
plt.text(0.03, 0.875, "(a)", fontsize=font_size + 10, weight="bold", transform=ax.transAxes)
plt.legend(loc="lower right", ncol=2, fontsize=font_size-4)
plt.title("Conversion Efficiency of Different D1", fontsize=font_size)

plt.subplot(122)

plt.plot(x1, y1, c="red", linewidth=2, linestyle="-.", marker="v", markersize=10, label="shifting angle")
plt.xticks([5, 8, 11, 14, 17], rotation=0, size=font_size)
plt.xlabel("Thickness of Ag[nm]", fontsize=font_size)
plt.ylabel("Shifting Angle[°]", fontsize=font_size)
plt.ylim(2, 3.8)
plt.legend(loc="right", fontsize=font_size)

ax1 = plt.gca()
ax2 = ax1.twinx()
ax2.plot(x1, y11, c="blue", linewidth=2, linestyle="--", marker="s",
         markersize=10, label="reduced efficiency")
ax2.plot(twisy.zx, twisy.z2, c="black", linewidth=1, linestyle=":", marker="X", markersize=10, label="Efficacy")
plt.ylim(0.05, 0.225)
ax = plt.gca()
plt.ylabel("changing efficiency", fontsize=font_size)
plt.text(0.03, 0.875, "(b)", fontsize=font_size + 10, weight="bold", transform=ax.transAxes)
plt.title("Efficacy of Different D1", fontsize=font_size)
# ax1._label('D1(nm)')
# ax1.label('Shifting Angle(deg)')
# ax2.ylabel('K-conversion')

plt.legend(loc="best", fontsize=font_size)
plt.savefig("Figure3-4.pdf")
plt.close()
# plt.subplots_adjust(left=None, bottom=0.1, right=None, top=0.9, wspace=0.2, hspace=0.3)



