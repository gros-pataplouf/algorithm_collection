strings = ['racecar', 'acerrac', 'aaccerr', 'naa', 'aan', 'todo', 'doto', 'code', 'bob']

# Output: group_permutations_of_palindromes(strings)
# [['aaccerr', 'acerrac', 'racecar'], ['aan', 'naa'], ['bob']]

def is_permutation_of_palindrome(word):
    hashtable = {}
    for letter in word:
        if not hashtable.get(letter):
            hashtable[letter] = 1
        else:
            hashtable[letter] += 1
    uneven = list(filter(lambda entry: entry % 2 != 0, list(hashtable.values())))
    if len(uneven) > 1:
        return False
    return True



def group_palindromes(input_lst, result=None, hashtable=None):
    if result is None:
        result = []
    if hashtable is None:
        hashtable ={}
    for word in strings:
        split_word = list(word)
        split_word.sort()
        print(split_word)
        # look whether it is a palindrome:
        if is_permutation_of_palindrome(word):
            sorted_word = "".join(split_word)
            if not hashtable.get(sorted_word):
                hashtable[sorted_word] = [word]
            else:
                hashtable[sorted_word].append(word)
    for value in hashtable.values():
        result.append(value)
    for entry in result:
        entry.sort()
    return result

print(group_palindromes(strings))

# solution
def group_permutations_of_palindromes(strings):
    permutations_of_palindromes = {}

    # Iterate through all O(n) strings in our array
    for string in strings:
        # Check if each string is a palindrome O(c)
        if is_permutation_of_palindrome(string):
            # Sort our string's order O(c log c)
            # Permutations will sort to the same string
            sorted_string = ''.join(sorted(string))

            # Initialize the key to an array if we
            # haven't seen any of the string's permutations yet
            if sorted_string not in permutations_of_palindromes:
                permutations_of_palindromes[sorted_string] = []

            permutations_of_palindromes[sorted_string].append(string)

    # This will return all the values of the hash table as an array
    # Since the values are also arrays, this is the form of the result we want
    return list(permutations_of_palindromes.values())


# We use the modulo operator to determine if a number is odd
def is_odd(num):
    return num % 2 != 0

# All O(c) operations
def is_permutation_of_palindrome(string):
    # Use a hash table to count the occurence of each character in a string
    # These are sequential O(c) operations
    character_count_table = {}

    for char in string:
        if char not in character_count_table:
            character_count_table[char] = 0

        character_count_table[char] += 1

    # Sum the number of characters that contain an odd count
    odd_character_count = 0
    for character_count in character_count_table.values():
        if is_odd(character_count):
            odd_character_count += 1

    # If only one character has an odd count, this function returns true
    return odd_character_count <= 1