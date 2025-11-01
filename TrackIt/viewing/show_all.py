import os
import pandas as pd

def clear_screen():
    # For Windows
    if os.name == 'nt':
        os.system('cls')
    # For Mac/Linux
    else:
        os.system('clear')

def show_all(df):
    """
    Show all of the expeses that the user has recorded down. 
    It only show 20 items at a time, to prevent overcrowding. 
    The user can "scroll", using ">" and "<"
    The user can enter "q" to quit

    Parameters
    ----------
    df : DataFrame
        expenses.xlsx

    Returns
    -------
    str
        DESCRIPTION.

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
                return " "

            else:
                print("Sorry I don't understand")