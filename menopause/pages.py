from otree.api import Page
from .models import Player, C

import logging

logger = logging.getLogger(__name__)


class Garmin(Page):
    form_model = 'player'
    form_fields = ['garmin_id', 'garmin_wear_frequency', 'garmin_engagement']

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        if not player.participant.label:
            # If the plasyer label was not set on the participant label, set it base on user input
            player.participant.label = player.garmin_id


class Questionnaire1(Page):
    form_model = 'player'
    form_fields = [
        'age',
        'gender',
        'other_gender',
        't_gender',
        'legal_gender',
        'nationality',
        'ethnicity',
        'other_ethnicity',
    ]

    @staticmethod
    def is_displayed(player: Player):
        return player.is_playing()


class Questionnaire1b(Page):
    form_model = 'player'
    form_fields = [
        'children',
        'height_ft',
        'height_in',
        'weight',
        'exercise',
        'lk_physical_health',
        'lk_mental_health',
        'attention_chk1',
    ]

    @staticmethod
    def is_displayed(player: Player):
        return player.is_playing()


class Questionnaire2(Page):
    form_model = 'player'
    form_fields = [
        'q2_flush',
        'q2_heart',
        'q2_sleep',
        'q2_mood',
        'q2_irritabiity',
        'q2_anxiety',
        'q2_exhaustion',
        'q2_sex',
        'q2_bladder',
        'q2_discomfort',
        'q2_dryness',
        'attention_chk2',
    ]

    @staticmethod
    def is_displayed(player: Player):
        return player.is_playing()


class Questionnaire3(Page):
    form_model = 'player'
    form_fields = [
        'q3_concentrate',
        'q3_worry',
        'q3_useful',
        'q3_capable',
        'q3_strain',
        'q3_difficulties',
        'q3_enjoy',
        'q3_face_up',
        'q3_unhappy',
        'q3_confidence',
        'q3_worthless',
        'q3_happy',
    ]

    @staticmethod
    def is_displayed(player: Player):
        return player.is_playing()

    @staticmethod
    def before_next_page(player, timeout_happened):
        # Did they fail the attention checks?
        if player.attention_chk1 != 4 and player.attention_chk2 != 4:
            player.participant.vars['status'] = 'Atn-Check-Fail'


class QuestMeno1(Page):
    form_model = 'player'
    form_fields = ['meno1']

    @staticmethod
    def is_displayed(player: Player):
        return player.is_playing() and player.legal_gender == "Female"


class QuestMeno2N(Page):
    form_model = 'player'

    @staticmethod
    def is_displayed(player: Player):
        return player.is_playing() and player.legal_gender == "Female" and player.meno1 == "No"

    @staticmethod
    def get_form_fields(player: Player):
        reasons = [reason['name'] for reason in C.MENO2N_REASON]
        return ['meno2N_reason_other', 'meno2N_age', 'meno2N_monthyear'] + reasons


class QuestMeno2Y(Page):
    form_model = 'player'

    @staticmethod
    def is_displayed(player: Player):
        return player.is_playing() and player.legal_gender == "Female" and player.meno1 == "Yes, but they were not regular"

    @staticmethod
    def get_form_fields(player: Player):
        reasons = [reason['name'] for reason in C.MENO2Y_REASON]
        return ['meno2Y_reason_other'] + reasons


page_sequence = [Garmin,
                 Questionnaire1, Questionnaire1b, Questionnaire2,
                 Questionnaire3, QuestMeno1, QuestMeno2N, QuestMeno2Y]
