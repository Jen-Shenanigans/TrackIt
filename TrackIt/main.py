#-------------------------------------------
#Import necessary modules
#-------------------------------------------

import openpyxl
import os
import pandas as pd
from expense import add_expense
from view import view_expenses
from set_budget import budget_set
import time

#-------------------------------------------
#Clearing console
#-------------------------------------------

def clear_screen():
    # For Windows
    if os.name == 'nt':
        os.system('cls')
    # For Mac/Linux
    else:
        os.system('clear')

if __name__ == "__main__":
    #-------------------------------------------
    #Creating file if it hasn't exist yet
    #-------------------------------------------
    filename = "expenses.xlsx"

    if not os.path.exists(filename):
        wb = openpyxl.Workbook() #Making Excel
        ws = wb.active #Make it active
        ws.append(["Date", "Amount", "Category", "Payment Methods", "Year", "Month"]) #Add headings
        wb.save(filename) #Save it
    else:
        pass

    #-------------------------------------------
    #Load the Excel
    #-------------------------------------------

    wb = openpyxl.load_workbook(filename) #Loading the Excel
    ws = wb.active #Make it active

    #-------------------------------------------
    #Read the Excel
    #-------------------------------------------

    df = pd.read_excel("expenses.xlsx")

    #---------------------------------------------
    #Main Menu
    #---------------------------------------------

    print("Welcome to TrackIt — your personal expense tracker!")
    print("You can record and view how your money flows, even if it was decades ago!")
    print("How can I help you today?\n")
    while True:
        print("\n[1] Add expense")
        print("[2] View your expenses")
        print("[3] Set/change monthly budget")
        print("[4] Exit")
        print("\nPlease select your activity")
        activity = input()

        #If [1] is chosen
        if activity == "1":
            clear_screen()
            print(add_expense(ws))
            wb.save(filename)
            df = pd.read_excel("expenses.xlsx")  #Refresh
            time.sleep(3)
            clear_screen()

        #If [2] is chosen
        elif activity == "2":
            clear_screen()
            view_expenses(df)

        #If [3] is chosen
        elif activity == "3":
            clear_screen()
            print(budget_set())
        
        #If [4] is chosen
        elif activity == "4":
            clear_screen()
            print("Goodbye!")
            time.sleep(5)
            clear_screen()
            break

        #If the user type random other stuff
        else:
            print("Sorry I don't understand.")

    #---------------------------------------------
    #Saving the Excel
    #---------------------------------------------
    wb.save(filename)