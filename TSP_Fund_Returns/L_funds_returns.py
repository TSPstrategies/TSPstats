import pandas as pd
import matplotlib

# read in csv files containing monthly L Fund returns and contributions by month
monthly_contributions_file = "monthly_max_contributions.csv"
lfunds_file = "L_fundreturns.csv"

contributions = pd.read_csv(monthly_contributions_file)
lfunds = pd.read_csv(lfunds_file, index_col = False)

original_lfunds = pd.DataFrame(lfunds[['month', 'LIncome', 'L2020', 'L2030', 'L2040']])

l_2050 = pd.DataFrame(lfunds[['month', 'L2050']])
l_2050 = l_2050.dropna()

l_funds_df = pay.merge(original_lfunds, on='month')
l_2050 = pay.merge(l_2050, on='month')

# get an updated sum of total contributions over the lifetime of investing in the given fund(s)
total_contributions = l_funds_df['contribution'].sum()
print(total_contributions)

total_contributions_l_2050 = l_2050['contribution'].sum()
print(total_contributions_l_2050)

income_change = ((l_funds_df['LIncome'] * .01) + 1)
l2020_change = ((l_funds_df['L2020'] * .01) + 1)
l2030_change = ((l_funds_df['L2030'] * .01) + 1)
l2040_change = ((l_funds_df['L2040'] * .01) + 1)

l_funds_df['income_returns'] = income_change
l_funds_df['2020_returns'] = l2020_change
l_funds_df['2030_returns'] = l2030_change
l_funds_df['2040_returns'] = l2040_change

l_funds_df.to_csv("../TSPstats/TSP_Fund_Returns/l_funds_monthly_returns.csv")
l_funds_df.tail()

# run calculations for each fund (note: this version is not as 'pythonic' as other potential approaches, but I wanted to detail the basic approach for the GitHub repo)
total_return_income = []

x = 0
rolling_incometotal = 0

for contribution in contributions:
    rolling_incometotal = (contribution + rolling_incometotal) * l_funds_df.iloc[x, 6]
    
    total_return_income.append(rolling_incometotal)
    x += 1

print(f"All done calculating final L Income Fund returns, which is {rolling_incometotal}")

total_return_2020 = []


x = 0
rolling_2020total = 0

for contribution in contributions:
    rolling_2020total = (contribution + rolling_2020total) * l_funds_df.iloc[x, 7]
    
    total_return_2020.append(rolling_2020total)
    x += 1

print(f"all done calculating final L 2020 Fund returns, which is {rolling_2020total}")

total_return_2030 = []

x = 0
rolling_2030total = 0

for contribution in contributions:
    rolling_2030total = (contribution + rolling_2030total) * l_funds_df.iloc[x, 8]
    
    total_return_2030.append(rolling_2030total)
    x += 1

print(f"all done calculating final L 2030 Fund returns, which is {rolling_2030total}")

total_return_2040 = []

x = 0
rolling_2040total = 0

for contribution in contributions:
    rolling_2040total = (contribution + rolling_2040total) * l_funds_df.iloc[x, 9]
    
    total_return_2040.append(rolling_2040total)
    x += 1

print(f"all done calculating final L 2040 Fund returns, which is {rolling_2040total}")

l2050_change = ((l_2050['L2050'] * .01) + 1)

l_2050['2050_returns'] = l2050_change

l2050_contributions = l_2050['contribution']

total_return_2050 = []

x = 0
rolling_2050total = 0

for contribution in l2050_contributions:
    rolling_2050total = (contribution + rolling_2050total) * l_2050.iloc[x, 3]
    
    total_return_2050.append(rolling_2050total)
    x += 1

print(f"all done calculating final L 2050 Fund returns, which is {rolling_2050total}")

lfund_totalreturns = pd.DataFrame({
    'month': l_funds_df['month'],
    'LIncome': total_return_income,
    'L2020': total_return_2020,
    'L2030': total_return_2030,
    'L2040': total_return_2040,
})

lfund_totalreturns = lfund_totalreturns.round(decimals=2)
lfund_totalreturns.to_csv("../TSPstats/TSP_Fund_Returns/l_funds_total_returns.csv")

l2050_returns = pd.DataFrame({
    'month': l_2050['month'],
    'L2050': total_return_2050,
})

l2050_returns = l2050_returns.round(decimals=2)
l2050_returns.to_csv("../TSPstats/TSP_Fund_Returns/l2050_total_returns.csv")

lfund_totalreturns = lfund_totalreturns.set_index('month')
l2050_returns = l2050_returns.set_index('month')


matplotlib.rcdefaults()

lfund_totalreturns.plot(legend=True, grid=True, title='L Fund Returns, 2005-2019')
l2050_returns.plot(legend=True, grid=True, title='L 2050 Fund Returns, 2011-2019')
