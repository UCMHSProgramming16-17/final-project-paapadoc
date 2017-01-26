#Upload csv, pandas, numpy, and bokeh data
import csv
import pandas as pd
import numpy as np
import bokeh

#open the csv file
df = pd.read_csv('Pokemon.csv')
#Import Bar, output_file, save
from bokeh.charts import Bar, output_file, save
#Create the Graph file
output_file("PokeBar.html")
#Put the data from pokemon.csv into a graph
PokeBar = Bar(df, 'Type 2', '#',  agg = 'count', title="Number of Pokemon per Secondary Type")
#Save it as PokeBar
save(PokeBar)