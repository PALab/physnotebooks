import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def T(Rs,L,C,omega):
    '''Outputs the transfer function of a L and C in series. Inputs are:
    Rs - the (small, but finite) resistance of a real L and C
    component in series.  L - inductance, C- capacitance, omega -
    angular frequency.'''
    zs = Rs +1j*omega*L + 1/(1j*omega*C)
    return R/(R+zs)


C = 2.2e-9   # F
R = 300     # ohm
L = 10e-3   # H
f = np.logspace(start=2, stop=6, base=10, num=10001, endpoint=True)
omega = 2.0*np.pi*f

omega0 = 1/np.sqrt(L*C)
f0=omega0/(2*np.pi)
Rp = 1000 # tune this with your real data!!
def T(Rp,L,C,omega):
    '''Outputs the transfer function of a L and C in series. Inputs are:
    Rs - the (small, but finite) resistance of a real L and C
    component in series.  L - inductance, C- capacitance, omega -
    angular frequency.'''
    zp = 1/(1/Rp +1j*(omega*C - 1/(omega*L)))
    return R/(R+zp)

# calling the transfer function, for particular input parameters:
TD = T(Rp,L,C,omega)

filename = 'filterD.txt'
df = pd.read_csv(filename,skiprows=3,names=["f","T","phi"], sep='\s+')
plt.plot(df['f'],df['T'])
plt.show()

fig, (ax1, ax2) = plt.subplots(num=1, nrows=2, clear=True)
ax1.semilogx(f, 20*np.log10(np.abs(TD)),label='$T_D$')
ax1.axvline(f0,color='r',linestyle='--')
ax2.semilogx(f, np.angle(TD)*180/np.pi,label='$T_D$')
plt.xlabel('Frequency (Hz)')
ax1.set_ylabel('Magnitude (dB)')
ax2.set_ylabel('Phase Angle (degrees)')
ax1.legend()
ax2.legend()
plt.savefig('filterD.pdf')
plt.show()
