from os import environ
from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup,
    BasePlayer, Currency as cu
)
import logging

from common.definitions import ETHNICITY, NATIONALITY

logger = logging.getLogger(__name__)
author = 'Scott Vincent'


class C(BaseConstants):
    NAME_IN_URL = 'questionnaire'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    #
    # Demographics page
    #
    age = models.IntegerField(
        min=0,
        max=120,
        label="What is your age (in years)?"
    )

    gender = models.StringField(
        label="Which of the following best describes your gender?",
        choices=[
            "Man (including Trans Man / Trans Male)",
            "Woman (including Trans Woman / Trans Female)",
            "Non-binary (please specify if you wish)",
            "Prefer not to say",
        ],
        widget=widgets.RadioSelect
    )

    gender_nonbinary_text = models.StringField(
        blank=True,
        label="If you wish, you may specify your gender:"
    )

    transgender = models.StringField(
        label="Do you self-identify as transgender?",
        choices=["Yes", "No", "Prefer not to say"],
        widget=widgets.RadioSelect
    )

    legal_sex = models.StringField(
        label="What is your sex as recorded on legal or official documents?",
        choices=["Male", "Female", "Prefer not to say"],
        widget=widgets.RadioSelect
    )

    nationality = models.StringField(
        label="What is your nationality?",
        choices=NATIONALITY
    )

    ethnicity = models.StringField(
        label="How would you describe your ethnicity? (Options defined by UK Office for National Statistics)",
        choices=ETHNICITY,
        widget=widgets.RadioSelect
    )

    children = models.StringField(
        label="Do you have any children?",
        choices=["Yes", "No", "Prefer not to say"],
        widget=widgets.RadioSelect
    )

    height_cm = models.IntegerField(
        min=50, max=260,
        blank=True,
        label="What is your height (in centimetres)?"
    )

    height_prefer_no = models.BooleanField(
        blank=True,
        label="Prefer not to say"
    )

    weight_kg = models.IntegerField(
        min=20, max=300,
        blank=True,
        label="What is your weight (in kilograms)?"
    )

    weight_prefer_no = models.BooleanField(
        blank=True,
        label="Prefer not to say"
    )

    attention_check = models.StringField(
        label="Please read carefully: to show you are paying attention, select “Strongly agree” for this question.",
        choices=[
            "Strongly disagree",
            "Disagree",
            "Neutral",
            "Agree",
            "Strongly agree"
        ],
        widget=widgets.RadioSelect
    )

    #
    # Employment page
    #
    employment_status = models.StringField(
        label="Which of the following best describes your current employment situation?",
        choices=[
            "Employed full-time",
            "Employed part-time",
            "Self-employed / Freelancer",
            "Currently unemployed",
            "Student",
            "Retired",
            "Other (please specify)"
        ],
        widget=widgets.RadioSelect
    )

    employment_other_text = models.StringField(blank=True)

    work_arrangement = models.StringField(
        label="How would you describe your usual work arrangement?",
        choices=[
            "Fully on-site",
            "Fully remote / work from home",
            "Hybrid (mix of home and on-site)",
            "Not applicable (e.g., not currently working)"
        ],
        widget=widgets.RadioSelect
    )

    work_sector = models.StringField(
        label="In which sector do you currently work (or have most recently worked)?",
        choices=[
            "Public sector (e.g., education, healthcare, government)",
            "Private sector (e.g., business, industry, finance)",
            "Non-profit or charity sector",
            "Academic or research institution",
            "Other (please specify)",
            "Not applicable"
        ],
        widget=widgets.RadioSelect
    )

    work_sector_other_text = models.StringField(blank=True)

    income = models.StringField(
        label="What is your approximate monthly net income (after taxes) in GBP (£)?",
        choices=[
            "Less than £1,000",
            "£1,000-£1,999",
            "£2,000-£2,999",
            "£3,000-£3,999",
            "£4,000-£4,999",
            "£5,000 or more",
            "Prefer not to say"
        ],
        widget=widgets.RadioSelect
    )

    weekly_hours = models.StringField(
        label="On average, how many hours per week do you work (including paid and unpaid overtime)?",
        choices=[
            "Fewer than 10 hours",
            "10-19 hours",
            "20-29 hours",
            "30-39 hours",
            "40 hours or more",
            "Not applicable"
        ],
        widget=widgets.RadioSelect
    )

    performance_rating = models.IntegerField(
        label="Over the past month, how would you rate your typical work performance compared to your usual level?",
        choices=[1, 2, 3, 4, 5],
        widget=widgets.RadioSelect
    )

