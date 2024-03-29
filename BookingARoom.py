"""Going to a contest such as NWERC is not all fun and games,
there are also some worldly matters to tend to. One of these is to
book hotel rooms in time, before all the rooms in town are booked.
In this problem, you should write a program to search for available
 rooms in a given hotel. The hotel has r rooms, numbered from 1 to r,
 and you will be given a list describing which of these rooms are already booked.

Input
The input consists of:

one line with two integers r and n (1≤r≤100, 0≤n≤r), the number of rooms
in the hotel and the number of rooms that are already booked, respectively;

n lines, each with an integer between 1 and r (inclusive), a room number that
is already booked;

All n room numbers of the already booked rooms are distinct.

Output
If there are available rooms, output the room number of any such room. Otherwise, output “too late”."""
import random

def Room():
    x = [int(z) for z in input().split()]
    Ava = x[0]
    Booked = x[1]
    if Ava == Booked:
        return "too late"
    else:
        List = []
        for i in range(Booked):
            List.append(int(input()))
            List.sort()
        for j in range(Ava + 1):
            if j not in List and j != 0:
                return j


print(Room())


def test():
    x = int(input())
    List = []
    for i in range(x):
        List.append(input())
        print(List[i])
    print(List)


#test()
