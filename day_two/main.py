def part_one(data):
    horizontal = 0
    depth = 0

    for line in data:
        direction, amount = line.split()

        if 'forward' in direction:
            horizontal += int(amount)
        elif 'down' in direction:
            depth += int(amount)
        elif 'up' in direction:
            depth -= int(amount)
        else:
            print('no direction given')

    return horizontal * depth

# --------------------------------------------------------------

def part_two(data):
    aim = 0
    depth = 0
    horizontal = 0

    for line in data:
        direction, amount = line.split()

        if 'forward' in direction:
            horizontal += int(amount)
            new_depth = (aim * int(amount))
            depth += new_depth
        elif 'down' in direction:
            aim += int(amount)
        elif 'up' in direction:
            aim -= int(amount)
        else:
            print('no directions!')
    
    return horizontal * depth

# --------------------------------------------------------------

with open('data.txt') as file:
    data = file.readlines()

    print(part_one(data))
    print(part_two(data))