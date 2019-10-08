# how many times each word shows up in the sentence.

from collections import Counter

sentence = 'Hello world!. Have a good day. Do you know how many times Hello shows up in this sentence? There are many ways to say Hello'
words = sentence.split()

print(Counter(words))
c = Counter(words)

print(c.most_common(3))

