import matplotlib.pyplot as plt
from PyEMD import EMD

import van_der_pol as vdp

x, t = vdp.getSignal(noise=.5)
emd = EMD()
IMF = emd(x, t)

N = IMF.shape[0] + 1

plt.subplot(N, 1, 1)
plt.plot(t, x, 'r')
plt.title("Van der pol")

for n, imf in enumerate(IMF/2):
    plt.subplot(N, 1, n + 2)
    plt.plot(t, imf, 'g')
    plt.title("IMF " + str(n + 1))

plt.tight_layout()
plt.savefig('simple_example')
plt.show()
