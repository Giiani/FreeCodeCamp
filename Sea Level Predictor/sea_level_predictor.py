from cProfile import label
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

def draw_plot():
    # Read data from file
    df= pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.scatter(x="Year",y='CSIRO Adjusted Sea Level', data=df, label="CSIRO Sea Level")
    
    # Create first line of best fit
    regress = linregress(df['Year'],df['CSIRO Adjusted Sea Level'])
    Ax1= np.arange(df['Year'].min(),2050,1)
    Ay1 = Ax1 * regress.slope + regress.intercept
    
    plt.plot(Ax1, Ay1)
    
    # Create second line of best fit
    df_second = df[df['Year']>=2000]
    
    second_regress = linregress(df_second['Year'],df_second['CSIRO Adjusted Sea Level'])
    Ax2 = np.arange(2000,2050,1)
    Ay2 = Ax2* second_regress.slope + second_regress.intercept
    
    plt.plot(Ax2, Ay2)
    
    # Add labels and title
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")

    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()