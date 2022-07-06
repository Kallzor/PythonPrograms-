def split_me_daddy(x):
    return [char for char in x]


x = input()

word = split_me_daddy(x)

for i in range(len(word)):
    if word[i] == "a":
        del word[:i]
        break

new = ""

for j in word:
    new += j


print(new)

