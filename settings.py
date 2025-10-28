from os import environ

SESSION_CONFIGS = [
    dict(
        name='Tiles',
        app_sequence=['consent', 'solo_app', 'menopause', 'completion'],
        num_demo_participants=1,
        debug_mode=False,
        use_browser_bots=True,
    ),
    dict(
        name='NoConsent',
        display_name='TEST - no consent',
        app_sequence=['solo_app'],
        num_demo_participants=1,
        debug_mode=True,
        use_browser_bots=False,
    ),
    dict(
        name='MenopauseNoConsent',
        display_name='TEST - Survey, no consent',
        app_sequence=['menopause'],
        num_demo_participants=1,
        use_browser_bots=False,
    ),
    dict(
        name='CompletionNoConsent',
        display_name='TEST - Completion, no consent',
        app_sequence=['completion'],
        num_demo_participants=1,
        use_browser_bots=False,
    ),
]

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1.00, participation_fee=1.00, doc=""
)

PARTICIPANT_FIELDS = ["Stage1_star_rating", "Stage1_count",
                      "Stage2_star_rating", "Stage2_count",
                      "Stage3_star_rating", "Stage3_count",]
SESSION_FIELDS = []

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'en'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'USD'
USE_POINTS = True

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """ """

SECRET_KEY = '1283572204412'

# CONSTANTS
TASK_TIME_SECONDS = 1*60
TRIAL_TIME_SECONDS = 4*60

FIXED_RATE = 5
PIECE_RATE = 2
COMPETITION_RATE = 3

DROPOUT_STATES_PLAYING = "Playing"
DROPOUT_STATES_DROPOUT = "Dropout"
DROPOUT_STATES_NON_CONSENT = "Non Consent"
