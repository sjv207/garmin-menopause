from otree.api import Page
from .models import C, Player
import logging

logger = logging.getLogger('memMatchPages')


class TrialInstructions(Page):
    pass


class Trial(Page):
    timeout_seconds = C.TRIAL_TIME_SECONDS

    @staticmethod
    def before_next_page(player, timeout_happened):
        pass
        # player.calc_payoff()
        # player.calc_final_payoff()

    @staticmethod
    def live_method(player: Player, data):
        return player.live_method_tiles(data)


class Results(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == C.NUM_ROUNDS


page_sequence = [TrialInstructions, Trial, Results]
