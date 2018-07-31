# Implement an autocomplete system. That is, given a query string s and a set of all possible query strings,
# return all strings in the set that have s as a prefix.


def auto_complete(stringlist, s):
    # We check every string

    for word in stringlist:
        # We slice it so that we can compare the prefix of the given string and the current word

        if word[0:len(s)] == s:
            continue
        else:
            # If the prefixes are not the same then we remove the word from the list

            stringlist.remove(word)
    # We return the new stringlist with the words that were not removed

    return stringlist


def main():
    wordlist = ["dog", "deer", "deal"]
    s = "de"
    print(auto_complete(wordlist, s))


main()
