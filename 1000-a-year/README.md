# Calculating annual returns

This repo details the calculations for yearly returns as detailed in [this post](https://tspstrategies.com/long-term-investing/1000-a-year/ "What Does $1,000 A Year Matter?").

The file "annual_returns.csv" contains the total annual returns of the S&P 500 from 1980 to 1987 from [this site](https://www.macrotrends.net/2526/sp-500-historical-annual-returns), and for the corresponding Thrift Savings Plan C Fund from [this site](https://www.tsp.gov/fund-performance/) for the remaining years through 2019. 

### Using a spreadsheet

Open the .csv file in a spreadsheet. For calculations of increasing contributions (in column "D"), start with "0" in the head of column "E" and then use the following formula down the column starting with "=(E1+D2)*C2".

For steady ($1,000) annual contributions, start with "0" in the head of column "G", and use the following formula down the column starting with "=(G1+F2)*C2". 

Change the annual increases by changing the ".05" for the column "D" formula "=D1*1.05" to your desired percent change.

### Using Pandas

Use the attached "annualReturns.py" python script, and adjust as desired. 

Good luck! 
