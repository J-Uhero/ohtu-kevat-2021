class Player:
    def __init__(self, name, nationality, assists, goals, penalties, team, games):
        self.name = name
        self.nationality = nationality
        self.assists = assists
        self.goals = goals
        self.penalties = penalties
        self.team = team
        self.games = games
        self.points = int(goals) + int(assists)

    def give_nationality(self):
        return self.nationality

    def give_points(self):
        return self.points
    
    def __str__(self):
        return f"{self.name:21}{self.team}{self.goals:3} +{self.assists:3} = " \
               f"{str(self.points)}"
