class Player:
    def __init__(self, name, nationality, goals, assists, team):
        self.team = team
        self.goals = goals
        self.assists = assists
        self.name = name
        self.nationality = nationality
        self.points=self.goals+self.assists
    
    def __str__(self):
        return f"{self.name:20}{self.team}{self.goals:4}  +{self.assists:3}  ={self.goals+self.assists:4}"
