class Player:
    def __init__(self, name, score, hearts):
        '''Initializes the player object'''
        self.name = name
        self.score = score
        self.score_upload = False
        self.hearts = hearts