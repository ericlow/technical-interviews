# Solution — Parking Garage

## See `parking_garage.py` for full implementation

## Design Decisions

### Single `spots` dict + `parkedCars` lookup
- `spots: dict[int, ParkingSpot]` — all spots in one collection
- `parkedCars: dict[str, int]` — license plate → spot_id for O(1) unpark lookup
- Avoids maintaining multiple collections in sync; filter by size at search time
- Trade-off: `autopark` is O(n) scan. For small garages this is fine; at scale, could maintain `available_by_size: dict[Size, set[int]]`

### Size compatibility
```python
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
                if best_spot is None or spot.distance < best_spot.distance:
                    best_spot = spot
    return best_spot
```
- Iterates by size preference (exact fit first, then larger)
- Tracks best (minimum distance) spot across all compatible sizes

### Requirement 4 — Entrance + exit optimization
Extend `ParkingSpot` with `entrance_distance` and `exit_distance`. Score = `entrance_distance + exit_distance`. Pick minimum score among compatible spots.

```python
# Extended spot scoring
score = spot.entrance_distance + spot.exit_distance
if best_spot is None or score < best_score:
    best_spot = spot
    best_score = score
```

## Complexity

| Operation | Time |
|---|---|
| `park` | O(1) |
| `unpark` | O(1) |
| `autopark` (current) | O(n) |
| `autopark` (with size buckets + heap) | O(log n) |
