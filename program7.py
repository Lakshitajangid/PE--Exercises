#  create a Python program that takes a list of integers as input and prints the largest and smallest numbers in the list. 

print("Welcome to the Range Finder!")
integer_list = input("Please enter a list of integers, separated by commas: ")

# Split the input string into individual integers
numbers = [int(num) for num in integer_list.split(",")]

# Find the largest and smallest numbers in the list
large = max(numbers)
small= min(numbers)

# Display the results
print("Thank you for providing the list of integers.")
print("The largest number in the list is:", large)
print("The smallest number in the list is:", small)
