def part_one(readings):
    increased_tally = 0
    last_reading = readings[0]

    for reading in readings:
        if reading > last_reading:
            increased_tally += 1
        last_reading = reading
    return increased_tally


def part_two(readings):
    depth_increase_count = 0
    prev_sum = sum(readings[:3])

    for index in range(3, len(readings)):
        new_sum = sum(readings[index-2 : index+1])
        if new_sum > prev_sum:
            depth_increase_count +=1
        prev_sum = new_sum

    return depth_increase_count

with open('data.txt') as file:
    readings = file.readlines()
    readings = list(map(int, readings))

    print(part_one(readings))
    print(part_two(readings))