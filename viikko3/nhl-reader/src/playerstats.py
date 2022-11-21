from playerreader import PlayerReader
from player import Player

class PlayerStats:
    def __init__(self, reader):
        self.reader = reader

    def top_scorers_by_nationality(self, nationality):
        players = []
        for player in self.reader.get_players():
            if player.nationality == "FIN":
                players.append(player)
        
        return sorted(players, reverse=True)
