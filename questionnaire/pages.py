from otree.api import (Page)
import logging


logger = logging.getLogger(__name__)


class Demographics(Page):
    form_model = 'player'
    form_fields = [
        'age', 'gender', 'transgender', 'legal_sex',
        'nationality', 'ethnicity', 'children',
        'height_cm', 'height_prefer_no',
        'weight_kg', 'weight_prefer_no',
        'attention_check'
    ]


class Employment(Page):
    form_model = 'player'
    form_fields = [
        'employment_status',
        'employment_other_text',
        'work_arrangement',
        'work_sector',
        'work_sector_other_text',
        'income',
        'weekly_hours',
        'performance_rating'
    ]


class GlobalPreferences(Page):
    form_model = 'player'
    form_fields = [
        'patience',
        'risk',
        'altruism',
        'trust',
        'reciprocity',
        'retaliation'
    ]


class Health(Page):
    form_model = 'player'
    form_fields = [
        'physical_health',
        'fatigue_typical',
        'fatigue_feel',
        'fatigue_starting',
        'fatigue_rundown',
        'fatigue_average',
        'chronic_condition',
        'chronic_condition_details'
    ]


class Lifestyle(Page):
    form_model = 'player'
    form_fields = [
            'caffeine',
            'alcohol',
            'nicotine',
            'medication',
            'medication_text'
        ]


class Chronotype(Page):
    form_model = 'player'
    form_fields = ['chronotype', 'shift_work']


class PhysicalActivity(Page):
    form_model = 'player'
    form_fields = ['pa_frequency', 'pa_demand']


page_sequence = [Demographics, Employment, GlobalPreferences, Health, Lifestyle, Chronotype, PhysicalActivity]
