from os import environ

SESSION_CONFIGS = [
    dict(
        name='MGAT',
        app_sequence=['Welcome', 'Mind_game', 'Ultimatum', 'Tullock', 'Final_questionnaireTr'],
        num_demo_participants=4,
        participation_fee=2
     ),
    dict(
        name='MGATControl',
        app_sequence=['Welcome', 'Mind_gameC', 'Ultimatum', 'Tullock', 'Final_questionnaire'],
        num_demo_participants=4,
        participation_fee=2
     ),
    dict(
         name='Test',
         app_sequence=['Mind_game', 'Tullock'],
         num_demo_participants=6,
     ),
]

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1.00, participation_fee=0.00, doc=""
)

PARTICIPANT_FIELDS = ['payoffgameone']
SESSION_FIELDS = ['gr']

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'en'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'GBP'
USE_POINTS = False

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """ """

DEBUG = False

SECRET_KEY = '7232152639646'
