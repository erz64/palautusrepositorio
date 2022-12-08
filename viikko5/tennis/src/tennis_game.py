class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_score = 0
        self.player2_score = 0

    def won_point(self, player_name):
        if player_name == "player1":
            self.player1_score = self.player1_score + 1
        else:
            self.player2_score = self.player2_score + 1

    def get_score(self):
        if self.player1_score == self.player2_score:
            score = self.game_tied()
        elif self.player1_score >= 4 or self.player2_score >= 4:
            score = self.game_won_or_match_point()
        else:
            score = self.normal_score()

        return score
    
    def game_tied(self):
        if self.player1_score == 0:
                score = "Love-All"
        elif self.player1_score == 1:
            score = "Fifteen-All"
        elif self.player1_score == 2:
            score = "Thirty-All"
        elif self.player1_score == 3:
            score = "Forty-All"
        else:
            score = "Deuce"

        return score
    
    def game_won_or_match_point(self):
        score_difference = self.player1_score - self.player2_score

        if score_difference == 1:
            score = "Advantage player1"
        elif score_difference == -1:
            score = "Advantage player2"
        elif score_difference >= 2:
            score = "Win for player1"
        else:
            score = "Win for player2"

        return score
    
    def normal_score(self):
        score = ""
        if self.player1_score == 0:
            score += "Love"
        elif self.player1_score == 1:
            score += "Fifteen"
        elif self.player1_score == 2:
            score += "Thirty"
        elif self.player1_score == 3:
            score += "Forty"
        score += "-"
        if self.player2_score == 0:
            score += "Love"
        elif self.player2_score == 1:
            score += "Fifteen"
        elif self.player2_score == 2:
            score += "Thirty"
        elif self.player2_score == 3:
            score += "Forty"
        return score