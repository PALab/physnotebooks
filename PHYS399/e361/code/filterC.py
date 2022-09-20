import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

filename = './filterC.txt'
df = pd.read_csv(filename,skiprows=3,names=["f","T","phi"], sep='\s+')
print(df)

#linear scale:
absT = 10**(df['T']/20)

#plt.semilogx(df['f'],absT,'o')
plt.plot(df['f'],absT,'o')
plt.show()

plt.semilogx(df['f'], absT**2,'o')
plt.show()

C = 22e-9   # F
R = 82     # ohm
L = 10e-3   # H
f = np.logspace(start=2, stop=6, base=10, num=10001, endpoint=True)
omega = 2.0*np.pi*f
omega0 = 1/np.sqrt(L*C)
f0=omega0/(2*np.pi)

#Rs = 100 # tune this with your real data!!

def T(Rs,L,C,omega):
    '''Outputs the transfer function of a L and C in series. Inputs are:
    Rs - the (small, but finite) resistance of a real L and C
    component in series.  L - inductance, C- capacitance, omega -
    angular frequency.'''
    zs = Rs +1j*omega*L + 1/(1j*omega*C)
    return R/(R+zs)


# How big is Rs? Let's compare a few values to the real data:
Rss = [10, 100, 1000]
# calling the transfer function, for particular input parameters:
fig, (ax1, ax2) = plt.subplots(num=1, nrows=2, clear=True)
ax1.semilogx(df['f'], df['T'],label='data',marker='o')
ax2.semilogx(df['f'], df['phi'],label='data',marker='o')
ax2.axvline(f0,color='r',linestyle='--',label='$f_0$')
ax1.axvline(f0,color='r',linestyle='--',label='$f_0$')
for Rs in Rss:
    TC = T(Rs,L,C,omega)
    ax1.semilogx(f, 20*np.log10(np.abs(TC)),label=str(Rs))
    ax2.semilogx(f, np.angle(TC)*180/np.pi,label=str(Rs))
    
plt.xlabel('Frequency (Hz)')
ax1.set_ylabel('Magnitude (dB)')
ax2.set_ylabel('Phase Angle (degrees)')
ax1.legend()
ax2.legend()
#plt.savefig('filterC.pdf')
plt.show()
