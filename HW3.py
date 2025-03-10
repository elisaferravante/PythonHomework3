def count_unique_words(file_name):
    """
    Opens a file, reads its contents, and returns the number of unique words.
    :param file_name: the name of the file to read
    :return: number of unique words in the file
    """
    try:
        fp = open(file_name, "r")  # Open the file in read mode
        text = fp.read()  # Read the entire content of the file
        fp.close()  # Close the file after reading

        # Remove punctuation and convert to lowercase
        text = text.lower().replace(".", "").replace(",", "").replace("!", "").replace("?", "")

        words = text.split()  # Split the text into a list of words
        unique_words = set(words)  # Convert the list to a set to get unique words

        return len(unique_words)

    except:
        print("There was an error opening or reading the file.")
        return 0


# Compare two books
book1 = "Psychology of the stock market"
book2 = "After the stock market crash of November, 1929"

unique_words_book1 = count_unique_words(book1)
unique_words_book2 = count_unique_words(book2)

print("Unique words in", book1, ":", unique_words_book1)
print("Unique words in", book2, ":", unique_words_book2)

if unique_words_book1 > unique_words_book2:
    print(book1, "has more unique words.")
elif unique_words_book1 < unique_words_book2:
    print(book2, "has more unique words.")
else:
    print("Both books have the same number of unique words.")