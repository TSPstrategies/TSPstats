## Calculating Total Returns of the TSP Funds 

Here is an outline of my approach to calculating the TSP fund returns from their inception to the present. 

The calculations are done by taking a monthly TSP contribution (the max contribution for the year divided by 12), adding it to the rolling sum of previous investments/returns, and calculating the month-end return based on how the given fund performed for the month. 

_For maximum yearly contributions ("Effective Deferral Limits") allowed in the TSP since its inception, see [this chart](https://www.tspstrategies.com/assets/studies/tspcontributionlimits87-13.pdf). For the latest contribution limits, see [this post](https://www.tspstrategies.com/long-term-investing/increase-in-2019-tsp-deferral-limit/) and [this post](https://www.tspstrategies.com/thrift-savings-plan-updates/increase-in-2018-tsp-deferral-limits/)._

The monthly returns for each of the funds are taken from official data on the [TSP website](https://www.tsp.gov/InvestmentFunds/FundPerformance/monthlyReturns.html), and/or calculated based on the closing prices from the final trading day of one month to the next ([available here](https://www.tsp.gov/InvestmentFunds/FundPerformance/index.html)).

The "tsp_fund_return_calcs.py" sample python script joins the return figures in the "g_ifundreturns.csv" file, updated monthly, with the file "monthly_max_contributions.csv" in a pandas DataFrame and conducts the calculations. 

Similarly, the "L_funds_returns.py" script joins the return figures in "L_fundreturns.csv" with "monthly_max_contributions.csv" in a pandas DataFrame and conducts the calculations. 

The resultant files with the calculations are titled "gcf_fund_monthly_returns.csv", "si_funds_monthly_returns.csv", "gcf_funds_total_returns.csv", "si_funds_total_returns.csv", "l_funds_monthly_returns.csv", "l_funds_total_returns.csv", "l2050_fund_monthly_returns", and "l2050_total_returns.csv". 

![G, F, C Fund Returns](https://github.com/TSPstrategies/TSPstats/blob/master/TSP_Fund_Returns/gcffundcomp.png)

![S, I Fund Returns](https://github.com/TSPstrategies/TSPstats/blob/master/TSP_Fund_Returns/sifundcomp.png)

![L Funds Returns](https://github.com/TSPstrategies/TSPstats/blob/master/TSP_Fund_Returns/lfundtotalreturns.png)

![L 2050 Fund Returns](https://github.com/TSPstrategies/TSPstats/blob/master/TSP_Fund_Returns/l2050totalreturns.png)


See the python files for further explanations about calculations. 
