#Upload csv, pandas, numpy, and bokeh data
import csv
import pandas as pd
import numpy as np
import bokeh

#open the csv file
df = pd.read_csv('Pokemon.csv')
#Import Bar, output_file, save
from bokeh.charts import Bar, output_file, save
#Create the graph file
output_file("PokemonBar.html")
#Put the data from pokemon.csv into a graph
PokemonBar = Bar(df, 'Type 1', '#', agg='count', title="Number of Pokemon per Type")
#Save it as PokemonBar
save(PokemonBar)