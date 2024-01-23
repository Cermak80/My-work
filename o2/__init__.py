from otree.api import *


doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'o2'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    co2 = models.IntegerField(label="")
    winCo2 = models.IntegerField(initial=0)

    def Payoff(Player):
        from random import randint
        o = randint(1, 100)
        if o <= 5:
            Player.winCo2 = 1
            Player.participant.vars["Co2Win"] = Player.winCo2
            Player.payoff = cu(1000 - Player.co2)
            Player.participant.vars["payoffCo2"] = cu(1000 - Player.co2)
        else:
            Player.participant.vars["payoffCo2"] = 0
            Player.participant.vars["Co2Win"] = Player.winCo2

def co2_error_message(Player, value):
    if value != 0 and value != 100 and value != 200 and value != 300 and value != 400 and value != 500 and value != 600 \
            and value != 700 and value != 800 and value != 900 and value != 1000:
        return 'Částka musí být násobkem stovky a nemůže být více než 1000!'\
            #and value != 1100 and value != 1200 and value != 1300\
            #and value != 1400 and value != 1500 and value != 1600 and value != 1700 and value != 1800 and value != 1900 and value != 2000:



# PAGES
class MyPage(Page):
    form_model = Player
    form_fields = ["co2"]

    def before_next_page(player: Player, timeout_happened):
        Player.Payoff(player)

class ResultsWaitPage(WaitPage):
    pass


class Results(Page):
    pass


page_sequence = [Results, MyPage]
