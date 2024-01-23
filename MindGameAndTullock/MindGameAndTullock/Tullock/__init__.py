from otree.api import *


doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'Tullock'
    PLAYERS_PER_GROUP = 2
    NUM_ROUNDS = 1

    participation_fee = 2


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    def payoff(group:BaseGroup):
        p1 = group.get_player_by_id(1)
        p2 = group.get_player_by_id(2)
        if p1.Investment > 0:
            if p2.Investment > 0:
                share = p1.Investment / (p1.Investment + p2.Investment)
                share2 = 1 - share
        if p1.Investment == 0:
            if p2.Investment > 0:
                share = 0
                share2 = 1
            if p2. Investment == 0:
                share = 0.5
                share2 = 0.5
        if p2.Investment == 0:
            if p1.Investment > 0:
                share = 1
                share2 = 0
        for n in group.get_players():
            if n.id_in_group == 1:
                p1.opponent_payT = int(((100 - p2.Investment) + share2 * 200))
                n.win_in_tokens = int(((100 - n.Investment) + share * 200))
                x = int(((100 - p1.Investment) + share * 200))
                p1.payoff = x * 0.01
                p1.pay = x * 0.01

            if n.id_in_group == 2:
                n.opponent_payT = int(((100 - p1.Investment) + share * 200))
                n.win_in_tokens = int(((100 - p2.Investment) + share2 * 200))
                y = int(((100 - p2.Investment) + share2 * 200))
                p2.payoff = y * 0.01
                p2.pay = y * 0.01

        for k in group.get_players():
            if k.id_in_group == 1:
                p1.opponent_pay = p2.pay
                k.Coll_investment = p2.Investment
                if p1.Expectation_ >= p2.Investment - 10:
                    if p1.Expectation_ <= p2.Investment + 10:
                        p1.payoff = p1.payoff + 0.5
                        k.prediction = 1
            if k.id_in_group == 2:
                p2.opponent_pay = p1.pay
                k.Coll_investment = p1.Investment
                if p2.Expectation_ >= p1.Investment - 10:
                    if p2.Expectation_ <= p1.Investment + 10:
                        p2.payoff = p2.payoff + 0.5
                        k.prediction = 1


class Player(BasePlayer):
    Investment = models.IntegerField(initial=0)
    Expectation_ = models.IntegerField(initial=0)
    Coll_investment = models.IntegerField()
    win_in_tokens = models.IntegerField()
    opponent_pay = models.CurrencyField()
    opponent_payT = models.IntegerField()
    prediction = models.IntegerField(initial=0)
    pay = models.FloatField()
    Other_left = models.IntegerField(initial=0)


# PAGES
class InvestmentPage(Page):
    @staticmethod
    def live_method(self, data):
        if data['t'] == 'final':
            response = dict()
            finalvalue = int(data['v'])
            self.Investment = finalvalue
            if self.Investment < 0:
                response.update(t="Nothing")
            if self.Investment >= 0:
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
class WaitforallPage(WaitPage):
    wait_for_all_groups = True


class ExpectationPage(Page):
    @staticmethod
    def live_method(self, data):
        if data['t'] == 'final':
            response = dict()
            finalvalue = int(data['v'])
            self.Investment = finalvalue
            if self.Expectation_ < 0:
                response.update(t="Nothing")
            if self.Expectation_ >= 0:
                response.update(t='submit')
            return {self.id_in_group: response}

    timeout_seconds = 300

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


class ResultsWaitPage(WaitPage):
    def after_all_players_arrive(group: Group):
        group.payoff()

class Page1T(Page):
    @staticmethod
    def live_method(self, data):
        if data['t'] == 'final':
            final = int(data['final_value'])
            self.Investment = final
        if data['t'] == 'final2':
            final2 = int(data['final_value2'])
            self.Expectation_ = final2

    timeout_seconds = 300

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

class ResultsTullock(Page):
    def vars_for_template(player: Player):
        return dict(
            inv=player.Investment,
            coll_inv=player.Coll_investment,
            w_in_tokens=player.win_in_tokens,
            payoff=round(player.pay,2),
            opponent_pay=player.opponent_pay,
            opponent_payT=player.opponent_payT,
            Expectation=player.Expectation_,
            prediction=player.prediction


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

class TotalResults(Page):
    def vars_for_template(player: Player):
        return dict(
            Tullockpayoff=player.payoff,
            participation_fee=C.participation_fee,
            payoffgameone=player.participant.vars.get('payoffgameone'),
            TotalPayoff=player.payoff + C.participation_fee + player.participant.vars.get('payoffgameone')
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


class LeftPage(Page):
    def is_displayed(player: Player):
        return player.Other_left > 0

    def vars_for_template(player: Player):
        return dict(
            Other_left=player.Other_left
        )
class HelpWaitPage2(WaitPage):
    pass


page_sequence = [Page1T, HelpWaitPage2, LeftPage, ResultsWaitPage, ResultsTullock,
                 HelpWaitPage2, LeftPage, TotalResults, HelpWaitPage2, LeftPage]
