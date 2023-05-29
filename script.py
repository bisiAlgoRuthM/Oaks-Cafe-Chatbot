# Define your functions
def coffee_bot(): 
  print("Welcome to OAKS cafe!")
  size = get_cup_size()
  type = get_drink_type()
  cup = get_cup_type()
  print("Alright, that\'s a {} {} in a {}!".format(size, type, cup) )
  name = input("Can I get your name please?")
  print("Thanks, {}! Your drink will be ready shortly.".format(name))

def print_error():
    print("I'm sorry, I did not understand your selection. Please enter the corresponding letter for your response.")


def get_cup_size():
    res = input('What size drink can I get for you? \n[a] Small \n[b] Medium \n[c] Large \n> ')
    
    if res == "a":
        return "small"
    elif res == "b":
        return "medium"
    elif res == "c":
        return "large"
    else:
        print_error()
        return get_cup_size()


def get_drink_type():
    res = input("What type of drink would you like? \n[a] Brewed Coffee \n[b] Mocha \n[c] Latte")
    if res == "a":
        return "Brewed Coffee"
    elif res == "b":
        return "Mocha"
    elif res == "c":
        return order_latte()
    else:
        print_error()
        return get_drink_type()

    
def order_latte():
    res = input("And what kind of milk for your latte? \n [a] 2% milk \n [b] Non-fat milk \n [c] Soy milk")
    if res == "a":
        return "regular latte"
    elif res == "b":
        return "non-fat latte"
    elif res == "c":
        return "soy latte"
    else:
        print_error()
        return order_latte()

def get_cup_type():
    res = input("What type of cup would you like \n[a] plastic cup \n [b] reusable cup")
    if res == "a":
        return "plastic cup"
    elif res == "b":
        return "reusable cup"
    else:
        print_error()
        return get_cup_type()
    
# Call coffee_bot()!
coffee_bot()


