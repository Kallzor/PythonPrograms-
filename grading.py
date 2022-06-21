def grade():
    num_list = list(map(int, input().split()))
    n = int(input())
    grade = 5
    for i in range(len(num_list)):
        if n >= num_list[i]:
            grade = i
            break

    if grade == 0:
        print("A")
    elif grade == 1:
        print("B")
    elif grade == 2:
        print("C")
    elif grade == 3:
        print("D")
    elif grade == 4:
        print("E")
    else:
        print("F")


grade()
