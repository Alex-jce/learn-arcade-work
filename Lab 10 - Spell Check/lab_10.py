import re

# This function takes in a line of text and returns
# a list of words in the line.
def split_line(line):
    return re.findall('[A-Za-z]+(?:\'[A-Za-z]+)?',line)


""" Read in lines from a file """

# Open file, and automatically close when we exit this block.
the_dictionary = open("dictionary.txt")

# Create a list to store names.
dictionary_list = []
# Loop through each line in the file.
for line in the_dictionary:
    dictionary_list.append(line.strip())

the_dictionary.close()

# Linear Search
print("--- Linear Search ---")
# Open AliceInWonderland
chapter_one = open("AliceInWonderland200.txt")
# Set variable and track loops.
for variable, line in enumerate(chapter_one):
    # Assign chapter one to list and get rid of any unneeded symbols in the text
    word_list = []
    line = split_line(line)
    # Read each word, and set the position.
    for word in word_list:
        current_position = 0

        # Check each word one by one to find misspelled words.
        while current_position < len(dictionary_list) and dictionary_list[current_position] != word.upper():
            current_position += 1

        # If misspelled words are found print the word and line it is found on.
        if current_position < len("dictionary.txt"):
            print(f"line {variable + 1},misspelled word:{word}")

chapter_one.close()

print("--- Binary Search ---")

# Open Alice In Wonderland
chapter_one = open("AliceInWonderLand200.txt")
# Create a for loop to look through each word and track the amount of loops.
for variable, line in enumerate(chapter_one):
    chapter_one = split_line(line)
    for word in chapter_one:

        # Set the upper and lower bounds
        lower_bound = 0
        upper_bound = len(dictionary_list) - 1
        found = False

        # Set code to check word in the middle of the text for misspelling. Also define middle
        while lower_bound <= upper_bound and not found:
            middle = (lower_bound + upper_bound) // 2

            # Set code so that when current position is incorrect the lower bound is shifted up by one and the upper
            # bound is shifted down
            if dictionary_list[middle] < word.upper():
                lower_bound = middle + 1

            elif dictionary_list[middle] > word.upper():
                upper_bound = middle -1

            # If compared items are equivalent then do not print anything.
            else:
                found = True

        # If values are not equivalent then print the misspelled words an the lines they are found on.
        if not found:
            print(f"line {variable + 1}, misspelled:{word}")

chapter_one.close()
