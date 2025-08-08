# Stine Saugmann Jespersen

import random

# Some example items - feel free tho change them
items = ["Sandwich", "Salad", "Cake"]
prices = [65, 45, 50]
inventories = [100, 50, 100]


def simulate_customers():
    StudentsArriving = random.randint(100, 500)
    sales = []
    endinventory = inventories[:]
    for student in range(StudentsArriving):
        student = random.randint(1, 2)
        if student == 1:
            item = random.choice(items)
            idx = items.index(item)
            sales.append(idx)
            if endinventory[idx] > 0:
                endinventory[idx] -= 1
    return sales, endinventory


def process_sales():
    sales, endinventory = simulate_customers()
    revenue = 0
    for sale in sales:
        revenue += prices[sale]
    return revenue

def costs():
    sales, endinventory = simulate_customers()
    costs = [endinventory[i] * prices[i] / 2 for i in range(len(items))]
    return costs


def generate_report():
    revenue = process_sales()
    sales, endinventory = simulate_customers()
    cost = costs()
    sold = [inventories[i] - endinventory[i] for i in range(len(items))]
    print(f"{items[0]}:\n"
          f"  Sold:           {sold[0]}\n"
          f"  Inventory left: {endinventory[0]}\n"
          f"  Revenue:        {sold[0] * prices[0]}\n")

    print(f"{items[1]}:\n"
          f"  Sold:           {sold[1]}\n"
          f"  Inventory left: {endinventory[1]}\n"
          f"  Revenue:        {sold[1] * prices[1]}\n")

    print(f"{items[2]}:\n"
          f"  Sold:           {sold[2]}\n"
          f"  Inventory left: {endinventory[2]}\n"
          f"  Revenue:        {sold[2] * prices[2]}\n")


    print(f"\nThe total revenue is {revenue}"
          f"\nThe total cost is {cost}")
    

    
generate_report()



