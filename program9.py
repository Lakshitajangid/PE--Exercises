# create a Python program that reads a file and counts the number of words in the file. The program will provide users with the word count information, along with additional functionality to enhance their text analysis process.



def count_words(file_path):
    try:
        with open(file_path, 'r') as file:
            text = file.read()
            word_count = len(text.split())
            return word_count
    except FileNotFoundError:
        print("File not found.")
    except IsADirectoryError:
        print("Please provide a valid file path.")

def word_count_analyzer():
    print("Welcome to the Word Count Analyzer!")
    file_path = input("Please enter the path or name of the file to count the number of words: ")

    count = count_words(file_path)
    if count is not None:
        print("Thank you for providing the file.")
        print("The number of words in the file is:", count)

word_count_analyzer()
