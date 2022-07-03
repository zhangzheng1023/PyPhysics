# -*- coding: UTF-8 -*-
# @Author   : zhang_z
# @Time     : 2022-05-17

import pandas as pd
import matplotlib.pyplot as plt

# Set Times New Roman
plt.rc("font", family="Times New Roman")

data_dir = pd.read_excel(io="data4.xlsx", sheet_name=None)

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

x1 = [12, 13, 14, 15, 16, 17, 18]
x2 = [3, 4, 5, 6, 7, 8, 9, 10]
y1 = []
y2 = []


def getMax(data1, data2):
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
    print("data1_max = {}, data2_max = {}".format(data1_max, data2_max))
    print("the shifting angle = {}".format(data2_max - data1_max))
    return data2_max - data1_max


y1.append(getMax(y_1_1, y_2_1))
y1.append(getMax(y_1_2, y_2_2))
y1.append(getMax(y_1_3, y_2_3))
y1.append(getMax(y_1_4, y_2_4))
y1.append(getMax(y_1_5, y_2_5))
y1.append(getMax(y_1_6, y_2_6))
y1.append(getMax(y_1_7, y_2_7))

# y2.append(getMax(y_3_1, y_4_1))
# y2.append(getMax(y_3_2, y_4_2))
# y2.append(getMax(y_3_3, y_4_3))
# y2.append(getMax(y_3_4, y_4_4))
# y2.append(getMax(y_3_5, y_4_5))
# y2.append(getMax(y_3_6, y_4_6))
# y2.append(getMax(y_3_7, y_4_7))
# y2.append(getMax(y_3_8, y_4_8))


# ===============================================================
figure1 = plt.figure()  # create an empty figure

plt.figure(figsize=(10, 8))

# plt.subplot(1, 2, 1)
plt.xlabel('Incident Angle(deg)')
plt.ylabel('K-Conversion Efficiency')

line1 = plt.plot(x_data, y_1_1, c="red", linewidth=1.5, linestyle=":", label="D1 = 12nm 0%")
line2 = plt.plot(x_data, y_2_1, c="red", linewidth=1.5, linestyle="-", label="D1 = 12nm 4.6%")
line3 = plt.plot(x_data, y_1_2, c="blue", linewidth=1.5, linestyle=":", label="D1 = 13nm 0%")
line4 = plt.plot(x_data, y_2_2, c="blue", linewidth=1.5, linestyle="-", label="D1 = 13nm 4.6%")
line5 = plt.plot(x_data, y_1_3, c="black", linewidth=1.5, linestyle=":", label="D1 = 14nm 0%")
line6 = plt.plot(x_data, y_2_3, c="black", linewidth=1.5, linestyle="-", label="D1 = 14nm 4.6%")
line7 = plt.plot(x_data, y_1_4, c="green", linewidth=1.5, linestyle=":", label="D1 = 15nm 0%")
line8 = plt.plot(x_data, y_2_4, c="green", linewidth=1.5, linestyle="-", label="D1 = 15nm 4.6%")
line9 = plt.plot(x_data, y_1_5, c="yellow", linewidth=1.5, linestyle=":", label="D1 = 16nm 0%")
line10 = plt.plot(x_data, y_2_5, c="yellow", linewidth=1.5, linestyle="-", label="D1 = 16nm 4.6%")
line11 = plt.plot(x_data, y_1_6, c="orange", linewidth=1.5, linestyle=":", label="D1 = 17nm 0%")
line12 = plt.plot(x_data, y_2_6, c="orange", linewidth=1.5, linestyle="-", label="D1 = 17nm 4.6%")
line13 = plt.plot(x_data, y_1_7, c="green", linewidth=1.5, linestyle=":", label="D1 = 18nm 0%")
line14 = plt.plot(x_data, y_2_7, c="green", linewidth=1.5, linestyle="-", label="D1 = 18nm 4.6%")

# figure1_max
# line31 = plt.plot(x1, y1, c="red", linewidth=1.5, linestyle=":", label="D1 = 12nm 0%")
# line32 = plt.plot(x2, y2, c="red", linewidth=1.5, linestyle=":", label="D1 = 12nm 0%")


# line15 = plt.plot(x_data, y_3_1, c="red", linewidth=1.5, linestyle=":", label="D2 = 3nm 0%")
# line16 = plt.plot(x_data, y_4_1, c="red", linewidth=1.5, linestyle="-", label="D2 = 3nm 4.6%")
# line17 = plt.plot(x_data, y_3_2, c="blue", linewidth=1.5, linestyle=":", label="D2 = 4nm 0%")
# line18 = plt.plot(x_data, y_4_2, c="blue", linewidth=1.5, linestyle="-", label="D2 = 4nm 4.6%")
# line19 = plt.plot(x_data, y_3_3, c="black", linewidth=1.5, linestyle=":", label="D2 = 5nm 0%")
# line20 = plt.plot(x_data, y_4_3, c="black", linewidth=1.5, linestyle="-", label="D2 = 5nm 4.6%")
# line21 = plt.plot(x_data, y_3_4, c="green", linewidth=1.5, linestyle=":", label="D2 = 6nm 0%")
# line22 = plt.plot(x_data, y_4_4, c="green", linewidth=1.5, linestyle="-", label="D2 = 6nm 4.6%")
# line23 = plt.plot(x_data, y_3_5, c="yellow", linewidth=1.5, linestyle=":", label="D2 = 7nm 0%")
# line24 = plt.plot(x_data, y_4_5, c="yellow", linewidth=1.5, linestyle="-", label="D2 = 7nm 4.6%")
# line25 = plt.plot(x_data, y_3_6, c="orange", linewidth=1.5, linestyle=":", label="D2 = 8nm 0%")
# line26 = plt.plot(x_data, y_4_6, c="orange", linewidth=1.5, linestyle="-", label="D2 = 8nm 4.6%")
# line27 = plt.plot(x_data, y_3_7, c="green", linewidth=1.5, linestyle=":", label="D2 = 9nm 0%")
# line28 = plt.plot(x_data, y_4_7, c="green", linewidth=1.5, linestyle="-", label="D2 = 9nm 4.6%")
# line29 = plt.plot(x_data, y_3_8, c="red", linewidth=1.5, linestyle=":", label="D2 = 10nm 0%")
# line30 = plt.plot(x_data, y_4_8, c="red", linewidth=1.5, linestyle="-", label="D2 = 10nm 4.6%")

# set axis
plt.xlim(20, 50)
plt.ylim(0, 1)

plt.legend(loc="upper left")






plt.show()


