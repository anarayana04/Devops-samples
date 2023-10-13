car_cost_per_hour = 20
bike_cost_per_hour = 10
hours_per_day = 6
num_cars = int(input("Enter the number of cars parked: "))
num_bikes = int(input("Enter the number of bikes parked: "))
total_collection = (num_cars * car_cost_per_hour * hours_per_day) + (num_bikes * bike_cost_per_hour * hours_per_day)

# Determine if it's a good day or a bad day
if total_collection >= 10000:
    print("It's a good day!")
else:
    print("It's a bad day.")