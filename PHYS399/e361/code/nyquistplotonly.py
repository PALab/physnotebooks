import numpy as np
import matplotlib.pyplot as plt

C = 2.8e-9   # F
R = 5000     # ohm
omega0 = 1/(R*C)
f0 = omega0/(2*np.pi)

f = np.logspace(start=2, stop=6, base=10, num=10001, endpoint=True)
omega = 2.0*np.pi*f

TA = 1/(1-1j*(omega0/omega))

plt.plot(np.real(TA),np.imag(TA))
plt.xlabel('$\Re e(T_A$)')
plt.ylabel('$\Im m(T_A)$')
plt.axis('equal')
plt.savefig('nyquist.pdf')
plt.show()
