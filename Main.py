# WGU ID: 011413746
#Manuel Marcano
#C950 WGUPS Package Tracking Action Program
import csv
import datetime
import Truck

from Package import Package
from Hashmap import HashMap
from builtins import ValueError

#logic for csv files
# read file of address
with open("CSV/WGUPS_Distance_Table.csv") as csvfile:
    CSV_Distance = csv.reader(csvfile)
    CSV_Distance = list(CSV_Distance)

# read file of distance
with open("CSV/WGUPS_Address_File.csv") as csvfile1:
    CSV_Address = csv.reader(csvfile1)
    CSV_Address = list(CSV_Address)

# read file of package
with open("CSV/WGUPS_Package_File.csv") as csvfile2:
    CSV_Package = csv.reader(csvfile2)
    CSV_Package = list(CSV_Package)

#hashmap instantiation
def package_data_loader(filename, packageTable):
    with open(filename) as packageFile:
        packagereader = csv.reader(packageFile)
        # logic to get package data from csv files
        for package in packagereader:
            packageId = int(package[0])
            packageAddress = package[1]
            packageCity= package[2]
            packageState = package[3]
            packageZipcode = package[4]
            packageDeadline = package[5]
            packageWeight = package[6] #
            packageStatus = "Residing in hub"

            package = Package(packageId, packageAddress, packageCity, packageState, packageZipcode, packageDeadline, packageWeight, packageStatus) #object

            packageTable.insert(packageId, package)

#method to find distances between 2 given addresses
    #read csv distance file(taking x y values) to find row and col in the csv file
def distance_loader(x_value, y_value):
    distance = CSV_Distance[x_value][y_value]
    if distance == '':
        distance = CSV_Distance[y_value][x_value] #inverse

    return float(distance)

#method to get from address csv file
    #for loop with if statement
def address_loader(address):
    for r in CSV_Address:
        if address == r[2]:
            return int(r[0])

#instantiation of 3 truck objects
truck_1 = Truck.Truck(15, 20, None, 0.0, [1, 13, 14, 8, 6, 20, 29, 30, 31, 14, 37, 40], datetime.timedelta(hours=12), "4001 South 700 East") #
truck_2 = Truck.Truck(30, 12, None, 0.0, [9, 3, 21, 14, 15, 19, 27, 30, 31, 24, 32, 55], datetime.timedelta(hours=17), "4001 South 700 East")
truck_3 = Truck.Truck(17, 15, None, 0.0, [7, 2, 18, 15, 16, 25, 25, 30, 31, 34, 20, 32], datetime.timedelta(hours=8, minutes=30), "4001 South 700 East")

#load truck instantiation using package array to place object ids into each truck
packageTable = HashMap()
package_data_loader("CSV/WGUPS_Package_File.csv", packageTable)

#method for nearest neighbor algorithm
    #With using Truck objects, this algorithm method will place the packages in order, record how many miles the route is, and determine the time each package is delivered.
    #This method will passthrough one truck object.
def delivering_loader(truck):
    not_delivering = []
    for packageId in truck.packages:
        package = packageTable.get(packageId)

        # Skip delayed packages if the truck's time is before their arrival time (9:05 AM)
        if package.id in [6, 25, 28, 32] and truck.time < datetime.timedelta(hours=9, minutes=5):
            continue
        # Enforce truck-specific package assignments
        if package.id in [3, 18, 36] and (truck is not truck_2):
            continue  # Only load these packages on Truck 2
        if package.id in [2, 4, 14, 20] and (truck is not truck_1):
            continue  # Only load these packages on Truck 1

        # Update address for package #9 at 10:20 AM
        if package.id == 9 and truck.time >= datetime.timedelta(hours=10, minutes=20):
            package.address = "410 S State St"
            package.city = "Salt Lake City"
            package.state = "UT"
            package.zipcode = "84111"
            package.status = "Ready for delivery"

        # Assign the truck number to the package
        if truck is truck_1:
            package.truck_number = 1
        elif truck is truck_2:
            package.truck_number = 2
        elif truck is truck_3:
            package.truck_number = 3

        not_delivering.append(package)

    truck.packages.clear()

    # iterate through list of not_delivering until none
    while len(not_delivering) > 0:
        next_address = 2000
        next_package = None
        for package in not_delivering:

            # Skip package #9 if the address is not yet corrected
            if package.id == 9 and truck.time < datetime.timedelta(hours=10, minutes=20):
                continue

            #distance only once
            current_distance = distance_loader(address_loader(truck.address), address_loader(package.address))

            # Find the nearest package
            if current_distance <= next_address:
                next_address = current_distance
                next_package = package

            # Ensure Packages 13, 15, and 19 are delivered together
            if package.id in [13, 15, 19]:
                for group_id in [13, 15, 19]:
                    if group_id not in truck.packages:
                        truck.packages.append(group_id)

        # addition to nearest package into truck.packages
        truck.packages.append(next_package.id)
        not_delivering.remove(next_package)

        truck.mileage += next_address
        truck.address = next_package.address
        truck.time += datetime.timedelta(hours=next_address / 18)

        next_package.delivery = truck.time
        next_package.departure_time = truck.depart_time
        #if next_package.departure is None:  # Set departure time only once
            #next_package.departure = truck.depart_time
    # After the method is written call three times, once for each truck object
    delivering_loader(truck_1)
    delivering_loader(truck_2)
    truck_3.depart_time = min(truck_1.time, truck_2.time) #depart_time
    delivering_loader(truck_3)

#CLI, Class Main definition. if statement with nested if-else structure
class Main:
    print("Western Governors University Parcel Service")
    print("Mileage for rute: ")
    print("Truck 1: ", truck_1.mileage)
    print("Truck 2: ", truck_2.mileage)
    print("Truck 3: ", truck_3.mileage)
    print("Combined Total: ", truck_1.mileage + truck_2.mileage + truck_3.mileage)

    # first; ask for time, then ask if to look single package track or all packages
    text = input("Press 'time' to view package statuses, 'truck' to view truck-specific details, or any key to quit:\n")

    if text == "time":
        try:
            usertime = input("enter 'time' to continue with status of package.(format: HH:MM:SS)\n")
            (h, m, s) = usertime.split(":")
            convert_timedelta = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
            secondinput = input("type 'solo' for status of individual package. write 'all' for a rundown of all packages\n")

            if secondinput == "solo":
                try:
                    soloinput = input("enter package ID\n")
                    package = packageTable.get(int(soloinput))
                    package.package_update(convert_timedelta)
                    print(str(package))
                except ValueError:
                    print("Invalid ID. Program ended")
                    exit()
    #then; data display and program termination
            elif secondinput == "all":
                try:
                    for packageID in range(1, 41):
                        package = packageTable.get(packageID)
                        package.package_update(convert_timedelta)
                        print(str(package))
                except ValueError:
                    print("Invalid ID. Program ended")
                    exit()

            else:
                print("Invalid input. Program ended.")
                exit()

        except ValueError:
            print("Invalid input. Program ended.")
            exit()

    elif text == "truck":
        try:
            truck_no = input("Enter Truck No (1, 2, or 3):\n")

            if truck_no == "1":
                print(f"Truck 1 Mileage: {truck_1.mileage} miles")
                print("Packages on Truck 1:")
                for packageID in truck_1.packages:
                    package = packageTable.get(packageID)
                    print(str(package))

            elif truck_no == "2":
                print(f"Truck 2 Mileage: {truck_2.mileage} miles")
                print("Packages on Truck 2:")
                for packageID in truck_2.packages:
                    package = packageTable.get(packageID)
                    print(str(package))

            elif truck_no == "3":
                print(f"Truck 3 Mileage: {truck_3.mileage} miles")
                print("Packages on Truck 3:")
                for packageID in truck_3.packages:
                    package = packageTable.get(packageID)
                    print(str(package))

            else:
                print("Invalid input. Program ended")
                exit()
        except ValueError:
            print("Invalid ID. Program ended")
            exit()

    else:
        print("Invalid input. Program ended")
        exit()