from otree.api import Bot
from .pages import (Demographics, Employment, GlobalPreferences,
                    Health, Lifestyle, Chronotype, PhysicalActivity,
                    AMS, GeneralHealth, PartA, PartB, PartC, PartD, PartE,
                    PartF, EQ5D, PHQ9, GAD7)
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
            'ethnicity': "White: Irish",
            'children': "No",
            'height_cm': 175,
            'height_prefer_no': False,
            'weight_kg': 70,
            'weight_prefer_no': False,
            'attention_check': "Strongly agree"
        }
        yield Employment, {'employment_status': "Employed full-time",
                           'employment_other_text': "",
                           'work_arrangement': "Fully on-site",
                           'work_sector': "Non-profit or charity sector",
                           'work_sector_other_text': "",
                           'income': "£30,000-£30,999",
                           'weekly_hours': "30-39 hours",
                           'performance_rating': 2}
        yield GlobalPreferences, {'patience': 7,
                                  'risk': 5,
                                  'altruism': 6,
                                  'trust': 4,
                                  'reciprocity': 8,
                                  'retaliation': 3}
        yield Health, {'physical_health': 2,
                       'fatigue_typical': 3,
                       'fatigue_feel': 4,
                       'fatigue_starting': 2,
                       'fatigue_rundown': 3,
                       'fatigue_average': 3,
                       'chronic_condition': "No",
                       'chronic_condition_details': ""}
        yield Lifestyle, {'caffeine': "1",
                          'alcohol': "Never",
                          'nicotine': "No",
                          'medication': "No",
                          'medication_text': ""
                          }
        yield Chronotype, {'chronotype': "Definite morning type",
                           'shift_work': "No"}
        yield PhysicalActivity, {'pa_frequency': "Never",
                                 'pa_demand': 2}
        yield AMS, {'ams1': "2",
                    'ams2': "3",
                    'ams3': "1",
                    'ams4': "2",
                    'ams5': "4",
                    'ams6': "2",
                    'ams7': "3",
                    'ams8': "2",
                    'ams9': "1",
                    'ams10': "2",
                    'ams11': "3",
                    'ams12': "2",
                    'ams13': "4",
                    'ams14': "2",
                    'ams15': "3",
                    'ams16': "2",
                    'ams17': "1",
                    }
        yield GeneralHealth, {'q3_concentrate': 2,
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
        yield PartA, {'menopause_status': "Don't know", }
        yield PartB, {"last_period_time": "Over 12 months ago",
                      "last_period_date": "DD/MM/YYYY",
                      "period_length": "7 days or longer",
                      "bleeding_amount": "Heavy",
                      "cycle_regularity": "Somewhat irregular",
                      "symptom_interference": 3,
                      "cramps": "Never",
                      "headaches": "Never",
                      "mood_swings": "Never",
                      "trouble_concentrating": "Never",
                      "breast_tenderness": "Never",
                      "absent_periods": "No",
                      }
        yield PartC, {"reason_contraceptive": True,
                      "reason_menopause": True,
                      "reason_pregnancy": True,
                      "reason_surgery": True,
                      "reason_chemo": True,
                      "reason_eating": True,
                      "reason_endocrine": True,
                      "reason_pcos": True,
                      "reason_none": True,
                      "reason_other": "Blah",
                      }
        yield PartD, {"age_menopause": 50, "uterus_ovaries_removed": "No", "current_hrt": "No"}
        yield PartE, {"used_combined": True,
                      "used_progestin": True,
                      "used_ius": True,
                      "used_emergency": True,
                      "used_none": True,
                      }
        yield PartF, {"pregnant": "No",
                      "recent_pregnancy": "No",
                      "postpartum_weeks": "No",
                      "breastfeeding": "No",
                      }
        yield EQ5D, {'mobility': "I have no problems in walking about",
                     'selfcare': "I have no problems with self-care",
                     'activities': "I have no problems with performing my usual activities",
                     'pain': "I have no pain or discomfort",
                     'anxiety': "I am not anxious or depressed",
                     }
        yield PHQ9, {
            'phq1': '0',
            'phq2': '1',
            'phq3': '2',
            'phq4': '3',
            'phq5': '0',
            'phq6': '1',
            'phq7': '2',
            'phq8': '3',
            'phq9': '0',
            'impairment': 'Not difficult at all'
        }
        yield GAD7, {
            'gad1': '0',
            'gad2': '1',
            'gad3': '2',
            'gad4': '3',
            'gad5': '0',
            'gad6': '1',
            'gad7': '2',
            'gad_impairment': 'Not difficult at all'
        }
