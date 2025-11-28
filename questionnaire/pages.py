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

    @staticmethod
    def is_displayed(player):
        return player.session.config.get('show_Demographics', True)


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

    @staticmethod
    def is_displayed(player):
        return player.session.config.get('show_Employment', True)


class GlobalPreferences(Page):
    form_model = 'player'
    form_fields = [
        'patience',
        'risk',
        'altruism',
        'trust',
        'reciprocity',
        'retaliation'
    ]

    @staticmethod
    def is_displayed(player):
        return player.session.config.get('show_GlobalPreferences', True)


class Health(Page):
    form_model = 'player'
    form_fields = [
        'physical_health',
        'fatigue_typical',
        'fatigue_feel',
        'fatigue_starting',
        'fatigue_rundown',
        'fatigue_average',
        'chronic_condition',
        'chronic_condition_details'
    ]

    @staticmethod
    def is_displayed(player):
        return player.session.config.get('show_Health', True)


class Lifestyle(Page):
    form_model = 'player'
    form_fields = [
        'caffeine',
        'alcohol',
        'nicotine',
        'medication',
        'medication_text'
    ]

    @staticmethod
    def is_displayed(player):
        return player.session.config.get('show_Lifestyle', True)


class Chronotype(Page):
    form_model = 'player'
    form_fields = ['chronotype', 'shift_work']

    @staticmethod
    def is_displayed(player):
        return player.session.config.get('show_Chronotype', True)


class PhysicalActivity(Page):
    form_model = 'player'
    form_fields = ['pa_frequency', 'pa_demand']

    @staticmethod
    def is_displayed(player):
        return player.session.config.get('show_PhysicalActivity', True)


class AMS(Page):
    form_model = 'player'
    form_fields = [
        'ams1', 'ams2', 'ams3', 'ams4', 'ams5',
        'ams6', 'ams7', 'ams8', 'ams9', 'ams10', 'ams11',
        'ams12', 'ams13', 'ams14', 'ams15', 'ams16', 'ams17'
    ]

    @staticmethod
    def is_displayed(player):
        return player.session.config.get('show_AMS', True)


class GeneralHealth(Page):
    form_model = 'player'
    form_fields = [
        'q3_concentrate',
        'q3_worry',
        'q3_useful',
        'q3_capable',
        'q3_strain',
        'q3_difficulties',
        'q3_enjoy',
        'q3_face_up',
        'q3_unhappy',
        'q3_confidence',
        'q3_worthless',
        'q3_happy',
    ]

    @staticmethod
    def is_displayed(player):
        return player.session.config.get('show_GeneralHealth', True)


# -------------------------------
# PART A – SCREENING
# -------------------------------
class PartA(Page):
    form_model = "player"
    form_fields = ["menopause_status"]

    @staticmethod
    def is_displayed(player):
        return player.session.config.get('show_PartA', True)


# -------------------------------
# PART B – MENSTRUAL CHARACTERISTICS
# -------------------------------
class PartB(Page):
    form_model = "player"
    form_fields = [
        "last_period_time",
        "last_period_date",
        "period_length",
        "bleeding_amount",
        "cycle_regularity",
        "symptom_interference",
        "cramps",
        "headaches",
        "mood_swings",
        "trouble_concentrating",
        "breast_tenderness",
        "absent_periods"
    ]

    @staticmethod
    def is_displayed(player):
        # Menstruating OR peri OR unsure
        return player.menopause_status in [
            "Peri-menopause - I've had a period within 12 months and have symptoms",
            "No - I am still menstruating and not experiencing symptoms of menopause",
            "Don't know",
            "Prefer not to say"
        ] and player.session.config.get('show_PartB', True)


# -------------------------------
# PART C – REASONS PERIODS STOPPED
# -------------------------------
class PartC(Page):
    form_model = "player"
    form_fields = [
        "reason_contraceptive",
        "reason_menopause",
        "reason_pregnancy",
        "reason_surgery",
        "reason_chemo",
        "reason_eating",
        "reason_endocrine",
        "reason_pcos",
        "reason_none",
        "reason_other"
    ]

    @staticmethod
    def is_displayed(player):
        # If PartB was shown...
        if PartB.is_displayed(player) and player.last_period_time in [
            "Between 3 and 6 months ago",
            "Between 6 and 12 months ago",
            "Over 12 months ago"
        ] and player.session.config.get('show_PartC', True):
            return True
        else:
            return False


# -------------------------------
# PART D – MENOPAUSE & HRT
# -------------------------------
class PartD(Page):
    form_model = "player"
    form_fields = ["age_menopause", "uterus_ovaries_removed", "current_hrt"]

    @staticmethod
    def is_displayed(player):
        # Displayed if:
        # A: Post-menopause OR
        # B: last period > 3 months ago (likely amenorrheic)
        return (
            player.menopause_status.startswith("Post-menopause")
            or player.last_period_time in [
                "Between 3 and 6 months ago",
                "Between 6 and 12 months ago",
                "Over 12 months ago"
            ] and player.session.config.get('show_PartD', True)
        )


# -------------------------------
# PART E – CONTRACEPTIVE USE
# -------------------------------
class PartE(Page):
    form_model = "player"
    form_fields = [
        "used_combined",
        "used_progestin",
        "used_ius",
        "used_emergency",
        "used_none"
    ]

    # Always shown EXCEPT:
    # If PartD showed AND HRT = YES → skip to F
    @staticmethod
    def is_displayed(player):
        if PartD.is_displayed(player) and player.current_hrt == "Yes" and player.session.config.get('show_PartE', True):
            return False
        return True


# -------------------------------
# PART F – PREGNANCY CHECK
# -------------------------------
class PartF(Page):
    form_model = "player"
    form_fields = [
        "pregnant",
        "recent_pregnancy",
        "postpartum_weeks",
        "breastfeeding"
    ]

    @staticmethod
    def is_displayed(player):
        return player.session.config.get('show_PartF', True)


class EQ5D(Page):
    form_model = 'player'
    form_fields = ['mobility', 'selfcare', 'activities', 'pain', 'anxiety']

    @staticmethod
    def is_displayed(player):
        return player.session.config.get('show_EQ5D', True)


class PHQ9(Page):
    form_model = 'player'
    form_fields = [
        'phq1', 'phq2', 'phq3', 'phq4', 'phq5', 'phq6', 'phq7', 'phq8', 'phq9',
        'impairment'
    ]

    @staticmethod
    def is_displayed(player):
        return player.session.config.get('show_PHQ9', True)


class GAD7(Page):
    form_model = 'player'
    form_fields = [
        'gad1', 'gad2', 'gad3', 'gad4', 'gad5', 'gad6', 'gad7',
        'gad_impairment'
    ]

    @staticmethod
    def is_displayed(player):
        return player.session.config.get('show_GAD7', True)


page_sequence = [Demographics, Employment, GlobalPreferences, Health, Lifestyle, Chronotype,
                 PhysicalActivity,
                 AMS, GeneralHealth, PartA,
                 PartB,
                 PartC,
                 PartD,
                 PartE,
                 PartF,
                 EQ5D, PHQ9, GAD7
                 ]
