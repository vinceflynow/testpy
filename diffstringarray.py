#!/usr/bin/env python3
A = ['dog', 'cat', 'monkey', 'pig']
B = ['cat', 'rat', 'dog', 'monkey']
setA = set(A)
setB = set(B)
print(setB - setA)
print(setB ^ setA)
print(setB & setA)
print(setB | setA)

print('dog' in A)
print('boldogruff'.find('dog'))
print('boldogruff'.replace('dog', 'cat'))