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
from nidaqmx.constants import TerminalConfiguration

import nidaqmx

class CPC:
    def __init__(self,entriesDAQ,entriesScan,entriesHV):
        self.setVal(entriesDAQ,entriesScan,entriesHV)

    def setVal(self,entriesDAQ,entriesScan,entriesHV):
        self.device_name=str(entriesDAQ[0].get())
        self.Vmin=float(entriesDAQ[1].get())
        self.Vmax=float(entriesDAQ[2].get())
        self.sampleTime=float(entriesScan[2].get())
        self.mode=int(entriesScan[6].get())
        self.time_rate = 0.01
        self.N = int(self.sampleTime/self.time_rate*0.5)

    def getC(self):
        C_all = []
        t_all = []
        task = nidaqmx.Task()
        task.ai_channels.add_ai_voltage_chan(self.device_name,min_val=self.Vmin,max_val=self.Vmax,terminal_config=TerminalConfiguration.RSE)
        task.start()
        start_time = time.perf_counter()
        for i in np.arange(self.N):
            data = task.read()
            d_time = time.perf_counter()-start_time
            C_all.append(data)
            t_all.append(d_time)
            time.sleep(self.time_rate)
        task.stop()
        task.close()
        print(np.average(C_all))
        if(self.mode==-1):
            ret=10**(np.average(C_all)-3)
        return ret

    def timeOpt(self):
        C_all = []
        t_all = []
        task = nidaqmx.Task()
        task.ai_channels.add_ai_voltage_chan(self.device_name,min_val=self.Vmin,max_val=self.Vmax)
        task.start()
        start_time = time.perf_counter()
        for i in np.arange(self.N):
            data = task.read()
            d_time = time.perf_counter()-start_time
            C_all.append(data)
            t_all.append(d_time)
            time.sleep(self.time_rate)
        task.stop()
        task.close()
        self.N = int(self.N/d_time*self.sampleTime)
