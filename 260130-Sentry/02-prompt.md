# Sentry On-Site — Parking Garage (Python)

## Type
Python coding — OOP design, progressive requirements

## Problem

Design a parking garage system. Implement progressively more sophisticated versions of `park`.

## Classes (given)

```python
class Size(Enum):
    SMALL = 1
    MEDIUM = 2
    LARGE = 3

class Car:
    licensePlate: str
    size: Size

class ParkingSpot:
    spot_id: int
    size: Size
    distance: int  # distance to exit
    car: Car | None

class ParkingGarage:
    spots: dict[int, ParkingSpot]
    parkedCars: dict[str, int]  # license plate -> spot_id
```

## Requirements

### Requirement 1 — Basic park/unpark
- `park(spot_id, car) -> bool`: park a car in a specific spot
- `unpark(car) -> bool`: remove a car from its spot
- Return `False` if: spot doesn't exist, car is None, car already parked, spot already occupied

### Requirement 2 — Size-based auto-parking
- `autopark(car) -> bool`: find any compatible spot automatically
- A small car fits in small, medium, or large spots
- A medium car fits in medium or large spots
- A large car fits only in large spots

### Requirement 3 — Distance optimization
- `autopark` should prefer the spot with the **smallest distance** to exit among compatible spots
- Still respect size compatibility

### Requirement 4 — Entrance/exit optimization
- Extend to consider both entrance and exit distances
- Optimize for **total travel distance** (entrance → spot + spot → exit)

## Design questions to discuss
- Single `spots` dict vs separate `small_spots`, `medium_spots`, `large_spots`?
- How to efficiently look up which spot a car is in (for unpark)?
