word_dictionary = {}

user_string = input("please enter a string")
words_list = user_string.split()
for word in words_list:
    if word in word_dictionary:
        word_dictionary[word] += 1
    else:
        word_dictionary[word] = 1

words_list = list(word_dictionary.keys())
words_list.sort()

longest_word = max(len(word) for word in words_list)
for word in words_list:
    print("{:{}}: {}".format(word, longest_word, word_dictionary[word]))


