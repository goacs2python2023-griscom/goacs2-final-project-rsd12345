import csv
from math import pi
import pandas as pd

from bokeh.plotting import figure, show
from bokeh.palettes import Category20c
from bokeh.transform import cumsum
from bokeh.layouts import gridplot, row, column

#colors for pie chart
chart_colors = ["blue", "grey"]


#list to hold raw data from files
atlantic_list = []
pacific_list = []


#open and read atlantic.csv
with open("atlantic.csv", mode="r") as file:
    csvFile = csv.reader(file)
    for lines in csvFile:
        atlantic_list.append(lines)

#open and read pacific.csv
with open("pacific.csv", mode="r") as file:
    csvFile = csv.reader(file)
    for lines in csvFile:
        pacific_list.append(lines)



#piechart -- hurricanes vs typhoons

#atlantic

atlantic_dict = {
    "Hurricane":0,
    "Typhoon":0
    }

for weatherEvent in atlantic_list:
    if weatherEvent[5].strip() == "HU":
        atlantic_dict["Hurricane"] += 1
    elif weatherEvent[5].strip() == "TS":
        atlantic_dict["Typhoon"] += 1

print(atlantic_dict["Hurricane"])
print(atlantic_dict["Typhoon"])
print("__________")
atlantic_data = pd.Series(atlantic_dict).reset_index(name="value").rename(columns={"index":"type"})
atlantic_data["angle"] = atlantic_data["value"]/atlantic_data["value"].sum() * 2 * pi
atlantic_data["color"] = chart_colors[:len(atlantic_dict)]

atlantic_pie = figure(height=500, title="Atlantic", toolbar_location=None, tools="hover", tooltips="@country: @value", x_range=(-0.5, 1.0))

atlantic_pie.wedge(x=0, y=1, radius=0.5, start_angle=cumsum('angle', include_zero=True), end_angle=cumsum('angle'),
        line_color="white", fill_color='color', legend_field='type', source=atlantic_data)
atlantic_pie.axis.axis_label = None
atlantic_pie.axis.visible = False
atlantic_pie.grid.grid_line_color = None

#pacific

pacific_dict = {
    "Hurricane":0,
    "Typhoon":0
}
for weatherEvent in pacific_list:
    if weatherEvent[5].strip() == "HU":
        pacific_dict["Hurricane"] += 1
    elif weatherEvent[5].strip() == "TS":
        pacific_dict["Typhoon"] += 1

print(pacific_dict["Hurricane"])
print(pacific_dict["Typhoon"])

pacific_data = pd.Series(pacific_dict).reset_index(name="value").rename(columns={"index":"type"})
pacific_data["angle"] = pacific_data["value"]/pacific_data["value"].sum() * 2 * pi
pacific_data["color"] = chart_colors[:len(pacific_dict)]

pacific_pie = figure(height=500, title="Pacific", toolbar_location=None, tools="hover", tooltips="@country: @value", x_range=(-0.5, 1.0))

pacific_pie.wedge(x=0, y=1, radius=0.5, start_angle=cumsum('angle', include_zero=True), end_angle=cumsum('angle'),
        line_color="white", fill_color='color', legend_field='type', source=pacific_data)
pacific_pie.axis.axis_label = None
pacific_pie.axis.visible = False
pacific_pie.grid.grid_line_color = None


show(row(atlantic_pie, pacific_pie))