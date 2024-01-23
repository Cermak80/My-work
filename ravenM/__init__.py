from otree.api import *


doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'ravenM'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
    answers = [5, 1, 4, 1, 5, 2, 7, 8, 8, 7, 6, 3, 7, 5, 4, 8, 1, 3]

    odmena = 10


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    score = models.IntegerField(initial=0)

    def CreateRavens(Player):
        ravens = []
        for x in range(1,19):
            ravens.append("Raven_"+str(x))
        Player.participant.vars["ravens"] = ravens

    def Pay(Player):
        Player.payoff = cu(C.odmena * Player.score)
        Player.participant.vars["payoffRaven"] = cu(C.odmena * Player.score)

# PAGES
class MyPage(Page):
    timeout_seconds = 900
    def vars_for_template(player: Player):
        return dict(
            raven=player.participant.vars.get("ravens"),
            firstpic=player.participant.vars.get("ravens")[0],
        )

    @staticmethod
    def live_method(player, data):
        if data['t'] == C.answers[data['ind']]:
            player.score += 1

    def before_next_page(player: Player, timeout_happened):
        player.Pay()


class ResultsWaitPage(WaitPage):
    pass


class Results(Page):
    def before_next_page(player: Player, timeout_happened):
        player.CreateRavens()


page_sequence = [Results, MyPage]
