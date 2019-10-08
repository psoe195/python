# how many times each word shows up in the sentence.
# Created date: 10/7/2018
# Modified date: 10/7/2019
# Display 5 common words

from collections import Counter

sentence = 'Hello world!. Have a good day. Do you know how many times Hello shows up in this sentence? There are many ways to say Hello'
words = sentence.split()

print(Counter(words))
c = Counter(words)

print(c.most_common(5))

