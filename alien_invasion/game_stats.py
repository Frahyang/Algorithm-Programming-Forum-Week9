class GameStats():
    '''Track statistics for Alien Invasion'''

    def __init__(self, ai_settings):
        '''Initialise statistics'''
        self.ai_settings = ai_settings
        self.reset_stats()

        #Start Alien Invasion in an active state
        self.game_active = False #Necessary to create a play button

        #High score should never be reset
        self.high_score = 0

    def reset_stats(self):
        '''Initialise statistics that can change during the game'''
        self.ships_left = self.ai_settings.ships_limit
        self.score = 0
        self.level = 1