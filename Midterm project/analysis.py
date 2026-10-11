# -*- coding: utf-8 -*-
"""
Created on Fri Oct  9 23:40:18 2026

@author: brian
I'm analyzing the data that I collected for my midterm project in this script.
"""
import os
from pathlib import Path
import pandas as pd
from matplotlib import pyplot as plt

cwd = Path(os.getcwd())
dataPath = cwd/"Data.xlsx"
dataset = pd.read_excel(dataPath, "Data")
# %%
dataset.loc[dataset.Location.str.startswith("Jenkins & Felgar"), "shortLocation"] = "Jenkins, across from SEC parking"
dataset.loc[dataset.Location.str.startswith("Felgar"), "shortLocation"] = "Across from Gallogly Hall"
dataset.loc[dataset.Location.str.startswith("Asp"), "shortLocation"] = "Across from Memorial Union"
dataset.loc[dataset.Location.str.startswith("Trout"), "shortLocation"] = "Trout street"

"""Rearranging the data so that as you go down the dataset, you go from east to
west, heading from Trout Street towards the center of the campus ending up at
Memorial Union"""
dataset.loc[dataset.Location.str.startswith("Trout"), "locationIndex"] = 0
dataset.loc[dataset.Location.str.startswith("Jenkins & Felgar"), "locationIndex"] = 1
dataset.loc[dataset.Location.str.startswith("Felgar"), "locationIndex"] = 2
dataset.loc[dataset.Location.str.startswith("Asp"), "locationIndex"] = 3
dataset.sort_values("locationIndex", inplace=True, ignore_index=True)


"""Let's make 2 bar charts.

The 1st bar chart will plot the number of non-public-transit vehicles and the
number of pedestrians at each location. Each location will have 2 bars, 1 for
the number of non-public-transit vehicles I observed and 1 for the number of
pedestrians I observed.

The 2nd bar chart will plot ratios of either non-public-transit vehicles to
pedestrians or pedestrians to non-public-transit vehicles, whichever is greater
than 1
"""

dataset["nonPublicTransit"] = dataset.TotalVehicles - dataset.PublicTransitVehicles
dataset["vehicleToPedestrian"] = dataset.nonPublicTransit/dataset.Pedestrians
dataset["pedestrianToVehicle"] = dataset.Pedestrians/dataset.nonPublicTransit
# dataset.set_index("shortLocation", inplace=True)
# %%
"""Making the 1st bar chart of vehicle & pedestrian volumes (not of ratios)"""
barCharts = plt.Figure((25, 12))
volumeAxes = barCharts.add_subplot(1, 2, 1)
volumeAxes.set_xlabel("Position")
volumeAxes.set_ylabel("Number of vehicles or pedestrians")
# dataset1 = dataset.filter(["nonPublicTransit", "Pedestrians"])
volumeBarChart = volumeAxes.grouped_bar([dataset.nonPublicTransit.tolist(), dataset.Pedestrians.tolist()], tick_labels=dataset.shortLocation.tolist(), labels=["Non-public-transit vehicles", "Pedestrians"])
# volumeAxes.grouped_bar([dataset.nonPublicTransit.tolist(), dataset.Pedestrians.tolist()], tick_labels=dataset.shortLocation.tolist(), labels=["Non-public-transit vehicles", "Pedestrians"])
for bar in volumeBarChart.bar_containers:
    volumeAxes.bar_label(bar)
volumeAxes.grid(axis="y")
volumeAxes.legend()
# %%
"""Making the 2nd bar chart of ratios of traffic volumes"""
ratioAxes = barCharts.add_subplot(1, 2, 2)
ratioAxes.set_xlabel("Position")
ratioAxes.set_ylabel("Ratio")
ratioBarChart = ratioAxes.grouped_bar([dataset.vehicleToPedestrian, dataset.pedestrianToVehicle], tick_labels=dataset.shortLocation, labels=["Non-public-transit vehicle: Pedestrian", "Pedestrian: Non-public-transit vehicle"])
ratioAxes.grid(axis="y")
ratioAxes.legend()

for bar in ratioBarChart.bar_containers:
    ratioAxes.bar_label(bar, fmt="{:.3f}")

figurePath = cwd/"Traffic bar charts.png"
barCharts.savefig(figurePath, dpi=400, bbox_inches="tight")
