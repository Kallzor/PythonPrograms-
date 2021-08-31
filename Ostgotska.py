def ostgosta():
    sentence = input().split(" ")
    n = 0
    for i in sentence:
        if "ae" in i:
            n += 1
    procent = n / len(sentence)
    if float(procent) >= 0.4:
        print("dae ae ju traeligt va")
    else:
        print("haer talar vi rikssvenska")



ostgosta()

