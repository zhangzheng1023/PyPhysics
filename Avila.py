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

# 0.302704071	1.164367	2.339882	1.455224	1.821829
# 0.400084717	1.393514	3.076941	1.803938	2.445232
xx = []
yy = []
yy300 = []
yy200 = []

def plot_fiber_data():
    index = 1.05
    lambda0 = 0.400084717e-6
    lambda300 = 0.302704071

    pd_real = 1.393514
    pd_img = 3.076941
    pd_h_real = 1.803938
    pd_h_img = 2.445232
    pd_ref = complex(pd_real, pd_img)
    pd_h_ref = complex(pd_h_real, pd_h_img)

    pd_real_300 = 1.164367
    pd_img_300 = 2.339882
    pd_h_real_300 = 1.455224
    pd_h_img_300 = 1.821829
    pd_ref_300 = complex(pd_real_300, pd_img_300)
    pd_h_ref_300 = complex(pd_h_real_300, pd_h_img_300)



    while index <= 1.95:
        xx.append(index)
        pd_theta_spp = comsol(lambda0, pd_ref, 1.0003+0j, index)
        pd_h_theta_spp = comsol(lambda0, pd_h_ref, 1.0003+0j, index)
        theta = pd_theta_spp - pd_h_theta_spp
        yy.append(theta)

        pd_theta_spp_300 = comsol(lambda300, pd_ref_300, 1.0003+0j, index)
        pd_h_theta_spp_300 = comsol(lambda300, pd_h_ref_300, 1.0003+0j, index)
        theta_300 = pd_theta_spp_300 - pd_h_theta_spp_300
        yy300.append(theta_300)

        index += 0.001

plt.xlabel("index")
# plt.ylabel("Normalized Intensity(a.u.)")
plt.ylabel("ThetaSPP(deg)")

plot_fiber_data()

l1, = plt.plot(xx, yy, c='red', linewidth=1.5, linestyle='-', label=u"400nm")
l2, = plt.plot(xx, yy300, c='blue', linewidth=1.5, linestyle='-', label=u"300nm")
# l3, = plt.plot(x, y3, c='blue', linewidth=1.5, linestyle='-', label=u"Pd-H(Palm)")
plt.legend()
plt.show()
