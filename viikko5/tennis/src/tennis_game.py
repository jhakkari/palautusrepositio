class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_points = 0
        self.player2_points = 0

    def won_point(self, player_name):
        if player_name == "player1":
            self.player1_points = self.player1_points + 1
            return

        self.player2_points = self.player2_points + 1

    def draw(self):
        points = self.player1_points
        message = ""
        if points == 0:
            message = "Love-All"
        if points == 1:
            message = "Fifteen-All"
        if points == 2:
            message = "Thirty-All"
        if points == 3:
            message = "Forty-All"
        if points >= 4:
            message = "Deuce"

        return message

    def different_over_4_points(self):
        message = ""
        player1_points = self.player1_points - self.player2_points
        if player1_points == 1:
            message = "Advantage player1"
        elif player1_points == -1:
            message = "Advantage player2"
        elif player1_points >= 2:
            message = "Win for player1"
        else:
            message = "Win for player2"
        
        return message

    def different_points(self):
        return self.stringbuilder(self.player1_points) + "-" + self.stringbuilder(self.player2_points)
    
    def stringbuilder(self, points):
        if points == 0:
            return "Love"
        elif points == 1:
            return "Fifteen"
        elif points == 2:
            return "Thirty"
        elif points == 3:
            return "Forty"

    def get_score(self):
        score = ""
        temp_score = 0

        if self.player1_points == self.player2_points:
            return self.draw()

        if self.player1_points >= 4 or self.player2_points >= 4:
            return self.different_over_4_points()

        return self.different_points()
