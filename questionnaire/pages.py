from otree.api import (Page)
import logging


logger = logging.getLogger(__name__)


class Demographics(Page):
    form_model = 'player'

    def get_form_fields(player):
        fields = [
            'age', 'gender', 'transgender', 'legal_sex',
            'nationality', 'ethnicity', 'children',
            'height_cm', 'height_prefer_no',
            'weight_kg', 'weight_prefer_no',
            'attention_check'
        ]

        # Show text box only if Non-binary selected
        if player.gender == "Non-binary (please specify if you wish)":
            fields.insert(fields.index('transgender'), 'gender_nonbinary_text')

        return fields


page_sequence = [Demographics]
