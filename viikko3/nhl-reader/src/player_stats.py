class PlayerStats:
    def __init__(self, reader):
        self.reader = reader
        self.players = self.reader.get_players()
    
    def top_scorers_by_nationality(self, nationality):
        scorers = []
        for player in self.players:
            if player.nationality == nationality:
                scorers.append(player)
        scorers.sort(reverse=True, key=lambda player: player.points)
        return scorers