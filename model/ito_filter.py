# coding=utf8
import matplotlib.pyplot as plt
import numpy as np
import math
import basic
from materials.ITO import ito_dielectric_complex
from materials.fiber_core import fiber_core_refractive


# theta_c 为在不同角度下的
def theta_c(n1, lam):
    d2 = ito_dielectric_complex(lam)
    n2 = basic.convert_dielectric_refractive(d2).real
    theta_c = math.degrees(math.asin(n2/n1))
    return theta_c


x = []
y = []
wavelength = 400e-9
while wavelength <= 900e-9:
    x.append(wavelength*1e9)
    y.append(theta_c(1.83, wavelength))
    wavelength = wavelength + 0.1e-9
plt.plot(x, y)
plt.show()