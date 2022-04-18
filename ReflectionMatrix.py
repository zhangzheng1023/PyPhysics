import math
import cmath
import basic
import matplotlib.pyplot as plt


def calculate_ref(thickness, lam0, die_2, n_prism, theta_1, n_air):
    beta_2 = 2*math.pi*thickness/lam0*cmath.sqrt(die_2-(n_prism*n_prism*math.sin(theta_1)*math.sin(theta_1)))

    q_1 = cmath.sqrt(n_prism**2-(n_prism*n_prism*math.sin(theta_1)*math.sin(theta_1)))/n_prism**2
    q_2 = cmath.sqrt(die_2-(n_prism*n_prism*math.sin(theta_1)*math.sin(theta_1)))/die_2
    q_3 = cmath.sqrt(n_air**2 - (n_prism * n_prism * math.sin(theta_1) * math.sin(theta_1))) / n_air**2

    m11 = cmath.cos(beta_2)
    m12 = complex(0, -1*cmath.sin(beta_2)/q_2)
    m21 = complex(0, -1*q_2*cmath.sin(beta_2))
    m22 = cmath.cos(beta_2)

    r = ((m11 + m12*q_3)*q_1 - (m21 + m22*q_3))/((m11 + m12*q_3)*q_1 + (m21 + m22*q_3))
    # R = abs(r)*abs(r)
    R = abs(r)**2
    return R


x = []
reflection = []
reflection2 = []
index = 0
while index <= 89.9:
    x.append(index)
    reflection.append(calculate_ref(10e-9, 488e-9, -4.030851883574537+5.386931931784143j,
                                    1.68, math.radians(index), 1.00029))
    # reflection2.append(calculate_ref(10e-9, 300e-9, 2.005509 + 2.83011j, 1.3425, math.radians(index), 1.00029))
    index += 0.1


plt.xlabel("Angle(deg)")
plt.ylabel("ThetaSPP(deg)")


l1, = plt.plot(x, reflection, c='red', linewidth=1.5, linestyle='-', label=u"Pd(Palm)")
# l2, = plt.plot(x, reflection2, c='blue', linewidth=1.5, linestyle=':', label=u"Pd(Palm)")
# l3, = plt.plot(x, y3, c='blue', linewidth=1.5, linestyle='-', label=u"Pd-H(Palm)")
plt.legend()
plt.show()

print(math.degrees(math.asin(math.sin(math.radians(52.5-10))*1.3425/1.00029)))