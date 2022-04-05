
def word_counter(str):
    counts = dict()
    word = str.split()

    for wrd in word:
        if wrd in counts:
            counts[wrd] += 1
        else:
            counts[wrd] = 1
    return counts

print(word_counter("Seb seb Sebas"))