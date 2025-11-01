import os

def clear_screen():
    # For Windows
    if os.name == 'nt':
        os.system('cls')
    # For Mac/Linux
    else:
        os.system('clear')

def budget_set():
    """
    Prompt users to change their budget, or view them

    Returns
    -------
    str
        DESCRIPTION.

    """
    gee = input("[1] Set/change monthly budget \n[2] View your monthly budget\n")

    if gee == "1":
        while True:
            try:
                budget = float(input("Enter your budget: "))
                with open("budget.txt", "w") as f:
                    f.write(str(budget)) 
                return "Budget has been updated!"
            except ValueError:
                print("Sorry, numbers only.")

    elif gee == "2":
        if not os.path.exists("budget.txt"):  # check if file exists
            print("Please set budget first")
        else:
            clear_screen()
            with open("budget.txt", "r") as f:
                content = f.read().strip()
                if content == "":
                    print("Set budget first")
                else:
                    return f"Your budget is: {content}"
    
    else:
        return "Sorry, I don't understand"


if __name__ == "__main__":
    budget_set()