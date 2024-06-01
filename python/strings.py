# str = "blabla"
# for letter in str:
#     print(letter)
# print(id(str))
# print(id(str.replace("a","u")))
# print(str)
# str += "!"
# print(str)
# print(id(str))

# Input
strings = ['racecar', 'acerrac', 'aaccerr', 'naa', 'aan', 'todo', 'doto', 'code', 'bob']

# Output: group_permutations_of_palindromes(strings)
[['aaccerr', 'acerrac', 'racecar'], ['aan', 'naa'], ['bob']]
"""
a string must satisfy the following conditions to be included:
must be permutation of a palindrome
is a palindrome: for index in range len(str): if str[index] != str[-index] return False
is a permutation of a palindrome: 
each letter occurs a multiple of 2 times 
if uneven, each letter but one occurs a multiple of 2 times

create an empty array for storing the hashtables
create an empty array for storing the answer
create an empty array for storing the unordered answer array
make a hashtable for each string: letter, nums of occs. 
decide whether it is a permutation of a palindrome:
=> each letter occurs a multiple of 2 times and 1 letter may be an orphan
if it is a perm of pal: 
    append to first array

        add {hashtable : ['word']}


""" 

def search_and_group_palindrome_permutations(word_list:[str], answer=None, intermediate_answer=None) -> []:
    if answer is None:
        answer = []
    if intermediate_answer is None:
        intermediate_answer = []
    for word in word_list:
        ordered = list(word)
        ordered.sort()
        print(ordered)
        


search_and_group_palindrome_permutations(strings)

