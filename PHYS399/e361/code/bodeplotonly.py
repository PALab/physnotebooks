import numpy as np
import matplotlib.pyplot as plt

C = 2.8e-9   # F
R = 5000     # ohm
omega0 = 1/(R*C)
f0 = omega0/(2*np.pi)

f = np.logspace(start=2, stop=6, base=10, num=10001, endpoint=True)
omega = 2.0*np.pi*f

TA = 1/(1-1j*(omega0/omega))

# Find the cut off frequency:
print(np.abs(TA))
difference_array = np.abs(np.abs(TA)-1/np.sqrt(2))
index = difference_array.argmin()
cutofff = f[index]

fig, (ax1, ax2) = plt.subplots(num=1, nrows=2, clear=True)
ax1.semilogx(f, 20*np.log10(np.abs(TA)))
ax1.axhline(-3,color='r',linestyle='--')
ax1.axvline(cutofff,color='r',linestyle='--')
ax2.semilogx(f, np.angle(TA)*180/np.pi)
plt.xlabel('Frequency (Hz)')
ax1.set_ylabel('Magnitude (dB)')
ax2.set_ylabel('Phase Angle (degrees)')
plt.savefig('bodeplot.pdf')
plt.show()
