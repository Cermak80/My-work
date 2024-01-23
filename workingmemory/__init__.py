from otree.api import *

doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'workingmemory'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1

    odmenaa = 10


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    ind = models.IntegerField(initial=3)
    correct_answers = models.IntegerField(initial=0)
    correct_answers2 = models.IntegerField(initial=0)
    wrong_answers = models.IntegerField(initial=0)
    mistake = models.IntegerField(initial=0)

    def generate_list(Player,o):
        from random import randint
        random_num = []
        for i in range(0, o):
            rn = randint(1, 9)
            random_num.append(rn)
        return random_num

    def payoff_func(Player):
        x = C.odmenaa * Player.correct_answers
        y = C.odmenaa * Player.correct_answers2
        Player.payoff = cu(x + y)
        Player.participant.vars["payoffWork"] = x + y


# PAGES
class Introduction(Page):
    def before_next_page(player: Player, timeout_happened):
        Player.generate_list(player, player.ind)


class WM(Page):
    def vars_for_template(player: Player):
        return dict(
            xd=Player.generate_list(player, player.ind)
        )

    @staticmethod
    def live_method(player, data):
        response = dict()
        if data['t'] == 'answer':

            if data['answer'] == "spravne":
                response.update(t='ok')
                player.correct_answers += 1
                player.ind += 1
                player.mistake = 0
            else:
                player.mistake += 1
                if player.mistake == 2:
                    response.update(t='ggwp')
                    player.mistake = 0
                    player.ind = 3
                else:
                    response.update(t='notok')
                player.wrong_answers += 1
        return {player.id_in_group: response}




class WM2(Page):
    def vars_for_template(player: Player):
        return dict(
            xd2=Player.generate_list(player, player.ind)
        )

    @staticmethod
    def live_method(player, data):
        response = dict()
        if data['t'] == 'answer':

            if data['answer'] == "spravne":
                response.update(t='ok')
                player.correct_answers2 += 1
                player.ind += 1
                player.mistake = 0
            else:
                player.mistake += 1
                if player.mistake == 2:
                    response.update(t='ggwp')
                else:
                    response.update(t='notok')
                player.wrong_answers += 1
        return {player.id_in_group: response}

    def before_next_page(player: Player, timeout_happened):
        player.payoff_func()

class MidPage(Page):
    pass
page_sequence = [Introduction, WM,MidPage, WM2]
