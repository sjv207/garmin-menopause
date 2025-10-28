import random
from otree.api import Bot
from .pages import (Garmin, QuestMeno1, QuestMeno2N, QuestMeno2Y, Questionnaire1b,
                    Questionnaire1, Questionnaire2, Questionnaire3)


class PlayerBot(Bot):
    def play_round(self):
        yield Garmin, {
            'garmin_id': "abc@123.com",
            'garmin_wear_frequency': "Only when I exercise",
            'garmin_engagement': True
        }
        yield Questionnaire1, {
            'age': 20,
            'gender': "Man (including Trans Male/Trans Man)",
            't_gender': False,
            'legal_gender': "Female",
            'nationality': "Jordanian",
            'ethnicity': "White",
        }
        yield Questionnaire1b, {
            'children': False,
            'height_ft': 5,
            'height_in': 6,
            'weight': 45,
            'exercise': "1 to 2 times per week",
            'lk_physical_health': 3,
            'lk_mental_health': 3,
            'attention_chk1': 4,
        }
        yield Questionnaire2, {
            'q2_flush': 3,
            'q2_heart': 3,
            'q2_sleep': 3,
            'q2_mood': 3,
            'q2_irritabiity': 3,
            'q2_anxiety': 3,
            'q2_exhaustion': 3,
            'q2_sex': 3,
            'q2_bladder': 3,
            'q2_discomfort': 3,
            'q2_dryness': 3,
            'attention_chk2': 4,
        }
        yield Questionnaire3, {
            'q3_concentrate': 2,
            'q3_worry': 2,
            'q3_useful': 2,
            'q3_capable': 2,
            'q3_strain': 2,
            'q3_difficulties': 2,
            'q3_enjoy': 2,
            'q3_face_up': 2,
            'q3_unhappy': 2,
            'q3_confidence': 2,
            'q3_worthless': 2,
            'q3_happy': 2,
        }
        if self.player.legal_gender == "Female":
            response = random.choice(["Yes, and they were regular",
                                      "Yes, but they were not regular",
                                      "No",
                                      ])
            yield QuestMeno1, {'meno1': response}

        if self.player.legal_gender == "Female" and self.player.meno1 == "No":
            yield QuestMeno2N

        elif self.player.legal_gender == "Female" and self.player.meno1 == "Yes, but they were not regular":
            yield QuestMeno2Y, {
                'trt_hrt': False,
                'trt_testosterone': False,
                'trt_oestrogren': False,
                'trt_antidepressants': False,
                'trt_night_sweats': False,
                'trt_cbt': False,
                'trt_excercise': False,
            }


def live_update(player, data):
    player.num_correct = data['correct']
    player.num_total = data['total']
