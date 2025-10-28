from otree.api import (
    models,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
)
import logging
from settings import TASK_TIME_SECONDS, TRIAL_TIME_SECONDS, FIXED_RATE, PIECE_RATE, COMPETITION_RATE

logger = logging.getLogger('memMatchModels')


author = 'Scott Vincent'


class C(BaseConstants):
    NAME_IN_URL = 'app'
    PLAYERS_PER_GROUP = None
    # Running time of experiment, in minutes
    TASK_TIME_SECONDS = TASK_TIME_SECONDS
    TRIAL_TIME_SECONDS = TRIAL_TIME_SECONDS
    NUM_ROUNDS = 1
    FIXED_RATE = FIXED_RATE
    PIECE_RATE = PIECE_RATE
    COMPETITION_RATE = COMPETITION_RATE


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    def live_method_tiles(self, data, stage_name):
        logger.info(f"live_method data: {data}")
        if f"{stage_name}_star_rating" not in self.participant.vars:
            self.participant.vars[f"{stage_name}_star_rating"] = 0.0
            self.participant.vars[f"{stage_name}_count"] = 0

        if data['status'] != 'failed' and data['status'] != 'new_game':
            self.participant.vars[f"{stage_name}_star_rating"] += data['star_rating']
            self.participant.vars[f"{stage_name}_count"] += 1

        logger.info(f"{stage_name} total stars: {self.participant.vars[f'{stage_name}_star_rating']}, count: {self.participant.vars[f'{stage_name}_count']}")

        return {self.id_in_group: {"status": "new_game",
                                   "star_rating": self.participant.vars[f"{stage_name}_star_rating"],
                                   "debug": self.session.config['debug_mode'],
                                   }}
