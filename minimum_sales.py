annual_profit = ( 30000 - 5000)
fixed_sales = (6/100 * 5000) + (8/100 * 5000)
annual_profit -= fixed_sales
sales = (10/100 * 10000)
sales_count = 2
while (annual_profit > 0) :
    annual_profit -= sales
    sales_count += 1

print("We need to make " , sales_count , " sales")


