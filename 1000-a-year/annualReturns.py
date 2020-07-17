import pandas as pd

file = "annual_returns.csv"

yearly = pd.read_csv(file)

yearly_pct = yearly.loc[:,'return']
year = yearly.loc[:,'year']

def yearly_investments(initial_investment, increase, years):
    rolling_investments = []
    i = 0
    if increase == 0:
        while i < years:
            rolling_investments.append(initial_investment)
            i += 1
    else:
        if increase < 1:
            increase = increase + 1
        else:
            increase = (increase * .01) + 1
            
        while i < years:
            rolling_investments.append(initial_investment)
            initial_investment = initial_investment * increase
            i += 1
    return rolling_investments

def yearly_returns(yearly_amount, increase, years):
    total = 0
    count = 0
    inv = yearly_investments(yearly_amount, increase, years)
    rolling_total = []
    for r in yearly_pct:
        total = round((total + inv[count]) * r, 2)
        rolling_total.append(total)
        print("The return as of December", year[count], " is $", total)
        count += 1
    return rolling_total

def main():
    yearly_returns(1000, 0, 40)

if __name__ =="__main__":
    main()