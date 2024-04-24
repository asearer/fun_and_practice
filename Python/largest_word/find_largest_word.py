# Function to find the largest word in a given string
def find_largest_word(input_string):
    # Split the string into a list of words
    words = input_string.split()
    # Return the largest word if the list is not empty, else return an empty string
    return max(words, key=len) if words else ""
