# Lane Class
class lane:

    def __init__(self,id,max_players):
        self._lane_id = id
        self._max_players = max_players

    def getMaxPlayers(self):
        return self._max_players
        
    def getLaneId(self):
        return self._lane_id