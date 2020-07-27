from sectorPieChart import getData, pieChart
from pandasPieChart import getDataDF, pieChartDF

cfund_sectors = "sp500bysector20200723.csv"
ifund_sectors = "EFA_holdings20200723.csv"

def main(csvFile, df):
    return pieChart(csvFile), pieChartDF(df)

if __name__ == "__main__":
    main(cfund_sectors, ifund_sectors)
