# coding=utf-8
import math
import basic
import pandas as pd
import matplotlib.pyplot as plt


# 仿真取refractive_2 = 1.05
# refractive_3 = 1.75
def comsol(lambda_0, metal_refractive, air_refractive_2, fiber_n):
    # pd_650nm_refractive = 1.8 + 4.42j  -- COMSOL 自带材料
    metal_dielectric = basic.convert_refractive_dielectric(metal_refractive)
    dielectric_2 = basic.convert_refractive_dielectric(air_refractive_2)
    dielectric_constant_3 = basic.convert_refractive_dielectric(fiber_n)
    beta = basic.calculate_propagation_constant(metal_dielectric, dielectric_2, lambda_0)
    length = basic.calculate_spp_propagation_length(beta)
    theta = basic.calculate_kretschmann_theta(beta, dielectric_constant_3, lambda_0)
    return math.degrees(theta)


data = pd.read_excel("Palm.xlsx")
x = []
y1 = []
y2 = []
y3 = []

def plot_thets_spp(air_refractive_2, fiber_n):
    index = 0
    while index <= 669:
        x.append(data.iloc[index, 0])
        lambda0 = data.iloc[index, 0]*1e-6
        pd_real = data.iloc[index, 1]
        pd_img = data.iloc[index, 2]
        pd_ref = complex(pd_real, pd_img)
        pd_theta_spp = comsol(lambda0, pd_ref, air_refractive_2, fiber_n)
        y1.append(pd_theta_spp)

        pd_h_real = data.iloc[index, 3]
        pd_h_img = data.iloc[index, 4]
        pd_h_ref = complex(pd_h_real, pd_h_img)
        pd_h_theta_spp = comsol(lambda0, pd_h_ref, air_refractive_2, fiber_n)
        y2.append(pd_h_theta_spp)
        y3.append(pd_theta_spp-pd_h_theta_spp)
        index += 1


plt.xlabel("Wavelength(μm)")
# plt.ylabel("Normalized Intensity(a.u.)")
plt.ylabel("ThetaSPP(deg)")


plot_thets_spp(1.00029+0j, 1.89)
l1, = plt.plot(x, y1, c='red', linewidth=1.5, linestyle='-', label=u"Pd(Palm)")
l2, = plt.plot(x, y2, c='blue', linewidth=1.5, linestyle='-', label=u"Pd-H(Palm)")
# l3, = plt.plot(x, y3, c='blue', linewidth=1.5, linestyle='-', label=u"Pd-H(Palm)")
plt.legend()
plt.show()


lam = 300e-9
pd_real = 1.1616365
pd_img = 2.321701

pd_ref = complex(pd_real, pd_img)
pd_theta_spp = comsol(lam, pd_ref, 1.00029+0j, 1.33)
print(pd_theta_spp)