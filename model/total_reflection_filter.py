# coding=utf-8
# 全内反射滤波器模型 total internal reflection filter model

import matplotlib.pyplot as plt
import numpy as np
import math
import basic
from materials.ITO import ito_dielectric_complex
from materials.fiber_core import fiber_core_refractive

# 计算在该模型下theta_c 即全内反射临界角

def au_dielectric_complex(lambda_0):
    lambda_c = 8.9342e-6
    lambda_p = 1.6826e-7
    epsilon_complex = 1 - (lambda_0**2*lambda_c)/(lambda_p**2*(lambda_c+complex(0, lambda_0)))
    return epsilon_complex

x = []
y1 = []
y2 = []
y3 = []
plt.xlabel("Wavelength(nm)")
plt.ylabel("alpha[deg]")
wavelength = 400e-9
while wavelength <= 900e-9:
    x.append(wavelength*1e9)
    ito_refractive = basic.convert_dielectric_refractive(ito_dielectric_complex(wavelength))
    #fiber_refractive = fiber_core_refractive(wavelength)
    fiber_refractive = 1.7
    #    math.degrees(math.asin(ito_refractive.real / fiber_refractive.real))
    temp = ito_refractive.real/fiber_refractive.real

    # =====================
    air = complex(1.05, 0)
    beta = basic.calculate_propagation_constant(au_dielectric_complex(wavelength), air, wavelength)
    fiber_die = fiber_refractive**2
    y2.append((90+math.degrees(basic.calculate_kretschmann_theta(beta, fiber_die, wavelength)))/2)
    # =====================

    if temp > 1:
        wavelength = wavelength + 0.1e-9
        y1.append(np.nan)
        y3.append(np.nan)
        continue
    else:
        temp2 = math.degrees(math.asin(temp))
        y1.append(temp2)
        if (temp2 >= 63.95979451855001) and (temp2 <= 66.61388784155113):
            y3.append(temp2)
        else:
            y3.append(np.nan)
        wavelength = wavelength + 0.1e-9


#l1,= plt.plot(y1, x, c='black', linewidth=1, linestyle='-', label=u"特定角度下发生全反射的截止波长")
l2,= plt.plot(y2, x, c='red', linewidth=1, linestyle='-', label=u"特定角度的期望SPR波长")
l2,= plt.plot(y3, x, c='black', linewidth=1, linestyle='-', label=u"特定角度的截止波长")
print (y2[0],y2[-1])
plt.legend()
plt.show()

