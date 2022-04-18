import math
import basic

def add_value(x1, y1, x2, y2, target):
    if target < x1 or target > x2:
        return "target错误"
    val = y1 + (y2-y1)*(target-x1)/(x2-x1)
    return val


print(add_value(292.4, 1.49, 300.09, 1.53, 300))
print(add_value(292.4, 1.878, 300.09, 1.889, 300))

print(add_value(299.510895, 1.160753, 301.107483, 1.16252, 300))
print(add_value(299.510895, 2.315671, 301.107483, 2.327731, 300))


# 多层折射率转换模型
def ref_convert(air_degree, air_n, prism_n):
    theta2 = math.degrees(math.asin(air_n*math.sin(air_degree)/prism_n))

    return theta2


print(basic.convert_refractive_dielectric(1.5295318595578675 + 1.8888712613784135j))
print(basic.convert_refractive_dielectric(1.1612943096772617 + 2.3193655074746897j))
print(basic.convert_refractive_dielectric(3.1414 + 3.3143j))
