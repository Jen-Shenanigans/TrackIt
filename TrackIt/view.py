import pandas as pd
import os
from viewing.filter import filter_expenses
from viewing.overview import overview
from viewing.show_all import show_all

#------------------------------------
# Clear screen function
#------------------------------------
#Complete
def clear_screen():
    # For Windows
    if os.name == 'nt':
        os.system('cls')
    # For Mac/Linux
    else:
        os.system('clear')

#------------------------------------
# Menu Function
#------------------------------------
#Complete
def view_expenses(df):
    """
    "Prompt user to select one of the three options:
        1) Spending overview
        2) Showing all of the expenses recorded
        3) Filtering expenses"

    Parameters
    ----------
    df : DataFrame
        expenses.xlsx

    Returns
    -------
    None
        DESCRIPTION.

    """
    while True:
        print(
        "Please select the following: \n" \
        "[1] Spending Overview \n" \
        "[2] Showing all expenses\n" \
        "[3] Filter expenses \n")

        option = input()

        if option == "1":
            return overview(df)
        
        elif option == "2":
            return show_all(df)
        
        elif option == "3":
            return filter_expenses(df)
        
        else:
            print("Sorry I don't understand")

if __name__ == "__main__":
    df = pd.read_excel("expenses.xlsx")
    print(view_expenses(df))