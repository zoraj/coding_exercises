# http://stackoverflow.com/questions/746082/how-to-find-list-of-possible-words-from-a-letter-matrix-boggle-solver#750012

DICTIONARY_PATH = 'words.txt'

grid = "fxie amlo ewbx astu".split()
nrows, ncols = len(grid), len(grid[0])

# A dictionary word that could be a solution must use only the grid's
# letters and have length >= 3. (With a case-insensitive match.)
import re
alphabet = ''.join(set(''.join(grid)))
bogglable = re.compile('[' + alphabet + ']{3,}$', re.I).match 
# {m,n} Causes the resulting RE to match from m to n repetitions of the preceding RE, 
# attempting to match as many repetitions as possible. 

# What is the dollar sign for? Is it necessary? 


# rstrip = right strip
# lstrip = left strip
# strip = strip white space from both sides
words = set(word.rstrip('\n') for word in open(DICTIONARY_PATH) if bogglable(word))
prefixes = set(word[:i] for word in words
               for i in range(2, len(word)+1))

def solve():
    for y, row in enumerate(grid):
        for x, letter in enumerate(row):
            for result in extending(letter, ((x, y),)):
                yield result

def extending(prefix, path):
    if prefix in words:
        yield (prefix, path)
    for (nx, ny) in neighbors(path[-1]):
        if (nx, ny) not in path:
            prefix1 = prefix + grid[ny][nx]
            if prefix1 in prefixes:
                for result in extending(prefix1, path + ((nx, ny),)):
                    yield result

def neighbors((x, y)):
    for nx in range(max(0, x-1), min(x+2, ncols)):
        for ny in range(max(0, y-1), min(y+2, nrows)):
            yield (nx, ny)

# Print a maximal-length word and its path:
print max(solve(), key=lambda (word, path): len(word))


print "all the words are shown as following:"
print ' '.join(sorted(set(word for (word, path) in solve())))