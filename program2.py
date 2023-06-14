#  suppose you are addworking on a text analysis tool for a language learning application in which identify all the vowels in the given sentence wap for tha same

def count_vowels(sentence):
    vowels = 'AEIOU'
    vowel_count = sum([1 for char in sentence.upper() if char in vowels])
    total_characters = sum([1 for char in sentence if char.isalpha()])

    vowel_percentage = (vowel_count / total_characters) * 100 if total_characters > 0 else 0

    return vowel_count, vowel_percentage

# Display the welcome message here
print("Welcome to the Vowel Counter!")

# take input as a sentence from the user
sentence = input("Please enter a sentence to count the number of vowels: ")

# calling the function here
vowel_count, vowel_percentage = count_vowels(sentence)
 
 #dispay statements
print("\nThank you for providing the sentence.")
print("The number of vowels in the sentence is:", vowel_count)
print("The percentage of vowels in the sentence is: {:.2f}%".format(vowel_percentage))
