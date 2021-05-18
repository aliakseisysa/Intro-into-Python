time = int(input("Enter the time (in seconds): "))
print(f"{time} seconds is equal to {(time // 60) // 60} hr {(time // 60) % 60} min {time % 60} sec")