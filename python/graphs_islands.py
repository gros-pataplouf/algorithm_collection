input1 = [ 
                ['~', '~', '~', '~', '~', '~', '#', '#', '#', '#', '~', '~', '~', '~'],
                ['~', '~', '~', '#', '#', '#', '#', '~', '~', '~', '~', '~', '~', '~'],
                ['~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '#', '#', '#', '#'],
                ['~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '#', '#', '#'],
                ['~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '#', '#', '#'],
                ]
input2 = [
            ['~', '~', '~', '#', '#'],
            ['~', '~', '~', '#', '#'],
            ['~', '#', '~', '~', '~'],
            ['~', '~', '#', '~', '~'],
            ['~', '~', '~', '~', '#'],
                ]


LAND = '#'

def find_islands(matrix):
    num_of_islands = 0
    items_visited = set()
    for idx, row in enumerate(matrix):
        for jdx, item in enumerate(row):
            if item == LAND and (idx, jdx) not in items_visited:
                num_of_islands += 1
                #start graph search
                items_to_visit = []
                items_visited.add((idx, jdx))
                items_to_visit.append((idx, jdx))
                while items_to_visit:
                    elt = items_to_visit.pop()
                    if elt[0] > 0:
                        coordinates = (elt[0]-1,elt[1])
                        y, x = coordinates
                        upper_neighbor = matrix[y][x]
                        if upper_neighbor == LAND and coordinates not in items_visited:
                            items_to_visit.append(coordinates)
                            items_visited.add(coordinates)
                    if elt[0] < len(matrix) - 1:
                        coordinates = (elt[0]+1,elt[1])
                        y, x = coordinates
                        lower_neighbor = matrix[y][x]
                        if lower_neighbor == LAND and coordinates not in items_visited:
                            items_to_visit.append(coordinates)
                            items_visited.add(coordinates)
                    if elt[1] > 0:
                        coordinates = (elt[0],elt[1]-1)
                        y, x = coordinates
                        left_neighbor = matrix[y][x]
                        if left_neighbor == LAND and coordinates not in items_visited:
                            items_to_visit.append(coordinates)
                            items_visited.add(coordinates)
                    if elt[1] < len(row) - 1:
                        coordinates = (elt[0],elt[1]+1)
                        y, x = coordinates
                        print(coordinates, row)
                        right_neighbor = matrix[y][x]
                        if right_neighbor == LAND and coordinates not in items_visited:
                            items_to_visit.append(coordinates)
                            items_visited.add(coordinates)
       
    return num_of_islands

print(find_islands(input2))

#solution 
LAND = '#'
WATER = '~'

def count_islands(map):
    if (not map) or (not map[0]) or (not map[0][0]):
        return 0

    num_rows = len(map)
    num_cols = len(map[0])
    island_count = 0

    for row in range(num_rows):
        for col in range(num_cols):
            # We found another uncounted island
            if map[row][col] == LAND:
                island_count += 1
                # Mark all the pieces of land for the island as viewed
                mark_land_as_viewed_dfs(map, row, col)

    return island_count

def mark_land_as_viewed_dfs(map, row, col):
    num_rows = len(map)
    num_cols = len(map[0])

    # Stopping condition:
    # 1. Outside of the map
    # 2. Reached an adjacent water node
    is_outside_map = row < 0 or col < 0 or row >= num_rows or col >= num_cols
    if is_outside_map or map[row][col] == WATER:
        return

    # Recursive case:
    # 1. Mark the node as viewed by flipping it to water
    # 2. Check the nodes adjacent to the current

    map[row][col] = WATER
    mark_land_as_viewed_dfs(map, row - 1, col)
    mark_land_as_viewed_dfs(map, row + 1, col)
    mark_land_as_viewed_dfs(map, row, col - 1)
    mark_land_as_viewed_dfs(map, row, col + 1)

    return
