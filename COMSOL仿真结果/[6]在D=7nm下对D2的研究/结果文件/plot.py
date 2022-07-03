# -*- coding: UTF-8 -*-
# @Author   : zhang_z
# @Time     : 2022-05-17

import pandas as pd
import matplotlib.pyplot as plt


data_dir = pd.read_excel(io="data6.xlsx", sheet_name=None)

# GET DATA
# ===============================================================
data = data_dir["6-1-1"]
x_data = data["Column1"]
y_1_1 = data["Column2"]

data = data_dir["6-1-2"]
y_1_2 = data["Column2"]

data = data_dir["6-1-3"]
y_1_3 = data["Column2"]

data = data_dir["6-1-4"]
y_1_4 = data["Column2"]

data = data_dir["6-1-5"]
y_1_5 = data["Column2"]

data = data_dir["6-1-6"]
y_1_6 = data["Column2"]

data = data_dir["6-1-7"]
y_1_7 = data["Column2"]

data = data_dir["6-1-8"]
y_1_8 = data["Column2"]

data = data_dir["6-1-9"]
y_1_9 = data["Column2"]

data = data_dir["6-1-10"]
y_1_10 = data["Column2"]

data = data_dir["6-1-11"]
y_1_11 = data["Column2"]

data = data_dir["6-2-1"]
y_2_1 = data["Column2"]

data = data_dir["6-2-2"]
y_2_2 = data["Column2"]

data = data_dir["6-2-3"]
y_2_3 = data["Column2"]

data = data_dir["6-2-4"]
y_2_4 = data["Column2"]

data = data_dir["6-2-5"]
y_2_5 = data["Column2"]

data = data_dir["6-2-6"]
y_2_6 = data["Column2"]

data = data_dir["6-2-7"]
y_2_7 = data["Column2"]

data = data_dir["6-2-8"]
y_2_8 = data["Column2"]

data = data_dir["6-2-9"]
y_2_9 = data["Column2"]

data = data_dir["6-2-10"]
y_2_10 = data["Column2"]

data = data_dir["6-2-11"]
y_2_11 = data["Column2"]

# ===============================================================
# Get Max len 0-600

x1 = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
y1 = []  # y1 记录峰值之间的差值
y11 = []  # y11 记录data2的尖锐程度
z = [] # 记录峰值


def getMax(data1, data2):
    end_data = data2[600]
    top_data = 0
    top_data1 = 0
    data1_max = 0
    data2_max = 0
    for x in range(601):
        if x == 0 or x == 600:
            continue
        if data1[x] > data1[x-1] and data1[x] > data1[x+1]:
            if x_data[x] > 33:
                data1_max = x_data[x]
                top_data1 = data1[x]


        if data2[x] > data2[x - 1] and data2[x] > data2[x + 1]:
            if x_data[x] > 33:
                data2_max = x_data[x]
                top_data = data2[x]
    change_val = top_data - end_data
    y11.append(change_val)
    rate = change_val/top_data
    z.append(top_data1)
    print("Changing val = {}".format(rate))
    # print("data1_max = {}, data2_max = {}".format(data1_max, data2_max))
    print("the shifting angle = {}".format(data2_max - data1_max))
    return data2_max - data1_max



print("D2 = 5nm")
y1.append(getMax(y_1_1, y_2_1))
print("D2 = 6nm")
y1.append(getMax(y_1_2, y_2_2))
print("D2 = 7nm")
y1.append(getMax(y_1_3, y_2_3))
print("D2 = 8nm")
y1.append(getMax(y_1_4, y_2_4))
print("D2 = 9nm")
y1.append(getMax(y_1_5, y_2_5))
print("D2 = 10nm")
y1.append(getMax(y_1_6, y_2_6))
print("D2 = 11nm")
y1.append(getMax(y_1_7, y_2_7))
print("D2 = 12nm")
y1.append(getMax(y_1_8, y_2_8))
print("D2 = 13nm")
y1.append(getMax(y_1_9, y_2_9))
print("D2 = 14nm")
y1.append(getMax(y_1_10, y_2_10))
print("D2 = 15nm")
y1.append(getMax(y_1_11, y_2_11))


# ===============================================================
# zx = [6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]
# z = []
# z2 = []
#
# # 需要找出最佳的D1值 根据前文的情况
# # 我们认为为了在一定程度上的取得
#
# for x in range(14):
#     if x == 0:
#         continue
#     dele_val = y1[x-1] - y1[x]
#     get_val = y11[x] - y11[x-1]
#     z.append(get_val/dele_val)
#     z2.append((y11[x]-y11[0])/(y1[0]-y1[x]))
#     print(z2)
# # 对z进行归一化进行处理
# # z2max = 0.13795830860946953
# # z2min = 0.11218071175063674
# z2max = 0.14
# z2min = 0.1
#
# for i in range(13):
#     rate = (z2[i]-z2min)/(z2max-z2min)
#     z2[i] = 0.2*rate

# tempx = [12, 13, 14, 15]
# tempy = []
# for i in range(4):
#     index = 7 + i
#     tempy.append((y1[index]-y1[6])/(z[6] - z[index]))


tempy = []
for i in range(11):
    tempy.append(y1[i]/(1-z[i]))


fig = plt.figure(figsize=(10, 8))
ax1 = fig.add_subplot(111)
ax1.plot(x1, y1, c="red", linewidth=2, linestyle="-.", marker="v", markersize=12, label="shifting angle")
plt.legend(loc="best")

ax2 = ax1.twinx()
# ax2.plot(x1, y11, c="blue", linewidth=2, linestyle="--", marker="s", markersize=12, label="rate of decline")
# ax2.plot(x1, z, c="black", linewidth=1, linestyle=":", marker="X", markersize=12, label="rate of decline")
ax2.plot(x1, tempy, c="black", linewidth=1, linestyle=":", marker="X", markersize=12, label="rate of decline")
plt.title('Figure3.b', fontsize=25)


# ax1._label('D1(nm)')
# ax1.label('Shifting Angle(deg)')
# ax2.ylabel('K-conversion')

plt.legend(loc="best")


plt.show()

# z = []
# z.append(0)

# 需要找出最佳的D1值 根据前文的情况
# 我们认为为了在一定程度上的取得




