#5. Write a program that accepts a string as input, capitalizes the first letter of each
#word in the string, and then returns the result string.
#Examples:
#"hi"=> returns "Hi"
#"i love programming"=> returns "I Love Programming"


def capitalize_words(input_string):

    words = input_string.split()
    capitalized_words = [word[0].upper() + word[1:]
    for word in words if word]
    return ' '.join(capitalized_words)


if __name__ == "__main__":
   
    print("Enter a string:")
    user_input = input()  
    
 
    result = capitalize_words(user_input)
    print("Capitalized string:", result)
