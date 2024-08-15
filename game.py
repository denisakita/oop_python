class Player:
    num_players = 0  # Class attribute

    def __init__(self, name):
        self.name = name  # Instance attribute
        self.mana = 100
        self.num_players += 1
        print('self:', self.num_players)


p1 = Player(name='John')
print('Player:', Player.num_players)
