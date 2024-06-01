# @param {List[int]} array
# @param {int} target
# @return {List[List[int]]}
def get_target_indexes(array, target):
  # Your solution here
  value_index_dict = {}
  answer_array = []
  for item in array:
    value_index_dict[item] = array.index(item)
  print(value_index_dict)
  for item in array:
    print(target-item)
    if (target - item) in value_index_dict:
        if value_index_dict[target - item] != array.index(item):
            answer_array.append([value_index_dict.pop(target - item),array.index(item)])
            value_index_dict.pop(item)
  return answer_array
   
  
array = [4, -3, 80, 2, 9, 13, 5, 8]
target = 10
dict = {4: 0, -3: 1, 80: 2, 2: 3, 9: 4, 13: 5, 5: 6, 8: 7}

print(get_target_indexes(array, target))