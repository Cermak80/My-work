from otree.api import *


doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'Final_questionnaire'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    q1 = models.StringField(label="1. What is your biological sex?", choices=["Male", "Female"], widget=widgets.RadioSelectHorizontal)
    q2 = models.IntegerField(label="2. What is your age (in years)? ", max=150, min=0)
    q3 = models.StringField(label="3. Have you experienced any armed conflict (heard fire, seen damage, etc.)?", choices=["Yes", "No", "I don´t know"], widget=widgets.RadioSelectHorizontal)
    q4 = models.StringField(label="4. Have you seen any casualties?", choices=["Yes", "No", "I don´t know"], widget=widgets.RadioSelectHorizontal)
    q5 = models.StringField(label="5. Was anyone you knew killed or injured in the conflict?", choices=["Yes", "No", "I don´t know"], widget=widgets.RadioSelectHorizontal)
    q6 = models.StringField(label="6. Did you feel cheated in part 1 of the experiment? ", choices=["Yes", "No", "I don´t know"], widget=widgets.RadioSelectHorizontal)
    Other_left = models.IntegerField(initial=0)

# PAGES
class MyPage(Page):
    form_model = 'player'
    form_fields = ['q1', 'q2', 'q3', 'q4', 'q5']

    def is_displayed(player: Player):
        return player.participant.vars.get('payoffgameone') == 2

    timeout_seconds = 120
    @staticmethod
    def before_next_page(player, timeout_happened):
        if timeout_happened:
            player.payoff = 0
            p2 = player.group.get_player_by_id(2)
            p1 = player.group.get_player_by_id(1)
            player.Other_left = 2

            if player.id_in_group == 1:
                p2.payoff = 1
                p2.Other_left = 1
            if player.id_in_group == 2:
                p1.payoff = 1
                p1.Other_left = 1


class ResultsWaitPage(WaitPage):
    pass


class Results(Page):
    form_model = 'player'
    form_fields = ['q1', 'q2', 'q3', 'q4', 'q5']

    def is_displayed(player: Player):
        return player.participant.vars.get('payoffgameone') == 0

    timeout_seconds = 120
    @staticmethod
    def before_next_page(player, timeout_happened):
        if timeout_happened:
            player.payoff = 0
            p2 = player.group.get_player_by_id(2)
            p1 = player.group.get_player_by_id(1)
            player.Other_left = 2

            if player.id_in_group == 1:
                p2.payoff = 1
                p2.Other_left = 1
            if player.id_in_group == 2:
                p1.payoff = 1
                p1.Other_left = 1

class FinalPage(Page):
    pass
class LeftPage(Page):
    def is_displayed(player: Player):
        return player.Other_left > 0

    def vars_for_template(player: Player):
        return dict(
            Other_left=player.Other_left
        )
class HelpWaitPage2(WaitPage):
    pass

page_sequence = [MyPage, Results, FinalPage]
