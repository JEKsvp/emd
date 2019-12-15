import matplotlib.pyplot as plt
from PyEMD import EMD
import sin_signal as ss

s, t = ss.getSignal()
emd = EMD()
IMF = emd(s, t)

N = IMF.shape[0] + 1

plt.subplot(N, 1, 1)
plt.plot(t, s, 'r')
plt.title("Sin signal")

for n, imf in enumerate(IMF/2):
    plt.subplot(N, 1, n + 2)
    plt.plot(t, imf, 'g')
    plt.title("IMF " + str(n + 1))

plt.tight_layout()
plt.savefig('simple_example')
plt.show()
