import pandas as pd
import os
import datetime

def clear_screen():
    # For Windows
    if os.name == 'nt':
        os.system('cls')
    # For Mac/Linux
    else:
        os.system('clear')

def gee(df):
    """
    A way to "scroll", so the user can see 20 items at a time, otherwise it would take up a lot of the screen. 
    User can press ">" to go next, and "<" to go back
    The "q" button is to quit the navigation

    Parameters
    ----------
    df : DataFrame
        expenses.xlsx

    Returns
    -------
    str
        If users hasn't enter any expense yet, or deleted all of them, we prompt them to add in expense first

    """
    n = 0
    m = 20

    c = df
    clear_screen()

    #-----------------------------------------------------
    #Sorting out dates
    #-----------------------------------------------------
    c["Date"] = pd.to_datetime(c["Date"]) #Change to datetime format
    c = c.sort_values("Date") #Sort date in chronological order
    c = c.reset_index(drop=True) #Reset the index


    if len(c) == 0:
        return "Please enter an expense first.\n"

    clear_screen()
    print(c[n:m])
    if m > len(c):
        print(f"Showing {n+1}-{len(c)} of {len(c)}")
    else:
        print(f"Showing {n+1}-{m} of {len(c)}")
    
    if len(c) >= 20:
        while True:
            back_forth = input("[<] Back \n[>] Forward \n[q] Quit \n")
            if back_forth == ">":
                if m >= len(c):
                    print("Sorry, you can't do that")
                else:
                    n += 20
                    m += 20
                clear_screen()
                print(c[n:m])

                if m > len(c):
                    print(f"Showing {n+1}-{len(c)} of {len(c)}")
                else:
                    print(f"Showing {n+1}-{m} of {len(c)}")
            
            elif back_forth == "<":
                if n == 0:
                    print("Sorry, you can't do that")
                else:
                    n -= 20
                    m -= 20
                clear_screen()
                print(c[n:m])
                print(f"Showing {n+1}-{m} of {len(c)}")

            elif back_forth.lower() == "q":
                clear_screen()
                break

            else:
                print("Sorry I don't understand")

def filter_expenses(df):
    """
    Prompt user to choose the following:
        1) Date range
        2) Categories
        3) Payment type

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
        clear_screen()
        filterby = input("Filter by: \n[1] Date range \n[2] Categories \n[3] Payment type \n")

        if filterby == "1":
            return filter_one(df)
        
        elif filterby == "2":
            return filter_two(df)
        
        elif filterby == "3":
            return filter_three(df)
        
        else:
            clear_screen()
            print("Sorry I don't understand")

def filter_one(df):
    """
    Prompt user to enter VALID starting date and ending date.
    The starting date can never be later than ending date
    
    Parameters
    ----------
    df : DataFram
        expenses.xlsx

    Returns
    -------
    TYPE
        DESCRIPTION.

    """
    df["Date"] = pd.to_datetime(df["Date"]).dt.date

    while True:
        try:
            date_b4_yr = int(input("Please enter the starting year: "))
            date_b4_mon = int(input("Please enter the starting month: "))
            date_b4_day = int(input("Please enter the starting day: "))
            date_b4 = datetime.date(date_b4_yr, date_b4_mon, date_b4_day)
            print(f"Starting date: {date_b4}")
        except ValueError:
            print("Invalid date, please try again.")
            continue

        try:
            date_af_yr = int(input("Please enter the ending year: "))
            date_af_mon = int(input("Please enter the ending month: "))
            date_af_day = int(input("Please enter the ending day: "))
            date_af = datetime.date(date_af_yr, date_af_mon, date_af_day)   
            print(f"Ending date: {date_af}")
        except ValueError:
            print("Invalid date, please try again.") 
            continue     

        if date_b4 > date_af:
            print("Sorry, the starting date must be before the ending date.")          
        else:
            df = df[df["Date"].between(date_b4, date_af)]
            return gee(df)

def filter_two(df):
    """
    Prompt user to choose VALID category, limiting them to choose 16 categories to avoid unneccesary error

    Parameters
    ----------
    df : DataFrame
        expenses.xlsx

    Returns
    -------
    None
        DESCRIPTION.

    """
    category_options = {
        1: "Housing",
        2: "Food and Beverages",
        3: "Transportation",
        4: "Health and Insurance",
        5: "Education",
        6: "Technology",
        7: "Shopping",
        8: "Subscriptions",
        9: "Utilities and Bills",
        10: "Travel and Leisure",
        11: "Gifts and Donations",
        12: "Loan Payments",
        13: "Hobbies",
        14: "Pets",
        15: "Groceries"}
    categories1 = [
        "Housing",
        "Food and Beverages",
        "Transportation",
        "Health and Insurance",
        "Education",
        "Technology",
        "Shopping",
        "Subscriptions",
        "Utilities and Bills",
        "Travel and Leisure",
        "Gifts and Donations",
        "Loan Payments",
        "Hobbies",
        "Pets",
        "Groceries"]
    while True:
        print(
            "Please select a category: \n" 
            "[1] Housing \n" \
            "[2] Food and Beverages \n" \
            "[3] Transportation \n" \
            "[4] Health and Insurance \n" \
            "[5] Education \n" \
            "[6] Technology \n" \
            "[7] Shopping \n" \
            "[8] Subscriptions \n" \
            "[9] Utilities and bills \n" \
            "[10] Travel and Leisure \n" \
            "[11] Gifts and Donations \n" \
            "[12] Loan payments \n" \
            "[13] Hobbies \n" \
            "[14] Pets \n" \
            "[15] Groceries \n" \
            "[16] Others")

        try:
            category = int(input())
            if category == 16:
                df = df[~df["Category"].isin(categories1)]
                return gee(df)
            elif category in category_options:
                cat = category_options[category]
            else:
                clear_screen()
                print("Sorry, I don't understand")                
        except ValueError:
            clear_screen()
            print("Sorry, I don't understand")
            continue

        df = df[df["Category"] == cat]
        return gee(df)

def filter_three(df):
    """
    Prompt user to choose VALID payment type, limiting them to choose 5 type to avoid unneccesary error

    Parameters
    ----------
    df : DataFrame
        expenses.xlsx

    Returns
    -------
    None
        DESCRIPTION.

    """
    payment_option = {
    1: "Cash", 
    2: "Cards, including debit and credit cards",
    3: "Installments",
    4: "Bank transfer",
    5: "E-wallet"
        }
    
    payment1 = ["Cash",
                "Cards, including debit and credit cards", 
                "Installments",
                "Bank transfer",
                "E-wallet"
                ]
    while True:
        print("Please select a payment method: \n" \
        "[1] Cash \n" \
        "[2] Cards, including debit and credit cards \n" \
        "[3] Installments \n" \
        "[4] Bank transfer \n" \
        "[5] E-wallet \n" \
        "[6] Others")

        try:
            payment = int(input())
            if payment == 6:
                df = df[~df["Payment Methods"].isin(payment1)]
                return gee(df)
            elif payment in payment_option:
                pay = payment_option[payment]
            else:
                clear_screen()
                print("Sorry, I don't understand.")
        except ValueError:
            clear_screen()
            print("Sorry, I don't understand.")
        
        df = df[df["Payment Methods"] == pay]
        return gee(df)
    
