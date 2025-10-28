from otree.api import (
    models,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    widgets
)
import logging
from common import definitions


logger = logging.getLogger(__name__)


def make_field_3(label: str):
    return models.IntegerField(label=label, choices=C.LIKERT3, widget=widgets.RadioSelect)


def make_field_5(label: str, blank: bool = False):
    return models.IntegerField(label=label, choices=C.LIKERT5, widget=widgets.RadioSelect, blank=blank)


def make_field_10(label: str):
    return models.IntegerField(label=label, choices=C.LIKERT10, widget=widgets.RadioSelect)


class C(BaseConstants):
    NAME_IN_URL = 'menopause'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
    LIKERT3 = [[i, ''] for i in range(4)]
    LIKERT5 = [[i, ''] for i in range(5)]
    LIKERT10 = [[i, ''] for i in range(11)]
    TREATMENT_ATTRS = [
        dict(name='trt_hrt', label='Hormone replacement therapy (HRT)'),
        dict(name='trt_testosterone', label='Testosterone gel for reduced sex drive'),
        dict(name='trt_oestrogren', label='Oestrogen for vaginal dryness and discomfort'),
        dict(name='trt_antidepressants', label='Antidepressants'),
        dict(name='trt_night_sweats', label='Blood pressure medicine called clonidine or an epilepsy medicine called gabapentin to reduce" \
             " hot flushes and night sweats'),
        dict(name='trt_cbt', label='Cognitive behavioural therapy (CBT)'),
        dict(name='trt_excercise', label='Exercising (walking, cycling, etc.)'),
    ]
    MENO2Y_REASON = [
        dict(name='meno2Y_preg', label='Prenancy or breastfeeding'),
        dict(name='meno2Y_horm', label='Hormonal contraceptives'),
        dict(name='meno2Y_perimeno', label='Perimenopause'),
        dict(name='meno2Y_chemo', label='Chemotherapy or radiant therapy'),
        dict(name='meno2Y_noobv', label='No obvious reason'),
        dict(name='meno2Y_notsay', label='Prefer not to say'),
        dict(name='meno2Y_other', label='Other reason, please specify'),
    ]
    MENO2N_REASON = [
        dict(name='meno2N1_surg', label='Surgery'),
        dict(name='meno2N1_meno', label='Menopause'),
        dict(name='meno2N1_preg', label='Prenancy or breastfeeding'),
        dict(name='meno2N1_horm', label='Hormonal contraceptives'),
        dict(name='meno2N1_chemo', label='Chemotherapy or radiant therapy'),
        dict(name='meno2N1_noobv', label='No obvious reason'),
        dict(name='meno2N1_notsay', label='Prefer not to say'),
        dict(name='meno2N1_other', label='Other, please specify'),
    ]


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    garmin_engagement = models.BooleanField(
        choices=[[True, "Yes, I have a Garmin account and I am happy to share my data with the researchers."],
                 [False, "Yes, I have a Garmin account but I do not want to share my data with the researchers."]],
        label="Can we use your Garmin data?",
        widget=widgets.RadioSelect)
    garmin_id = models.StringField(label="Please enter your Garmin email here. ")
    garmin_wear_frequency = models.StringField(
        choices=[["Daily", "Daily"],
                 ["Only when I exercise", "Only when I exercise"],
                 ["Several times a week", "Several times a week"],
                 ["Once a week", "Once a week"],
                 ["Several times a month", "Several times a month"],
                 ["Once a month", "Once a month"],
                 ["Less than once a month", "Less than once a month"]],
        label="How often do you wear your Garmin device?",
        widget=widgets.RadioSelect)
    donation_amount_cancer_research = models.IntegerField(
        label="Cancer Reserch UK is a charity that funds research into all 200 types of cancer. ")
    donation_amount_brotish_heart_foundation = models.IntegerField(
        label="British Heart Foundation is a charity that funds research into heart and circulatory diseases. ")
    donation_amount_macmillan = models.IntegerField(
        label="Macmillan Cancer Support is a charity that provides support to people affected by cancer. ")
    donation_amount_save_the_children = models.IntegerField(
        label="Save the Children is a charity that works to improve the lives of children around the world. ")
    donation_amount_oxfam = models.IntegerField(
        label="Please state here the amount you would like to keep for yourself. ")

    # Questionnaire 1 fields
    age = models.IntegerField(label="What is your age in years?", min=18)
    gender = models.StringField(choices=[
        "Man (including Trans Male/Trans Man)",
        "Woman (including Trans Female/Trans Women)",
        "Non-binary",
        "Other",
        "Rather not say",], label="What is your gender?")
    other_gender = models.StringField(
        blank=True, label="If you would like to give more details about your gender, state them here:")
    t_gender = models.BooleanField(label="Do you self-identify as transgender?",
                                   choices=[[True, "Yes"], [False, "No"]])
    legal_gender = models.StringField(label="What is your sex, as recorded on legal/official documents?",
                                      choices=["Male", "Female"])
    nationality = models.StringField(label="What is your Nationality?", choices=definitions.nationality)
    ethnicity = models.StringField(label="What is your ethnic group? ",
                                   choices=["Asian, Asian British",
                                            "Black, Black British, Caribbean or African",
                                            "Mixed or Multiple",
                                            "White",
                                            "Other (please specify below)"],
                                   widget=widgets.RadioSelect)
    other_ethnicity = models.StringField(blank=True, label="Other ethnicity")
    children = models.BooleanField(label="Do you have children")
    height_ft = models.IntegerField(label="What is your height in feet?", min=3, max=7)
    height_in = models.IntegerField(label="What is your height in inches?", min=0, max=11)
    weight = models.IntegerField(label="What is your weight in kg?", min=40)
    exercise = models.StringField(label="In the last 12 months, how often have you participated in some kind of exercise? ",
                                  choices=[
                                      "3 to 4 times per week",
                                      "1 to 2 times per week",
                                      "1 to 2 times per month",
                                      "Not at all, i.e. may have been due to pregnancy or ill health",
                                  ])
    lk_physical_health = make_field_10(
        "How physically healthy do you feel?")
    lk_mental_health = make_field_10(
        "How mentally healthy do you feel?")
    attention_chk1 = models.IntegerField(label="Please choose the number 4 from the following drop-down menu.",
                                         choices=[1, 2, 3, 4, 5])

    # Questionnaire 2
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
    attention_chk2 = make_field_5("Please choose the scale Very Severe. ")

    # Questionnaire 3
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

    # Querstionnaire 4 - Female only
    period = models.StringField(label="Are you currently experiencing regular menstrual cycles?", choices=[
        "Yes",
        "No, because I use a hormonal contraceptive",
        "No, because I am during one of the stages of Menopause (see below)",
        "No, please give details below ",
    ])

    meno1 = models.StringField(label="In the last 12 months, have you had periods or menstrual bleedings?", choices=[
        "Yes, and they were regular",
        "Yes, but they were not regular",
        "No",
    ])

    menopause = models.StringField(label="Which of the following applies to you?",
                                   choices=[
                                       "I am Perimenopause.",
                                       "I am Menopause.",
                                       "I am Post menopause.",
                                       "None of this applies to me.",
                                   ])
    period_details = models.StringField(blank=True)
    trt_hrt = models.BooleanField(blank=True)
    trt_testosterone = models.BooleanField(blank=True)
    trt_oestrogren = models.BooleanField(blank=True)
    trt_antidepressants = models.BooleanField(blank=True)
    trt_night_sweats = models.BooleanField(blank=True)
    trt_cbt = models.BooleanField(blank=True)
    trt_excercise = models.BooleanField(blank=True)

    meno2Y_preg = models.BooleanField(blank=True)
    meno2Y_horm = models.BooleanField(blank=True)
    meno2Y_perimeno = models.BooleanField(blank=True)
    meno2Y_chemo = models.BooleanField(blank=True)
    meno2Y_noobv = models.BooleanField(blank=True)
    meno2Y_notsay = models.BooleanField(blank=True)
    meno2Y_other = models.BooleanField(blank=True)

    meno2N1_surg = models.BooleanField(blank=True)
    meno2N1_meno = models.BooleanField(blank=True)
    meno2N1_preg = models.BooleanField(blank=True)
    meno2N1_horm = models.BooleanField(blank=True)
    meno2N1_chemo = models.BooleanField(blank=True)
    meno2N1_noobv = models.BooleanField(blank=True)
    meno2N1_notsay = models.BooleanField(blank=True)
    meno2N1_other = models.BooleanField(blank=True)

    meno2Y_reason_other = models.StringField(
        blank=True, label="If you stated Other above, please provide further information.")
    meno2N_reason_other = models.StringField(
        blank=True, label="If you stated Other above, please provide further information.")
    meno2N_age = models.IntegerField(label="What was your age in years when you had your last period? If you never had your period, "
                                     "please state 1.", min=1, max=80, blank=True)

    meno2N_monthyear = models.StringField(blank=True, label="Do you maybe remember the month and year of your last period? Please state "
                                          "month.year. For example, if it was May 2025, this would be 05.2025")

    def is_playing(self):
        if 'status' not in self.participant.vars:
            self.participant.vars['status'] = "Playing"
        return self.participant.vars['status'] == "Playing"
