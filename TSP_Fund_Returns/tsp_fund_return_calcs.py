import pandas as pd
import datetime
import matplotlib

# read in the csv files for monthly contributions and monthly fund returns 

pay = pd.read_csv("monthly_max_contributions.csv")
pay['month'] = pd.to_datetime(pay['month'])
funds = pd.read_csv("g_ifundreturns.csv", index_col = False)

# change the data type of the month to datetime format

funds['month'] = pd.to_datetime(funds['month'])

# because the funds started at different times, split the funds df into two dataframes and drop NaNs

original_funds = pd.DataFrame(funds[['month', 'G Fund', 'C Fund', 'F Fund']])
si_funds = pd.DataFrame(funds[['month', 'S Fund', 'I Fund']])
si_funds = si_funds.dropna()

# merge each df with monthly contributions df

si_funds = pay.merge(si_funds, on='month')
tsp_df = pay.merge(original_funds, on='month')

# insert columns to conduct calculations 

g_change = ((tsp_df['G Fund'] * .01) + 1)
c_change = ((tsp_df['C Fund'] * .01) + 1)
f_change = ((tsp_df['F Fund'] * .01) + 1)

tsp_df['g_returns'] = g_change
tsp_df['c_returns'] = c_change
tsp_df['f_returns'] = f_change

s_change = ((si_funds['S Fund'] * .01) + 1)
i_change = ((si_funds['I Fund'] * .01) + 1)


si_funds['s_returns'] = s_change
si_funds['i_returns'] = i_change

contributions = tsp_df['contribution']
si_contributions = si_funds['contribution']

# conduct calculations (this is for the G Fund)

total_return_gfund = []

x = 0
rolling_gfundtotal = 0

for contribution in contributions:
    rolling_gfundtotal = (contribution + rolling_gfundtotal) * tsp_df.iloc[x, 5]
    
    total_return_gfund.append(rolling_gfundtotal)
    x += 1

print(f"All done calculating final G Fund returns, which is {rolling_gfundtotal}")


# a similar calculation for the S Fund

total_return_sfund = []

x = 0
rolling_sfundtotal = 0

for contribution in si_contributions:
    rolling_sfundtotal = (contribution + rolling_sfundtotal) * si_funds.iloc[x, 4]
    
    total_return_sfund.append(rolling_sfundtotal)
    x += 1

print(f"all done calculating final S Fund returns, which is {rolling_sfundtotal}")

# print the returns to another dataframe and set 'month' as the index

gcf_returns = pd.DataFrame({
    'month': tsp_df['month'],
    'G Fund': total_return_gfund,
    'C Fund': total_return_cfund,
    'F Fund': total_return_ffund,
})

si_returns = pd.DataFrame({
    'month': si_funds['month'],
    'S Fund': total_return_sfund,
    'I Fund': total_return_ifund,
})

gcf_returns = gcf_returns.set_index('month')
si_returns = si_returns.set_index('month')

# finally, plot as desired

gcf_returns.plot(legend=True, grid=True, title='G, C, F Fund Returns, 1988-2019')


