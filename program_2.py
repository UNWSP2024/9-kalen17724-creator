# Program #2: Random Number File Writer
# Write a program that writes a series of random numbers (up to 1000) to a file.
# Each random number should be in the range of 1 through 500. 
# The application should let the user specify how many random numbers the file will hold 


import random 

def random_numbers(): 
    with open("random_numbers.txt", "w") as file:
        #user input to know how many numbers will be printed in the file
        amount_of_numbers = int(input("How many numbers do you want printed into the file? "))
        #making sure the number is under 1000
        if amount_of_numbers > 1000:
            print("You can only generate 1000 numbers")
            return random_numbers()
        #making sure the number is greater than 0
        elif amount_of_numbers < 1:
            print("You can only generate numbers between 1 and 1000")
            return random_numbers()
        #doing the work to print the numbers in the file
        for i in range(amount_of_numbers):
            number = random.randint(1, 500)
            file.write(str(number) + "\n")

    print(f"{amount_of_numbers} random numbers have been written to random_numbers.txt")
     
#Calling the function 
random_numbers()