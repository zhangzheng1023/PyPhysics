# -*- coding: UTF-8 -*-
# @Author   : zhang_z
# @Time     : 2022-04-18

import pandas as pd
import matplotlib.pyplot as plt

# 整体返回一个字典 key为Sheet名称 val为单页内容
data_dir = pd.read_excel(io="../data/DATA1.xlsx", sheet_name=None)

data_dir["data1"]

