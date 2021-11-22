# coding=utf-8
import math
import basic


# 计算Ag在450nm波长时相关属性
# Ag在450.9nm时，折射率N=0.04+2.657j
# Ag在659.5nm时，折射率N=0.05+4.483j
def silver_659nm_test():
    lambda_0 = 659.5e-9
    silver_659nm_refractive = 0.05+4.483j
    print ("Ag在659nm下，复折射率为{}".format(silver_659nm_refractive))
    silver_659nm_dielectric = basic.convert_refractive_dielectric(silver_659nm_refractive)
    print ("Ag在659nm下，复介电常数为{}".format(silver_659nm_dielectric))
    # 不妨设电介质为空气
    air_refractive = 1.00029+0j
    air_dielectric = basic.convert_refractive_dielectric(air_refractive)
    beta = basic.calculate_propagation_constant(silver_659nm_dielectric, air_dielectric, lambda_0)
    print ("Ag在659nm下，以Air为电介质层的传播常数beta={}".format(beta))
    length = basic.calculate_spp_propagation_length(beta)
    print ("Ag在659nm下，以Air为电介质层的传播长度L={}微米".format(length))
    dielectric_constant_3 = basic.convert_refractive_dielectric(1.6)
    print (dielectric_constant_3)
    theta = basic.calculate_kretschmann_theta(beta, dielectric_constant_3, lambda_0)
    print ("Ag在659nm下，以Air为电介质层，折射率为1.6的棱镜激发SPP\n入射角度theta={}[rad]，{}[deg]"
           .format(theta, math.degrees(theta)))


# 仿真取refractive_2 = 1.05
# refractive_3 = 1.75
def comsol_test():
    lambda_0 = 659.5e-9
    silver_659nm_refractive = 0.05 + 4.483j
    silver_659nm_dielectric = basic.convert_refractive_dielectric(silver_659nm_refractive)
    refractive_2 = 1.05+0j
    dielectric_2 = basic.convert_refractive_dielectric(refractive_2)
    beta = basic.calculate_propagation_constant(silver_659nm_dielectric, dielectric_2, lambda_0)
    length = basic.calculate_spp_propagation_length(beta)
    dielectric_constant_3 = basic.convert_refractive_dielectric(1.75)
    theta = basic.calculate_kretschmann_theta(beta, dielectric_constant_3, lambda_0)
    print ("SPP传播长度为{}微米\ntheta角度为{}[rad]{}[deg]\n对应的alpha角度为{}[deg]"
           .format(length, theta, math.degrees(theta), (90+math.degrees(theta))/2))


comsol_test()



