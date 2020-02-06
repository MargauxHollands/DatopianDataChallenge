'''
Created on 6 Feb 2020

@author: Margaux
'''
import altair as alt
import pandas as pd

# Read csv to DataFrame
dfDaily = pd.read_csv('Data/DailyPrices.csv')
dfMonthly = pd.read_csv('Data/MonthlyPrices.csv')
# Plot data
chartDaily = alt.Chart(dfDaily).mark_line().encode(
    x=alt.X('Date', axis=alt.Axis(labelOverlap=True)),
    y='Price (Dollars per Million Btu)'
    ).properties(
    width = 1000,
    )

chartMonthly = alt.Chart(dfMonthly).mark_line().encode(
    x = alt.X('Date', axis=alt.Axis(labelOverlap=True)),
    y = 'Price (Dollars per Million Btu)'
    ).properties(
    width = 1000,
    )

# Save Graph
chartDaily.save('DailyPricesGraph.html')
chartMonthly.save('MonthlyPricesGraph.html')