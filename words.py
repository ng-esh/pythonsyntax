words = ["hello", "world", "python", "programming"]

for word in words:
    print(word.upper())

def print_upper_words_1(words):
    """Print each word from the list in uppercase."""
    for word in words:
        print(word.upper())

# Test case
print_upper_words_1(["hello", "world", "python", "programming"])

def print_upper_words_2(words):
    """Print each word that starts with 'e' in uppercase."""
    for word in words:
        if word.startswith('e') or word.startswith('E'):
            print(word.upper())

# Test case
print_upper_words_2(["hello", "world", "eagle", "Earth", "programming"])

def print_upper_words(words, must_start_with):
    """Print each word in uppercase that starts with any of the specified letters."""
    for word in words:
        if word[0].lower() in must_start_with:
            print(word.upper())

# Test case
print_upper_words(["hello", "hey", "goodbye", "yo", "yes"], must_start_with={"h", "y"})
