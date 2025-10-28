from otree.api import Bot, Submission

from .pages import (TrialInstructions, Trial,
                    Stage1Instructions, Stage1,
                    Stage2Instructions, Stage2,
                    Stage3Instructions, Stage3,)


class PlayerBot(Bot):
    def play_round(self):
        yield TrialInstructions
        Trial.live_method(self.player, {'status': 'success', 'star_rating': 3.5})
        Trial.live_method(self.player, {'status': 'success', 'star_rating': 1.5})
        Trial.live_method(self.player, {'status': 'success', 'star_rating': 2.21})
        yield Submission(Trial, {}, check_html=False)

        yield Stage1Instructions
        Stage1.live_method(self.player, {'status': 'success', 'star_rating': 2.0})
        Stage1.live_method(self.player, {'status': 'success', 'star_rating': 3.0})
        yield Submission(Stage1, {}, check_html=False)
        yield Stage2Instructions
        Stage2.live_method(self.player, {'status': 'success', 'star_rating': 4.0})
        Stage2.live_method(self.player, {'status': 'success', 'star_rating': 1.0})
        yield Submission(Stage2, {}, check_html=False)
        yield Stage3Instructions
        Stage3.live_method(self.player, {'status': 'success', 'star_rating': 5.0})
        Stage3.live_method(self.player, {'status': 'success', 'star_rating': 2.5})
        yield Submission(Stage3, {}, check_html=False)
