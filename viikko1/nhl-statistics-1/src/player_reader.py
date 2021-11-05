from urllib import request
from player import Player
import ssl

class PlayerReader:
    def __init__(self, url):
        #self._url = "https://nhlstatisticsforohtu.herokuapp.com/players.txt"
        self._url = url

    def get_players(self):
        ssl._create_default_https_context = ssl._create_unverified_context
        #tein tämän lisäyksen, koska tietojen hakeminen ei vaikuttanut muuten
        #onnistuvan macOS:llä. googlasin ongelman ja löysin ratkaisun täältä:
        #https://clay-atlas.com/us/blog/2021/09/26/python-en-urllib-error-ssl-certificate/

        players_file = request.urlopen(self._url)
        players = []

        for line in players_file:
            decoded_line = line.decode("utf-8")
            parts = decoded_line.split(";")

            if len(parts) > 3:
                player = Player(
                    parts[0].strip(),
                    parts[1].strip(),
                    int(parts[3].strip()),
                    int(parts[4].strip())
                )

                players.append(player)

        return players
