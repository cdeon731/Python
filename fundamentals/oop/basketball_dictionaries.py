class Player:
    def __init__(self, data):
        self.name = data ["name"]
        self.age = data ["age"]
        self.position = data ["position"]
        self.team = data ["team"]
    
    def __repr__(self):
        display = f"Player: {self.name}, Age: {self.age}, Position: {self.position}, Team: {self.team}"
        return display

    @classmethod
    def add_players(cls, data):
        player_objects = []
        for dict in data:
            player_objects.append(cls(dict))
        return player_objects

kevin = {
    "name": "Kevin Durant", 
    "age":34, 
    "position": "small forward", 
    "team": "Brooklyn Nets"
}
jason = {
    "name": "Jason Tatum", 
    "age":24, 
    "position": "small forward", 
    "team": "Boston Celtics"
}
kyrie = {
    "name": "Kyrie Irving", 
    "age":32, "position": "Point Guard", 
    "team": "Brooklyn Nets"
}
    
# Player instances 
kevin_durant = Player(kevin)
jason_tatum = Player(jason)
kyrie_irving = Player(kyrie)

print(kevin_durant.team)
print(jason_tatum.age)
print(kyrie_irving.position)

players = [
    {
    "name": "Kevin Durant", 
    "age":34, 
    "position": "small forward", 
    "team": "Brooklyn Nets"
    },
    {
    "name": "Jason Tatum", 
    "age":24, 
    "position": "small forward", 
    "team": "Boston Celtics"
    },
    {
    "name": "Kyrie Irving", 
    "age":32, "position": "Point Guard", 
    "team": "Brooklyn Nets"
    },
    {
    "name": "Damian Lillard", 
    "age":33, "position": "Point Guard", 
    "team": "Portland Trailblazers"
    },
    {
    "name": "Joel Embiid", 
    "age":32, "position": "Power Foward", 
    "team": "Philidelphia 76ers"
    },
    {
    "name": "", 
    "age":16, 
    "position": "P", 
    "team": "en"
    }
]

new_team = []
for player_dict in players:
    player = Player(player_dict)
    new_team.append(player)

print(new_team)