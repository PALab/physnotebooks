import numpy as np
import matplotlib.pyplot as plt

C = 2.2e-9   # F
R = 10000     # ohm
f0 = 1/(R*C)
omega0 = f0*2*np.pi

f = np.logspace(start=2, stop=6, base=10, num=10001, endpoint=True)
omega = 2.0*np.pi*f

TA = 1/(1-1j*(omega0/omega))
TB = 1/(1+1j*(omega/omega0))

fig, (ax1, ax2) = plt.subplots(num=1, nrows=2, clear=True)
ax1.semilogx(f, 20*np.log10(np.abs(TA)),'k', label='$T_A$')
ax1.semilogx(f, 20*np.log10(np.abs(TB)),'--r', label='$T_B$')
#ax1.axhline(-3,color='r',linestyle='--')
ax1.axvline(f0,color='r',linestyle='-.', label='$f_0$')
ax1.legend()
ax2.semilogx(f, np.angle(TA)*180/np.pi,'k', label='$T_A$')
ax2.semilogx(f, np.angle(TA)*180/np.pi,'--r', label='$T_B$')
ax2.legend()
plt.xlabel('Frequency (Hz)')
ax1.set_ylabel('Magnitude (dB)')
ax2.set_ylabel('Phase Angle (degrees)')
plt.savefig('filterA.pdf')
plt.show()
