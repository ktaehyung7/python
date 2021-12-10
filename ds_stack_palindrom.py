def is_palindrome4(word):
    return word == word[::-1]

def is_palindrome(word):
    stack=[]
    for letter in word:
        stack.append(letter)
    for letter in word:
        if stack.pop() != letter:
            return False
    return True