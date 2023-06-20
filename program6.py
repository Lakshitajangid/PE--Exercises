def reverse_message(input_string):
    reversed_string = input_string[::-1]
    return reversed_string

def main():
    print("Welcome to the Message Reverser!")
    user_input = input("Please enter your message: ")
    reversed_input = reverse_message(user_input)
    print("Thank you for your message.")
    print("The reversed version of your message is:", reversed_input)

if __name__ == "__main__":
    main()
