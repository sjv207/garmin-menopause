from otree.api import Page
from .models import C, Player
import logging

logger = logging.getLogger('memMatchPages')


class TrialInstructions(Page):
    pass


class Trial(Page):
    timeout_seconds = C.TRIAL_TIME_SECONDS

    @staticmethod
    def before_next_page(player, timeout_happened):
        pass
        # player.calc_payoff()
        # player.calc_final_payoff()

    @staticmethod
    def live_method(player: Player, data):
        return player.live_method_tiles(data, "Trial")


class Stage1Instructions(Page):
    pass


class Stage1(Page):
    timeout_seconds = C.TASK_TIME_SECONDS

    @staticmethod
    def before_next_page(player, timeout_happened):
        pass
        # player.calc_payoff()
        # player.calc_final_payoff()

    @staticmethod
    def live_method(player: Player, data):
        return player.live_method_tiles(data, "Stage1")


class Stage2Instructions(Page):
    pass


class Stage2(Page):
    timeout_seconds = C.TASK_TIME_SECONDS

    @staticmethod
    def before_next_page(player, timeout_happened):
        pass
        # player.calc_payoff()
        # player.calc_final_payoff()

    @staticmethod
    def live_method(player: Player, data):
        return player.live_method_tiles(data, "Stage2")


class Stage3Instructions(Page):
    pass


class Stage3(Page):
    timeout_seconds = C.TASK_TIME_SECONDS

    @staticmethod
    def before_next_page(player, timeout_happened):
        pass
        # player.calc_payoff()
        # player.calc_final_payoff()

    @staticmethod
    def live_method(player: Player, data):
        return player.live_method_tiles(data, "Stage3")


page_sequence = [TrialInstructions, Trial,
                 Stage1Instructions, Stage1,
                 Stage2Instructions, Stage2,
                 Stage3Instructions, Stage3,]
