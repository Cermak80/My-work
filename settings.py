from os import environ


SESSION_CONFIGS = [
     dict(
         name='real_effort',
         app_sequence=["o2",'real_effort'],
         num_demo_participants=2,
     ),
    dict(
         name='workingmemory',
         app_sequence=['workingmemory'],
         num_demo_participants=2,
     ),
    dict(
         name='ExpDotazni',
         app_sequence=['ExpDotaznik'],
         num_demo_participants=2,
     ),
    dict(
         name='timepreferences',
         app_sequence=['timepreferences'],
         num_demo_participants=2,
    ),
    dict(
         name='riskcharts',
         app_sequence=['riskcharts'],
         num_demo_participants=2,
    ),
    dict(
         name='ravenM',
         app_sequence=['ravenM'],
         num_demo_participants=2,
    ),
    dict(
        name='Finalni_verze',
        app_sequence=['payment', 'Introduction', 'real_effort', 'timepreferences', 'riskcharts',
                      "o2", 'ExpDotaznik', 'workingmemory', 'ravenM', 'payoffscreen'],
        num_demo_participants=2,
        participation_fee=200
    ),
    dict(
         name='TestPayment',
         app_sequence=['Introduction','payment','timepreferences','riskcharts'],
         num_demo_participants=2,
    ),

]

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1.00, participation_fee=0.00, doc=""
)

PARTICIPANT_FIELDS = ['string', 'expiry','vouchers','vsechnyotazky', 'Seznam','ravens', 'kolikukolu','datumukolu','typukolu',
                      'cisloukolu', 'vyhra', 'payoffCo2', 'payoffRaven', 'PayoffWork','Co2Win','Kod']
SESSION_FIELDS = []

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'en'



# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'Kč'
USE_POINTS = False

DEBUG = False

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """ """

SECRET_KEY = '3088178564789'
