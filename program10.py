# Python program that finds the second-largest number in a list of integers. The program will provide users with the second-largest number, along with additional functionality to enhance their data analysis capabilities.


def find_second_largest_price(prices):
    # Convert the input string to a list of prices
    price_list = [float(price) for price in prices.split(",")]

    # Remove any duplicates from the list
    unique_prices = list(set(price_list))

    if len(unique_prices) < 2:
        return "Insufficient data. Please provide at least two different prices."

    # Find the second-largest price using the max() function
    second_largest = max(unique_prices)
    unique_prices.remove(second_largest)
    second_largest = max(unique_prices)

    return second_largest


# Prompt the user for input
print("Welcome to the Stock Price Analyzer!")
price_input = input("Please enter a list of stock prices, separated by commas: ")

# Call the function and display the result
result = find_second_largest_price(price_input)
print("Thank you for providing the stock prices.")
print("The second-largest price in the list is:", result)
