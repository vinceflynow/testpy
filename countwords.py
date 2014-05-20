from collections import Counter
words = ['apple', 'apple', 'banana', 'banana', 'banana', 'pear', 'banana', 'pear', 'pear', 'pear', 'pear', 'pear']
freqs = dict(Counter(words))
print(freqs)