# By Steven Kha 2018

class GameStats:
    """Track statistics for Alien Invasion."""
    def __init__(self, ai_settings):
        """Initialize statistics."""
        self.ai_settings = ai_settings

        # Start game in an inactive state.
        self.game_active = False
        self.start_game = False


# By Steven Kha 2018