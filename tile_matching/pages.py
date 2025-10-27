from ._builtin import Page
from .models import C, Player
import logging

logger = logging.getLogger('memMatchPages')


class TilePage(Page):
    timeout_seconds = C.TASK_TIME_SECONDS * 100

    @staticmethod
    def before_next_page(player: Player, timeout_happened: bool):
        player.calc_payoff()
        player.calc_final_payoff()

    @staticmethod
    def live_method(player: Player, data):
        logger.info(f"live_method data: {data}")

        if data['status'] != 'failed' and data['status'] != 'new_game':
            player.stars_running_total += data['star_rating']
            player.num_correct_running_total += 1

        return {player.id_in_group: {"status": "new_game",
                                     "star_rating": player.stars_running_total,
                                     "debug": player.session.config['debug_mode']}}


class Results(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == C.NUM_ROUNDS

    @staticmethod
    def js_vars(player: Player):
        return dict(final_payoff=player.participant.payoff_plus_participation_fee())


class InstructionsTiles(Page):
    pass


page_sequence = [InstructionsTiles, TilePage, Results]
