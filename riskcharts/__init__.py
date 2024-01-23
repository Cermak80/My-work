from otree.api import *


doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'riskcharts'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    qrc1 = models.StringField()
    qrc2 = models.StringField()
    qrc3 = models.StringField()
    qrc4 = models.StringField()
    qrc5 = models.StringField()
    qrc6 = models.StringField()
    qrc7 = models.StringField()
    qrc8 = models.StringField()
    qrc9 = models.StringField()
    qrc10 = models.StringField()
    qrc11 = models.StringField()
    qrc12 = models.StringField()
    qrc13 = models.StringField()
    qrc14 = models.StringField()
    qrc15 = models.StringField()
    qrc16 = models.StringField()
    qrc17 = models.StringField()
    qrc18 = models.StringField()
    qrc19 = models.StringField()
    qrc20 = models.StringField()
    qrc21 = models.StringField()
    qrc22 = models.StringField()
    qrc23 = models.StringField()
    qrc24 = models.StringField()
    qrc25 = models.StringField()
    qrc26 = models.StringField()
    qrc27 = models.StringField()
    qrc28 = models.StringField()
    qrc29 = models.StringField()
    qrc30 = models.StringField()
    qrc31 = models.StringField()
    qrc32 = models.StringField()
    qrc33 = models.StringField()
    qrc34 = models.StringField()
    qrc35 = models.StringField()
    qrc36 = models.StringField()
    qrc37 = models.StringField()
    qrc38 = models.StringField()
    qrc39 = models.StringField()
    qrc40 = models.StringField()
    qrc41 = models.StringField()
    qrc42 = models.StringField()
    qrc43 = models.StringField()
    qrc44 = models.StringField()
    qrc45 = models.StringField()
    qrc46 = models.StringField()
    qrc47 = models.StringField()
    qrc48 = models.StringField()
    qrc49 = models.StringField()
    qrc50 = models.StringField()
    qrc51 = models.StringField()
    qrc52 = models.StringField()
    qrc53 = models.StringField()
    qrc54 = models.StringField()
    qrc55 = models.StringField()
    pocet_ukolu = models.IntegerField(initial=0)

    def paymentFunction(Player):
        if Player.participant.vars.get("typukolu") == "Risk chart":
            k = Player.participant.vars.get("cisloukolu")
            q_name = "qrc{}".format(k)

            Player.participant.vars["kolikukolu"] = getattr(Player, q_name)


    def set_qrc_field_value(Player, field_number, value):
        field_name = f"qrc{field_number}"
        setattr(Player, field_name, value)
    def ListCreation(Player):
        from random import shuffle
        import random
        Seznam = []
        for p in range(1, 56):
            Seznam.append(p)
        shuffled_first_25 = random.sample(Seznam[:25], k=25)

        # Nahrazení původních prvních 25 čísel promíchanými čísly
        Seznam[:25] = shuffled_first_25
        shuffled_remaining = random.sample(Seznam[25:], k=len(Seznam[25:]))
        Seznam[25:] = shuffled_remaining
        Player.participant.vars["Seznam"] = Seznam

    def ChanceFunction(Player):
        from random import randint
        x = randint(1,10)
        if Player.participant.vars.get("vyhra") == 1:
            if Player.participant.vars.get("typukolu") == "Risk chart":
                if Player.participant.vars.get("cisloukolu") == 1:
                    if Player.qrc1 == "A":
                        Player.pocet_ukolu = 144
                    if Player.qrc1 == "B":
                        if x <= 5:
                            Player.pocet_ukolu = 120
                        else:
                            Player.pocet_ukolu = 192
                if Player.participant.vars.get("cisloukolu") == 2:
                    if Player.qrc2 == "A":
                        if x <= 5:
                            Player.pocet_ukolu = 120
                        else:
                            Player.pocet_ukolu = 192
                    if Player.qrc2 == "B":
                        if x <= 5:
                            Player.pocet_ukolu = 96
                        else:
                            Player.pocet_ukolu = 240
                if Player.participant.vars.get("cisloukolu") == 3:
                    if Player.qrc3 == "A":
                        if x <= 5:
                            Player.pocet_ukolu = 96
                        else:
                            Player.pocet_ukolu = 240
                    if Player.qrc3 == "B":
                        if x <= 5:
                            Player.pocet_ukolu = 72
                        else:
                            Player.pocet_ukolu = 288
                if Player.participant.vars.get("cisloukolu") == 4:
                    if Player.qrc4 == "A":
                        if x <= 5:
                            Player.pocet_ukolu = 72
                        else:
                            Player.pocet_ukolu = 288
                    if Player.qrc4 == "B":
                        if x <= 5:
                            Player.pocet_ukolu = 48
                        else:
                            Player.pocet_ukolu = 336
                if Player.participant.vars.get("cisloukolu") == 5:
                    if Player.qrc5 == "A":
                        if x <= 5:
                            Player.pocet_ukolu = 48
                        else:
                            Player.pocet_ukolu = 336
                    if Player.qrc5 == "B":
                        if x <= 5:
                            Player.pocet_ukolu = 24
                        else:
                            Player.pocet_ukolu = 360
                if Player.participant.vars.get("cisloukolu") == 6:
                    if Player.qrc6 == "A":
                        if x <= 5:
                            Player.pocet_ukolu = 144
                        else:
                            Player.pocet_ukolu = 144
                    if Player.qrc6 == "B":
                        if x <= 5:
                            Player.pocet_ukolu = 126
                        else:
                            Player.pocet_ukolu = 198
                if Player.participant.vars.get("cisloukolu") == 7:
                    if Player.qrc7 == "A":
                        if x <= 5:
                            Player.pocet_ukolu = 126
                        else:
                            Player.pocet_ukolu = 198
                    if Player.qrc7 == "B":
                        if x <= 5:
                            Player.pocet_ukolu = 108
                        else:
                            Player.pocet_ukolu = 252
                if Player.participant.vars.get("cisloukolu") == 8:
                    if Player.qrc8 == "A":
                        if x <= 5:
                            Player.pocet_ukolu = 108
                        else:
                            Player.pocet_ukolu = 252
                    if Player.qrc8 == "B":
                        if x <= 5:
                            Player.pocet_ukolu = 90
                        else:
                            Player.pocet_ukolu = 306
                if Player.participant.vars.get("cisloukolu") == 9:
                    if Player.qrc9 == "A":
                        if x <= 5:
                            Player.pocet_ukolu = 90
                        else:
                            Player.pocet_ukolu = 306
                    if Player.qrc9 == "B":
                        if x <= 5:
                            Player.pocet_ukolu = 72
                        else:
                            Player.pocet_ukolu = 360
                if Player.participant.vars.get("cisloukolu") == 10:
                    if Player.qrc10 == "A":
                        if x <= 5:
                            Player.pocet_ukolu = 72
                        else:
                            Player.pocet_ukolu = 360
                    if Player.qrc10 == "B":
                        if x <= 5:
                            Player.pocet_ukolu = 48
                        else:
                            Player.pocet_ukolu = 384
                if Player.participant.vars.get("cisloukolu") == 11:
                    if Player.qrc11 == "A":
                        if x <= 5:
                            Player.pocet_ukolu = 144
                        else:
                            Player.pocet_ukolu = 144
                    if Player.qrc11 == "B":
                        if x <= 5:
                            Player.pocet_ukolu = 114
                        else:
                            Player.pocet_ukolu = 186
                if Player.participant.vars.get("cisloukolu") == 12:
                    if Player.qrc12 == "A":
                        if x <= 5:
                            Player.pocet_ukolu = 114
                        else:
                            Player.pocet_ukolu = 186
                    if Player.qrc12 == "B":
                        if x <= 5:
                            Player.pocet_ukolu = 84
                        else:
                            Player.pocet_ukolu = 228
                if Player.participant.vars.get("cisloukolu") == 13:
                    if Player.qrc13 == "A":
                        if x <= 5:
                            Player.pocet_ukolu = 84
                        else:
                            Player.pocet_ukolu = 228
                    if Player.qrc13 == "B":
                        if x <= 5:
                            Player.pocet_ukolu = 54
                        else:
                            Player.pocet_ukolu = 270
                if Player.participant.vars.get("cisloukolu") == 14:
                    if Player.qrc14 == "A":
                        if x <= 5:
                            Player.pocet_ukolu = 54
                        else:
                            Player.pocet_ukolu = 270
                    if Player.qrc14 == "B":
                        if x <= 5:
                            Player.pocet_ukolu = 24
                        else:
                            Player.pocet_ukolu = 312
                if Player.participant.vars.get("cisloukolu") == 15:
                    if Player.qrc15 == "A":
                        if x <= 5:
                            Player.pocet_ukolu = 24
                        else:
                            Player.pocet_ukolu = 312
                    if Player.qrc15 == "B":
                        if x <= 5:
                            Player.pocet_ukolu = 0
                        else:
                            Player.pocet_ukolu = 336
                if Player.participant.vars.get("cisloukolu") == 16:
                    if Player.qrc16 == "A":
                        if x <= 5:
                            Player.pocet_ukolu = 126
                        else:
                            Player.pocet_ukolu = 126
                    if Player.qrc16 == "B":
                        if x <= 5:
                            Player.pocet_ukolu = 108
                        else:
                            Player.pocet_ukolu = 180
                if Player.participant.vars.get("cisloukolu") == 17:
                    if Player.qrc17 == "A":
                        if x <= 5:
                            Player.pocet_ukolu = 108
                        else:
                            Player.pocet_ukolu = 180
                    if Player.qrc17 == "B":
                        if x <= 5:
                            Player.pocet_ukolu = 90
                        else:
                            Player.pocet_ukolu = 234
                if Player.participant.vars.get("cisloukolu") == 18:
                    if Player.qrc18 == "A":
                        if x <= 5:
                            Player.pocet_ukolu = 90
                        else:
                            Player.pocet_ukolu = 234
                    if Player.qrc18 == "B":
                        if x <= 5:
                            Player.pocet_ukolu = 72
                        else:
                            Player.pocet_ukolu = 288
                if Player.participant.vars.get("cisloukolu") == 19:
                    if Player.qrc19 == "A":
                        if x <= 5:
                            Player.pocet_ukolu = 72
                        else:
                            Player.pocet_ukolu = 288
                    if Player.qrc19 == "B":
                        if x <= 5:
                            Player.pocet_ukolu = 54
                        else:
                            Player.pocet_ukolu = 342
                if Player.participant.vars.get("cisloukolu") == 20:
                    if Player.qrc20 == "A":
                        if x <= 5:
                            Player.pocet_ukolu = 54
                        else:
                            Player.pocet_ukolu = 342
                    if Player.qrc20 == "B":
                        if x <= 5:
                            Player.pocet_ukolu = 30
                        else:
                            Player.pocet_ukolu = 366
                if Player.participant.vars.get("cisloukolu") == 21:
                    if Player.qrc21 == "A":
                        if x <= 5:
                            Player.pocet_ukolu = 162
                        else:
                            Player.pocet_ukolu = 162
                    if Player.qrc21 == "B":
                        if x <= 5:
                            Player.pocet_ukolu = 132
                        else:
                            Player.pocet_ukolu = 204
                if Player.participant.vars.get("cisloukolu") == 22:
                    if Player.qrc22 == "A":
                        if x <= 5:
                            Player.pocet_ukolu = 132
                        else:
                            Player.pocet_ukolu = 204
                    if Player.qrc22 == "B":
                        if x <= 5:
                            Player.pocet_ukolu = 102
                        else:
                            Player.pocet_ukolu = 246
                if Player.participant.vars.get("cisloukolu") == 23:
                    if Player.qrc23 == "A":
                        if x <= 5:
                            Player.pocet_ukolu = 102
                        else:
                            Player.pocet_ukolu = 246
                    if Player.qrc23 == "B":
                        if x <= 5:
                            Player.pocet_ukolu = 72
                        else:
                            Player.pocet_ukolu = 288
                if Player.participant.vars.get("cisloukolu") == 24:
                    if Player.qrc24 == "A":
                        if x <= 5:
                            Player.pocet_ukolu = 72
                        else:
                            Player.pocet_ukolu = 288
                    if Player.qrc24 == "B":
                        if x <= 5:
                            Player.pocet_ukolu = 42
                        else:
                            Player.pocet_ukolu = 330
                if Player.participant.vars.get("cisloukolu") == 25:
                    if Player.qrc25 == "A":
                        if x <= 5:
                            Player.pocet_ukolu = 42
                        else:
                            Player.pocet_ukolu = 330
                    if Player.qrc25 == "B":
                        if x <= 5:
                            Player.pocet_ukolu = 18
                        else:
                            Player.pocet_ukolu = 354
                if Player.participant.vars.get("cisloukolu") == 26:
                    if Player.qrc26 == "A":
                        if x == 1:
                            Player.pocet_ukolu = 96
                        else:
                            Player.pocet_ukolu = 120
                    if Player.qrc26 == "B":
                        if x == 1:
                            Player.pocet_ukolu = 6
                        else:
                            Player.pocet_ukolu = 231
                if Player.participant.vars.get("cisloukolu") == 27:
                    if Player.qrc27 == "A":
                        if x <= 2:
                            Player.pocet_ukolu = 96
                        else:
                            Player.pocet_ukolu = 120
                    if Player.qrc27 == "B":
                        if x <= 2:
                            Player.pocet_ukolu = 6
                        else:
                            Player.pocet_ukolu = 231
                if Player.participant.vars.get("cisloukolu") == 28:
                    if Player.qrc28 == "A":
                        if x <= 3:
                            Player.pocet_ukolu = 96
                        else:
                            Player.pocet_ukolu = 120
                    if Player.qrc28 == "B":
                        if x <= 3:
                            Player.pocet_ukolu = 6
                        else:
                            Player.pocet_ukolu = 231
                if Player.participant.vars.get("cisloukolu") == 29:
                    if Player.qrc29 == "A":
                        if x <= 4:
                            Player.pocet_ukolu = 96
                        else:
                            Player.pocet_ukolu = 120
                    if Player.qrc29 == "B":
                        if x <= 4:
                            Player.pocet_ukolu = 6
                        else:
                            Player.pocet_ukolu = 231
                if Player.participant.vars.get("cisloukolu") == 30:
                    if Player.qrc30 == "A":
                        if x <= 5:
                            Player.pocet_ukolu = 96
                        else:
                            Player.pocet_ukolu = 120
                    if Player.qrc30 == "B":
                        if x <= 5:
                            Player.pocet_ukolu = 6
                        else:
                            Player.pocet_ukolu = 231
                if Player.participant.vars.get("cisloukolu") == 31:
                    if Player.qrc31 == "A":
                        if x <= 6:
                            Player.pocet_ukolu = 96
                        else:
                            Player.pocet_ukolu = 120
                    if Player.qrc31 == "B":
                        if x <= 6:
                            Player.pocet_ukolu = 6
                        else:
                            Player.pocet_ukolu = 231
                if Player.participant.vars.get("cisloukolu") == 32:
                    if Player.qrc32 == "A":
                        if x <= 7:
                            Player.pocet_ukolu = 96
                        else:
                            Player.pocet_ukolu = 120
                    if Player.qrc32 == "B":
                        if x <= 7:
                            Player.pocet_ukolu = 6
                        else:
                            Player.pocet_ukolu = 231
                if Player.participant.vars.get("cisloukolu") == 33:
                    if Player.qrc33 == "A":
                        if x <= 8:
                            Player.pocet_ukolu = 96
                        else:
                            Player.pocet_ukolu = 120
                    if Player.qrc33 == "B":
                        if x <= 8:
                            Player.pocet_ukolu = 6
                        else:
                            Player.pocet_ukolu = 231
                if Player.participant.vars.get("cisloukolu") == 34:
                    if Player.qrc34 == "A":
                        if x <= 9:
                            Player.pocet_ukolu = 96
                        else:
                            Player.pocet_ukolu = 120
                    if Player.qrc34 == "B":
                        if x <= 9:
                            Player.pocet_ukolu = 6
                        else:
                            Player.pocet_ukolu = 231
                if Player.participant.vars.get("cisloukolu") == 35:
                    if Player.qrc35 == "A":
                        if x <= 9:
                            Player.pocet_ukolu = 96
                        else:
                            Player.pocet_ukolu = 96
                    if Player.qrc35 == "B":
                        if x <= 9:
                            Player.pocet_ukolu = 6
                        else:
                            Player.pocet_ukolu = 6
                if Player.participant.vars.get("cisloukolu") == 36:
                    if Player.qrc36 == "A":
                        if x <= 1:
                            Player.pocet_ukolu = 72
                        else:
                            Player.pocet_ukolu = 90
                    if Player.qrc36 == "B":
                        if x <= 1:
                            Player.pocet_ukolu = 5
                        else:
                            Player.pocet_ukolu = 173
                if Player.participant.vars.get("cisloukolu") == 37:
                    if Player.qrc37 == "A":
                        if x <= 2:
                            Player.pocet_ukolu = 72
                        else:
                            Player.pocet_ukolu = 90
                    if Player.qrc37 == "B":
                        if x <= 2:
                            Player.pocet_ukolu = 5
                        else:
                            Player.pocet_ukolu = 173
                if Player.participant.vars.get("cisloukolu") == 38:
                    if Player.qrc38 == "A":
                        if x <= 3:
                            Player.pocet_ukolu = 72
                        else:
                            Player.pocet_ukolu = 90
                    if Player.qrc38 == "B":
                        if x <= 3:
                            Player.pocet_ukolu = 5
                        else:
                            Player.pocet_ukolu = 173
                if Player.participant.vars.get("cisloukolu") == 39:
                    if Player.qrc39 == "A":
                        if x <= 4:
                            Player.pocet_ukolu = 72
                        else:
                            Player.pocet_ukolu = 90
                    if Player.qrc39 == "B":
                        if x <= 4:
                            Player.pocet_ukolu = 5
                        else:
                            Player.pocet_ukolu = 173
                if Player.participant.vars.get("cisloukolu") == 40:
                    if Player.qrc40 == "A":
                        if x <= 5:
                            Player.pocet_ukolu = 72
                        else:
                            Player.pocet_ukolu = 90
                    if Player.qrc40 == "B":
                        if x <= 5:
                            Player.pocet_ukolu = 5
                        else:
                            Player.pocet_ukolu = 173
                if Player.participant.vars.get("cisloukolu") == 41:
                    if Player.qrc41 == "A":
                        if x <= 6:
                            Player.pocet_ukolu = 72
                        else:
                            Player.pocet_ukolu = 90
                    if Player.qrc41 == "B":
                        if x <= 6:
                            Player.pocet_ukolu = 5
                        else:
                            Player.pocet_ukolu = 173
                if Player.participant.vars.get("cisloukolu") == 42:
                    if Player.qrc42 == "A":
                        if x <= 7:
                            Player.pocet_ukolu = 72
                        else:
                            Player.pocet_ukolu = 90
                    if Player.qrc42 == "B":
                        if x <= 7:
                            Player.pocet_ukolu = 5
                        else:
                            Player.pocet_ukolu = 173
                if Player.participant.vars.get("cisloukolu") == 43:
                    if Player.qrc43 == "A":
                        if x <= 8:
                            Player.pocet_ukolu = 72
                        else:
                            Player.pocet_ukolu = 90
                    if Player.qrc43 == "B":
                        if x <= 8:
                            Player.pocet_ukolu = 5
                        else:
                            Player.pocet_ukolu = 173
                if Player.participant.vars.get("cisloukolu") == 44:
                    if Player.qrc44 == "A":
                        if x <= 9:
                            Player.pocet_ukolu = 72
                        else:
                            Player.pocet_ukolu = 90
                    if Player.qrc44 == "B":
                        if x <= 9:
                            Player.pocet_ukolu = 5
                        else:
                            Player.pocet_ukolu = 173
                if Player.participant.vars.get("cisloukolu") == 45:
                    if Player.qrc45 == "A":
                        if x <= 9:
                            Player.pocet_ukolu = 72
                        else:
                            Player.pocet_ukolu = 72
                    if Player.qrc45 == "B":
                        if x <= 9:
                            Player.pocet_ukolu = 5
                        else:
                            Player.pocet_ukolu = 5
                if Player.participant.vars.get("cisloukolu") == 46:
                    if Player.qrc46 == "A":
                        if x <= 1:
                            Player.pocet_ukolu = 120
                        else:
                            Player.pocet_ukolu = 150
                    if Player.qrc46 == "B":
                        if x <= 1:
                            Player.pocet_ukolu = 8
                        else:
                            Player.pocet_ukolu = 289
                if Player.participant.vars.get("cisloukolu") == 47:
                    if Player.qrc47 == "A":
                        if x <= 2:
                            Player.pocet_ukolu = 120
                        else:
                            Player.pocet_ukolu = 150
                    if Player.qrc47 == "B":
                        if x <= 2:
                            Player.pocet_ukolu = 8
                        else:
                            Player.pocet_ukolu = 289
                if Player.participant.vars.get("cisloukolu") == 48:
                    if Player.qrc48 == "A":
                        if x <= 3:
                            Player.pocet_ukolu = 120
                        else:
                            Player.pocet_ukolu = 150
                    if Player.qrc48 == "B":
                        if x <= 3:
                            Player.pocet_ukolu = 8
                        else:
                            Player.pocet_ukolu = 289
                if Player.participant.vars.get("cisloukolu") == 49:
                    if Player.qrc49 == "A":
                        if x <= 4:
                            Player.pocet_ukolu = 120
                        else:
                            Player.pocet_ukolu = 150
                    if Player.qrc49 == "B":
                        if x <= 4:
                            Player.pocet_ukolu = 8
                        else:
                            Player.pocet_ukolu = 289
                if Player.participant.vars.get("cisloukolu") == 50:
                    if Player.qrc50 == "A":
                        if x <= 5:
                            Player.pocet_ukolu = 120
                        else:
                            Player.pocet_ukolu = 150
                    if Player.qrc50 == "B":
                        if x <= 5:
                            Player.pocet_ukolu = 8
                        else:
                            Player.pocet_ukolu = 289
                if Player.participant.vars.get("cisloukolu") == 51:
                    if Player.qrc51 == "A":
                        if x <= 6:
                            Player.pocet_ukolu = 120
                        else:
                            Player.pocet_ukolu = 150
                    if Player.qrc51 == "B":
                        if x <= 6:
                            Player.pocet_ukolu = 8
                        else:
                            Player.pocet_ukolu = 289
                if Player.participant.vars.get("cisloukolu") == 52:
                    if Player.qrc52 == "A":
                        if x <= 7:
                            Player.pocet_ukolu = 120
                        else:
                            Player.pocet_ukolu = 150
                    if Player.qrc52 == "B":
                        if x <= 7:
                            Player.pocet_ukolu = 8
                        else:
                            Player.pocet_ukolu = 289
                if Player.participant.vars.get("cisloukolu") == 53:
                    if Player.qrc53 == "A":
                        if x <= 8:
                            Player.pocet_ukolu = 120
                        else:
                            Player.pocet_ukolu = 150
                    if Player.qrc53 == "B":
                        if x <= 8:
                            Player.pocet_ukolu = 8
                        else:
                            Player.pocet_ukolu = 289
                if Player.participant.vars.get("cisloukolu") == 54:
                    if Player.qrc54 == "A":
                        if x <= 9:
                            Player.pocet_ukolu = 120
                        else:
                            Player.pocet_ukolu = 150
                    if Player.qrc54 == "B":
                        if x <= 9:
                            Player.pocet_ukolu = 8
                        else:
                            Player.pocet_ukolu = 289
                if Player.participant.vars.get("cisloukolu") == 55:
                    if Player.qrc55 == "A":
                        if x <= 0:
                            Player.pocet_ukolu = 120
                        else:
                            Player.pocet_ukolu = 120
                    if Player.qrc55 == "B":
                        if x <= 9:
                            Player.pocet_ukolu = 8
                        else:
                            Player.pocet_ukolu = 8





# PAGES
class MyPage(Page):
    def vars_for_template(player: Player):
        return dict(
            seznam=player.participant.vars.get("Seznam"),
            prvniobrazek=player.participant.vars.get("Seznam")[0]
        )

    @staticmethod
    def live_method(player, data):
        if data['t'] == 'A':
            cislootazky = player.participant.vars.get("Seznam")[data['tohlekolo']]
            player.set_qrc_field_value(cislootazky, "A")
        if data['t'] == 'B':
            cislootazky = player.participant.vars.get("Seznam")[data['tohlekolo']]
            player.set_qrc_field_value(cislootazky, "B")

    def before_next_page(player: Player, timeout_happened):
        player.ChanceFunction()
class ResultsWaitPage(WaitPage):
    pass


class InformationPage(Page):
    def before_next_page(player: Player, timeout_happened):
        Player.ListCreation(player)


page_sequence = [InformationPage,MyPage]
