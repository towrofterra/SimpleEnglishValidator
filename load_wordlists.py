wordlist_850 = open("1500.txt", "r")
words = wordlist_850.read().split(',')
words.sort()
print(len(words))

sorted_wordlist = open("1500_new.txt", "w")
for word in words:
    print(word)
    sorted_wordlist.write(word+",")

wordlist_850.close()
sorted_wordlist.close()
