class Truck:
    def __init__(self, capacity, speed, load, mileage, packages, depart_time, address):
        self.capacity = capacity
        self.speed = speed
        self.load = load
        self.mileage = mileage
        self.packages = packages
        self.depart_time = depart_time
        self.time = depart_time
        self.address = address

    def __str__(self):
        return (
               f"Truck(capacity={self.capacity}, speed={self.speed}, load={self.load}, "
               f"mileage={self.mileage}, packages={self.packages}, "
               f"depart_time={self.time}, address={self.address})"
        )