from otree.api import *


doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'Mind_gameC'
    PLAYERS_PER_GROUP = 2
    NUM_ROUNDS = 1

    Actor_role = "actor"
    Observer_role = "observer"

class Subsession(BaseSubsession):
    pass





class Group(BaseGroup):
    roll = models.IntegerField()
    def payoffC_function(group: BaseGroup):
        from random import randint
        a = randint(1, 6)
        group.roll = a
        for n in group.get_players():
            if n.role == C.Actor_role:
                if a < 3:
                    n.payoff = 2
                    n.Rolled = 1
                    n.Win = 1
                if a > 2:
                    n.payoff = 0
                    n.Rolled = 2
                    n.Win = 0
            if n.role == C.Observer_role:
                if a < 3:
                    n.payoff = 0
                    n.Rolled = 1
                    n.Win = 0
                if a > 2:
                    n.payoff = 2
                    n.Rolled = 2
                    n.Win = 1
        for k in group.get_players():
            k.session.vars['gr'] = group.subsession.get_group_matrix()

    def help_function(group: BaseGroup):
        for n in group.get_players():
            n.participant.vars['payoffgameone'] = n.payoff

class Player(BasePlayer):
    Rolled = models.IntegerField()
    Win = models.IntegerField()
    Other_left = models.IntegerField(initial=0)

# PAGES
class Info(Page):
    def vars_for_template(player: Player):
        return dict(
            role=player.role,
            roleA=C.Actor_role,
            roleO=C.Observer_role
        )

    timeout_seconds = 180

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
    def after_all_players_arrive(group: Group):
        group.payoffC_function()


class Results(Page):
    def vars_for_template(player: Player):
        return dict(
            role=player.role,
            roleA=C.Actor_role,
            roleO=C.Observer_role,
            rolled=player.Rolled,
            win=player.Win,
            roll=player.group.roll,
        )

    timeout_seconds = 60

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

class HelpPage(WaitPage):
    def after_all_players_arrive(group: Group):
        group.help_function()


class WaitforAll(WaitPage):
    wait_for_all_groups = True


class GroupWaitPage(WaitPage):
    group_by_arrival_time = True

class LeftPage(Page):
    def is_displayed(player: Player):
        return player.Other_left > 0

    def vars_for_template(player: Player):
        return dict(
            Other_left=player.Other_left
        )


class HelpWaitPage2(WaitPage):
    pass


page_sequence = [Info, HelpWaitPage2, LeftPage, ResultsWaitPage, HelpPage, Results, HelpWaitPage2, LeftPage]
