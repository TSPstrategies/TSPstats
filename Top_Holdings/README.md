# Top Holdings in the C, S, and I Funds

This repo maintains the files for the top holdings in the C, S, and I Funds, as d in [this post](https://tspstrategies.com/fund-related-news/top-holdings/ "Top Holdings in the C, I, and S Funds").

The original data can be found on Blackrock's main site [here](https://www.blackrock.com/us/individual/products/239726/ishares-core-sp-500-etf) and [here](https://www.blackrock.com/us/individual/products/239623/ishares-msci-eafe-etf). Blackrock is the manager of the C, S, and I Funds, although these pages are the Exchange Traded Funds available to the public as "IVV" and "EFA". Thus, there might be some small discrepencies. Relatively less information is available with a percentage breakdown of total holdings of the S Fund, but information on the top ten is available on Vanguard's "VXF" ETF investor page [here](https://investor.vanguard.com/etf/profile/portfolio/VXF/quarter-end-holdings). The VXF closely resembles the S Fund.

Since the composition of the funds change over time, some of the file names contain timestamps for the date of the information. 

This repo also maintains some of the scripts and functions used for graphing the updated holdings. The script "pandasPieChart.py" charts sector holdings using the "groupby" function in pandas, while the "sectorPieChart.py" charts sector holdings from a .csv of sectors and their percentages. Both files are included in this repo, as are the resultant pie charts. 

Sector-related data is detailed in the article "[Tech and the TSP](https://tspstrategies.com/fund-related-news/tech-and-the-tsp/ "Tech and the TSP")".