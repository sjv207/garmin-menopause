import time
from settings import DROPOUT_STATES_NON_CONSENT
from .models import C, Player
from otree.api import Page
import logging


logger = logging.getLogger(__name__)


class Consent(Page):
    timeout_seconds = C.CONSENT_TIMEOUT
    form_model = 'player'
    form_fields = ['consent']
    timeout_submission = {'consent': False}

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        if timeout_happened:
            player.consent = False
            player.participant.vars['consent_dropout'] = True
        else:
            player.participant.vars['status'] = "PLAYING"

    @staticmethod
    def app_after_this_page(player: Player, upcoming_apps):
        if player.consent is False:
            logger.info(f"Player did not consent, moving them on. Label: {player.participant.label}")
            player.participant.vars['dropout_state'] = DROPOUT_STATES_NON_CONSENT
            return upcoming_apps[-1]


class Information(Page):
    pass


class Introduction(Page):
    @staticmethod
    def vars_for_template(player: Player):
        return {"conversion_rate": player.conversion_rate()[1], "ecus": player.conversion_rate()[0]}


page_sequence = [Consent, Information, Introduction]