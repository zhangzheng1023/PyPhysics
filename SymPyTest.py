import sympy as sym
import matplotlib.pyplot as plt
import cmath

# Symbols Defined
d2, d3 = sym.symbols('d_2 d_3')
M, M2, M3 = sym.symbols('M M2 M3')
beta2, beta3 = sym.symbols('beta_2 beta_3')
q1, q2, q3, q4 = sym.symbols('q_1 q_2 q_3 q_4')
n1, theta1, lamda = sym.symbols('n_1 theta_1 lambda')
varepsilon_1, varepsilon_2, varepsilon_3, varepsilon_4 = sym.symbols('varepsilon_1 varepsilon_2 '
                                                                     'varepsilon_3 varepsilon_4')
re1, re2, re3, re4 = sym.symbols('{Re(\\varepsilon_{1})} {Re(\\varepsilon_{2})} '
                                 '{Re(\\varepsilon_{3})} {Re(\\varepsilon_{4})}')
im1, im2, im3, im4 = sym.symbols('{Im(\\varepsilon_{1})} {Im(\\varepsilon_{2})} '
                                 '{Im(\\varepsilon_{3})} {Im(\\varepsilon_{4})}')

varepsilon_1 = varepsilon_1.subs(varepsilon_1, re1 + im1*sym.I)
varepsilon_2 = varepsilon_2.subs(varepsilon_2, re2 + im2*sym.I)
varepsilon_3 = varepsilon_3.subs(varepsilon_3, re3 + im3*sym.I)
varepsilon_4 = varepsilon_4.subs(varepsilon_4, re4 + im4*sym.I)

# =======================================================
varepsilon_1 = varepsilon_1.subs(varepsilon_1, 1.80230625)
varepsilon_2 = varepsilon_2.subs(varepsilon_2, -1.228366932658731 + 5.7781775457630795*sym.I)
varepsilon_3 = varepsilon_3.subs(varepsilon_3, -4.030851883574537 + 5.386931931784143*sym.I)
varepsilon_4 = varepsilon_4.subs(varepsilon_4, 1.0005800840999999)

n1 = n1.subs(n1, 1.3425)

d2 = d2.subs(d2, 40e-9)
d3 = d3.subs(d3, 10e-9)
lamda = lamda.subs(lamda, 300e-9)

# =======================================================


def GenerateQ(varepsilon):
    return sym.sqrt(varepsilon-(n1**2)*(sym.sin(theta1)**2))/varepsilon


q1 = q1.subs(q1, GenerateQ(varepsilon_1))
q2 = q2.subs(q2, GenerateQ(varepsilon_2))
q3 = q3.subs(q3, GenerateQ(varepsilon_3))
q4 = q4.subs(q4, GenerateQ(varepsilon_4))


def GenerateBeta(d, varepsilon):
    return (2*sym.pi*d)/lamda*sym.sqrt(varepsilon-(n1**2)*(sym.sin(theta1)**2))


beta2 = beta2.subs(beta2, GenerateBeta(d2, varepsilon_2))
beta3 = beta3.subs(beta3, GenerateBeta(d2, varepsilon_3))


# Generate Characteristic Matrix
def GenerateMatrix(beta, q):
    return sym.Matrix([
        [sym.cos(beta), -sym.I*sym.sin(beta)/q],
        [-sym.I*q*sym.sin(beta), sym.cos(beta)]
    ])


m2 = GenerateMatrix(beta2, q2)
m3 = GenerateMatrix(beta3, q3)
m = m2*m3

m11 = m[0, 0]
m12 = m[0, 1]
m21 = m[1, 0]
m22 = m[1, 1]

rp = ((m11 + m12*q4)*q1 - (m21 + m22*q4))/((m11 + m12*q4)*q1 + (m21 + m22*q4))

Rp = sym.sympify(abs(rp)**2)

# Rpp = sym.diff(Rp, theta1)

index = 40
x = []
y = []
while index <= 70:
    x.append(index)
    y.append(Rp.evalf(subs={'theta_1': index*sym.pi/180}))
    index += 0.1

plt.xlabel("Angle(deg)")
plt.ylabel("ThetaSPP(deg)")


l1, = plt.plot(x, y, c='red', linewidth=1.5, linestyle='-', label=u"Pd(Palm)")

plt.legend()
plt.show()

