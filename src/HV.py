import datetime
import time
import numpy as np
import threading

from matplotlib import pyplot as plt
import matplotlib.animation as animation
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
import matplotlib.ticker as ptick

import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo

import nidaqmx

class HV:
    def __init__(self,entriesDAQ,entriesHV):
        self.setVal(entriesDAQ,entriesHV)

    def setVal(self,entriesDAQ,entriesHV):
        self.device_name=str(entriesDAQ[3].get())
        self.slope=float(entriesHV[0].get())
        self.bias=float(entriesHV[1].get())
        self.Vmin=float(entriesDAQ[4].get())
        self.Vmax=float(entriesDAQ[5].get())

    def HVout(self,V):
        Vin=(V-self.bias)/self.slope
        task=nidaqmx.Task()
        task.ao_channels.add_ao_voltage_chan(self.device_name,min_val=self.Vmin,max_val=self.Vmax)
        task.start()
        print(Vin)
        task.write(Vin)
        task.close()
