def filter_words(word_list):
    if word_list[0]=='h':
        return word_list

l=['hello','are', 'cat','dog','ham','hi','go','to','heart']
print(list(filter(filter_words,l)))
