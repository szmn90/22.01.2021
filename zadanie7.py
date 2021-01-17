def longest_word("PanTadeusz.txt"):
    word_len = []
    for n in PanTadeusz.txt:
        word_len.append((len(n), n))
    word_len.sort()
    return word_len[-1][1]

print(longest_word)

#nie dziala 