#2. Write a Python function that checks whether a word or phrase is palindrome or
# not.
# Note: A palindrome is word, phrase, or sequence that reads the same
# backward as forward, e.g., madam,kayak,racecar, or a phrase "nurses run"

def is_palindrome(word):

    word = word.lower().replace(" ", "")
    
   
    length = 0
    for _ in word:
        length += 1

  
    for i in range(length // 2):
        if word[i] != word[length - i - 1]:
            return False

    return True

print(is_palindrome("nurses run")) 
print(is_palindrome("madam")) 
print(is_palindrome("kayak"))
print(is_palindrome("racecar")) 
print(is_palindrome("apple"))
