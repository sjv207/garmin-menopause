import random
from otree.api import (
    models,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
)
import logging
from settings import FIXED_RATE, PIECE_RATE, COMPETITION_RATE


logger = logging.getLogger(__name__)

author = 'Scott Vincent'


class C(BaseConstants):
    NAME_IN_URL = 'completion'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
    FIXED_RATE = FIXED_RATE
    PIECE_RATE = PIECE_RATE
    COMPETITION_RATE = COMPETITION_RATE


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    final_status = models.StringField()
    payment_part = models.IntegerField()
    stars_count = models.FloatField()
    tiles_count = models.IntegerField()

    def is_playing(self):
        return self.participant.vars['status'] in ["PLAYING", "Finished"]

    def calc_final_payoff(self):
        """
        Calculate the final payoff for the player based on their session configuration.
        """

        if 'task_payment' not in self.participant.vars:
            pay_task = random.choice(range(1, 4))
            self.payment_part = pay_task

            self.stars_count = self.participant.vars[f'Stage{pay_task}_star_rating']
            self.tiles_count = self.participant.vars[f'Stage{pay_task}_count']

            if pay_task == 1:
                payment = C.FIXED_RATE
            elif pay_task == 2:
                payment = self.stars_count * C.PIECE_RATE
            elif pay_task == 3:
                payment = self.stars_count * C.COMPETITION_RATE

            self.participant.vars['task_payment'] = payment
            self.participant.payoff = payment

        logger.info(f"Task payment set to: {self.participant.vars['task_payment']}, payoff: {self.participant.payoff}")
