def magic():
    s = input()
    word = set(list(s))
    if len(s) == len(word):
        print("1")
    else:
        print("0")

magic()
