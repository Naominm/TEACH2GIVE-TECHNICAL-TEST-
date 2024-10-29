def is_pangram(sentence):
    
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
                'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    
   
    found_letters = [0] * 26 
    
    
    sentence = sentence.lower()
    
    for char in sentence:
        if char in alphabet:  
            index = alphabet.index(char)  
            found_letters[index] = 1 
    

    for mark in found_letters:
        if mark == 0:
          
            return False

    return True
print(is_pangram("The quick brown fox jumps over the lazy dog"))  
print(is_pangram("Hello World"))  
