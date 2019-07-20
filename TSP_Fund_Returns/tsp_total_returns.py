Import pandas as pd

total_return_gfund = []

x = 0
rolling_gfundtotal = 0

for contribution in contributions:
    rolling_gfundtotal = (contribution + rolling_gfundtotal) * tsp_df.iloc[x, 5]
    
    total_return_gfund.append(rolling_gfundtotal)
    x += 1

print(f"All done calculating final G Fund returns, which is {rolling_gfundtotal}")