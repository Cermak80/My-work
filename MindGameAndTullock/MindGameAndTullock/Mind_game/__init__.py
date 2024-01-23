from otree.api import *


doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'Mind_game'
    PLAYERS_PER_GROUP = 2
    NUM_ROUNDS = 1

    Actor_role = "actor"
    Observer_role = "observer"


class Subsession(BaseSubsession):
    pass





class Group(BaseGroup):
    def payoff_function(group: BaseGroup):
        p2 = group.get_player_by_id(2)
        for n in group.get_players():
            if n.role == C.Actor_role:
                if n.Yes_or_no == 1:
                    n.payoff = 2
                    p2.payoff = 0
                    p2.More_or_less = 2
                if n.Yes_or_no == 2:
                    n.payoff = 0
                    p2.payoff = 2
                    p2.More_or_less = 1
        for k in group.get_players():
            k.session.vars['gr'] = group.subsession.get_group_matrix()

    def help_function(group: BaseGroup):
        for n in group.get_players():
            n.participant.vars['payoffgameone'] = n.payoff


class Player(BasePlayer):
    Roll_the_dice = models.IntegerField(label="Please roll the die in private now and write down the number that comes up:",
                                        min=1,
                                        max=6)

    Yes_or_no = models.IntegerField(label="",
                                    choices=[(1, "Yes"), (2, "No")],
                                    widget=widgets.RadioSelectHorizontal)

    More_or_less = models.IntegerField()
    Other_left = models.IntegerField(initial=0)
# PAGES
class Roll(Page):
    form_model = 'player'
    form_fields = ['Roll_the_dice', 'Yes_or_no']
    timeout_seconds = 240

    def is_displayed(player: Player):
        return player.role == C.Actor_role

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



class RollO(Page):
    def is_displayed(player: Player):
        return player.role == C.Observer_role

    timeout_seconds = 240

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

class PayoffWaitPage(WaitPage):
    def after_all_players_arrive(group: Group):
        group.payoff_function()


class Results(Page):
    def is_displayed(player: Player):
        return player.role == C.Actor_role

    def vars_for_template(player: Player):
        return dict(
            Rtd=player.Yes_or_no

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

class ResultsO(Page):
    def is_displayed(player: Player):
        return player.role == C.Observer_role

    def vars_for_template(player: Player):
        return dict(
            Mol=player.More_or_less

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


class HelpWaitPage(WaitPage):
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

page_sequence = [ Roll, RollO,HelpWaitPage2,LeftPage, PayoffWaitPage, HelpWaitPage, Results, ResultsO,HelpWaitPage2, LeftPage]
