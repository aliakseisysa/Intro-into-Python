revenue = int(input("Enter your revenue: "))
costs = int(input("Enter your costs: "))
if revenue > costs:
    print(f"Congrats! Your profit is {revenue - costs}")
elif revenue < costs:
    print(f"Unfortunately your loss is {costs - revenue}")
else:
    print("No loss, no gain.")
if revenue > costs:
    print(f"The return on revenue is {(revenue - costs)/revenue}")
    staff = int(input("Enter your employees number: "))
    print(f"The profit per employee is {(revenue - costs)/staff}")