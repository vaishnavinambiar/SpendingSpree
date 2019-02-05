default = 1000
notify = raw_input("You have " + str(default)+ " money to spend")

def spendings_one(default):
    """  """
    user = float(raw_input("Enter the cost of the item."))
    choice = raw_input("Are you sure you want to spent?")
    balance = default - user
    if choice == str('y'):
        return ("You have "+ str(balance)+" remaining")
    elif choice == str('n'):
        return ("No spendings")

def spendings_two(balance):
    """ """
    user_one = float(raw_input("Enter the cost of the item."))
    choice_one = raw_input("Are you sure you want to spent?")
    balance_one = balance - user_one
    if choice_one== str('y'):
        return("You have "+str(balance_one)+" remaining")
    elif choice_one == str('n'):
        return ("You have "+str(balance)+" remaining")
    
       
def spendings_three(balance_one):
    """ """
    user_two = float(raw_input("Enter the cost of the item."))
    choice_two = raw_input("Are you sure you want to spent?")
    balance_two = balance_one - user_two
    if choice_two == str('y'):
        return  ("You have "+str(balance_two)+" remaining")
    elif choice_two == str('n'):
        return ("You have "+str(balance_one)+"  remaining")

def spendings_four(balance_two):
    """ """
    user_three = float(raw_input("Enter the cost of the item."))
    choice_three = raw_input("Are you sure you want to spent?")
    balance_three = balance_two- user_three
    if choice_three == str('y'):
        return ("You have" +str(balance_three)+" remaining")
    elif choice_three == str('n'):
        return ("You have "+str(balance_two)+"  remaining")

def spendings_five(balance_three):
    """ """
    user_four = float(raw_input("Enter the cost of the item."))
    choice_four = raw_input("Are you sure you want to spent?")
    balance_four = balance_three - user_four
    if choice_four == str('y'):
        return ("You dont have enough money to purchase and now owe :"+str(balance_four))
    elif choice_four== str('n'):
        return ("You have "+str(balance_three)+"  remaining")



if __name__ == "__main__":
    print spendings_one(default)
    print spendings_two(default)
    print spendings_three(default)
    print spendings_four(default)
    print spendings_five(default)




