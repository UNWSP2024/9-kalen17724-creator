# Program #1: Item Counter
# Assume a file containing a series of names (as strings) is named names.txt 
# (Use the included example file names.txt) and exists on the computer's disk.
# Write a program that displays the number of names that are stored in the file.

def count_file_lines():
    ######################
    # Add your code here #
    ######################
    print('In the count_file_lines function')



# You don't need to change anything below this line:
if __name__ == '__main__':
    count_file_lines()def count_number_of_names():
    count = 0
    with open("names.txt", "r") as file:
        for line in file: 
            count += 1 
    print("There are a total of", count,"names")
    return count

count_number_of_names()    