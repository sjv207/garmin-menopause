from os import environ
from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup,
    BasePlayer, Currency as cu
)
import logging

logger = logging.getLogger(__name__)
author = 'Scott Vincent'


class C(BaseConstants):
    NAME_IN_URL = 'consent'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
    CONSENT_TIMEOUT = int(environ.get('CONSENT_TIMEOUT', 120))  # This is in seconds


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    consent = models.BooleanField(widget=widgets.CheckboxInput, default=False, initial=False)

    def consent_error_message(self, value):
        if not value:
            return 'You must accept the consent form in order to proceed with the study!'

    def conversion_rate(self):
        rate = 1 / self.session.config['real_world_currency_per_point']
        return [cu(rate).to_real_world_currency(self.session), int(rate)]
