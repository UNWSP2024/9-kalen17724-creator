# Program #3: Average Numbers
# Assume a file containing a series of integers is named numbers.txt and exists on the computer's disk.
# (please use the provided numbers.txt)
# Write a program that reads all of the numbers stored in the file and calculates their total.  

# The program should handle the following exceptions: 

# It should handle any IOError exceptions that are raised.
# It should handle any ValueError exceptions that are raised when the items that are read from the file 
# are converted to a number.
def sum_numbers_from_file():
    ######################
    # Add your code here #
    ######################
    print('In the sum_numbers_from_file function')
    try:
        #list to hold the numbers
        numbers = []
        #opening the file of numbers
        with open("numbers.txt", "r") as file:
            for line in file:
                #transferring the numbers in an integar
                numbers.append(int(line.strip()))
                #Finding the sum of the number
                total = sum(numbers)
        print('The sum of the numbers is: ',total)


    #Handling any IOError 
    except IOError as e:
        print("An error has occurred while accessing the file:", e)
    #Handling any ValueError
    except ValueError as v:
        print("An error occured while reading the file:", v)    


# You don't need to change anything below this line:
if __name__ == '__main__':
    sum_numbers_from_file()