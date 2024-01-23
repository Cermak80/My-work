from otree.api import *


doc = """
První kolo druhé části experimentu
"""


class C(BaseConstants):
    NAME_IN_URL = 'C12'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1

    poradi = [1,2]

    c = [10,30,50,70,90,110,130,150,170,190]





class Subsession(BaseSubsession):
    def mixer(subsession, seznamhracu):
        import random
        random.shuffle(seznamhracu)
        VyslednySeznam = []
        for x in seznamhracu:
            VyslednySeznam.append([x])
            if x == len(VyslednySeznam):
                return False
        return VyslednySeznam




def creating_session(subsession):
    from itertools import cycle
    from random import shuffle
    seznam = cycle(C.poradi)
    for x in subsession.get_players():
        from random import randint
        x.poradi = next(seznam)







class Group(BaseGroup):
    pass



class Player(BasePlayer):
    poradi = models.IntegerField()
    hraA1 = models.StringField(label="",
                               choices=["A", "B"],
                               widget=widgets.RadioSelect)
    hraA2 = models.StringField(label="",
                               choices=["A", "B"],
                               widget=widgets.RadioSelect)
    hraA3 = models.StringField(label="",
                               choices=["A", "B"],
                               widget=widgets.RadioSelect)
    hraA4 = models.StringField(label="",
                               choices=["A", "B"],
                               widget=widgets.RadioSelect)
    hraA5 = models.StringField(label="",
                               choices=["A", "B"],
                               widget=widgets.RadioSelect)
    hraA6 = models.StringField(label="",
                               choices=["A", "B"],
                               widget=widgets.RadioSelect)
    hraA7 = models.StringField(label="",
                               choices=["A", "B"],
                               widget=widgets.RadioSelect)
    hraA8 = models.StringField(label="",
                               choices=["A", "B"],
                               widget=widgets.RadioSelect)
    hraA9 = models.StringField(label="",
                               choices=["A", "B"],
                               widget=widgets.RadioSelect)
    hraA10 = models.StringField(label="",
                               choices=["A", "B"],
                               widget=widgets.RadioSelect)



    hraB1 = models.StringField(label="",
                               choices=["A", "B"],
                               widget=widgets.RadioSelect)
    hraB2 = models.StringField(label="",
                               choices=["A", "B"],
                               widget=widgets.RadioSelect)
    hraB3 = models.StringField(label="",
                               choices=["A", "B"],
                               widget=widgets.RadioSelect)
    hraB4 = models.StringField(label="",
                               choices=["A", "B"],
                               widget=widgets.RadioSelect)
    hraB5 = models.StringField(label="",
                               choices=["A", "B"],
                               widget=widgets.RadioSelect)
    hraB6 = models.StringField(label="",
                               choices=["A", "B"],
                               widget=widgets.RadioSelect)
    hraB7 = models.StringField(label="",
                               choices=["A", "B"],
                               widget=widgets.RadioSelect)
    hraB8 = models.StringField(label="",
                               choices=["A", "B"],
                               widget=widgets.RadioSelect)
    hraB9 = models.StringField(label="",
                               choices=["A", "B"],
                               widget=widgets.RadioSelect)
    hraB10 = models.StringField(label="",
                                choices=["A", "B"],
                                widget=widgets.RadioSelect)



    hraC1 = models.StringField(label="",
                               choices=["A", "B"],
                               widget=widgets.RadioSelect)
    hraC2 = models.StringField(label="",
                               choices=["A", "B"],
                               widget=widgets.RadioSelect)
    hraC3 = models.StringField(label="",
                               choices=["A", "B"],
                               widget=widgets.RadioSelect)
    hraC4 = models.StringField(label="",
                               choices=["A", "B"],
                               widget=widgets.RadioSelect)
    hraC5 = models.StringField(label="",
                               choices=["A", "B"],
                               widget=widgets.RadioSelect)
    hraC6 = models.StringField(label="",
                               choices=["A", "B"],
                               widget=widgets.RadioSelect)
    hraC7 = models.StringField(label="",
                               choices=["A", "B"],
                               widget=widgets.RadioSelect)
    hraC8 = models.StringField(label="",
                               choices=["A", "B"],
                               widget=widgets.RadioSelect)
    hraC9 = models.StringField(label="",
                               choices=["A", "B"],
                               widget=widgets.RadioSelect)
    hraC10 = models.StringField(label="",
                                choices=["A", "B"],
                                widget=widgets.RadioSelect)


# funkce pro hráče
    def Zacatek(Player,id,lis):
        x = Player.group.get_player_by_id(id)
        x.participant.vars["protihraci"] = lis
        Player.participant.vars["MojeVyhry"] = []

    def Zacatek_dva(Player):
        #Tady se definují jednotlivé skupiny pro první kolo:
        souperi = Player.skupiny()
        Player.Zacatek(Player.id_in_group,souperi[Player.id_in_group-1])

    def AfterRound(Player,souper,typhry):
        import random
        VylosovanyNaklad = random.randint(1,10)
        VylosovanyNakladC = C.c[VylosovanyNaklad-1]
        VylosovanyNakladSouper = random.randint(1,10)
        VylosovanyNakladSouperC = C.c[VylosovanyNakladSouper-1]
        MujSouper = Player.group.get_player_by_id(Player.participant.vars.get("protihraci")[souper-1])
        Vyhra = 0
        if typhry == 1:
            MojeVolba = getattr(Player, f'hraA{VylosovanyNaklad}')
            SouperovaVolba = getattr(MujSouper,f'hraA{VylosovanyNakladSouper}')
            if MojeVolba == "A":
                if SouperovaVolba == "A":
                    Vyhra = 280 - VylosovanyNakladC
                else:
                    Vyhra = 320 - VylosovanyNakladC
            if MojeVolba == "B":
                if SouperovaVolba == "A":
                    Vyhra = 120
                else:
                    Vyhra = 280

        if typhry == 2:
            MojeVolba = getattr(Player, f'hraA{10 + VylosovanyNaklad}')
            SouperovaVolba = getattr(MujSouper,f'hraA{10 + VylosovanyNakladSouper}')
            if MojeVolba == "A":
                if SouperovaVolba == "A":
                    Vyhra = 280 - VylosovanyNakladC
                else:
                    Vyhra = 320 - VylosovanyNakladC
            if MojeVolba == "B":
                if SouperovaVolba == "A":
                    Vyhra = 120
                else:
                    Vyhra = 280

        if typhry == 3:
            MojeVolba = getattr(Player, f'hraB{VylosovanyNaklad}')
            SouperovaVolba = getattr(MujSouper,f'hraB{VylosovanyNakladSouper}')
            if MojeVolba == "A":
                if SouperovaVolba == "A":
                    Vyhra = 220 - VylosovanyNakladC
                else:
                    Vyhra = 380 - VylosovanyNakladC
            if MojeVolba == "B":
                if SouperovaVolba == "A":
                    Vyhra = 180
                else:
                    Vyhra = 220

        if typhry == 4:
            MojeVolba = getattr(Player, f'hraB{10 + VylosovanyNaklad}')
            SouperovaVolba = getattr(MujSouper,f'hraB{10 + VylosovanyNakladSouper}')
            if MojeVolba == "A":
                if SouperovaVolba == "A":
                    Vyhra = 220 - VylosovanyNakladC
                else:
                    Vyhra = 380 - VylosovanyNakladC
            if MojeVolba == "B":
                if SouperovaVolba == "A":
                    Vyhra = 180
                else:
                    Vyhra = 220

        if typhry == 5:
            MojeVolba = getattr(Player, f'hraC{VylosovanyNaklad}')
            SouperovaVolba = getattr(MujSouper,f'hraC{VylosovanyNakladSouper}')
            if MojeVolba == "A":
                if SouperovaVolba == "A":
                    Vyhra = 250 - VylosovanyNakladC
                else:
                    Vyhra = 370 - VylosovanyNakladC
            if MojeVolba == "B":
                if SouperovaVolba == "A":
                    Vyhra = 130
                else:
                    Vyhra = 250

        if typhry == 6:
            MojeVolba = getattr(Player, f'hraC{10 + VylosovanyNaklad}')
            SouperovaVolba = getattr(MujSouper,f'hraC{10 + VylosovanyNakladSouper}')
            if MojeVolba == "A":
                if SouperovaVolba == "A":
                    Vyhra = 250 - VylosovanyNakladC
                else:
                    Vyhra = 370 - VylosovanyNakladC
            if MojeVolba == "B":
                if SouperovaVolba == "A":
                    Vyhra = 130
                else:
                    Vyhra = 250
        Player.participant.vars["MojeVyhry"].append([VylosovanyNakladC,MojeVolba,SouperovaVolba,Vyhra,typhry,VylosovanyNakladSouperC])
        print(Player.participant.vars.get("MojeVyhry"))

    def skupiny(Player):
        if len(Player.subsession.get_players()) == 12:
            souperi = [[3, 5, 9, 11, 5, 11], [4, 6, 10, 12, 10, 12], [1, 9, 5, 7, 11, 7], [2, 10, 6, 8, 12, 8],
                       [7, 1, 3, 9, 1, 9],
                       [8, 2, 4, 10, 2, 10], [5, 11, 11, 3, 9, 3], [6, 12, 12, 4, 10, 4], [11, 3, 1, 5, 7, 5],
                       [12, 4, 2, 6, 8, 6],
                       [9, 7, 7, 1, 3, 1], [10, 8, 8, 2, 4, 2]]
        if len(Player.subsession.get_players()) == 18:
            souperi = [[3, 5, 7, 9, 11, 15], [4, 6, 8, 10, 12, 16], [1, 7, 5, 11, 9, 13], [2, 8, 6, 12, 10, 14],
                       [7, 1, 3, 13, 15, 9], [8, 2, 4, 14, 16, 10], [5, 3, 1, 15, 13, 11], [6, 4, 2, 16, 14, 12],
                       [11, 13, 15, 1, 3, 5], [12, 14, 16, 2, 4, 6], [9, 15, 13, 3, 1, 7], [10, 16, 14, 4, 2, 8],
                       [15, 9, 11, 5, 7, 3], [16, 10, 12, 6, 8, 4], [13, 11, 9, 7, 5, 1], [14, 12, 10, 8, 6, 2],
                       [15, 1, 3, 5, 7, 9], [16, 2, 4, 6, 8, 10]]
        if len(Player.subsession.get_players()) == 24:
            souperi = [[3, 5, 7, 11, 13, 23], [4, 6, 8, 12, 14, 24], [1, 7, 5, 13, 11, 21], [2, 8, 6, 14, 12, 22],
                       [7, 1, 3, 15, 9, 13], [8, 2, 4, 16, 10, 14], [5, 3, 1, 21, 23, 17], [6, 4, 2, 22, 24, 18],
                       [11, 13, 15, 23, 5, 15], [12, 14, 16, 24, 6, 16], [9, 15, 13, 1, 3, 19], [10, 16, 14, 2, 4, 20],
                       [15, 9, 11, 3, 1, 5], [16, 10, 12, 4, 2, 6], [13, 11, 9, 5, 21, 9], [14, 12, 10, 6, 22, 10],
                       [19, 21, 23, 19, 19, 7], [20, 22, 24, 20, 20, 8], [17, 23, 21, 17, 17, 11],
                       [18, 24, 22, 18, 18, 12],
                       [23, 17, 19, 7, 15, 3], [24, 18, 20, 8, 16, 4], [21, 19, 17, 9, 7, 1], [22, 20, 18, 10, 8, 2]]
        if len(Player.subsession.get_players()) == 2:
            souperi = [[2,2,2,2,2,2],[1,1,1,1,1,1]]
        if len(Player.subsession.get_players()) ==  6:
            souperi = [[3,5,3],[4,6,4],[1,5,5],[2,6,2],[1,1,3],[2,2,2]]

        return souperi



# PAGES
class FirstPage(Page):
    def before_next_page(player: Player, timeout_happened):
        player.Zacatek_dva()

class Game1(Page):
    form_model = Player
    form_fields = ["hraA1","hraA2","hraA3","hraA4","hraA5","hraA6","hraA7","hraA8","hraA9","hraA10",]

    def is_displayed(player: Player):
        return player.poradi == 1
    def vars_for_template(player: Player):
        h = []
        for x in C.c:
            levahorni = 280-int(x)
            pravahorni = 320-int(x)
            h.append([x,levahorni,pravahorni])

        return dict(
            c=h,
        )

class Game12(Page):
    form_model = Player
    form_fields = ["hraA11", "hraA12", "hraA13", "hraA14", "hraA15", "hraA16", "hraA17", "hraA18", "hraA19", "hraA20", ]

    def is_displayed(player: Player):
        return player.poradi == 1
    def vars_for_template(player: Player):
        h = []
        for x in C.c:
            levahorni = 280-int(x)
            pravahorni = 320-int(x)
            h.append([x,levahorni,pravahorni])

        return dict(
            c=h,
        )


class Game2(Page):
    def is_displayed(player: Player):
        return player.poradi == 1
    form_model = Player
    form_fields = ["hraB1", "hraB2", "hraB3", "hraB4", "hraB5", "hraB6", "hraB7", "hraB8", "hraB9", "hraB10", ]

    def vars_for_template(player: Player):
        h = []
        for x in C.c:
            levahorni = 250 - int(x)
            pravahorni = 370 - int(x)
            h.append([x, levahorni, pravahorni])

        return dict(
            c=h,
        )

class Game22(Page):
    def is_displayed(player: Player):
        return player.poradi == 1
    form_model = Player
    form_fields = ["hraB11", "hraB12", "hraB13", "hraB14", "hraB15", "hraB16", "hraB17", "hraB18", "hraB19", "hraB20", ]

    def vars_for_template(player: Player):
        h = []
        for x in C.c:
            levahorni = 250 - int(x)
            pravahorni = 370 - int(x)
            h.append([x, levahorni, pravahorni])

        return dict(
            c=h,
        )



class WaitPage1(WaitPage):
    def after_all_players_arrive(group: Group):
        for x in group.get_players():
            if x.poradi == 1:
                x.AfterRound(1, 1)
            if x.poradi == 2:
                x.AfterRound(1, 5)


class WaitPage2(WaitPage):
    def after_all_players_arrive(group: Group):
        for x in group.get_players():
            if x.poradi == 1:
                x.AfterRound(2, 2)
            if x.poradi == 2:
                x.AfterRound(2, 5)


class WaitPage3(WaitPage):
    def after_all_players_arrive(group: Group):
        for x in group.get_players():
            if x.poradi == 1:
                x.AfterRound(2, 3)
            if x.poradi == 2:
                x.AfterRound(2, 3)


class WaitPage4(WaitPage):
    def after_all_players_arrive(group: Group):
        for x in group.get_players():
            if x.poradi == 1:
                x.AfterRound(4, 4)
            if x.poradi == 2:
                x.AfterRound(4, 3)


class WaitPage5(WaitPage):
    def after_all_players_arrive(group: Group):
        for x in group.get_players():
            if x.poradi == 1:
                x.AfterRound(3, 5)
            if x.poradi == 2:
                x.AfterRound(3, 1)

class WaitPage6(WaitPage):
    def after_all_players_arrive(group: Group):
        for x in group.get_players():
            if x.poradi == 1:
                x.AfterRound(6, 6)
            if x.poradi == 2:
                x.AfterRound(6, 1)


class Game3(Page):
    def is_displayed(player: Player):
        return player.poradi == 1
    form_model = Player
    form_fields = ["hraC1", "hraC2", "hraC3", "hraC4", "hraC5", "hraC6", "hraC7", "hraC8", "hraC9", "hraC10" ]

    def vars_for_template(player: Player):
        h = []
        for x in C.c:
            levahorni = 250 - int(x)
            pravahorni = 370 - int(x)
            h.append([x, levahorni, pravahorni])

        return dict(
            c=h,
        )


class Game32(Page):
    def is_displayed(player: Player):
        return player.poradi == 1
    form_model = Player
    form_fields = ["hraC11", "hraC12", "hraC13", "hraC14", "hraC15", "hraC16", "hraC17", "hraC18", "hraC19", "hraC20", ]

    def vars_for_template(player: Player):
        h = []
        for x in C.c:
            levahorni = 220 - int(x)
            pravahorni = 380 - int(x)
            h.append([x, levahorni, pravahorni])

        return dict(
            c=h,
        )

class Game1A(Page):
    form_model = Player
    form_fields = ["hraA11", "hraA12", "hraA13", "hraA14", "hraA15", "hraA16", "hraA17", "hraA18", "hraA19", "hraA20", ]

    def is_displayed(player: Player):
        return player.poradi == 2

    def vars_for_template(player: Player):
        h = []
        for x in C.c:
            levahorni = 280 - int(x)
            pravahorni = 320 - int(x)
            h.append([x, levahorni, pravahorni])

        return dict(
            c=h,
        )


class Game1A2(Page):
    form_model = Player
    form_fields = ["hraA1", "hraA2", "hraA3", "hraA4", "hraA5", "hraA6", "hraA7", "hraA8", "hraA9", "hraA10", ]

    def is_displayed(player: Player):
        return player.poradi == 2

    def vars_for_template(player: Player):
        h = []
        for x in C.c:
            levahorni = 280 - int(x)
            pravahorni = 320 - int(x)
            h.append([x, levahorni, pravahorni])

        return dict(
            c=h,
        )

class Game2A(Page):
    def is_displayed(player: Player):
        return player.poradi == 2
    form_model = Player
    form_fields = ["hraB11", "hraB12", "hraB13", "hraB14", "hraB15", "hraB16", "hraB17", "hraB18", "hraB19", "hraB20", ]

    def vars_for_template(player: Player):
        h = []
        for x in C.c:
            levahorni = 250 - int(x)
            pravahorni = 370 - int(x)
            h.append([x, levahorni, pravahorni])

        return dict(
            c=h,
        )


class Game2A2(Page):
    def is_displayed(player: Player):
        return player.poradi == 2
    form_model = Player
    form_fields = ["hraB1", "hraB2", "hraB3", "hraB4", "hraB5", "hraB6", "hraB7", "hraB8", "hraB9", "hraB10", ]

    def vars_for_template(player: Player):
        h = []
        for x in C.c:
            levahorni = 250 - int(x)
            pravahorni = 370 - int(x)
            h.append([x, levahorni, pravahorni])

        return dict(
            c=h,
        )

class Game3A(Page):
    def is_displayed(player: Player):
        return player.poradi == 2
    form_model = Player
    form_fields = ["hraC11", "hraC12", "hraC13", "hraC14", "hraC15", "hraC16", "hraC17", "hraC18", "hraC19", "hraC20" ]

    def vars_for_template(player: Player):
        h = []
        for x in C.c:
            levahorni = 250 - int(x)
            pravahorni = 370 - int(x)
            h.append([x, levahorni, pravahorni])

        return dict(
            c=h,
        )

class Game3A2(Page):
    def is_displayed(player: Player):
        return player.poradi == 2
    form_model = Player
    form_fields = ["hraC1", "hraC2", "hraC3", "hraC4", "hraC5", "hraC6", "hraC7", "hraC8", "hraC9", "hraC10"]

    def vars_for_template(player: Player):
        h = []
        for x in C.c:
            levahorni = 250 - int(x)
            pravahorni = 370 - int(x)
            h.append([x, levahorni, pravahorni])

        return dict(
            c=h,
        )

class Vysledek1(Page):
    def vars_for_template(player: Player):
        x = player.participant.vars.get("MojeVyhry")[0]

        return dict(
            naklad=x[0],
            mojevolba=x[1],
            soupervolba=x[2],
            vyhra=x[3],
            soupernaklad=x[5],
            poradi=player.poradi
        )


class Vysledek2(Page):
    def vars_for_template(player: Player):
        x = player.participant.vars.get("MojeVyhry")[1]

        return dict(
            naklad=x[0],
            mojevolba=x[1],
            soupervolba=x[2],
            vyhra=x[3],
            soupernaklad=x[5]
        )


class Vysledek3(Page):
    def vars_for_template(player: Player):
        x = player.participant.vars.get("MojeVyhry")[1]

        return dict(
            naklad=x[0],
            mojevolba=x[1],
            soupervolba=x[2],
            vyhra=x[3],
            soupernaklad=x[5],
            poradi=player.poradi
        )


class Vysledek4(Page):
    def vars_for_template(player: Player):
        x = player.participant.vars.get("MojeVyhry")[3]

        return dict(
            naklad=x[0],
            mojevolba=x[1],
            soupervolba=x[2],
            vyhra=x[3],
            soupernaklad=x[5]
        )


class Vysledek5(Page):
    def vars_for_template(player: Player):
        x = player.participant.vars.get("MojeVyhry")[2]

        return dict(
            naklad=x[0],
            mojevolba=x[1],
            soupervolba=x[2],
            vyhra=x[3],
            soupernaklad=x[5],
            poradi=player.poradi
        )


class Vysledek6(Page):
    def vars_for_template(player: Player):
        x = player.participant.vars.get("MojeVyhry")[5]

        return dict(
            naklad=x[0],
            mojevolba=x[1],
            soupervolba=x[2],
            vyhra=x[3],
            soupernaklad=x[5]
        )


class MainWaitPage(WaitPage):
    wait_for_all_groups = True


class SecondPage(Page):
    pass


class ThirdPage(Page):
    pass

class SecondpointPage(Page):
    pass



page_sequence = [FirstPage,MainWaitPage,SecondPage, MainWaitPage,SecondpointPage,MainWaitPage,ThirdPage,
                 MainWaitPage,Game1,Game3A2,WaitPage1,Vysledek1,
                 Game2, Game2A2,
                 WaitPage3, Vysledek3,
                 Game3, Game1A2,WaitPage5,Vysledek5]
