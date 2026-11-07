# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 19:19:17 2026

@author: brian

This script creates histograms to answer question 3 in the lab
"""
import os
from pathlib import Path
import pandas as pd
from matplotlib import pyplot as plt
import numpy as np

cwd = Path(os.getcwd())
dataFolder = cwd/"Earthquakes_and_Alaska"
dataPath = dataFolder/"Year and intensity of each earthquake.csv"
data = pd.read_csv(dataPath)
# %%
histograms = plt.figure("Earthquake histograms", (15, 6), 400)
yearsSubplot = histograms.add_subplot(1, 2, 1)
yearsSubplot.hist(data.year)
yearsSubplot.set_xlabel("Year")
yearsSubplot.set_ylabel("Number of earthquakes per decade")
yearsSubplot.set_xticks(np.arange(1900, 2001, 10))
yearsSubplot.grid()

intensitySubplot = histograms.add_subplot(1, 2, 2)
intensitySubplot.hist(data.intensity)
intensitySubplot.set_xlabel("Modified Mercalli Intensity")
intensitySubplot.set_ylabel("Number of earthquakes at each intensity")
intensitySubplot.set_xticks(np.arange(2, 12))
intensitySubplot.grid()
# %%
# Exporting the figure
figurePath = cwd/"Earthquakes in Alaska histograms.png"
if os.path.exists(figurePath) is False:
    histograms.savefig(figurePath, bbox_inches="tight")
