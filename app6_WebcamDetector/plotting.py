# generate bokeh plot
# imports
from datetime import datetime as dt
from bokeh.plotting import figure
from bokeh.io import output_file, show
from bokeh.models import HoverTool, ColumnDataSource
import pandas

# get DataFrame
link=r"D:\dev\practice_workspace\app6_WebcamDetector\resources\Times.csv"
df=pandas.read_csv(link,parse_dates=["Start","End"])

# debugging data
# print(df.columns)
# print(len(df))
# print(df["Start"])
# print(df["End"])

# setup ColumnDataSource
df["Start_string"]= df["Start"].dt.strftime("%Y-%m-%d %H:%M:%S")
df["End_string"]= df["End"].dt.strftime("%Y-%m-%d %H:%M:%S")
cds=ColumnDataSource(df)

# generate figure and set attributes
p=figure(plot_width=1000,plot_height=150, x_axis_type="datetime", sizing_mode="scale_both")
p.title.text="Motion Graph"
p.title.text_color="Gray"
p.title.text_font="times"
p.title.text_font_style="bold"
p.title.text_font_size="20pt"
p.title.align="center"

p.yaxis.minor_tick_line_color=None
p.ygrid[0].ticker.desired_num_ticks=1

# setup HoverTool
hover=HoverTool(tooltips=[("Start","@Start_string"), ("End","@End_string")])
p.add_tools(hover)

# input quadrant data and display
q=p.quad(left="Start",right="End",bottom=0, top=1, color="green", source=cds)
output_file(r"D:\dev\practice_workspace\app6_WebcamDetector\resources\timegraph.html")
show(p)
