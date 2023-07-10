import itertools

characters = 'abcdefghijklmnopqrstuvwxyz'
permutations = itertools.product(characters, repeat=5)

with open('permutations.txt', 'w') as file:
    for perm in permutations:
        line = 'fsrwjcfszeg' + ''.join(perm) + '\n'
        file.write(line)