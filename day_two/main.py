def format_data_part_one(data):
    orientation = {}

    for line in data:
        line = line.split()
        direction = line[0]
        amount = int(line[1])

        if direction in orientation:
            orientation[direction] += amount
        else:
            orientation[direction] = amount

    return orientation

def part_one(data):
    directions_dict = format_data_part_one(data)

    horizontal = directions_dict['forward']
    depth = (directions_dict['down'] - directions_dict['up'])
    total = horizontal * depth
    
    return total

# --------------------------------------------------------------

def format_data_part_two(data):
    orientation = {
        "aim": 0,
        "depth": 0,
        "horizontal": 0
        }

    for line in data:
        direction, amount = line.split()

        if 'forward' in direction:
            orientation['horizontal'] += int(amount)
            new_depth = (orientation['aim'] * int(amount))
            orientation['depth'] += new_depth
        elif 'down' in direction:
            orientation['aim'] += int(amount)
        elif 'up' in direction:
            orientation['aim'] -= int(amount)
        else:
            print('no directions!')

    return orientation

def part_two(data):
    directions_dict = format_data_part_two(data)

    horizontal = directions_dict['horizontal']
    depth = directions_dict['depth']
    total = horizontal * depth
    
    return total

# --------------------------------------------------------------

with open('data.txt') as file:
    data = file.readlines()

    print(part_one(data))
    print(part_two(data))