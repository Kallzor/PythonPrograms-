"""def beekeeper():
    vowels = ["aa", "ee", "ii", "oo", "uu", "yy"]
    while True:
        n = int(input())
        sum = 0
        gatekeep = 0
        bestWord = ""
        if n == 0:
            break
        for i in range(n):
            word = input()
            for vowel in vowels:
                sum += word.count(vowel)
                if sum > gatekeep:
                    gatekeep = sum
                    bestWord = word
        print(bestWord)

beekeeper()
                                   ska vara fkn rätt wtf"""


from sys import stdin

def count_wovels(w):
    v = [
        "aa",
        "ee",
        "ii",
        "oo",
        "uu",
        "yy"
    ]

    return sum([w.count(b) for b in v])

for x in stdin:
    n = int(x)
    if n == 0:
        continue

    most_c = -1
    words = []

    for i in range(n):
        word = stdin.readline().replace("\n", "")
        if count_wovels(word) > most_c:
            words.insert(0, word)
            most_c = count_wovels(word)

    print(words[0])

