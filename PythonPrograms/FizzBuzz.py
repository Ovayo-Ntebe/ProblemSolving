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
#The loop visits every element once: O(n).
#Each modulo operation takes constant time: O(1).
#Each conditional comparison takes constant time: O(1).
#Printing each result is treated as constant work per element.

def fizz_buzz(numbers):
    result = []
    for n in numbers:
        if((n%3 == 0) and (n%5 == 0)): #could have used mod 15 since its a lowest common multiple
            #print("FizzBuzz") #leetcode ussually wants thinngs returned in a list. so no prints
            result.append("FizzBuzz")
        elif(n%5 == 0):
            #print("Buzz")
            result.append("Buzz")
        elif((n%3 ==0)):
            #print("Fizz")
            result.append("Fizz")
        else:
            #print(n)
            result.append(str(n))
            
    return result
#test the function i guess
numbers = [1, 3, 5, 9, 10, 15, 22]
print(fizz_buzz(numbers))