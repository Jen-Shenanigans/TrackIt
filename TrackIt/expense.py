import datetime
import os

#Clear screen
def clear_screen():
    # For Windows
    if os.name == 'nt':
        os.system('cls')
    # For Mac/Linux
    else:
        os.system('clear')

#Creating custom date
def get_custom_date():
    """
    Prompt user to input valid date in YY-MM-DD format, so to make it standardized and easy manipulation.

    Returns
    -------
    TYPE
        DESCRIPTION.

    """
    while True:
        try:
            year = int(input("Please enter the year: "))
            month = int(input("Please enter the month: "))
            day = int(input("Please enter the day: "))
            if datetime.date(year, month, day) > datetime.date.today():
                print("You can't predict the future, can you?")
            else:
                return datetime.date(year, month, day)
        except ValueError:
            print("Invalid date, please try again.\n")

#Choosing category
def choose_category():
    """
    Prompt users to choose the category of spending

    Returns
    -------
    str
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
    while True:
        print(
            "Please select the category of your spending: \n" 
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
            "[15] Groceries \n"
            "[16] Others, please specify")

        try:
            category = int(input())
            if category == 16:
                other_category = input("Please specify your category: ")
                return other_category.title()
            elif category in category_options:
                return category_options[category]
            else:
                clear_screen()
                print("Sorry, I don't understand")                
        except ValueError:
            clear_screen()
            print("Sorry, I don't understand")

#Choosing payment method
def choose_payment():
    """
    Prompt the user to select their methods of payment

    Returns
    -------
    str
        DESCRIPTION.

    """
    clear_screen()
    payment_option = {
    1: "Cash", 
    2: "Cards, including debit and credit cards",
    3: "Installments",
    4: "Bank transfer",
    5: "E-wallet"
        }
    while True:
        print("Please select a payment method: \n" \
        "[1] Cash \n" \
        "[2] Cards, including debit and credit cards \n" \
        "[3] Installments \n" \
        "[4] Bank transfer \n" \
        "[5] E-wallet \n" \
        "[6] Others, please specify")

        try:
            payment = int(input())
            if payment == 6:
                payment = input("Please specify your payment method: ")
                return payment.title()
            elif payment in payment_option:
                return payment_option[payment]
            else:
                clear_screen()
                print("Sorry, I don't understand.")
        except ValueError:
            clear_screen()
            print("Sorry, I don't understand.")

#Main function for [1]
def add_expense(ws):
    """
    Prompt the user to enter valid date of spending, the amount spent, the category of the spendin

    Parameters
    ----------
    ws : openpyxl.worksheet.worksheet.Worksheet
        The excel file that you want to add an expense on 

    Returns
    -------
    str
        DESCRIPTION.

    """

    while True:
        print(f"Please enter your date. Today is {datetime.date.today()}, which follows the YYYY-MM-DD format.")
        date = input("[1] Today's date \n[2] Custom date \n")
        if date == "1":
            date1 = datetime.date.today()
            clear_screen()
            break
        elif date == "2":
            date1 = get_custom_date()
            clear_screen()
            break
        else:
            print("Sorry, I don't understand.")
            clear_screen()
            continue

    while True:
        try:
            amount = float(input("Enter the amount spent: "))
            break  # Exit loop if input is valid
        except ValueError:
            print("Your amount can only consist of numerals and decimals. Try again")

    category = choose_category()

    method = choose_payment()

    ws.append([date1, amount, category, method, date1.year, date1.month])
    last_row = ws.max_row
    ws[f"A{last_row}"].number_format = 'yyyy-mm-dd'  # Format date in Excel

    clear_screen()

    return "\nExpense added successfully!\n"