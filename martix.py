import cmath
import math
import matplotlib.pyplot as plt

lam0 = 300e-9
z = 35e-9

n_prism = 1.3425
n_metal = 1.16252+2.327731j
n_sample = 1.00029


def calculate_reflection(incident_angle):
    theta_1 = math.radians(incident_angle)
    theta_2 = cmath.acos(cmath.sqrt(1-(n_prism/n_metal)*(math.sin(theta_1)*math.sin(theta_1)))).real
    theta_3 = cmath.acos(cmath.sqrt(1-(n_prism/n_sample)*(math.sin(theta_1)*math.sin(theta_1)))).real

    q1 = n_prism*math.cos(theta_1)
    q2 = n_metal*math.cos(theta_2)
    q3 = n_sample*math.cos(theta_3)

    k0 = 2*math.pi/lam0*n_prism*math.sin(theta_1)

    m11 = cmath.cos(k0*n_metal*z*math.cos(theta_2))
    m12 = complex(0, (-1/q2)*math.sin(k0*n_metal*z*math.cos(theta_2)))
    m21 = complex(0, -1*q2*math.sin(k0*n_metal*z*math.cos(theta_2)))
    m22 = cmath.cos(k0*n_metal*z*math.cos(theta_2))

    r = ((m11 + m12*q3)*q1 - (m21+m22*q3))/((m11 + m12*q3)*q1 + (m21+m22*q3))
    R = abs(r**2)
    return R

x = []
ref = []


index = 0
while index <= 90:
    x.append(index)
    ref.append(calculate_reflection(index))
    index += 0.1


plt.xlabel("Wavelength(μm)")
# plt.ylabel("Normalized Intensity(a.u.)")
plt.ylabel("ThetaSPP(deg)")


l1, = plt.plot(x, ref, c='red', linewidth=1.5, linestyle='-', label=u"Pd(Palm)")
# l3, = plt.plot(x, y3, c='blue', linewidth=1.5, linestyle='-', label=u"Pd-H(Palm)")
plt.legend()
plt.show()



