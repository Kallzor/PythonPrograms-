def finalexam():
    n = int(input())
    counter = 0
    list_of_answers = []
    for i in range(n):
        list_of_answers.append(input())
    if list_of_answers[0] == "A":
        list_of_answers.pop(0)

    for j in list_of_answers:
        if j == "A":
            counter += 1
    print(counter)


finalexam()