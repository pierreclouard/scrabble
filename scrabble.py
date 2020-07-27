import time
import enchant
import itertools

# Set dict variable to use enchant dictionary
d = enchant.Dict("en_US")

# Ask user for his 7 letters
print('Hi, what are your 7 letters?')

time.sleep(0.5)

letters = []

for i in range(1, 8):
    letters.append(input(f"Letter {i}: "))

print(f"Your letters are {letters} ")

# Shuffle letters from users to find a right combination

words = list(itertools.permutations(letters))

words7 = []
words6 = []
words5 = []
words4 = []
words3 = []
words2 = []


for word in words:
    # transforming unique letters into words
    word = ''.join(word)
    test = d.check(f"{word}")
    # testing every possibilities
    if test is True:
        print(f"The word {word} exists! {len(word)} letters. Well done!)")
        words7.append(word)
    else:
        d.check(f"{word}")

print(words7)

# Need to create a loop that shuffles a group of 6, then 5, 4 ,3 letters etc until it finds an existing word.


# copying full list of letters
words6 = words7.copy()


# keeping only 6 characters per string, and testing them - c'est la ou je suis bloque putain
for word6 in words6:
    words6[:] = (elem[:6] for elem in words6)
    words6 = list(itertools.permutations(words6))
    print(words6)






