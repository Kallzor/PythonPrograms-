def run():
    a, b, c, d = list(map(int, input().split()))
    operations = ["+", "-", "*", "/"]
    for opt1 in operations:
        for opt2 in operations:
            if eval(f"a {opt1} b") == eval(f"c {opt2} d"):
                print(opt1, opt2)
                #Jag suger på python och programmering :)

run()