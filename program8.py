# create a Python program that takes a string as input and counts the number of occurrences of each character in the string. The program will provide users with the character count information, along with additional functionality to enhance their text analysis process.



def character_counter():
    print("Welcome to the Character Counter!")
    text = input("Please enter a string to count the occurrences of each character: ")
    
    character_count = {}
    for char in text:
        if char in character_count:
            character_count[char] += 1
        else:
            character_count[char] = 1
    
    print("Thank you for providing the string.")
    print("Character count:")
    for char, count in character_count.items():
        print(f"- '{char}': {count}")


# Test the character_counter function
character_counter()
