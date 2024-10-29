#4. Write a program that takes an integer as input and returns an integer with
#reversed digit ordering.
#Examples:
#For input 500, the program should return 5.
#For input -56, the program should return -65.
#For input -90, the program should return -9.
#For input 91, the program should return 19.

def reverse_integer(num):

    reversed_num = 0
    is_negative = False  
    if num < 0:
        is_negative = True 
        num = -num 
    while num > 0:
       
        last_digit = num % 10

        reversed_num = reversed_num * 10 + last_digit  
   
        num = num // 10  

    if is_negative:
        reversed_num = -reversed_num

    return reversed_num


if __name__ == "__main__":
    # input from the user
    user_input = int(input("Enter an integer: ")) 

    result = reverse_integer(user_input)
    print("Reversed integer:", result)
