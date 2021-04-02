"""Generate Markov text from text files."""
import random
from random import choice


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    long_ass_string = open(file_path).read()

    return long_ass_string


def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains('hi there mary hi there juanita')

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']

        >>> chains[('there','juanita')]
        [None]
    """

    chains = {}

    words = text_string.split()
    # print (words)
    #take words list and make a bunch of tuples as keys, create word pairs in our tuple-keys
    #for loop that goes through list of words, and 
    i = 0
    for i in range(len(words) - 2):
        key_pair = tuple((words[i], words[i + 1]))
        # print (key_pair)

        if key_pair in chains:
            #append value of words at i+2, append to the dictionary at the value of key-pair
            chains[key_pair].append(words[i+2])
        else:
            #make new list
            following_words = [words[i+2]]
            #make the value of words at i+2, append into list
            chains[key_pair] = following_words


        i += 1
    
    return chains





def make_text(chains):
    """Return text from chains."""

    words = []
    #pick a key (word1, word2)
    keys = chains.keys()
    keys_list = list(keys)
    word_pair = random.choice(keys_list)
    words.append(word_pair[0])
    
    while True:
        # if word_pair == ('Sam', 'I'):
        #     words.append(chains(('Sam', 'I')))

       

            #add it to words
            # print(f'First print{word_pair}')
            # print(type(word_pair))
            
        words.append(word_pair[1])
        
        if word_pair in chains:
            #pick a random word from the list assocaited with key (word3)    
            next_word = random.choice(chains[word_pair])
            word_pair = (word_pair[1], next_word)
            # print(f'second print{word_pair}')
            # print(type(word_pair))
        else:
            break

    #last word of first key and the word we just picked and make the next tuple (word2, word3)

    # repeat add it to words through make a new tuple

    return ' '.join(words)


input_path = 'green-eggs.txt'

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print(random_text)


# result =  make_chains(input_text)
# print(result)