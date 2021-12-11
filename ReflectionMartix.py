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
    R = abs(r)*abs(r)
    return R


x = []
reflection = []
reflection2 = []
index = 35
while index <= 70:
    x.append(index)
    reflection.append(calculate_ref(30e-9, 250e-9, 1.033012 + 1.98789j, 1.3425, math.radians(index), 1.00029))
    reflection2.append(calculate_ref(30e-9, 250e-9, 1.363482 + 1.323541j, 1.3425, math.radians(index), 1.00029))
    index += 0.1


plt.xlabel("Angle(deg)")
plt.ylabel("ThetaSPP(deg)")


l1, = plt.plot(x, reflection, c='red', linewidth=1.5, linestyle='-', label=u"Pd(Palm)")
l2, = plt.plot(x, reflection2, c='blue', linewidth=1.5, linestyle=':', label=u"Pd(Palm)")
# l3, = plt.plot(x, y3, c='blue', linewidth=1.5, linestyle='-', label=u"Pd-H(Palm)")
plt.legend()
plt.show()