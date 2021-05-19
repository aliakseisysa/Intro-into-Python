run_dist = float(input("Enter any positive number: "))
task_dist = float(input("Enter any positive number: "))
day = 1
while run_dist < task_dist:
    run_dist = 1.1*run_dist
    day += 1
print(day)
