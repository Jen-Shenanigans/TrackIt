import matplotlib.pyplot as plt
import seaborn as sns
import os
import pandas as pd
import numpy as np
import datetime

def clear_screen():
    # For Windows
    if os.name == 'nt':
        os.system('cls')
    # For Mac/Linux
    else:
        os.system('clear')


#Incomplete
def overview(df):
    """
    Give an overview of user's spending. This include:
        1) User's monthly budget
        2) User's monthly total spending, both in values and percentage
        3) Top five spendings
        4) Bottom five spendings
        5) Highest category count
        6) A graph showing how much they spend on each category and payment methods

    Parameters
    ----------
    df : DataFrame
        expenses.xlsx

    Returns
    -------
    None.

    """
    clear_screen()
    print(
    "------------------------------------- \n" \
    "OVERVIEW \n" \
    "------------------------------------- ")
    with open("budget.txt", "r") as f:
        budget = f.read()

    if budget != "":
        print(f"Your budget: RM{budget}")
        print(f"You have spend RM{monthly_total(df)} this month, which is {np.round(monthly_total(df)/float(budget)*100, 2)}% of your monthly budget \n")

    df = df.sort_values("Amount", ascending = False)
    df = df.reset_index(drop = True)
    print("Your top five spendings: ")
    print(df.head())

    df = df.sort_values("Amount")
    df = df.reset_index(drop = True)

    print("\nYour bottom five spendings:")
    print(df.head())

    print("\nYou frequently spent on: ") #Catergories
    print(df["Category"].value_counts()[0:3])
    
    sns.barplot(data = df, x = "Category", y = "Amount", estimator="sum", errorbar=None, hue="Payment Methods")
    plt.show()

def monthly_total(df):
    """
    Calculate the total amount spend in the current month of the current year

    Parameters
    ----------
    df : DataFrame
        expenses.xlsx

    Returns
    -------
    total : float
        Total spending in the current month of the current year

    """
    #Filter out this year
    year = df[df["Year"] == datetime.datetime.now().year]
    #Filter out this month of this year
    month = year[year["Month"] == datetime.datetime.now().month]

    total = month["Amount"].sum()
    return total


if __name__ == "__main__":
    df = pd.read_excel("expenses.xlsx")
    overview(df)