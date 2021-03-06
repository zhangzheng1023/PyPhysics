# coding=utf-8
import cmath
import math


# 将复折射率转换为复介电常数
def convert_refractive_dielectric(refractive_complex):
    dielectric_complex = refractive_complex**2
    return dielectric_complex


# 将复介电常数转换为复折射率
def convert_dielectric_refractive(dielectric_complex):
    refractive_complex = cmath.sqrt(dielectric_complex)
    return refractive_complex


# 计算SPP界面的传播常数
# 传入dielectric_complex_1为金属的复介电常数
# dielectric_complex_2为电介质的复介电常数，lambda_0为对应的波长
def calculate_propagation_constant(dielectric_complex_1, dielectric_complex_2, lambda_0):
    k0 = 2*math.pi/lambda_0
    beta = k0*cmath.sqrt((dielectric_complex_1*dielectric_complex_2)/(dielectric_complex_1+dielectric_complex_2))
    return beta


# 计算Kretschmann结构的激发角度theta
# 传入beta为对应频率的SPP传播常数，dielectric_complex_3为激发金属下层的复介电常数
# lambda_0为对应的激发频率
def calculate_kretschmann_theta(beta, dielectric_constant_3, lambda_0):
    beta_real = beta.real
    k = (2*math.pi/lambda_0)*math.sqrt(dielectric_constant_3)
    theta = math.asin(beta_real/k)
    return theta


# 计算激发SPP的传播长度
# 传入beta为对应频率的SPP传播常数
def calculate_spp_propagation_length(beta):
    length = 1/(2*beta.imag)*1e6
    return length



