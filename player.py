from score import score

# Player Class
class player(score):
    def __init__(self,lane_id,id,name,points):
        self._lane_id = lane_id
        self._player_id = id
        self._player_name = name
        self._total_points = 0
        self._points = points
    
    def addPoints(self,points):
        self._total_points += points

    def getPlayerId(self):
        return self._player_id

    def getPlayerName(self):
        return self._player_name

    def getTotalPoints(self):
        return self._total_points

    def getPlayerDetails(self):
        print("Lane Id :", self._lane_id)
        print("Player Id :", self._player_id)
        print("Name :", self._player_name)
        print('Points Scored in all 10 sets including extra balls in last set =>')
        print(self._points)