import os
import datetime
from tabulate import tabulate
import csv
from openpyxl import Workbook, load_workbook
from openpyxl.styles import Font
import sys

#path to the csv file
global expense, date, description
date = datetime.date.today()
date = date.strftime("%d-%m-%Y")
exp_record = "expenses.csv"
exl_record = f"expenses{date}.xlsx"


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


#function to display as a table
def view_exp():
    with open(exp_record,'r') as file:
        viewer = csv.reader(file)
        rows = list(viewer)  
        return rows


#function to export data as an excel sheet
def exp_excel():

    view_data = view_exp()

    if not os.path.exists(exl_record):
            workbook = Workbook()
            sheet = workbook.active
            sheet.title = f"Expenses {date}"

    sheet.append(view_data[0])
    for cell in sheet[1]:
        cell.font = Font(bold=True)

    for row in view_data[1:]:
        sheet.append(row)

    workbook.save(exl_record)

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
    # View Spendings
    print("Select Operation \n1. Print whole list \n2. Print list of particular date")
    flow = input("Select your operation: ")

    if flow == "1":
        view = view_exp()
        print(tabulate(view[1:], headers=view[0], tablefmt='pipe', showindex=range(1, len(view))))

        total_expense = sum(float(row[2]) for row in view[1:])
        print("\nTOTAL EXPENSES:",total_expense, "\n")

    elif flow == "2":

        view =  view_exp()

        print("Function not implemented")

    else: 
        print("Invalid Input")


elif op == '3':
    # Export Excel
    exp_excel()
    print("The expenses are exported in excelsheet. \nFind them in your source folder")

elif op == '4':
    #exit - Placeholder for the logic
    print("Exiting program.")
else:
    print("Invalid operation!")

