import re
import sys


def search(word):
    word = word.lower()
    wordlist_850 = open("850_sorted.txt", "r")
    words_850 = wordlist_850.read().split(',')
    wordlist_1500 = open("1500_sorted.txt", "r")
    words_1500 = wordlist_1500.read().split(',')

    wordlist_850.close()
    wordlist_1500.close()

    if word in words_850:
        print(word+" is in 850 wordlist")
        return True
    if word in words_1500:
        print(word+" is 1500 wordlist")
        return True

    print(word+" is not in any wordlist. Make it more basic")
    return False


# A doc is a string
def search_doc(doc):
    words = re.findall(r"[\w']+", doc)
    for word in words:
        search(word)


# MAIN
if len(sys.argv) > 1:
    args = sys.argv[1:]
    for arg in args:
        search_doc(arg)
else:
    print("Please enter words to be checked after the script name")


# Ogden's wordlist doesn't include "has", "it" or "is" - ridiculous