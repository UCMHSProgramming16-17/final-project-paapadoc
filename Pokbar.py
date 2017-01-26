#Upload csv, pandas, numpy, and bokeh data
import csv
import pandas as pd
import numpy as np
import bokeh

#open the csv file
df = pd.read_csv('Pokemon.csv')
#Import Bar, output_file, save
from bokeh.charts import Scatter, output_file, save

#Create the graph file
output_file("PokBar.html")
#Put the data from pokemon.csv into a graph
PokBar = Scatter(df, 'Attack', 'Defense', title = "Defense vs. Attack", xlabel = 'Attack', ylabel = 'Defense')

#Save it as Pokmon.html
save(PokBar)