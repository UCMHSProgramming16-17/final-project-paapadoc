#Upload csv, pandas, numpy, and bokeh data
import csv
import pandas as pd
import numpy as np
import bokeh

#open the csv file
df = pd.read_csv('Pokemon.csv')
#Import Bar, output_file, save
from bokeh.charts import Scatter, output_file, save
#Put the data from pokemon.csv into a graph
output_file("PokBar.html")
PokBar = Scatter(df, 'Attack', 'Defense', title = "Defense vs. Attack", xlabel = 'Attack', ylabel = 'Defense')
#Create the graph file

#Save it as Pokmon.html
save(PokBar)