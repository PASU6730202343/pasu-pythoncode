"""
Personal Finance Calculator
Student: pasu peryruthai 67302343
Date: 27/07/2025
Purpose: Calculate monthly budget and savings
"""

# รับข้อมูลรายได้กับคนใช้
monthly_income = float(input("Enter your monthly income (THB):   "))
rent_cost = float(input("Enter your rent or housing cost (THB): "))
food_budget = int(input("Enter your monthly food budget (THB): "))
transportation_cost = float(input("Enter your monthly transportation(THB): "))
entertainment_budget = int(input("Enter your entertainment budget (THB): "))
emergency_fund_percent = float(input("Enter emergency fund percentage : "))
investment_percent = float(input("Enter investment percentage : "))
#คำนวณค่าใช้จ่ายต่างๆ
total_fixed = rent_cost + transportation_cost
total_variable = food_budget + entertainment_budget
total_expenses = total_fixed + total_variable
remaining_income = monthly_income - total_expenses
emergency_fund = monthly_income * (emergency_fund_percent / 100)
investment_amount = monthly_income * (investment_percent / 100)
available_savings = remaining_income - emergency_fund - investment_amount
expense_ratio = (total_expenses / monthly_income) * 100
#output
print("\n=== MONTHLY BUDGET REPORT ===")   
print(f"Income: {monthly_income:.2f} THB")
print(f"Fixed Expenses: {total_fixed:.2f} THB")
print(f"Variable Expenses: {total_variable:.2f} THB")
print(f"Total Expenses: {total_expenses:.2f} THB")
print(f"Remaining: {remaining_income:.2f} THB")

print("\n=== SAVINGS BREAKDOWN ===")
print(f"Emergency Fund ({emergency_fund_percent:.0f}): {emergency_fund:.2f} THB")
print(f"Investment ({investment_percent:.0f}): {investment_amount:.2f} THB")
print (f"Available for Savings: {available_savings:.2f} THB")
print("\n=== ANALYSIS ===")
print(f"Expense Ratio: {expense_ratio:.2f}%")
