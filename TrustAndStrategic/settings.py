from os import environ

SESSION_CONFIGS = [
    dict(
         name='TrustAndStrategic',
         app_sequence=['informace'],
         num_demo_participants=12,
    ),

    dict(
         name='c12',
         app_sequence=['C12'],
         num_demo_participants=12,
    ),
    dict(
         name='c12_2part',
         app_sequence=['C12_2part'],
         num_demo_participants=2,
    ),

    dict(
        name='Cely_Experiment',
        app_sequence=['C12', 'C12_2part','informace',],
        num_demo_participants=2,
        participation_fee=50
    ),

]

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1.00, participation_fee=0.00, doc=""
)

PARTICIPANT_FIELDS = ["protihraci","MojeVyhry","VyslednaZprava","Pamatovak","VyslednaZpravaInf","Pojistka", "CoSePlati"]
SESSION_FIELDS = ["Poradi_kol"]

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'cz'

DEBUG = False

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'USD'
USE_POINTS = True

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """ """

SECRET_KEY = '3947669589939'
