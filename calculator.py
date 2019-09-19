import battery
import inverter

def create_battery():
    brand = input("What is the brand of the battery? : ")
    capacity = input("What is the capacity of the battery? : ")
    voltage = input("What is the voltage of the battery? : ")
    return battery.Battery(brand, capacity, voltage)

def calculate_runtime(battery):
    load = input("What is your total load in watts? :")
    runtime = battery.calculate_hours_from_load(load)
    print("Your {0} battery on a load of {1} will give you {2} hours runtime approx.".format(battery.brand, load, runtime))

batteryInstance = create_battery()
calculate_runtime(batteryInstance)
