#Aiden Clarke
#5/30.23
#exam 2 q3

nteams = int(input("how many batting teams are there?:"))

for team in range(1, nteams+1):
    nplayers = int(input(f" Team {team}: How many players are there"))
    while nplayers <=0:
        nplayers= int(input("invalid input please enter a positive number "))
    total_score = 0
    for player in range(1, nplayers +1):
        score = float(input(f"player {player} What was you score?:"))
        while score <0 or score > 1:
            score = float(input("invalid input please enter a positive number "))              
        total_score += score 
    BA= total_score / nplayers
    print(f"Team {team}'s average batting score was {BA:.3f} ")



input("press enter to exit")