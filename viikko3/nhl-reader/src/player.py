class Player:
    def __init__(self, name, nationality, assists, goals, penalties, team, games):
        self.name = name
        self.nationality = nationality
        self.assists = assists
        self.goals = goals
        self.penalties = penalties
        self.team = team
        self.games_count = games

    def __gt__(self, other_player):
        if self.goals + self.assists > other_player.goals + other_player.assists:
            return True

    def __str__(self):
        return (f"{self.name:20} {self.team} {self.goals} + {self.assists} = {self.goals + self.assists}")
