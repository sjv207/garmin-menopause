from os import environ
from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup,
    BasePlayer, Currency as cu
)
import logging

from common.definitions import NATIONALITY

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
        choices=[
            "English, Welsh, Scottish, Northern Irish or British",
            "Irish",
            "Gypsy or Irish Traveller",
            "Any other White background",
            "White and Black Caribbean",
            "White and Black African",
            "White and Asian",
            "Any other Mixed or Multiple ethnic background",
            "Indian",
            "Pakistani",
            "Bangladeshi",
            "Chinese",
            "Any other Asian background",
            "African",
            "Caribbean",
            "Any other Black, Black British, or Caribbean background",
            "Arab",
            "Any other ethnic group",
            "Prefer not to say",
        ],
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
