import numpy as np
import matplotlib.pyplot as plt

C = 2.2e-9   # F
R = 10000     # ohm
f0 = 1/(R*C)
omega0 = f0*2*np.pi

f = np.logspace(start=2, stop=6, base=10, num=10001, endpoint=True)
omega = 2.0*np.pi*f

TB = 1/(1+1j*(omega/omega0))

fig, (ax1, ax2) = plt.subplots(num=1, nrows=2, clear=True)
ax1.semilogx(f, 20*np.log10(np.abs(TB)))
ax1.axhline(-3,color='r',linestyle='--')
ax1.axvline(f0,color='r',linestyle='--')
ax2.semilogx(f, np.angle(TB)*180/np.pi)
plt.xlabel('Frequency (Hz)')
ax1.set_ylabel('Magnitude (dB)')
ax2.set_ylabel('Phase Angle (degrees)')
plt.savefig('filterB.pdf')
plt.show()
