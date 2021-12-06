class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_score = 0
        self.player2_score = 0

    def won_point(self, player_name):
        if self.player1_name == player_name:
            self.player1_score += 1
        else:
            self.player2_score += 1

    def score_max_three(self):
        results = {0: "Love",
                   1: "Fifteen",
                   2: "Thirty",
                   3: "Forty"}

        if self.player1_score == self.player2_score:
            return f"{results[self.player1_score]}-All"
        return f"{results[self.player1_score]}-{results[self.player2_score]}"
    
    def score_min_four(self):
        difference = self.player1_score - self.player2_score
        return_statement = ""

        if difference == 0:
            return "Deuce"
        elif abs(difference) == 1:
            return_statement += "Advantage "
        else:
            return_statement += "Win for "

        if difference > 0:
            return return_statement + "player1"  
        return return_statement + "player2"

    def get_score(self):
        if max(self.player1_score, self.player2_score) < 4:
            return self.score_max_three()
        else:
            return self.score_min_four()
