from sjvisualizer import DataHandler, Canvas, BarRace, StaticImage, PieRace, LineChart, StackedBarChart
import pandas as pd
import json
#import bar_chart_race as chart


df = DataHandler.DataHandler(excel_file='./data.xlsx',number_of_frames = 960).df

#some hard coded colors. If the team names change, these colors wont be used. This should really be moved to a seperate scrript that builds the colors JSON
#from the dynamic team names returned from the API but not going to do that now.

colors = { "Greener Pastures":[198,40,40], "Delta 49ers": [46,125,50], "CPI": [255,214,0], "Pollard Greens": [3,155,229],
          "Reaper's Keeper": [236,64,122], "The Smokin Doobies":[106,27,154], "Danzel's Little Bitch":[0,172,193], "The Cockblockers":[255,111,0],
          "The Dudes": [21,101,192], "PlugUglys": [102,187,106], "My Name's Jeff": [156,39,176], "Figure it out or Deets swears": [204,174,117]}


canvas = Canvas.canvas()
bar_chart = BarRace.bar_race(df=df, canvas=canvas.canvas, number_of_bars=12, colors=colors)
#bar_chart = StackedBarChart.stacked_bar_chart(df=df, canvas=canvas.canvas, colors=colors)

canvas.add_sub_plot(bar_chart)

canvas.add_title("Total Points Earned 2000-2022", color=(0,0,0))

#canvas.add_time(df=df)

canvas.play(fps=30)






