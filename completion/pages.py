from otree.api import Page
from .models import Player
import logging

logger = logging.getLogger(__name__)


class NonConsent(Page):
    @staticmethod
    def is_displayed(player: Player):
        if not player.is_playing():
            if player.participant.vars['status'] == "Non-Consent":
                player.final_status = "Non-Consent"
                return True


class AttentionCheckFail(Page):
    @staticmethod
    def is_displayed(player: Player):
        if not player.is_playing():
            if player.participant.vars['status'] == "Atn-Check-Fail":
                player.final_status = "Atn-Check-Fail"
                player.participant.payoff = 0
                return True


class Finish(Page):
    @staticmethod
    def is_displayed(player: Player):
        if player.is_playing():
            return True

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        player.calc_final_payoff()


class Results(Page):
    @staticmethod
    def vars_for_template(player: Player):
        player.participant.vars['status'] = "Finished"
        player.final_status = "Finished"
        logger.info(f"Final status for player {player.id_in_group}: {player.final_status}")
        return {
            'task_payoff': float(player.participant.payoff) * player.session.config['real_world_currency_per_point'],
        }

    @staticmethod
    def is_displayed(player: Player):
        if player.is_playing():
            return True


page_sequence = [NonConsent, AttentionCheckFail, Finish, Results]
