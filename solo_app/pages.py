from otree.api import Page
from .models import C, Player
import logging

logger = logging.getLogger('memMatchPages')


class TrialInstructions(Page):
    pass


class Trial(Page):
    @staticmethod
    def live_method(player: Player, data):
        return player.live_method_tiles(data, "Trial")

    @staticmethod
    def get_timeout_seconds(player):
        return player.session.config['TRIAL_TILE_GRID_TIMEOUT_SECONDS']


class Stage1Instructions(Page):
    pass


class Stage1(Page):
    @staticmethod
    def live_method(player: Player, data):
        return player.live_method_tiles(data, "Stage1")

    @staticmethod
    def get_timeout_seconds(player):
        return player.session.config['TILE_GRID_TIMEOUT_SECONDS']


class Stage2Instructions(Page):
    pass


class Stage2(Page):
    @staticmethod
    def live_method(player: Player, data):
        return player.live_method_tiles(data, "Stage2")

    @staticmethod
    def get_timeout_seconds(player):
        return player.session.config['TILE_GRID_TIMEOUT_SECONDS']


class Stage3Instructions(Page):
    pass


class Stage3(Page):
    @staticmethod
    def live_method(player: Player, data):
        return player.live_method_tiles(data, "Stage3")

    @staticmethod
    def get_timeout_seconds(player):
        return player.session.config['TILE_GRID_TIMEOUT_SECONDS']


page_sequence = [TrialInstructions, Trial,
                 Stage1Instructions, Stage1,
                 Stage2Instructions, Stage2,
                 Stage3Instructions, Stage3,]
