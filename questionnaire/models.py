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

    #
    # Preferences page
    #
    patience = models.IntegerField(
        label="How willing are you to give up something that is beneficial for you today in order to benefit more in the future?",
        choices=list(range(0, 11)),
        widget=widgets.RadioSelectHorizontal
    )

    risk = models.IntegerField(
        label="In general, how willing or unwilling are you to take risks?",
        choices=list(range(0, 11)),
        widget=widgets.RadioSelectHorizontal
    )

    altruism = models.IntegerField(
        label="How willing are you to give to good causes without expecting anything in return?",
        choices=list(range(0, 11)),
        widget=widgets.RadioSelectHorizontal
    )

    trust = models.IntegerField(
        label="Generally speaking, would you say that most people can be trusted, or that you can't be too careful in dealing with people?",
        choices=list(range(0, 11)),
        widget=widgets.RadioSelectHorizontal
    )

    reciprocity = models.IntegerField(
        label="If someone does you a favour, how likely is it that you would return the favour, even if it involved some cost to you?",
        choices=list(range(0, 11)),
        widget=widgets.RadioSelectHorizontal
    )

    retaliation = models.IntegerField(
        label="If someone insults you, how likely are you to react with some form of retaliation?",
        choices=list(range(0, 11)),
        widget=widgets.RadioSelectHorizontal
    )

    #
    # Health page
    #
    # Overall physical health (0–10)
    physical_health = models.IntegerField(
        label="Over the past month, how would you rate your overall physical health?",
        choices=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        widget=widgets.RadioSelectHorizontal
    )

    # Fatigue-related items (1–5)
    fatigue_typical = models.IntegerField(
        label="How fatigued have you generally felt during a typical day?",
        choices=[1, 2, 3, 4, 5],
        widget=widgets.RadioSelectHorizontal
    )

    fatigue_feel = models.IntegerField(
        label="I feel fatigued.",
        choices=[1, 2, 3, 4, 5],
        widget=widgets.RadioSelectHorizontal
    )

    fatigue_starting = models.IntegerField(
        label="I have trouble starting things because I am tired.",
        choices=[1, 2, 3, 4, 5],
        widget=widgets.RadioSelectHorizontal
    )

    fatigue_rundown = models.IntegerField(
        label="How run-down did you feel on average?",
        choices=[1, 2, 3, 4, 5],
        widget=widgets.RadioSelectHorizontal
    )

    fatigue_average = models.IntegerField(
        label="How fatigued were you on average?",
        choices=[1, 2, 3, 4, 5],
        widget=widgets.RadioSelectHorizontal
    )

    # Chronic health condition
    chronic_condition = models.StringField(
        label="Do you have any long-term or chronic health condition, illness, or disability that has lasted (or is expected to last) 12 months or more?",
        choices=["Yes", "No", "Prefer not to say"],
        widget=widgets.RadioSelect
    )

    chronic_condition_details = models.LongStringField(
        label="If yes, please specify (optional):",
        blank=True
    )

    #
    # Lifestyle page
    #
    caffeine = models.StringField(
        label="On average, how many caffeinated drinks (coffee, tea, energy drinks) do you consume per day?",
        choices=[
            "None",
            "1",
            "2–3",
            "4+",
            "Prefer not to say"
        ],
        widget=widgets.RadioSelect
    )

    alcohol = models.StringField(
        label="How often do you consume alcoholic drinks?",
        choices=[
            "Never",
            "Monthly or less",
            "2–4 times per month",
            "2–3 times per week",
            "4+ times per week"
        ],
        widget=widgets.RadioSelect
    )

    nicotine = models.StringField(
        label="Do you currently smoke or use nicotine products?",
        choices=[
            "Yes",
            "No",
            "Prefer not to say"
        ],
        widget=widgets.RadioSelect
    )

    medication = models.StringField(
        label="Are you currently taking any prescribed medication that might affect sleep, stress, or hormone levels?",
        choices=[
            "Yes",
            "No",
            "Prefer not to say"
        ],
        widget=widgets.RadioSelect
    )

    medication_text = models.StringField(
        blank=True,
        label="If yes, please specify (optional):"
    )

    #
    # Cronotype page
    #
    chronotype = models.StringField(
        label="How would you describe yourself?",
        choices=[
            "Definite morning type",
            "Rather morning type",
            "Rather evening type",
            "Definite evening type",
            "Prefer not to say"
        ],
        widget=widgets.RadioSelect
    )

    shift_work = models.StringField(
        label="Do you currently work rotating or night shifts?",
        choices=[
            "Yes, regularly",
            "Occasionally",
            "No",
            "Prefer not to say"
        ],
        widget=widgets.RadioSelect
    )

    #
    # Activitry page
    #
    pa_frequency = models.StringField(
        label="In the past month, how often did you engage in moderate or vigorous physical activity (≥ 30 min)?",
        choices=[
            "Never",
            "1-2 days/week",
            "3-4 days/week",
            "5+ days/week",
            "Prefer not to say"
        ],
        widget=widgets.RadioSelect
    )

    pa_demand = models.IntegerField(
        label="On average, how physically demanding are your typical daily activities (including work)? (1 = Not at all, 5 = Extremely)",
        choices=[1, 2, 3, 4, 5],
        widget=widgets.RadioSelectHorizontal
    )
