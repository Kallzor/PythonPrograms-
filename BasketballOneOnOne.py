"""Alice and Barbara played some friendly games of one-on-one basketball after work,
 and you agreed to help them keep score. The rules of the game were simple:

Each successful shot by a player earns them either one or two points;

The first player to eleven points wins, with one exception;

If the score is tied 10–10, the previous rule is replaced by a “win by 2” rule: the first player
 to lead the other by at least two points wins.

So for example, 11–7, 9–11, and 14–12 are possible final scores (but not 14–13).

Whenever Alice or Barbara scored points, you jotted down an A or B (indicating a score by Alice or by Barbara)
 followed by a 1 or 2 (the number of points scored). You have some records of the games Alice and Barbara
 played in this format, but do not remember who won each game. Can you reconstruct the winner from the game
  record?

Input
The input consists of a single line with no more than 200 characters: the record of one game.
The record consists of single letters (either A or B) alternating with single numbers (either 1 or 2)
, and includes no spaces or other extraneous characters. Each record will be a correct scoring history
 of a single completed game, played under the rules described above.

Output
Print a single character, either A or B: the winner of the recorded game."""

def Basket():
    AScore = 0
    BScore = 0
    n = input()
    for i in range(len(n)):
        if n[i] == "A":
            AScore += int(n[i+1])
        elif n[i] == "B":
            BScore += int(n[i+1])
    if int(BScore) > int(AScore):
        print("B")
    else:
        print("A")

Basket()
