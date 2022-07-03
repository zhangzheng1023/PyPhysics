# -*- coding: UTF-8 -*-
# @Author   : zhang_z
# @Time     : 2022-06-09
import copy
import math
import glo
import matplotlib.pyplot as plt


# real_angle = theta1 - alpha
def convert_theta2(theta1, n_prism):
    k = (math.sin(math.radians(theta1-glo.globalDict["Alpha"]))*n_prism)/glo.globalDict["N_air"]
    theta2 = math.degrees(math.asin(k))
    return theta2


# 获取一些列信息 包括data1/data2 峰值的大小以及位置
# def getMax(x_data, data1, data2):
def getMax(x_data, data1, data2, mark):
    length = len(data1)
    end_data = data2[length-1]

    data1_max_pos = 0
    data2_max_val = 0
    data2_max_pos = 0
    for x in range(length):
        if x == 0 or x == length-1:
            continue
        if data1[x] > data1[x-1] and data1[x] > data1[x+1]:
            data1_max_pos = x_data[x]

        if data2[x] > data2[x - 1] and data2[x] > data2[x + 1]:
            data2_max_val = data2[x]
            data2_max_pos = x_data[x]
            if mark == 1 and x_data[x] > 34:
                break
            if 2 < mark <= 2.2 and x_data[x] > 52:
                break
            if 2.3 <= mark <= 2.4 and x_data[x] > 42:
                break
            if 2.5 <= mark <= 2.6 and x_data[x] > 36:
                break
    print(data1_max_pos, data2_max_pos)
    shiftingAngle = data2_max_pos - data1_max_pos
    decreasingVal = data2_max_val - end_data
    decreasingRate = decreasingVal/data2_max_val
    return shiftingAngle, decreasingVal, decreasingRate


def getData(data, base, num):
    index = 1
    xData = []
    yData = []
    while index <= num:
        sheetName = "{}-{}".format(base, index)
        if index == 1:
            xData = data[sheetName]["Column1"]
        y_data = data[sheetName]["Column2"]
        yData.append(copy.deepcopy(y_data))
        index += 1
    return xData, yData


def doublePlot(pos, x_data, data1, data2, data3, data4, font_size, n_prism):
    plt.subplot(pos)
    # set ticks
    lineWidth = 2.5
    plt.plot(x_data, data1, color="red", linewidth=lineWidth, linestyle="-", label="N={} 0%".format(n_prism[0]))
    plt.plot(x_data, data2, color="red", linewidth=lineWidth, linestyle="--", label="N={} 4.6%".format(n_prism[0]))
    plt.plot(x_data, data3, color="blue", linewidth=lineWidth, linestyle="-", label="N={} 0%".format(n_prism[1]))
    plt.plot(x_data, data4, color="blue", linewidth=lineWidth, linestyle="--", label="N={} 4.6%".format(n_prism[1]))
    plt.yticks([0, 0.2, 0.4, 0.6, 0.8, 1.0], rotation=0, size=font_size)
    plt.ylim(0, 1)
    plt.xlabel("Incident Angle[°]", fontsize=font_size)
    plt.ylabel("Conversion Efficiency", fontsize=font_size)


def basePlot(pos, x_data, data1, data2, font_size):
    plt.subplot(pos)
    # set ticks
    plt.plot(x_data, data1, color="red", linewidth=4, linestyle="-", label="0%H2")
    plt.plot(x_data, data2, color="blue", linewidth=4, linestyle="--", label="4.6%H2")
    plt.yticks([0, 0.2, 0.4, 0.6, 0.8, 1.0], rotation=0, size=font_size)
    plt.ylim(0, 1)
    plt.xlabel("Incident Angle[°]", fontsize=font_size)
    plt.ylabel("Conversion Efficiency", fontsize=font_size)

