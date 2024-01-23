from otree.api import *


doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'payoffscreen'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    pass


# PAGES
class MyPage(Page):
    def vars_for_template(player: Player):
        return dict(
            payoffCo2=player.participant.vars.get("payoffCo2"),
            payoffRaven=player.participant.vars.get("payoffRaven"),
            payoffWorking=player.participant.vars.get("payoffWork"),
            Windohromady=player.participant.vars.get("payoffWork")+player.participant.vars.get("payoffRaven")+player.participant.vars.get("payoffCo2")+200,
            Co2Win=player.participant.vars.get("Co2Win"),

        )

class Results(Page):
    def vars_for_template(player: Player):
        return dict(
            kod=player.participant.vars.get("Kod"),
            typukolu=player.participant.vars.get("typukolu"),
            datumukolu=player.participant.vars.get("datumukolu"),
        )
page_sequence = [MyPage ,Results]
