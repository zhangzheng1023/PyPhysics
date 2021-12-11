# coding=utf-8
# The core of the optical fiber is assumed to be made of fused silica.
# The refractive index of fused silica varies with wavelength according to Sellmeier dispersion relation

import math
import numpy as np
import matplotlib.pyplot as plt


def fiber_core_refractive(lambda_0):
    a1 = 0.6961663
    a2 = 0.4079426
    a3 = 0.8974794
    b1 = 0.0684043e-6
    b2 = 0.1162414e-6
    b3 = 9.896161e-6
    k1 = (a1*lambda_0**2)/(lambda_0**2-b1*b1)
    k2 = (a2*lambda_0**2)/(lambda_0**2-b2*b2)
    k3 = (a3*lambda_0**2)/(lambda_0**2-b3*b3)
    refractive = math.sqrt(1+k1+k2+k3)
    return refractive


# 可视化
# x = []
# y = []
# wavelength = 400e-9
# while wavelength <= 900e-9:
#     x.append(wavelength*1e9)
#     y.append(fiber_core_refractive(wavelength))
#     wavelength = wavelength + 0.1e-9
# plt.plot(x, y)
# plt.show()

