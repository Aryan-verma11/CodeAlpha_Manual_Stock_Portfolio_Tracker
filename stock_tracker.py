stocks={
    "TCS":[19,2000,2100],
    "HCL":[10,1500,1300],
    "Infosys":[15,1300,1200]
}


total_investment = 0
total_value = 0

for company, data in stocks.items():
    qty=data[0]
    buy_price=data[1]
    current_price=data[2]

    investment=qty*buy_price
    current_value=qty*current_price
    profit_loss=current_value-investment

    pl_percent = (profit_loss / investment * 100) if investment > 0 else 0

    total_investment+=investment
    total_value+=current_value

    print(f"{company}:Investment={total_investment} current_value={current_value} P/L={profit_loss}\n")


print(f"total Investment=> {total_investment}") #tells total investment
print(f"total Current value=> {current_value}") #total current values
print(f"total Profit or Loss=> {total_value-total_investment}")#it tells profit or loss
print(f"P/L = {profit_loss} ({pl_percent:.2f}%)\n")


# Portfolio totals
total_profit_loss = total_value - total_investment
total_pl_percent = (total_profit_loss / total_investment * 100) if total_investment > 0 else 0

print(" Portfolio Summary: ")
print(f"  Total Investment    => {total_investment}")
print(f"  Total Current Value => {total_value}")
print(f"  Total Profit/Loss   => {total_profit_loss} ({total_pl_percent:.2f}%)")
