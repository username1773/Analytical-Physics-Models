# Ideal Electron Simulations

This folder contains Python scripts exploring **Random walks of Electrons** and related statistical properties. The focus is on **Computational Experimentation** to understand electron motion and its probabilistic behavior.

---

## Overview

The simulations implement random walks to model electron trajectories. The scripts allow for:

- Generating **3D random walks** of electrons  
- Creating **Histograms** of positional distributions  
- Calculating **Averages and Statistical properties** of the electron positions  

These models provide a computational way to **visualize randomness, study distributions, and explore statistical behavior** in a simplified physical context.

---

## Conclusion

From the simulations:

- The **Mean displacement** for one electron for a very large walk is approaching to zero.  
- The **Mean squared displacement** grows linearly with the number of steps \(n\), consistent with standard random walk theory.

---

## Notes

- The simulations are based on idealized assumptions for electron motion.
 
---
## Files and Descriptions

- `2elec3d.py` – Simulates trajectories of two electrons in 3D space.  
- `3dhist.py` – Creates 3D histograms of electron positions after multiple random walks in 2D.  
- `3dwalk.py` – Simulates a single 3D random walk of an electron.  
- `Histogram.py` – Generates histograms of electron positions in 1D.  
- `2ehistogram.py` – Generates histograms of collison frequency for two electrons.  
- `2electron.py` – Simulates random walks of two electrons in 1D.  
- `3dmean.py` – Calculates mean and mean-squared displacement for 3D walks.  
- `means.py` – Calculates mean and mean-squared displacement for 1D walks.  
- `Walkplot.py` – Plots trajectories of random walks in 1D.  
- `README.md` – Documentation for this folder.

## Contributing

Additional simulations, improved analysis, or visualization enhancements are welcome. Please maintain consistency and document any new additions.

