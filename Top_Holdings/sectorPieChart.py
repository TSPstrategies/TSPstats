import pandas as pd
import matplotlib.pyplot as plt

file = "sp500bysector20200723.csv"

def getData(csvName):
    '''the getData() function reads data from a csv with sectors and corresponding percent amounts'''
    df = pd.read_csv(csvName)
    df_indexed = df.set_index('sector')
    return df_indexed

def pieChart(csvName, fileName="CFundbySector.png", title="C Fund by Sector"):
    '''the pieChart() function calls the getData() function to read in a csv file of sectors by percent,
    and then the function charts the sectors by percentage amounts in a pie chart using matplotlib'''
    df_plotted = getData(csvName)
    fig = plt.figure(figsize=(6,6), dpi=200)
    ax = plt.subplot(111)
    title = title
    filename = fileName
    df_plotted.plot(kind='pie', y='percent', ax=ax, autopct='%1.2f%%', legend=False, title=title)
    plt.savefig(filename, bbox_inches='tight')


if __name__ == "__main__":
    pieChart(file)