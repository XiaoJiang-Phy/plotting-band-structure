"""
==============================
To plot the band structure
==============================
Getting EIGENVAL, DOSCAR and POSCAR by vasp.
By use the vaspkit deal with above data, it can get Band.dat or Reformatted_Band.dat.
"""
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

band = np.loadtxt('REFORMATTED_BAND.dat')  # import band data
#band_UP = np.loadtxt('REFORMATTED_BAND_UP.dat')
#band_DW = np.loadtxt('REFORMATTED_BAND_DW.dat')

label = pd.read_csv('KLABELS')  # import modified KLABELS
label = label.values.tolist()
klabel = np.shape(label)[0]


# extracting the number of k points and the number of energy bands
shape = np.shape(band)
# shape = np.shape(band_UP)
kpoints = shape[0]
n_band = shape[1]-1  # The first column is kpath
k_max = band[-1,0]
# k_max = band_UP[-1,0]

# labeling high symmetry point
Label=[]
Scale = []
for n in range(klabel):
    Label.append(label[n][0])
    Scale.append(label[n][1])

fig, ax= plt.subplots(figsize=(8.,6.),dpi=600)
ax.set_xlim(0.,k_max)    # the range of kpoints
ax.set_ylim(-2.,3.)      # the range of energy, fermi energy is adjusted to 0 eV

#ax.set_xlabel(r'$\mu_O$ $(eV)$',fontsize=18)
ax.set_ylabel("Energy (eV)",fontsize=18)

plt.xticks(Scale,Label,fontsize=12)
plt.yticks(fontsize=18)

# labeling high symmetry point
for i in range(klabel):
    ax.axvline(x=label[i][1],linewidth=1.5,linestyle='--',color='k')


# Label the Fermi level
ax.axhline(y=0.,linewidth=1.5,linestyle='--',color='k')

ax.plot(band[:,0], band[:,1:-1], color='blue')
# ax.plot(band_UP[:,0], band_UP[:,1:-1], color='blue')
# ax.plot(band_DW[:,0], band_DW[:,1:-1], color='red')

fig.tight_layout()
fig.savefig('Band.pdf')
fig.savefig('Band.png',format='png')

#print(label[0][1])




