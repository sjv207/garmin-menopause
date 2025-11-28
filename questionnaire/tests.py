from otree.api import Bot
from .pages import Demographics
import logging

logger = logging.getLogger(__name__)


class PlayerBot(Bot):

    def play_round(self):

        yield Demographics, {
            'age': 30,
            'gender': "Man (including Trans Man / Trans Male)",
            'transgender': "No",
            'legal_sex': "Male",
            'nationality': "American",
            'ethnicity': "Not Hispanic or Latino",
            'children': "No",
            'height_cm': 175,
            'height_prefer_no': False,
            'weight_kg': 70,
            'weight_prefer_no': False,
            'attention_check': "Strongly agree"
        }
