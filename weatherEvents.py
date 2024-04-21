import csv
from math import pi
import pandas as pd
import numpy as np

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

#piechart - atlantic vs pacific

combined_dict = {
    "Atlantic":len(atlantic_list),
    "Pacific":len(pacific_list)
}

atlantic_data = pd.Series(combined_dict).reset_index(name="value").rename(columns={"index":"type"})
atlantic_data["angle"] = atlantic_data["value"]/atlantic_data["value"].sum() * 2 * pi
atlantic_data["color"] = chart_colors[:len(combined_dict)]

pie_chart = figure(height=500, title="Number of Storms - Atlantic vs Pacific", toolbar_location=None, tools="hover", tooltips="@country: @value", x_range=(-0.5, 1.0))

pie_chart.wedge(x=0, y=1, radius=0.5, start_angle=cumsum('angle', include_zero=True), end_angle=cumsum('angle'),
        line_color="white", fill_color='color', legend_field='type', source=atlantic_data)
pie_chart.axis.axis_label = None
pie_chart.axis.visible = False
pie_chart.grid.grid_line_color = None


#bar graph - average wind comparison

oceans = ["Atlantic", "Pacific"]

average_winds = []

#atlantic
atlantic_winds = 0
for weatherEvent in atlantic_list:
    atlantic_winds += int(weatherEvent[8])

average_winds.append(atlantic_winds/(len(atlantic_list)+1))

#pacific
pacific_winds = 0
for weatherEvent in pacific_list:
    pacific_winds += int(weatherEvent[8])

average_winds.append(pacific_winds/(len(pacific_list)+1))
print(average_winds)

bar_graph = figure(x_range=oceans, title="Atlantic vs Pacific Average Max Winds", x_axis_label="Ocean", y_axis_label="Average Wind (MPH)")
bar_graph.vbar(x=oceans, top=average_winds, width=0.5)

show(row(pie_chart, bar_graph))


#ID,Name,Date,Time,Event,Status,Latitude,Longitude,Maximum Wind,Minimum Pressure,Low Wind NE,Low Wind SE,Low Wind SW,Low Wind NW,Moderate Wind NE,Moderate Wind SE,Moderate Wind SW,Moderate Wind NW,High Wind NE,High Wind SE,High Wind SW,High Wind NW