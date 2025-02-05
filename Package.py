class Package:
    def __init__(self, id, address, city, state, zipcode, deadline, weight, status):
        self.id = id
        self.address = address
        self.city = city
        self.state = state
        self.zipcode = zipcode
        self.deadline = deadline
        self.weight = weight
        self.status = status
        self.delivery = None
        self.departure = None
        self.truck_number = None


    def __str__(self):
        return (
               f"Package(id={self.id}, address={self.address}, city={self.city}, "
               f"state={self.state}, zipcode={self.zipcode}, "
               f"deadline={self.deadline}, weight={self.weight},"
               f"status={self.status}, "
               f"delivery={self.delivery}, departure={self.departure}, truck_number={self.truck_number}))"
        )

    def package_update(self, convert_timedelta):
        if self.delivery is not None and self.delivery < convert_timedelta:
            self.status = 'Package delivered'
            # Check if departure time is set and compare
        elif self.departure is not None and self.departure <= convert_timedelta:
            self.status = 'Package en route'
            # If neither condition is met, the package is still at the hub
        else:
            self.status = 'Package at hub'