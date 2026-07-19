status = ""

while status == "":
    flat_no = input("Enter the Flat Number ")
    daily_readings = []
    
    for n in range(1, 6):
        reading = float(input("Enter the electricity usage (in kilowatt-hours, as a decimal) for day " + str(n) + " "))
        daily_readings.append(reading)

    total = 0.0 
    for n in daily_readings:
        total = total + n
    print("The total electicity used in 5 days = ", total, "kWh")
    avg = total / 5
    print("The avaerage electicity used in 5 days = ", avg, "kWh")

    if total <= 100:
        print("Under budget: No extra charges.")
    elif total > 100 and total <= 150:
        print("Warning: Nearing maximum capacity.")
    else:
        penalty = (5) * ((total - 100) // 10)
        print(f"Penalty Amount = $ {penalty}")

    status = input("Type 'quit' to exit, or press Enter to process another flat: ")
    if status == "quit":
        break






        
        
