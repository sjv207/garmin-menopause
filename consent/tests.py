import random
from otree.api import Bot
from .pages import Consent, Introduction
import logging

logger = logging.getLogger(__name__)


class PlayerBot(Bot):

    def play_round(self):

        yield Consent, dict(consent=True)
        yield Introduction
