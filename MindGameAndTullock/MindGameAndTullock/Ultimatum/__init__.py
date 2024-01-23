from otree.api import *


doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'Ultimatum'
    PLAYERS_PER_GROUP = 2
    NUM_ROUNDS = 1

    Actor_role = "actor"
    Observer_role = "observer"


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    Share = models.IntegerField()
    MinV = models.IntegerField()
    Other_left = models.IntegerField(initial=0)


# PAGES
class Page1(Page):
    def is_displayed(player: Player):
        return player.role == C.Actor_role

    @staticmethod
    def live_method(self, data):
        if data['t'] == 'final':
            response = dict()
            finalvalue = int(data['v'])
            self.Share = finalvalue
            if self.Share < 0:
                response.update(t="Nothing")
            if self.Share >= 0:
                response.update(t='submit')
            return {self.id_in_group: response}

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

class Page1O(Page):
    def is_displayed(player: Player):
        return player.role == C.Observer_role

    @staticmethod
    def live_method(self, data):
        if data['c'] == 'final1':
            response = dict()
            finalvalue1 = int(data['d'])
            self.MinV = finalvalue1
            if self.MinV < 0:
                response.update(c="Nothing")
            if self.MinV >= 0:
                response.update(c='submit')
            return {self.id_in_group: response}

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


class WaitPageShuffle(WaitPage):
    @staticmethod
    def after_all_players_arrive(subsession):
        gr = subsession.session.vars.get('gr')
        subsession.set_group_matrix(gr)


class DecisionPage(Page):
    def is_displayed(player: Player):
        return player.role == C.Actor_role

    @staticmethod
    def live_method(self, data):
        if data['t'] == 'final2':
            final2 = int(data['final_value2'])
            self.Share = final2

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
class DecisionPageO(Page):
    def is_displayed(player: Player):
        return player.role == C.Observer_role
    @staticmethod
    def live_method(self, data):
        if data['t'] == 'final':
            final = int(data['final_value'])
            self.MinV = final

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

    timeout_seconds = 180
class LeftPage(Page):
    def is_displayed(player: Player):
        return player.Other_left > 0

    def vars_for_template(player: Player):
        return dict(
            Other_left=player.Other_left
        )
class HelpWaitPage2(WaitPage):
    pass

page_sequence = [DecisionPage, DecisionPageO,HelpWaitPage2,LeftPage]
