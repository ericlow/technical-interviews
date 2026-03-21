"""
ORIGINAL RESPONSE TO QUESTION

We are going to design a Parking Garage.  We will have to manage the state of parking spots and the vehicles as they
are parked, through the day.

2. implement a version of park which takes into account a size of car. there will be
small medium and large versions of cars and parking spaces.  if the car size is small
then it can fit into medium and large spaces. and so on.

3. implement a version of park which takes into account the distance to the parking lot exit
optimize so that we park a car that has optimal distance and size.

4. implement a version of park which takes into account the entrance and exit, and optimizes the overall distance

# Design Issues
1. should we have a single parking_garage.spots field and loop through all spots to find what we are looking for
or should we have lookups?
1a. small_spots, medium_spots, large_spots (needed in #2)
1b. for retrieving a spot, associated with a car. (needed in park, and unpark)


"""
import random
from enum import Enum

class Size(Enum):
    SMALL = 1
    MEDIUM =2
    LARGE = 3

class Car:
    def __init__(self, licensePlate, size:Size):
        self.licensePlate = licensePlate
        self.size = size

class ParkingSpot:
    def __init__(self, spot_id:int, size:Size, distance:int):
        self.spot_id = spot_id
        self.car = None
        self.size = size
        self.distance = distance

    def park(self, car:Car, parkingRegistry:dict):
        self.car = car
        parkingRegistry[car.licensePlate] = self.spot_id

class ParkingGarage:

    def __init__(self, size):
        self.spots = {}             # key = spot_id:int, value = ParkingSpot
        self.parkedCars = {}     # key liencse plates, val = id of spot
        for spot_id in range(size):
            self.spots[spot_id] = ParkingSpot(spot_id, random.choice(list(Size)), random.randint(1,100))

    def park(self, spot_id:int, car:Car) -> bool:
        """
            return False if not success
            return True if success
        """
        # does the spot_id exist?
        # is car none
        # is the car parked already?
        # is the spot available (is a car already in the spot)
        if (not spot_id in self.spots.keys() or
                car is None or
            car.licensePlate in self.parkedCars or
            self.spots[spot_id].car is not None
        ):
            return False

        # get the spot
        # associate car and spot
        # associate car in self.parkedCars
        self.spots[spot_id].park(car, self.parkedCars)

        return True

    def _find_right_size_spot(self, car):
        if car.size == Size.SMALL:
            preferences = [Size.SMALL, Size.MEDIUM, Size.LARGE]
        elif car.size == Size.MEDIUM:
            preferences = [Size.MEDIUM, Size.LARGE]
        else:
            preferences = [Size.LARGE]


        best_spot = None
        for size_pref in preferences:
            for spot in self.spots.values():
                if spot.size == size_pref and spot.car is None:
                    if best_spot is None:
                        best_spot = spot
                    if best_spot.distance > spot.distance:
                        best_spot = spot

        return best_spot

    def autopark(self, car:Car) -> bool:
        """
            return False if not success
            return True if success
        """
        # validation
        # car is None
        if car is None:
            return False

        spot = self._find_right_size_spot(car)
        if spot is None:
            return False

        spot.park(car, self.parkedCars)

        return True
    def unpark(self, car:Car) -> bool:
        """
            return False if not success
            return True if success
        """
        # does the spot_id exist?
        # is car none
        # is the car parked already?
        # is the spot available (is a car already in the spot)
        if (car is None or
            not car.licensePlate in self.parkedCars
        ):
            return False

        # get the spot
        spot_id = self.parkedCars[car.licensePlate]

        # disassociate car and spot
        # disassociate car in self.parkedCars
        self.spots[spot_id].car = None
        del self.parkedCars[car.licensePlate]

        return True

# Example usage and testing
if __name__ == "__main__":
    # Create garage with 10 spots
    garage = ParkingGarage(10)
    print(f"Created: {garage}\n")

    # Create some cars
    small_car = Car("ABC123", Size.SMALL)
    medium_car = Car("XYZ789", Size.MEDIUM)
    large_car = Car("BIG999", Size.LARGE)

    print("=== Requirement 1: Basic park/unpark ===")
    # Manual parking
    success = garage.park(0, small_car)
    print(f"Park {small_car} in spot 0: {success}")
    print(f"Garage: {garage}\n")

    print("=== Requirement 2: Size-based parking ===")
    # Auto parking (any compatible spot)
    success = garage.autopark(medium_car)
    print(f"Autopark {medium_car}: {success}")
    print(f"Garage: {garage}\n")


    print("=== Requirement 3: Distance optimization ===")
    # Optimal parking (closest compatible spot)
    success = garage.autopark(large_car)
    print(f"Park optimal {large_car}: {success}")

    print("=== Edge cases ===")
    # Try to park already parked car
    success = garage.park(5, small_car)
    print(f"Park already parked car: {success}")

    # Try to park in occupied spot
    success = garage.park(0, Car("NEW123", Size.SMALL))
    print(f"Park in occupied spot: {success}")

    # Unpark
    success = garage.unpark(small_car)
    print(f"Unpark {small_car}: {success}")
    print(f"Garage: {garage}")
