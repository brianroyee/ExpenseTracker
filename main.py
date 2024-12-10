import os
import datetime
from tabulate import tabulate
import csv
import pandas
import openpyxl
import sys

#path to the csv file
global expense, date, description
exp_record = "expenses.csv"
date = datetime.date.today()
date = date.strftime("%d-%m-%Y")


#check if the file is found in the directory, if not create one
try:
    if not os.path.exists(exp_record):
        with open(exp_record, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["DATE","DESCRIPTION","EXPENSE"])
except:
    print("Oops, something went wrong")
#function to add expense
def add_exp(date,description,expense):
    with open(exp_record, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([date,description,expense])


#print program menu
print("PERSONAL EXPENSE TRACKER \n************************")
print("MENU")
print("1. Add Expense \n2. View Spendings \n3. Export spendings \n4 .Exit")

op = input("Enter the selected operation: ")

if op == "1":
    # Add Expenses
    while True:
        expense = input("Enter Expense: ")
        description = input("Enter Description: ")
        
        try:
            expense = float(expense)
        except ValueError:
            print("Invalid input! Please enter a valid expense.")
            continue 

        add_exp(date,description,expense)

        flow = input("Would you like to add more? (Y/n)")
        
        if flow.lower() != "y":
            break


elif op == '2':
    # View Spendings - Placeholder for the logic
    print("Viewing all expenses (function not implemented).")

elif op == '3':
    # Export Exce - Placeholder for the logic
    print("Exporting spendings (function not implemented).")

elif op == '4':
    #exit - Placeholder for the logic
    print("Exiting program.")
else:
    print("Invalid operation!")

