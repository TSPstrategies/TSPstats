import pandas as pd
import matplotlib.pyplot as plt

file = "EFA_holdings20200723.csv"

def getDataDF(dfName):
    '''the getDataDF() function reads a dataset from a csv, creates a dataframe and reduces the df to sectors 
    and corresponding percent amounts by using the pandas groupby function'''
    # read in the csv
    df = pd.read_csv(dfName)
    # reduce the csv to two columns: one for sector, and one for percent; note that this step 
    # technically is not necessary, but including it here for illustrative purposes
    df = df[['sector', 'pct']]
    # delete the final rows that includes 'NaN' and negative numbers
    df = df.iloc[0:-2]
    # group by sector and sum the sectors
    df_indexed = df[['sector', 'pct']].groupby('sector').sum().sort_values(by='pct', ascending=False)
    # return the dataframe
    return df_indexed

def pieChartDF(csvName, fileName="IFundbySector.png", title="I Fund by Sector"):
    '''the pieChartDF() function calls the getDataDF() function to read in the pandas dataframe of sectors by percent,
    and then the function charts the sectors by percentage amounts in a pie chart using matplotlib'''
    df_plotted = getDataDF(csvName)
    fig = plt.figure(figsize=(6,6), dpi=200)
    ax = plt.subplot(111)
    title = title
    filename = fileName
    df_plotted.plot(kind='pie', y='pct', ax=ax, autopct='%1.2f%%', legend=False, title=title)
    plt.savefig(filename, bbox_inches='tight')

if __name__ == "__main__":
    pieChartDF(file)