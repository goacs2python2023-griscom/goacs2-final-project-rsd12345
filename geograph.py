import xyzservices.providers as xyz

from bokeh.plotting import figure, show

# range bounds supplied in web mercator coordinates
p = figure(x_range=(-20000000, -1000000), y_range=(-9000000, 12000000),
           x_axis_type="mercator", y_axis_type="mercator")
p.add_tile(xyz.OpenStreetMap.Mapnik)

show(p)