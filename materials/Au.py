# coding=utf-8
import basic
import matplotlib.pyplot as plt


def au_dielectric_complex(lambda_0):
    lambda_c = 8.9342e-6
    lambda_p = 1.6826e-7
    epsilon_complex = 1 - (lambda_0**2*lambda_c)/(lambda_p**2*(lambda_c+complex(0, lambda_0)))
    return epsilon_complex


# Au材料的折射率实部的可视化
x = []
y = []
wavelength = 400e-9
while wavelength <= 900e-9:
    x.append(wavelength*1e9)
    y.append(basic.convert_dielectric_refractive(au_dielectric_complex(wavelength)).real)
    wavelength = wavelength + 0.1e-9
plt.plot(x, y)
plt.show()