# TDMA control with DAQ (NI)
## 1. Overview
This code allows controlling 2 DMA's, their respective HV units, and a CPC for conducting TDMA measurements.  This code works with GUI as shown in the figure below.

<img width="1000" alt="fig1" src="https://user-images.githubusercontent.com/62391931/229002061-9c3ec45d-a4f5-4414-8076-6cedfea41ca8.png">

## 2. Usage
### 2.1. Executable version
TBA 
...

### 2.2. Run from source code
* For Anaconda user (you can get Anaconda from [here](https://www.anaconda.com/))
Most of labraries are installed for Anaconda user case but you only need to download NI-DAQ driver from this [link](https://www.ni.com/en-us/support/downloads/drivers/download.ni-daqmx.html#460239).  After the installation, you can run `HV.py` from any console like Powershell Prompt or JupyterLab.
* For not Anaconda user
You need to install the modules if it isn't: Numpy, Tkinter, Matplotlib, and [NI-DAQ driver](https://www.ni.com/en-us/support/downloads/drivers/download.ni-daqmx.html#460239), then you can run `HV.py`.  Here, the explanation is brielf since "not Anaconda" user may know a lot how to install and use it.

## Post-processing

For post-processing these measurements use the following GitHub repository:
  [Bidimensional_TDMA_inversion](https://github.com/Aerosol-Lab/Bidimensional_TDMA_inversion)

## Authors
* Dr. José Morán
* Dr. Tomoya Tamadate
* Hogan Lab.
* [Home page](https://hoganlab.umn.edu/)/[LinkedIn](https://www.linkedin.com/in/hogan-lab-994a3a246/)
* University of Minnesota
* HoganLaboratory[at]umn.edu
