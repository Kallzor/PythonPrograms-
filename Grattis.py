words = {}
def run():
    config()
    while 1:
        talk()


def config():
    fh = open("memory.txt", "r")
    for i in fh:
        key, value = i.split(":")
        words[key] = value
    fh.close()


def talk():
    x = input()
    if x in words.keys():
        print(words[x])
    else:
        print("What does that mean?")
        y = input()
        words[x] = y
        addToFile()
        print("Okay, added to my dictionary!")


def addToFile():
    fh = open("memory.txt", "w")
    for key in words:
        fh.write(key + ":" + words[key] + "\n")


run()