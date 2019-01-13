from bokeh.plotting import figure, output_file, show
import pandas as pd

df = pd.read_csv("biostats.csv")

p = figure(width=500, height=250, x_axis_type="datetime", sizing_mode='stretch_both')

p.line(df["Day"], df["Calories"], color="Blue", alpha=0.5)

output_file("calorie_graph.html")
show(p)
