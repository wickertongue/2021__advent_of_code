def part_one(readings):
    increased_tally = 0
    last_reading = readings[0]

    for reading in readings:
        if reading > last_reading:
            increased_tally += 1
        last_reading = reading
    print(increased_tally)

with open('data.txt') as file:
    readings = file.readlines()
    readings = list(map(int, readings))

    part_one(readings)