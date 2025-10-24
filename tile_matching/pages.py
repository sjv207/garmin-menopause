from ._builtin import Page
from .models import C, Player
import logging

logger = logging.getLogger('memMatchPages')


class TilePage(Page):
    form_model = 'player'
    form_fields = ['star_rating', 'game_stats']
    timeout_seconds = C.TASK_TIME_SECONDS

    # @staticmethod
    # def is_displayed(player: Player):
    #     if 'expiry' not in player.participant.vars:
    #         # Need to clear these at the beginning of the app
    #         player.participant.vars['num_correct'] = 0
    #         player.participant.vars['num_attempts'] = 0
    #         player.participant.vars['correct_answer'] = 0
    #         player.participant.vars['last_stars'] = 0
    #         # Set the game timer up too
    #         player.participant.vars['expiry'] = time.time() + C.total_time
    #         logger.info(f"Setting timer to : {player.participant.vars['expiry']}")

    #     if 'gameover' in player.participant.vars:
    #         return False
    #     else:
    #         return True

    @staticmethod
    def before_next_page(player: Player, timeout_happened: bool):
        player.calc_payoff()
        player.calc_final_payoff()

    @staticmethod
    def live_method(player: Player, data):
        logger.debug(f"live_method data: {data}")
        return {player.id_in_group: "newGame"}


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
