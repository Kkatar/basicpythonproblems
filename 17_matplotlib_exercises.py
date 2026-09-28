# 17. Python Matplotlib Exercise

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Exercise 1: Read Total profit of all months and show it using a line plot
sales_data = pd.read_csv("company_sales_data.csv")
print(sales_data.head())

monthList = sales_data["month_number"].tolist()
profitList = np.arange(100000, 500000, 50000).tolist()

plt.plot("month_number", "total_profit", data=sales_data)
plt.xlabel("Month Number")
plt.xticks(monthList)
plt.yticks(profitList)
plt.ylabel("Total profit")
plt.title("COMPANY PROFIT PER MONTH")
plt.show()

# Exercise 2: Get total profit of all months and show line plot with the following Style properties
plt.plot("month_number", "total_profit", data=sales_data, color="red", marker='o', markerfacecolor='black', linewidth=2, markersize=6)
plt.xlabel("Month Number")
plt.xticks(monthList)
plt.ylabel("Total Profit")
plt.yticks(profitList)
plt.legend(loc="upper left")
plt.title("COMPANY SALES FOR LAST YEAR")
plt.show()

# Exercise 3: Read all product sales data and show it using a multiline plot
quantityList = np.arange(1000, 20000, 2000)

plt.plot("month_number", "facecream", data=sales_data, marker="o")
plt.plot("month_number", "facewash", data=sales_data, marker="o")
plt.plot("month_number", "toothpaste", data=sales_data, marker="o")
plt.plot("month_number", "bathingsoap", data=sales_data, marker="o")
plt.plot("month_number", "shampoo", data=sales_data, marker="o")
plt.plot("month_number", "moisturizer", data=sales_data, marker="o")

plt.xticks(monthList)
plt.xlabel("Month Number")
plt.yticks(quantityList)
plt.ylabel("Sales of product in number of units")
plt.legend(loc="upper left")
plt.show()

# Exercise 4: Read toothpaste sales data of each month and show it using a scatter plot
plt.scatter("month_number", "toothpaste", data=sales_data)
plt.legend(loc="upper left")
plt.grid(color='r', linestyle='dashed', linewidth=0.5)
plt.xlabel("Month Number")
plt.ylabel("Quantity Sales")
plt.show()

# Exercise 5: Read face cream and facewash product sales data and show it using the bar chart
plt.bar([a - 0.25 for a in monthList], "facecream", data=sales_data, width=0.25, align="edge")
plt.bar([a + 0.25 for a in monthList], "facewash", data=sales_data, width=-0.25, align="edge")

plt.xticks(monthList)
plt.xlabel("Month Number")
plt.ylabel("quantity sales")
plt.legend()
plt.grid(color='r', linestyle='dashed', linewidth=0.5)
plt.show()

# Exercise 6: Read sales data of bathing soap of all months and show it using a bar chart. Save this plot to your hard disk
plt.bar("month_number", "total_units", data=sales_data)
plt.grid(True, linestyle="dashed")
plt.xticks(monthList)
plt.xlabel("Month Number")
plt.ylabel("Sales units in numbers")
plt.title("Bath soaping sales data")
plt.show()

# Exercise 7: Read the total profit of each month and show it using the histogram to see the most common profit ranges
profitList = sales_data["total_profit"].tolist()
profit_range = np.arange(150000, 350000, 25000)

plt.hist(profitList, profit_range, label="max profit range")
plt.legend()
plt.show()

# Exercise 8: Calculate total sale data for last year for each product and show it using a Pie chart
print(sales_data.head(2))

saleData = [sales_data["facecream"].sum(), sales_data["facewash"].sum(), sales_data["toothpaste"].sum(), sales_data["bathingsoap"].sum(), sales_data["shampoo"].sum(), sales_data["moisturizer"].sum()]
print(saleData)

labels = ['FaceCream', 'FaseWash', 'ToothPaste', 'Bathing soap', 'Shampoo', 'Moisturizer']

plt.pie(saleData, autopct="%1.1f%%", labels=labels)
plt.legend()
plt.show()

# Exercise 9: Read Bathing soap and facewash of all months and display it using the Subplot
plt.subplot(2, 1, 1)
plt.plot("month_number", "bathingsoap", data=sales_data, color="black", marker="o")
plt.title("sales data of bathing soap")

plt.subplot(2, 1, 2)
plt.plot("month_number", "facewash", data=sales_data, color="red", marker="o")
plt.xlabel("Month Number")
plt.title("sales data of facewash")
plt.ylabel("sales units in numbers")

plt.subplots_adjust(bottom=0.1, wspace=0.4, hspace=0.3)
plt.show()
