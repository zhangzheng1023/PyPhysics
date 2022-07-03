# -*- coding: UTF-8 -*-
# @Author   : zhang_z
# @Time     : 2022-06-11

globalDict = {}


def setValue(key, value):
    globalDict[key] = value


def getValue(key, default=None):
    try:
        return globalDict[key]
    except KeyError:
        return default

