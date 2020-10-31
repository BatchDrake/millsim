from matplotlib import pyplot as plt 
from millsim import HaloTreeDownloader, HaloPlotter
import traceback
import sys

HALO_COUNT  = 25
MASS_RANGES = [\
    (0, 1e10), (1e10, 1e11), (1e11, 1e12), (1e12, 1e13), (1e13, 1e30)]

dl = HaloTreeDownloader.HaloTreeDownloader()
dl.set_count(HALO_COUNT)

figno = 1

for i in MASS_RANGES:
    print(\
          "Retrieving {0} halos from {1:e} to {2:e} Msun... "\
          .format(HALO_COUNT, i[0], i[1]), end="", flush=True)
    
    try:
        dl.download_mass_range(i)
        halos = dl.get_halo_history()
        print("OK: {0} rows, {1} halos".format(dl.row_count(), len(halos)))
        
        fig, axes = plt.subplots(1, 2)
        plotter = HaloPlotter.HaloPlotter(halos)
        plotter.set_axes(axes[0])
        plotter.plotHalos(\
            figno, \
            "Halo mass evolution ({0} $M_\odot$ to {1} $M_\odot$)".format(\
                plotter.quantityToLatex(i[0]), plotter.quantityToLatex(i[1])))
        
        plotter.set_axes(axes[1])
        plotter.plotHaloMean(\
            figno, \
            "Halo mass evolution (mean, {0} $M_\odot$ to {1} $M_\odot$)".format(\
            plotter.quantityToLatex(i[0]), plotter.quantityToLatex(i[1])),\
            True)

        figno += 1    
        
    except Exception as e:
        print("error: " + str(e))
        
plt.show()
    