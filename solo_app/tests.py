from otree.api import Bot, Submission

from tile_matching.pages import InstructionsTiles, TilePage, Results


class PlayerBot(Bot):
    def play_round(self):
        yield InstructionsTiles
        TilePage.live_method(self.player, {'status': 'success', 'star_rating': 3.5})
        TilePage.live_method(self.player, {'status': 'success', 'star_rating': 1.5})
        TilePage.live_method(self.player, {'status': 'success', 'star_rating': 2.21})
        yield Submission(TilePage, {}, check_html=False)
        # yield Results
