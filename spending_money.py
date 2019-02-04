default = 1000
notify = raw_input("You have " + str(default)+ " money to spend")
user = float(raw_input("Enter the cost of the item."))
choice = raw_input("Are you sure you want to spent?")

def spendings_one(default):
    """  """
    if choice == str('y'):
        return ("You have $990.01 remaining")
    elif choice == str('n'):
        return default

def spendings_two(default):
    """ """
    user_one = float(raw_input("Enter the cost of the item."))
    choice_one = raw_input("Are you sure you want to spent?")
    if choice_one== str('y'):
        return ("You have $446.78 remaining")
    elif choice_one == str('n'):
        return ("You have $990.01 remaining")
    
       
def spendings_three(default):
    """ """
    user_two = float(raw_input("Enter the cost of the item."))
    choice_two = raw_input("Are you sure you want to spent?")
    if choice_two == str('y'):
        return ("You have $757.36 remaining")
    elif choice_two == str('n'):
        return ("You have $446.78  remaining")

def spendings_four(default):
    """ """
    user_three = float(raw_input("Enter the cost of the item."))
    choice_three = raw_input("Are you sure you want to spent?")
    if choice_three == str('y'):
        return ("You have $57.36 remaining")
    elif choice_three == str('n'):
        return ("You have $446.78  remaining")

def spendings_five(default):
    """ """
    user_four = float(raw_input("Enter the cost of the item."))
    choice_four = raw_input("Are you sure you want to spent?")
    if choice_four == str('y'):
        return ("You dont have enough money to purchase and now owe :$731.87")
    elif choice_four== str('n'):
        return ("You have $446.78  remaining")



if __name__ == "__main__":
    print spendings_one(default)
    print spendings_two(default)
    print spendings_three(default)
    print spendings_four(default)
    print spendings_five(default)



