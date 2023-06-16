def article_sorter():
    print("Welcome to the Article Title Sorter!")
    titles = input("Please enter a list of article titles, separated by commas:data analysis techniques ")

    #  here we are Spliting  the input into a list of titles
    titles = [title.strip() for title in titles.split(",")]

    # Sored the titles in alphabetical order
    sorted_titles = sorted(titles)

    # Display the sorted list of  article titles
    print("\nThank you for providing the article titles.")
    print("The sorted list of titles is:")
    for title in sorted_titles:
        print("-", title)

article_sorter()

