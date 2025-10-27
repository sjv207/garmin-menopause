from otree.api import Page
from .models import C, Player
import logging

logger = logging.getLogger('memMatchPages')


class InstructionsTiles(Page):
    pass


class TilePage(Page):
    timeout_seconds = C.TASK_TIME_SECONDS

    @staticmethod
    def before_next_page(player, timeout_happened):
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
                                     "debug": player.session.config['debug_mode'],
                                     }}


class Results(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == C.NUM_ROUNDS


page_sequence = [InstructionsTiles, TilePage, Results]
