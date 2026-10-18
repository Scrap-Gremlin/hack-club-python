# Outside Variables
line = ("=" * 30)
num_ords = "123456"
let_ords = ["c", "v", "h", "p", "s", "b"]
let_ords2 = ["h", "e", "a", "e", "a", "u"]
pizzas = []
b_input = ""
budget = b_input
or1 = 0
or2 = 0
out1 = 0
out2 = 0
# Lists
items = [("Cheese",8), ("Veggie",12), ("Hawaiian",12), ("Pepperoni",10), ("Sausage",10), ("Buffalo Chicken",12), ("",0)]
item_names = ["cheese", "veggie", "hawaiian", "pepperoni", "sausage", "buffalo chicken"]
stock = [5, 5, 5, 5, 5, 5]
# Functions
def order_exist(a):
    if a == "hawaiian":
        return True
    elif a == "pepperoni":
        return True
    elif a == "buffalo chicken":
        return True
    elif "n" not in a:
        return True
    else:
        return False
def order(a):
        b = items[a]
        c = b[1]
        return c
def p_type(a):
        if a != (7):
            b = items[a]
            c = b[0]
        else:
            b = ""
            c = ""
        return c
def is_in(a,b):
    if a in b:
        return True
    else:
        return False
def stock_take(a):
    if stock[a] <= 0:
        stock[a] = stock[a] - 1
        return True
    else:
        return False
print("       MARIO'S    PIZZA       ")
print(line)
print("        PIZZA     MENU        ")
print(line)
print("")
print("#1: Cheese..................$8")
print("#2: Veggie.................$12")
print("#3: Hawaiian...............$12")
print("#4: Pepperoni..............$10")
print("#5: Sausage................$10")
print("#6: Buffalo Chicken........$12")
print("")
print(line)
print("Welcome to Mario's Pizza!")
while isinstance(budget, str):
    b_input = input("What is your budget? ").replace("$", "")
    try:
        budget = int(b_input)
        if budget <= 7:
            budget = str(budget)
            print("That is not a valid budget.")
    except ValueError:
        print("Sorry, that is not a number. Please try again.")
while True:
    or1 = 0
    or2 = 0
    print(line)
    print(f"Your budget is ${budget}")
    while or1 == 0:
        if out1 == 1:
            print("Sorry, we are out of that item.\nPlease order again.")
        order1 = input("What kind of pizza would you like? ").lower().replace("#", "")
        if order1[0] in num_ords:
            order1i = (int(order1[0])) - 1
            if stock_take(order1i + 1) == True:
                or1 = 1
            elif stock_take(order1i) == False:
                out1 = 1
        elif order1[0] in let_ords and is_in(order1[1],let_ords2):
            order1i = let_ords.index(order1[0])
            if stock_take(order1i) == True:
                or1 = 1
            elif stock_take(order1i) == False:
                out1 = 1
        else:
            print("Sorry, we can't make that.")
    while or2 == 0:
        if out2 == 1:
            print("Sorry, we are out of that item.\nPlease order again")
        order2 = input("Anything else? ").lower().replace("#", "")        
        if order_exist(order2) == True:
            if order2[0] in num_ords:
                order2i = int(order2[0]) - 1
                if stock_take(order2i + 1) == True:
                    print(stock)
                    or2 = 1
                elif stock_take(order2i) == False:
            elif order2[0] in let_ords and is_in(order2[1,let_ords2]):
                order2i = let_ords.index(order2[0])
                if stock_take(order2i) == True:
                    or2 = 1
                elif stock_take(order2i) == False:
            else:
                print("Can you repeat that?")
        else:
            order2i = (7)
            or2 = 1
            print("I'll take that as a no.")
    order1_cost = order(order1i)
    type_1 = p_type(order1i)
    if order_exist(order2) == True:
        order2_cost = order(order2i)
        type_2 = " and one " + p_type(order2i)
    else:
        order2_cost = 0
        type_2 = ""
    full_order = "$" + str(order1_cost + order2_cost)
    print(f"So one {type_1 + type_2}.....")
    print(f"That will be {full_order}, please.")
    print(line)
    l_budget = budget
    budget = budget - int(full_order.replace("$", ""))
    print(f"Your budget is ${budget}")
    pizzas.append(p_type(order1i))
    pizzas.append(p_type(order2i))
    while '' in pizzas:
        pizzas.remove('')
    end = f"Bye! Have a great day!\nPizzas you have bought:{pizzas}"
    if budget == 0:
        print(end)
        break
    elif budget < 0:
        print("Sorry, you don't have enough money. You can't pay for that.")
        budget = l_budget
        again = order_exist(input("Would you like to reorder? (y/n) ").lower())
        if again == False:
            pizzas.remove(p_type(order1i))
            pizzas.remove(p_type(order2i))
            print(end)
            break
        elif again == True:
            pizzas.remove(p_type(order1i))
            pizzas.remove(p_type(order2i))
    elif order_exist(input("New order? (y/n) ").lower()) == False:
        print(end)
        break