from customstack import Stack, Node
matching_dict = {
    "{": "}", 
    "(": ")",
    "[": "]"
}

def has_valid_brackets(string):
    opening = Stack()
    for letter in string:
        if letter in matching_dict:
            opening.push(Node(letter))
        elif letter in matching_dict.values():
            if opening.peek() and matching_dict.get(opening.peek().data) == letter:
                opening.pop()
            else:
                return False
    if opening.top:
        return False
    return True

print(has_valid_brackets("()"))