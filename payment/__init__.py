from otree.api import *


doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'payment'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    win = models.IntegerField(initial=0)
    chosen_task = models.IntegerField(initial=0)
    platba = models.StringField()
    def losovani(Player):
        from random import randint
        x = randint(1, 100)

        if x < 6:
            Player.win = 1
            Player.participant.vars['vyhra'] = Player.win
            y = randint(1, 115)

            if y < 56:
                Player.platba = "Risk chart"
                Player.chosen_task = y
                Player.participant.vars['typukolu'] = "Risk chart"
                Player.participant.vars['cisloukolu'] = y
            if 92 > y >= 56:
                Player.platba = "offline time prefereces"
                Player.chosen_task = y - 55
                Player.participant.vars['typukolu'] = "offline time preferences"
                Player.participant.vars['cisloukolu'] = y - 55
            if y >= 92:
                Player.platba = "online time preferences"
                Player.chosen_task = y - 91
                Player.participant.vars['typukolu'] = "online time preferences"
                Player.participant.vars['cisloukolu'] = y - 91
        else:
            Player.participant.vars['typukolu'] = "Nebyl vybran"
            Player.participant.vars['cisloukolu'] = 0
            Player.participant.vars['vyhra'] = Player.win






# PAGES
class Results(Page):
    def before_next_page(player: Player, timeout_happened):
        player.losovani()

class MyPage(Page):
    pass


page_sequence = [Results]
