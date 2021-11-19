import requests
from player import Player
import datetime

def main():
    url = "https://nhlstatisticsforohtu.herokuapp.com/players"
    response = requests.get(url).json()

    #print("JSON-muotoinen vastaus:")
    #
    #print(response)

    players = []

    for player_dict in response:
        player = Player(
            player_dict['name'],
            player_dict['nationality'],
            player_dict['assists'],
            player_dict['goals'],
            player_dict['penalties'],
            player_dict['team'],
            player_dict['games']
        )

        players.append(player)

    print("Players from FIN ", str(datetime.datetime.now()))
    print()

    def points(player):
        return player.give_points()
    
    players.sort(key=points, reverse=True)

    for player in players:
        if player.give_nationality() == "FIN":
            print(player)

if __name__ == "__main__":
    main()
