# coding=utf-8
import spp


# 计算Ag在450nm波长时相关属性
# Ag在450.9nm时，折射率N=0.04+2.657j
def silver_450nm_test():
    lambda_0 = 450.9e-9
    silver_450nm_refractive = 0.04+2.657j
    print ("Ag在450.9nm下，复折射率为{}".format(silver_450nm_refractive))
    silver_450nm_dielectric = spp.convert_refractive_dielectric(silver_450nm_refractive)
    print ("Ag在450.9nm下，复介电常数为{}".format(silver_450nm_dielectric))
    # 不妨设电介质为空气
    air_refractive = 1.00029+0j
    air_dielectric = spp.convert_refractive_dielectric(air_refractive)
    beta = spp.calculate_propagation_constant(silver_450nm_dielectric, air_dielectric, lambda_0)
    print ("Ag在450.9nm下，以Air为电介质层的传播常数beta={}".format(beta))
    length = spp.calculate_spp_propagation_length(beta)
    print ("Ag在450.9nm下，以Air为电介质层的传播长度L={}微米".format(length))


silver_450nm_test()