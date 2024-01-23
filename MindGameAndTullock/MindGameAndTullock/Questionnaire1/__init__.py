from otree.api import *


doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'Questionnaire1'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    Qa1 = models.IntegerField(label="",
                              choices=[(10,"10 Very willing to take risks"), (9,"9"), (8,"8"), (7,"7"), (6,"6"), (5,"5"), (4,"4"), (3,"3"), (2,"2"), (1,"1"),
                                       (0,"0 Completely unwilling to take risks"), (99,"99 Don’t know")])

    Qb1 = models.IntegerField(label="",
                              choices=[(10, "10 Very willing to do so "), (9, "9"), (8, "8"), (7, "7"), (6, "6"),
                                       (5, "5"), (4, "4"), (3, "3"), (2, "2"), (1, "1"),
                                       (0, "0 Completely unwilling to do so "), (99, "99 Don’t know")])
    Qb2 = models.IntegerField(label="",
                              choices=[(10, "10 Very willing to do so "), (9, "9"), (8, "8"), (7, "7"), (6, "6"),
                                       (5, "5"), (4, "4"), (3, "3"), (2, "2"), (1, "1"),
                                       (0, "0 Completely unwilling to do so "), (99, "99 Don’t know")])
    Qb3 = models.IntegerField(label="",
                              choices=[(10, "10 Very willing to do so "), (9, "9"), (8, "8"), (7, "7"), (6, "6"),
                                       (5, "5"), (4, "4"), (3, "3"), (2, "2"), (1, "1"),
                                       (0, "0 Completely unwilling to do so "), (99, "99 Don’t know")])
    Qb4 = models.IntegerField(label="",
                              choices=[(10, "10 Very willing to do so "), (9, "9"), (8, "8"), (7, "7"), (6, "6"),
                                       (5, "5"), (4, "4"), (3, "3"), (2, "2"), (1, "1"),
                                       (0, "0 Completely unwilling to do so "), (99, "99 Don’t know")])

    Qc1 = models.IntegerField(label="",
                              choices=[(10, "10 Describes me perfectly "), (9, "9"), (8, "8"), (7, "7"), (6, "6"),
                                       (5, "5"), (4, "4"), (3, "3"), (2, "2"), (1, "1"),
                                       (0, "0 Does not describe me at all  "), (99, "99 Don’t know")])
    Qc2 = models.IntegerField(label="",
                              choices=[(10, "10 Describes me perfectly "), (9, "9"), (8, "8"), (7, "7"), (6, "6"),
                                       (5, "5"), (4, "4"), (3, "3"), (2, "2"), (1, "1"),
                                       (0, "0 Does not describe me at all  "), (99, "99 Don’t know")])
    Qc3 = models.IntegerField(label="",
                              choices=[(10, "10 Describes me perfectly "), (9, "9"), (8, "8"), (7, "7"), (6, "6"),
                                       (5, "5"), (4, "4"), (3, "3"), (2, "2"), (1, "1"),
                                       (0, "0 Does not describe me at all  "), (99, "99 Don’t know")])
    Qc4 = models.IntegerField(label="",
                              choices=[(10, "10 Describes me perfectly "), (9, "9"), (8, "8"), (7, "7"), (6, "6"),
                                       (5, "5"), (4, "4"), (3, "3"), (2, "2"), (1, "1"),
                                       (0, "0 Does not describe me at all  "), (99, "99 Don’t know")])
    Qc5 = models.IntegerField(label="",
                              choices=[(10, "10 Describes me perfectly "), (9, "9"), (8, "8"), (7, "7"), (6, "6"),
                                       (5, "5"), (4, "4"), (3, "3"), (2, "2"), (1, "1"),
                                       (0, "0 Does not describe me at all  "), (99, "99 Don’t know")])

# PAGES
class WelcomePage(Page):
    pass


class Qa(Page):
    form_model = 'player'
    form_fields = ['Qa1']


class Qb(Page):
    form_model = 'player'
    form_fields = ['Qb1','Qb2','Qb3','Qb4']


class Qc(Page):
    form_model = 'player'
    form_fields = ['Qc1','Qc2','Qc3','Qc4','Qc5']


page_sequence = [WelcomePage, Qa, Qb, Qc]
