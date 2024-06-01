matrix = [
	[ 4,  5,  6,  7,  8,  7,  6,  5,  4,  3,  2],
	[ 5,  6,  7,  8,  9,  8,  7,  6,  5,  4,  3],
	[ 6,  7,  8,  9, 10,  9,  8,  7,  6,  5,  4],
	[ 7,  8,  9, 10, 11, 10,  9,  8,  7,  6,  5],
	[ 8,  9, 10, "X", 12, 11, 10,  9,  8,  7,  6],
	[ 7,  8,  9, 10, 11, 100,  9,  8,  7,  6,  5],
	[ 6,  7,  8,  9, 10,  9,  8,  7,  6,  5,  4],
	[ 5,  6,  7,  8,  9,  8,  7,  6,  5,  4,  3],
	[ 4,  5,  6,  7,  8,  7,  6,  5,  4,  3,  2],
	[ 3,  4,  5,  6,  7,  6,  5,  4,  3,  2,  1],
	[ 2,  3,  4,  5,  6,  5,  4,  3,  2,  1,  0]
]


directions = [(1,0), (0,1), (-1,0), (0,-1)]
result_list = []

def walk(matrix, position_r, position_c, cycle_counter):
    while len(result_list) < len(matrix) * len(matrix[0]):
        current = matrix[position_r][position_c]
        result_list.append(current)
        matrix[position_r][position_c] = None

        try:
            next = matrix[position_r + directions[cycle_counter%4][1]][position_c + directions[cycle_counter%4][0]]
            if next is not None:
                position_r += directions[cycle_counter%4][1]
                position_c += directions[cycle_counter%4][0]
                return walk(matrix, position_r, position_c, cycle_counter)
            else:
                cycle_counter += 1
                position_r += directions[cycle_counter%4][1]
                position_c += directions[cycle_counter%4][0]
                return walk(matrix, position_r, position_c, cycle_counter)
        except IndexError:
            cycle_counter += 1
            position_r += directions[cycle_counter%4][1]
            position_c += directions[cycle_counter%4][0]
            return walk(matrix, position_r, position_c, cycle_counter)
    return result_list

walk(matrix, 0, 0, 0)
print(result_list)