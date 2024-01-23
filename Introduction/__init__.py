from otree.api import *


doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'Introduction'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


def creating_session(subsession):
    import random
    import string

    n_players = len(subsession.get_players())

    ids = []
    for i in range(0, n_players):
        new_id = random.choice(string.ascii_uppercase) \
                 + random.choice(string.ascii_uppercase) \
                 + random.choice(string.ascii_uppercase) \
                 + random.choice(string.ascii_uppercase) \
                 + random.choice(string.ascii_uppercase) \
                 + random.choice(string.ascii_uppercase) \
                 + str(random.randint(0, 9)) \
                 + str(random.randint(0, 9))

        while new_id in ids:
            new_id = random.choice(string.ascii_uppercase) \
                     + random.choice(string.ascii_uppercase) \
                     + random.choice(string.ascii_uppercase) \
                     + random.choice(string.ascii_uppercase) \
                     + random.choice(string.ascii_uppercase) \
                     + random.choice(string.ascii_uppercase) \
                     + str(random.randint(0, 9)) \
                     + str(random.randint(0, 9))

        ids.append(new_id)

    for p in subsession.get_players():
        p.paymentid = ids[p.id_in_subsession - 1]
        p.participant.vars["Kod"] = p.paymentid
class Group(BaseGroup):
    pass


class Player(BasePlayer):
    paymentid = models.StringField()


# PAGES
class MyPage(Page):
    pass


class ResultsWaitPage(WaitPage):
    pass


class Results(Page):
    pass


page_sequence = []
