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


page_sequence = [Demographics, Employment]
