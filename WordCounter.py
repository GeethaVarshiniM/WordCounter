def count_words(text):
    """
    Count the number of words in the given text.
    A word is defined as a sequence of characters separated by whitespace.
    
    Args:
    text (str): The input text from the user.
    
    Returns:
    int: The count of words in the text.
    """
    # Split the text into words using whitespace as the delimiter
    words = text.split()
    return len(words)

def main():
    """
    Main function to execute the Word Counter program.
    """
    # Prompt the user to enter a sentence or paragraph
    user_input = input("Enter a sentence or paragraph to count number of words: ").strip()
    
    # Error handling for empty input
    if not user_input:
        print("Error: You entered an empty input. Please provide some text.")
        return
    
    # Count the words using the count_words function
    word_count = count_words(user_input)
    
    # Display the result
    print(f"The number of words in the given text is: {word_count}")

# Run the main function
if __name__== "__main__":
    main()
