import numpy as np
import matplotlib.pyplot as plt
import argparse

# l'argument parser
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--input", required = True,
                help = "Chemin vers le fichier video")
args = ap.parse_args()
filename= args.input

#r=np.load(filename)
#Ecriture de la version c++
r=np.loadtxt(filename)
    
x=np.arange(r.size)
print r,x


fig, ax = plt.subplots(figsize=(8, 4))
ax.hist(-r[~np.isnan(r)],200,histtype='step',
        cumulative=True)
#ax.plot(x,r)




plt.show()
