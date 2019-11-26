from lane import lane
from player import player

# Lane Object l1
l1=lane(1,2)
print('Lane Id: ',l1.getLaneId())
print('Maximum Players: ',l1.getMaxPlayers())

# Player Objects player1 & player2
# This can also be made like user defined values
player1Points = [1,4,4,5,6,4,5,5,0,10,0,1,7,3,6,4,0,10,2,8,6]
player2Points = [1,4,4,5,6,4,5,5,0,10,0,1,7,3,6,4,0,10,2,8,7]
player1 = player(l1._lane_id,1,"Aadhi",player1Points)
player2 = player(l1._lane_id,2,"Bhuvana",player2Points)

# Calculating the score
player1.score()
player2.score()

# Updating the score
scores = []
scores.append(player1.getTotalPoints())
scores.append(player2.getTotalPoints())

# Printing the scores
print('Player 1 score = ',scores[0])
print('Player 2 score = ',scores[1])

# To find the winner & printing based on score 
# Here player 2's score is greater than player 1's score
# Hence Player 2 is the winner
maximum_score = max(scores)
index_value = scores.index(maximum_score)
print('The winner is player ',index_value+1)