def create_wordlist_file():
    """Create a woirdlist of all possible 5 character strings using their provided alphabet and write it to a file"""
    alphabet = "abcdef0123456789"
    wordlist = []
    for i in alphabet:
        for j in alphabet:
            for k in alphabet:
                for l in alphabet:
                    for m in alphabet:
                        wordlist.append(i + j + k + l + m)
    with open("wordlist.txt", "w") as f:
        for word in wordlist:
            f.write(word + "\n")
if __name__ == "__main__":
    create_wordlist_file()