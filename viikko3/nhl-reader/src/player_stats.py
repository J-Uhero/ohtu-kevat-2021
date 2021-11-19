from datetime import datetime

class PlayerStats:
    def __init__(self, reader):
        self.players = reader.read_players()

    def top_scorers_by_nationality(self, nationality: str):
        def points(player):
            return player.give_points()

        self.players.sort(key=points, reverse=True)

        player_list = []
        player_list.append(f"Players from {nationality} {datetime.now()}\n")

        for player in self.players:
            if player.give_nationality() == nationality:
                player_list.append(str(player))

        return player_list
