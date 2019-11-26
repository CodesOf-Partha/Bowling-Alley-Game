# Player Class
class player:
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

    def score(self):
        try:
            for i in range(0,len(self._points),2):
                if(i!=len(self._points)-1):
                    if(self._points[i]!=0 and self._points[i+1]!=0):
                        score = self._points[i]+self._points[i+1]
                        if ( score < 10 ):
                            self.addPoints(score)
                        if ( score == 10 ):
                            self.addPoints(15)
                    elif(self._points[i]==10 or self._points[i+1]==10):
                            self.addPoints(20)
                    else:
                        score = self._points[i]+self._points[i+1]
                        self.addPoints(score)
                else:
                    self.addPoints(self._points[i])
        except:
            pass