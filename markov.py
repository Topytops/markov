from random import choice


def open_and_read_file(file_path):
    """Takes file path as string; returns text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    contents = open("green-eggs.txt").read()


    return contents #"This should be a variable that contains your file text as one long string"


def make_chains(text_string):
    """Takes input text as string; returns _dictionary_ of markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> make_chains("hi there mary hi there juanita")
        {('hi', 'there'): ['mary', 'juanita'], ('there', 'mary'): ['hi'], ('mary', 'hi': ['there']}
    """
    chains = {}
    #open_and_read_file()
    words = text_string.split()
   
    
    for i in range(len(words) - 2): #Looping over the string of text in order to pull out the tuples, which are our Keys
        our_tuples = words[i], words[i + 1] #Our Tuples!
        if our_tuples not in chains:    
            chains[our_tuples] = [words[i + 2]] #Adding the value, which is the third item in text
        else:
            chains[our_tuples].append(words[i + 2])
    return chains

        



def make_text(chains):
    """Takes dictionary of markov chains; returns random text."""
    
    bi_gram = choice(chains.keys()) #Chose the random keys to determine our first bi-gram
    text = bi_gram[0] + ' ' + bi_gram[1]    #Created the new tuple from the random chosen bi-gram
    while bi_gram in chains:    #Made while loop to loop through the dicitionary, named chains
        chosen_value = choice(chains[bi_gram]) #Randomly selecting the first value and naming it to use in the loop
        text += ' ' + chosen_value #Created the new key based on the randomly selected value
        bi_gram = (bi_gram[1], chosen_value) #Next tuple to use in the loop
    

    return text


input_path = "green-eggs.txt"

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print random_text
