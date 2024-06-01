
class Queue:
    def __init__(self):
        self.queue = []

    # Assume this actually operates in O(1) time as an optimized queue should
    def enqueue(self, item):
        self.queue.insert(0, item)
    
    def dequeue(self):
        return self.queue.pop()

    def size(self):
        return len(self.queue)


satellites = {
  'base': ['sat0'],
  'sat0': ['base', 'sat1', 'sat3', 'sat4'],
  'sat1': ['sat0', 'sat2'],
  'sat2': ['sat1', 'sat3', 'sat4'],
  'sat3': ['sat0', 'sat2', 'sat4'],
  'sat4': ['sat0', 'sat2', 'sat3', 'sat5'],
  'sat5': ['sat4', 'ship']
}

# @param {map<str,List[str]>} satellites
# @return {List[str]}
def pilot_rocket(satellites):
    # Your solution here
    visited_nodes = set()
    nodes_to_visit = []
    paths = []
    paths.append(['base'])
    nodes_to_visit.append('base')
    visited_nodes.add('base')
    while 'ship' not in visited_nodes:
        current_node = nodes_to_visit.pop()
        for child in satellites[current_node]:
            if not child in visited_nodes:
                visited_nodes.add(child)
                nodes_to_visit.insert(0,child)
                for i in range(1, len(paths)+1):
                    print(i, len(paths), paths)
                    if paths[-i][-1] == current_node:
                        new_path = paths[-i].copy()
                        new_path.append(child)
                        paths.append(new_path)
                        if 'ship' in new_path:
                            return new_path
                        else:
                            break

    return None
# ['base', 'sat0', 'sat4', 'sat5', 'ship']
print(pilot_rocket(satellites))