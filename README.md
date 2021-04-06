# eg2DIS_Create

This repository contains the files to model the prefactor for the multiplicty ratios for the eg2 experiment.  

The python script CreateDISratio.py prints to the screen the values of zh for a constant distribution.  inside the sctipt, xlo is the lower limit of the range, xhi is the upper limit, and xbins is the number of bins.  The script will print the centroid of the bins "repeat" times.  The output can be saved in a histogram.  The script is run a second time with a different value for "repeat".  WHen the two histograms are divided, a histogram is created that has the prefactor vs zh.
