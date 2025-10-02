# CodeAlpha_Manual_Stock_Portfolio_Tracker


# 📊 Stock Portfolio Tracker (Python)

This is a simple **Python project** that helps you track your stock portfolio.  
It calculates how much you invested, the current value of your stocks, and shows whether you are in **profit or loss**.  
It also calculates the **percentage profit/loss** for each stock and for the whole portfolio.

---

## 🚀 Features
- Track multiple stocks using a Python dictionary  
- Calculate for each stock:
  - Investment (Qty × Buy Price)  
  - Current Value (Qty × Current Price)  
  - Profit / Loss (absolute value and %)  
- Show portfolio totals (total investment, total current value, overall P/L)  
- Beginner-friendly code with no extra libraries needed  

---

## 🛠️ How It Works
1. You define your portfolio inside a dictionary like this:

   ```python
   stocks = {
       "TCS": [19, 2000, 2100],
       "HCL": [10, 1500, 1300],
       "Infosys": [15, 1300, 1200]
   }


   "CompanyName": [Quantity, Buy Price, Current Price]

📊 Stock Portfolio Report

TCS:
  Investment    = 38000
  Current Value = 39900
  P/L           = 1900 (5.00%)

HCL:
  Investment    = 15000
  Current Value = 13000
  P/L           = -2000 (-13.33%)

Infosys:
  Investment    = 19500
  Current Value = 18000
  P/L           = -1500 (-7.69%)

📌 Portfolio Summary:
  Total Investment    => 72500
  Total Current Value => 70900
  Total Profit/Loss   => -1600 (-2.21%)

