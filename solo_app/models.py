from otree.api import (
    models,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
)
import logging
from settings import TASK_TIME_SECONDS, TRIAL_TIME_SECONDS

logger = logging.getLogger('memMatchModels')


author = 'Scott Vincent'


class C(BaseConstants):
    NAME_IN_URL = 'app'
    PLAYERS_PER_GROUP = None
    # Running time of experiment, in minutes
    TASK_TIME_SECONDS = TASK_TIME_SECONDS
    TRIAL_TIME_SECONDS = TRIAL_TIME_SECONDS
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    stars_running_total = models.FloatField(initial=0.0)
    num_correct_running_total = models.IntegerField(initial=0)

    def live_method_tiles(self, data):
        logger.info(f"live_method data: {data}")

        if data['status'] != 'failed' and data['status'] != 'new_game':
            self.stars_running_total += data['star_rating']
            self.num_correct_running_total += 1

        return {self.id_in_group: {"status": "new_game",
                                   "star_rating": self.stars_running_total,
                                   "debug": self.session.config['debug_mode'],
                                   }}
