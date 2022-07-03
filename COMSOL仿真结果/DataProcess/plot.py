# -*- coding: UTF-8 -*-
# @Author   : zhang_z
# @Time     : 2022-06-09

import pandas as pd
import glo
import base
import matplotlib.pyplot as plt

glo.setValue("N_air", 1.00029)


# -*- FIGURE 3-1 -*-
def plot3_1():
    data = pd.read_excel(io="./data/data1.xlsx", sheet_name=None)
    # get DATA 1
    xData, yData = base.getData(data, 1, 10)

    # init
    shiftingAngle = []
    decreasingVal = []
    decreasingRate = []
    mark = 1
    # get Feature
    for i in range(0, 10, 2):
        _shiftingAngle, _decreasingVal, _decreasingRate = base.getMax(xData, yData[i], yData[i+1], mark)
        shiftingAngle.append(_shiftingAngle)
        decreasingVal.append(_decreasingVal)
        decreasingRate.append(_decreasingRate)

    nameDir = {321: "Ag", 322: "Au", 323: "Al", 324: "None", 325: "ITO"}
    markDir = {321: "(a)", 322: "(b)", 323: "(c)", 324: "(d)", 325: "(e)"}
    # plot
    plt.figure(figsize=(17, 20))

    font_size = 20
    for i in range(1, 6):
        pos = 320 + i
        base.basePlot(pos, xData, yData[2*i-2], yData[2*i-1], font_size)
        ax = plt.gca()
        plt.text(0.03, 0.875, markDir[pos], fontsize=font_size+10, weight="bold", transform=ax.transAxes)
        plt.legend(loc="lower right", fontsize=font_size)
        plt.xticks([20, 30, 40, 50], rotation=0, size=font_size)
        plt.title(nameDir[pos], fontsize=font_size)

    yData.clear()
    for i in range(5):
        yData.append(1.8*shiftingAngle[i]*decreasingVal[i])

    plt.subplot(326)
    xData = ["Ag", "Au", "Al", "None", "ITO"]
    plt.yticks([0, 0.2, 0.4, 0.6, 0.8, 1.0], rotation=0, size=font_size)
    plt.ylim(0, 1)
    plt.bar(xData, yData, color="red", linewidth=4, linestyle="-")
    plt.xlabel("Materials", fontsize=font_size)
    plt.ylabel("Efficacy of Different Materials", fontsize=font_size)
    ax = plt.gca()
    plt.text(0.03, 0.875, "(f)", fontsize=font_size+10, weight="bold", transform=ax.transAxes)
    plt.xticks(xData, rotation=0, size=font_size)
    plt.title("Compare of Different Materials", fontsize=font_size)
    plt.subplots_adjust(left=None, bottom=0.1, right=None, top=0.9, wspace=0.2, hspace=0.3)
    plt.savefig("./figures/Figure3-1.pdf")
    plt.close()


# -*- FIGURE 3-2 -*-
def plot3_2():
    data = pd.read_excel(io="./data/data2.xlsx", sheet_name=None)
    # get DATA 2
    xData, yData = base.getData(data, 2, 12)

    # init
    shiftingAngle = []
    decreasingVal = []
    decreasingRate = []
    mark = 2
    # get Feature
    for i in range(0, 6):
        _shiftingAngle, _decreasingVal, _decreasingRate = base.getMax(xData, yData[i], yData[i+6], mark+(i+1)/10)
        shiftingAngle.append(_shiftingAngle)
        decreasingVal.append(_decreasingVal)
        decreasingRate.append(_decreasingRate)

    nameDir = {221: "N=1.33 N=1.45", 222: "N=1.57 N=1.68", 223: "N=1.75 N=1.89"}
    markDir = {221: "(a)", 222: "(b)", 223: "(c)"}
    prismDir = [[1.33, 1.45], [1.57, 1.68], [1.75, 1.89]]
    # plot
    plt.figure(figsize=(17, 15))
    font_size = 20
    for i in range(1, 4):
        pos = 220 + i
        base.doublePlot(pos, xData, yData[2*i-2], yData[2*i+4], yData[2*i-1], yData[2*i+5], font_size, prismDir[i-1])
        if i == 1:
            plt.xlim(35, 65)
            plt.xticks(rotation=0, size=font_size)
        if i == 2:
            plt.xlim(30, 55)
            plt.xticks(rotation=0, size=font_size)
        if i == 3:
            plt.xlim(25, 45)
            plt.xticks([25, 30, 35, 40, 45], rotation=0, size=font_size)
        ax = plt.gca()
        plt.text(0.03, 0.875, markDir[pos], fontsize=font_size+10, weight="bold", transform=ax.transAxes)
        plt.legend(loc="lower right", fontsize=font_size-3)
        plt.title(nameDir[pos], fontsize=font_size)

    plt.subplot(224)
    # set ticks
    xData = ["1.33", "1.45", "1.57", "1.68", "1.75", "1.89"]
    x_data = [1.33, 1.45, 1.57, 1.68, 1.75, 1.89]
    yMax1 = [55.20, 49.00, 44.20, 40.60, 38.65, 35.30]
    yMax2 = [59.70, 53.10, 47.90, 43.60, 41.40, 37.65]
    y = []
    glo.setValue("Alpha", 35)
    for i in range(6):
        yMax1[i] = base.convert_theta2(yMax1[i], x_data[i])
        yMax2[i] = base.convert_theta2(yMax2[i], x_data[i])
        y.append(yMax2[i] - yMax1[i])

    plt.plot(xData, shiftingAngle, color="red", linewidth=4, marker="v", markersize=15,
             linestyle=":", label="before convert")
    plt.plot(xData, y, color="blue", marker="X", linewidth=4, markersize=15, linestyle="--",
             label="after convert")
    plt.legend(fontsize=font_size - 3)
    plt.xticks(rotation=0, size=font_size)
    plt.yticks(rotation=0, size=font_size)
    plt.ylim(1, 8)
    plt.xlabel("Refractive Index of Prisms", fontsize=font_size)
    plt.ylabel("Shifting Angle[°]", fontsize=font_size)
    ax = plt.gca()
    plt.text(0.03, 0.875, "(d)", fontsize=font_size+10, weight="bold", transform=ax.transAxes)
    plt.subplots_adjust(left=None, bottom=0.1, right=None, top=0.9, wspace=0.2, hspace=0.3)
    plt.savefig("./figures/Figure3-2.pdf")


def plot_all():
    plot3_1()
    plot3_2()


plot_all()



