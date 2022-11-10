import numpy as np
import matplotlib.pyplot as plt
import sys
import tkinter
np.set_printoptions(threshold=sys.maxsize)


thtw = 32
cntttt = 8*thtw
napiecie_v = 5
przk_dane = (np.random.rand(10000)>0.5).astype(int)

procek = np.arange(0,2*len(przk_dane)) % 2

get_kod_ami = 1*przk_dane; ostatni = 0 


for ii in range(0,len(przk_dane)):
  if (get_kod_ami[ii]==1) and (ostatni==0):
    get_kod_ami[ii] = napiecie_v
    ostatni=1
  if (get_kod_ami[ii]==1) and (ostatni==1):
    get_kod_ami[ii]= -napiecie_v
    ostatni = 0
    kodowanie_clk = np.repeat(procek,thtw)



kolejnosc_danych = np.repeat(przk_dane,2*thtw)
kodowanie_nrzi = napiecie_v*kolejnosc_danych
kodowanie_nrz = napiecie_v*(2*kolejnosc_danych - 1)
kodowanie_rz = napiecie_v * (kolejnosc_danych * (1 - kodowanie_clk))
kodowanie_ami = np.repeat(get_kod_ami,2*thtw)
kodowanie_manchester = napiecie_v* (2*np.logical_xor(kolejnosc_danych,kodowanie_clk).astype(int)-1)



print("CLK= ", kodowanie_clk)
print("DATA= ", kolejnosc_danych)
print("NRZI= ", kodowanie_nrzi)
print("NRZ= ", kodowanie_nrz)
print("RZ= ", kodowanie_rz)
print("AMI= ", kodowanie_ami)
print("PE(MANCHESTER)= ", kodowanie_manchester)



fig, ax = plt.subplots(7,1, sharex='col', figsize=(14, 18), facecolor='white')
plt.get_current_fig_manager().set_window_title("Rodzaje kodowań sygnałów")
plt.text(-36, 74, 'CLK', size=20, color='red', style='italic')
plt.text(-36, 61, 'DATA', size=20, color='green', style='italic')
plt.text(-36, 48, 'NRZI', size=20, color='purple', style='italic')
plt.text(-36, 35, 'NRZ', size=20, color='purple', style='italic')
plt.text(-36, 21, 'RZ', size=20, color='purple', style='italic')
plt.text(-36, 8, 'AMI', size=20, color='purple', style='italic')
plt.text(-36, -5, 'PE', size=20, color='purple', style='italic')

ax[0].plot(kodowanie_clk[0:1500], color="red");ax[0].set_title('Symulacja poszczególnych typów kodowań', color="black", size=20)

ax[1].plot(kolejnosc_danych[0:1500], color="green", linestyle="--");ax[1].set_title('')

ax[2].plot(kodowanie_nrzi[0:1500], color="purple");ax[2].set_title('')

ax[3].plot(kodowanie_nrz[0:1500], color="purple");ax[3].set_title('')

ax[4].plot(kodowanie_rz[0:1500], color="purple");ax[4].set_title('') 

ax[5].plot(kodowanie_ami[0:1500], color="purple");ax[5].set_title('')

ax[6].plot(kodowanie_manchester[0:1500], color="purple");ax[6].set_title('')

plt.show()

# JAN KUPCZYK
