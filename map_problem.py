ph='How long are the words in this phrase'
w=ph.split(" ")
f=map(len,w)
print(list(f))


def word_lengths(phrase):
    return len(phrase.split(" "))

print(list(map(word_lengths,ph)))