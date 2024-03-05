stock_prices = [295, 320, 300, 312, 292]
# print(stock_prices[0]) #indexing of the list or can say like "array"
# print(stock_prices[1])
# print(stock_prices[2])

#to get index of a value given
# for i in range(len(stock_prices)):
#     if stock_prices[i] == 312:
#         print(i)

#inserting function 


# pos = int(input("Enter the postition you want to insert : "))
# val = int(input("Enter the value you want to insert : "))
# def ins(pos, val):
#     stock_prices.insert(pos, val)
# ins(pos, val)
# print(stock_prices)

monthly_expenses = [2200, 2350, 2600, 2130, 2190]

print(f"Extra Dollars spent in Feb compared to january : $ {monthly_expenses[1] - monthly_expenses[0]}")
print(f"Total Expense in first quarter (First 3 months) : $ {monthly_expenses[0] + monthly_expenses[1] + monthly_expenses[2]}")
print(f"Spent $2000 in which month :", 2000 in monthly_expenses)
monthly_expenses.append(1980)
print(f'Updated Expense added June Expense : {monthly_expenses}')

monthly_expenses[3] = monthly_expenses[3] - 200
print(f'Updated Montly Expense List : {monthly_expenses}')