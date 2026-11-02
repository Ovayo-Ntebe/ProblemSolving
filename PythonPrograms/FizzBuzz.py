#Write a function called fizz_buzz(numbers).
#Use a loop.
#Use conditional statements.
#Use the modulo operator (%).
# numbers = [1, 3, 5, 9, 10, 15, 22]

#Prints "Fizz" if a number is divisible by 3.
#Prints "Buzz" if a number is divisible by 5.
#Prints "FizzBuzz" if a number is divisible by both 3 and 5.
#Otherwise, prints the number itself.

#Time complezxity : I think O(n) since i am going through the list once just checking linerally

def fizz_buzz(numbers):
    for n in numbers:
        if((n%3 == 0) and (n%5 == 0)): 
            print("FizzBuzz")
        elif(n%5 == 0):
            print("Buzz")
        elif((n%3 ==0)):
            print("Fizz")
        else:
            print(n)
            
#test the function i guess
numbers = [1, 3, 5, 9, 10, 15, 22]
fizz_buzz(numbers)