from otree.api import (
    models,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency as c,
)
import math
import logging
from settings import TASK_TIME_SECONDS

logger = logging.getLogger('memMatchModels')


author = 'Your name here'

doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'tile_matching'
    PLAYERS_PER_GROUP = None
    # Running time of experiment, in minutes
    TASK_TIME_SECONDS = TASK_TIME_SECONDS
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):

    def creating_session(self):
        for p in self.get_players():
            p.participant.vars['last_stars'] = 0.0
            p.participant.vars['num_correct'] = 0.0


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    star_rating = models.FloatField()
    game_stats = models.LongStringField()
    stars_running_total = models.FloatField(initial=0.0)
    num_correct_running_total = models.IntegerField(initial=0)

    def calc_payoff(self):

        self.payoff = self.star_rating
        logger.debug(f"Payoff: {self.payoff}")

        self.participant.vars['last_stars'] = self.star_rating
        self.participant.vars['num_correct'] += self.star_rating

        logger.info(
            f"Total {self.participant.vars['num_correct']}, last attempt: {self.participant.vars['last_stars']}, round: {self.round_number}")

        # If this is the last round, store the final payout in participant.vars
        if (self.round_number == C.NUM_ROUNDS):
            set_participant_payoff_info(self.participant, "memory_matching")

    def calc_final_payoff(self):
        # Payoffs are integers, so just round up the score
        self.participant.payoff = c(math.ceil(self.participant.vars['num_correct']))
        logger.info(
            f"Setting final payment to: {self.participant.payoff}, from: {self.participant.vars['num_correct']}")


def set_participant_payoff_info(participant, task_name):
    vars = participant.vars
    if not vars or 'payouts' not in vars:
        vars['payouts'] = {}

    payouts = vars['payouts']

    # This will either create a new entry or update the current one
    new_entry = {task_name: vars['num_correct']}
    logger.info(f"Setting {task_name} payoff to: {vars['num_correct']}")
    payouts.update(new_entry)
