# generatePermutations('dev')
# // ['dev', 'dve', 'edv', 'evd', 'vde', 'ved']

# // Notice you include duplicate permutations if there are duplicate letters
# generatePermutations('bob')
# // ['bob', 'bbo', 'bob', 'bbo', 'obb', 'obb']

# If there are duplicate letters, you should include the duplicate permutations of each.
# Time and space complexity is not considered for the quality of the solution — focus on readable code.

#first letter + fct(str[1:])
#second letter + fct(str[1:])

"""
Take a character and treat it as the choice for each decision step
Remove this character from the string and pass the remaining characters recursively
Remove a new decision character at each lower depth until you only have one character remaining at the base case
Repeat for every character at every depth and combine the results
"""


def generate_permutations(string):
    # ** Base case ** - if the string is empty or 1 character, we just return that value
    if len(string) < 2:
        return [string]

    permutations_array = []
    permutations_array.sorted()

    # Iterate through all the characters in the string
    for i in range(len(string)):
        # We move a character to the front and recursively find the permutations of all the characters after it
        # Note that the "front" is relative to a given permutation depth
        front_character = string[i]

        # Remove the new front character from the string
        remaining_chars = string[:i] + string[i+1:]

        # Recursive call to generate an array of strings of the permutations of the remaining characters
        remaining_permutations = generate_permutations(remaining_chars)

        # Add each permutation to the result for a given depth
        for permutation in remaining_permutations:
            permutations_array.append(front_character + permutation)


    return permutations_array


print(generate_permutations("cornelia"))
