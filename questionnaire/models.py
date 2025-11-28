from os import environ
from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup,
    BasePlayer, Currency as cu
)
import logging

from common.definitions import ETHNICITY, NATIONALITY

logger = logging.getLogger(__name__)
author = 'Scott Vincent'


def make_field_5(label: str, blank: bool = False):
    return models.IntegerField(label=label, choices=C.LIKERT5, widget=widgets.RadioSelect, blank=blank)


def make_field_3(label: str):
    return models.IntegerField(label=label, choices=C.LIKERT3, widget=widgets.RadioSelect)


class C(BaseConstants):
    NAME_IN_URL = 'questionnaire'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
    LIKERT5 = [[i, ''] for i in range(6)]
    LIKERT3 = [[i, ''] for i in range(4)]


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

    #
    # Menopause page
    #
    q2_flush = make_field_5("Hot flushes, sweating (episodes of sweating)")
    q2_heart = make_field_5(
        "Heart discomfort (unusual awareness of heartbeat, heart skipping, heart racing, tightness)")
    q2_sleep = make_field_5(
        "Sleep problems (difficulty in falling asleep, difficulty in sleeping through, waking up early)")
    q2_mood = make_field_5("Depressive mood (feeling down, sad, on the verge of tears, lack of drive, mood swings)")
    q2_irritabiity = make_field_5("Irritability (feeling nervous, inner tension, feeling aggressive) ")
    q2_anxiety = make_field_5("Anxiety (inner restlessness, feeling panicky)")
    q2_exhaustion = make_field_5(
        "Physical and mental exhaustion (general decrease in performance, impaired memory, decrease in concentration, forgetfulness)")
    q2_sex = make_field_5("Sexual problems (change in sexual desire, in sexual activity and satisfaction)")
    q2_bladder = make_field_5(
        "Bladder problems (difficulty in urinating, increased need to urinate, bladder incontinence)")
    q2_discomfort = make_field_5("Joint and muscular discomfort (pain in the joints, rheumatoid complaints)")
    q2_dryness = make_field_5(
        "Dryness of vagina (sensation of dryness or burning in the vagina, difficulty with sexual intercourse)",
        blank=True)
    
    #
    # Andropause
    #

    # Common response options
    AMS_CHOICES = [
        "1",  # None
        "2",  # Mild
        "3",  # Moderate
        "4",  # Severe
        "5",  # Very severe
        "Prefer not to answer"
    ]

    # Psychological domain
    ams1 = models.StringField(
        label="Decline in your feeling of general well-being (mood, life satisfaction, general interest)",
        choices=AMS_CHOICES,
        widget=widgets.RadioSelectHorizontal
    )
    ams2 = models.StringField(
        label="Feeling nervous, inner tension, anxiety",
        choices=AMS_CHOICES,
        widget=widgets.RadioSelectHorizontal
    )
    ams3 = models.StringField(
        label="Physical exhaustion / lacking vitality (general decrease in performance, reduced activity)",
        choices=AMS_CHOICES,
        widget=widgets.RadioSelectHorizontal
    )
    ams4 = models.StringField(
        label="Decrease in muscular strength or endurance",
        choices=AMS_CHOICES,
        widget=widgets.RadioSelectHorizontal
    )
    ams5 = models.StringField(
        label="Depressive mood (feeling down, sad, lack of motivation)",
        choices=AMS_CHOICES,
        widget=widgets.RadioSelectHorizontal
    )

    # Somato-vegetative (physical) domain
    ams6 = models.StringField(
        label="Joint and muscular pain (lower back pain, joint pain, limb pain, general stiffness)",
        choices=AMS_CHOICES,
        widget=widgets.RadioSelectHorizontal
    )
    ams7 = models.StringField(
        label="Excessive sweating (unexpected or without physical exertion)",
        choices=AMS_CHOICES,
        widget=widgets.RadioSelectHorizontal
    )
    ams8 = models.StringField(
        label="Sleep problems (difficulty falling asleep, difficulty sleeping through)",
        choices=AMS_CHOICES,
        widget=widgets.RadioSelectHorizontal
    )
    ams9 = models.StringField(
        label="Increased need for sleep, often feeling tired",
        choices=AMS_CHOICES,
        widget=widgets.RadioSelectHorizontal
    )
    ams10 = models.StringField(
        label="Irritability",
        choices=AMS_CHOICES,
        widget=widgets.RadioSelectHorizontal
    )
    ams11 = models.StringField(
        label="Nervousness",
        choices=AMS_CHOICES,
        widget=widgets.RadioSelectHorizontal
    )

    # Sexual domain
    ams12 = models.StringField(
        label="Decrease in beard growth",
        choices=AMS_CHOICES,
        widget=widgets.RadioSelectHorizontal
    )
    ams13 = models.StringField(
        label="Decrease in ability/frequency to perform sexually",
        choices=AMS_CHOICES,
        widget=widgets.RadioSelectHorizontal
    )
    ams14 = models.StringField(
        label="Decrease in morning erections",
        choices=AMS_CHOICES,
        widget=widgets.RadioSelectHorizontal
    )
    ams15 = models.StringField(
        label="Decrease in sexual desire / libido",
        choices=AMS_CHOICES,
        widget=widgets.RadioSelectHorizontal
    )
    ams16 = models.StringField(
        label="Feeling that you have passed your peak",
        choices=AMS_CHOICES,
        widget=widgets.RadioSelectHorizontal
    )
    ams17 = models.StringField(
        label="Decrease in enjoyment of life or satisfaction with life in general",
        choices=AMS_CHOICES,
        widget=widgets.RadioSelectHorizontal
    )

    #
    # General Health page
    #
    q3_concentrate = make_field_3("Been able to concentrate on what you're doing?")
    q3_worry = make_field_3("Lost much sleep over worry?")
    q3_useful = make_field_3("Felt you were playing a useful part in things?")
    q3_capable = make_field_3("Felt capable of making decisions about things?")
    q3_strain = make_field_3("Felt constantly under strain?")
    q3_difficulties = make_field_3("Felt you couldn't overcome your difficulties?")
    q3_enjoy = make_field_3("Been able to enjoy your normal day-to-day activities?")
    q3_face_up = make_field_3("Been able to face up to your problems?")
    q3_unhappy = make_field_3("Been feeling unhappy and depressed?")
    q3_confidence = make_field_3("Been losing confidence in yourself?")
    q3_worthless = make_field_3("Been thinking of yourself as a worthless person?")
    q3_happy = make_field_3("Been feeling reasonably happy, all things considered?")

    # -------------------------------
    # PART A – SCREENING
    # -------------------------------
    menopause_status = models.StringField(
        label="Have you reached menopause yet? (Menopause = 12 months since last menstrual period)",
        choices=[
            "Post-menopause - my last menstrual period was over a year ago",
            "Peri-menopause - I've had a period within 12 months and have symptoms",
            "No - I am still menstruating and not experiencing symptoms of menopause",
            "Don't know",
            "Prefer not to say"
        ],
        widget=widgets.RadioSelect
    )

    # -------------------------------
    # PART B – MENSTRUAL CHARACTERISTICS
    # -------------------------------

    last_period_time = models.StringField(
        label="When was your last menstrual period?",
        choices=[
            "Within the past 3 months",
            "Between 3 and 6 months ago",
            "Between 6 and 12 months ago",
            "Over 12 months ago",
            "Prefer not to say"
        ],
        widget=widgets.RadioSelect
    )

    last_period_date = models.StringField(
        label="What date did your last period start? (DD/MM/YYYY, estimate if unsure)",
        blank=True
    )

    period_length = models.StringField(
        label="On average, how many days does your period usually last?",
        choices=[
            "1-2 days", "3-4 days", "5-6 days", "7 days or longer", "Prefer not to say"
        ],
        widget=widgets.RadioSelect
    )

    bleeding_amount = models.StringField(
        label="How would you describe the typical amount of menstrual bleeding you experience?",
        choices=[
            "Very light", "Light", "Moderate", "Heavy", "Very heavy", "Prefer not to say"
        ],
        widget=widgets.RadioSelect
    )

    cycle_regularity = models.StringField(
        label="How regular are your menstrual cycles?",
        choices=[
            "Regular (every 24-35 days)",
            "Somewhat irregular",
            "Very irregular or unpredictable",
            "Prefer not to say"
        ],
        widget=widgets.RadioSelect
    )

    symptom_interference = models.IntegerField(
        label="During your period, how much do menstrual symptoms interfere with daily activities?",
        choices=[1,2,3,4,5],
        widget=widgets.RadioSelectHorizontal
    )

    # Menstrual symptoms table
    # Values: "Never", "Occasionally", "Often", "Always", "Prefer not to say"
    symptom_choices = [
        "Never", "Occasionally", "Often", "Always", "Prefer not to say"
    ]

    cramps = models.StringField(label="Abdominal cramps or pelvic pain", choices=symptom_choices)
    headaches = models.StringField(label="Headaches or migraines", choices=symptom_choices)
    mood_swings = models.StringField(label="Mood swings or irritability", choices=symptom_choices)
    trouble_concentrating = models.StringField(label="Trouble concentrating", choices=symptom_choices)
    breast_tenderness = models.StringField(label="Breast tenderness or bloating", choices=symptom_choices)

    absent_periods = models.StringField(
        label="Have you ever experienced absent or erratic periods (not due to pregnancy or perimenopause)?",
        choices=[
            "Yes, in the past but not recently",
            "Yes, recently (within the last year)",
            "No",
            "Prefer not to say"
        ],
        widget=widgets.RadioSelect
    )

    # -------------------------------
    # PART C – REASONS PERIODS STOPPED
    # -------------------------------

    reason_contraceptive = models.BooleanField(label="Hormonal contraceptive use", blank=True)
    reason_menopause = models.BooleanField(label="Menopause", blank=True)
    reason_pregnancy = models.BooleanField(label="Pregnancy or breastfeeding", blank=True)
    reason_surgery = models.BooleanField(label="Surgery (e.g. hysterectomy)", blank=True)
    reason_chemo = models.BooleanField(label="Chemotherapy or radiation therapy", blank=True)
    reason_eating = models.BooleanField(label="Eating disorder", blank=True)
    reason_endocrine = models.BooleanField(label="Pituitary or endocrine disorder", blank=True)
    reason_pcos = models.BooleanField(label="Polycystic ovary syndrome (PCOS)", blank=True)
    reason_none = models.BooleanField(label="No obvious reason", blank=True)
    reason_other = models.StringField(label="Other reason (please describe)", blank=True)

    # -------------------------------
    # PART D – MENOPAUSE & HRT
    # -------------------------------
    age_menopause = models.IntegerField(
        label="At what age did you reach menopause? (0 = unsure)",
        min=0, max=70, blank=True
    )

    uterus_ovaries_removed = models.StringField(
        label="Have you had surgery that removed your uterus or ovaries?",
        choices=[
            "Yes, both ovaries removed",
            "Yes, uterus removed",
            "Yes, one ovary removed",
            "No",
            "Prefer not to say"
        ],
        widget=widgets.RadioSelect
    )

    current_hrt = models.StringField(
        label="Are you currently using hormone replacement therapy (HRT)?",
        choices=["Yes", "No", "Prefer not to say"],
        widget=widgets.RadioSelect
    )

    # -------------------------------
    # PART E – CONTRACEPTIVES / HORMONE TREATMENT
    # -------------------------------
    used_combined = models.BooleanField(label="Combined contraceptive pill, patch, ring", blank=True)
    used_progestin = models.BooleanField(label="Progesterone-only pill, injection, ring, implant", blank=True)
    used_ius = models.BooleanField(label="Hormonal intrauterine system (IUS, e.g., Mirena)", blank=True)
    used_emergency = models.BooleanField(label="Emergency contraception", blank=True)
    used_none = models.BooleanField(label="None of the above", blank=True)

    # -------------------------------
    # PART F – PREGNANCY CHECK
    # -------------------------------
    pregnant = models.StringField(
        label="Are you currently pregnant?",
        choices=["Yes", "No", "Prefer not to say"],
        widget=widgets.RadioSelect
    )

    recent_pregnancy = models.StringField(
        label="Have you been pregnant in the past 12 months?",
        choices=["Yes, within the past 12 months", "No", "Prefer not to say"],
        widget=widgets.RadioSelect
    )

    postpartum_weeks = models.StringField(
        label="If yes: how many weeks/months postpartum are you?",
        blank=True
    )

    breastfeeding = models.StringField(
        label="Are you currently breastfeeding?",
        choices=[
            "Yes, exclusively",
            "Yes, partially",
            "No",
            "Prefer not to say"
        ],
        widget=widgets.RadioSelect
    )
