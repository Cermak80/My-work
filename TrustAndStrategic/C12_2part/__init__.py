import random

from otree.api import *


doc = """
2. část experimentu C12
"""


class C(BaseConstants):
    NAME_IN_URL = 'C12_2part'
    PLAYERS_PER_GROUP = 2
    NUM_ROUNDS = 5

    Treatmenty = ["A","B","C","AR","BR","CR"]
    Poradi = [1,2,3,4,5,6]
    c = [10, 30, 50, 70, 90, 110, 130, 150, 170, 190]

class Subsession(BaseSubsession):
    def MixerSkupin(subsession):
        from random import shuffle
        if subsession.round_number == 1:
            skupiny = subsession.get_group_matrix()
            suda = []
            licha = []
            promenna = 0
            for x in subsession.get_group_matrix():
                licha.append(skupiny[promenna][0])
                suda.append(skupiny[promenna][1])
                promenna += 1

            shuffle(licha)
            shuffle(suda)
            Finalni_dvojice = []
            pomocna = 0
            for y in subsession.get_groups():
                mujlist=[licha[pomocna],suda[pomocna]]
                Finalni_dvojice.append(mujlist)
                pomocna += 1
            subsession.set_group_matrix(Finalni_dvojice)
        else:
            subsession.group_like_round(1)

        from itertools import cycle
        seznam = cycle(C.Treatmenty)
        for x in subsession.get_groups():
            x.Treatment = next(seznam)





class Group(BaseGroup):
    Treatment = models.StringField()


    def PaymentFunctionGroup(Group):
        from random import randint
        for x in Group.get_players():
            x.participant.vars["VyslednaZprava"]=[]
        CoSePlati = randint(1,13)
        for y in Group.get_players():
            y.CoSePlati = CoSePlati
            y.participant.vars["CoSePlati"] = CoSePlati
            if CoSePlati <= 3:
                Group.PaymentFunctionOption1()
            else:
                Group.PaymentFunctionOption2()



    def PaymentFunctionOption1(Group):
        from random import randint
        for x in Group.get_players():
            x.participant.vars["Pojistka"] = "1"
            x.participant.vars["VyslednaZprava"].append("Vylosovala se Vám výplata z první části experimentu")
            x.DruhVyplaty = "Prvni cast"
            KteraHra = randint(1, 3)
            x.Vyhra = x.participant.vars.get("MojeVyhry")[KteraHra-1][3]
            x.payoff = cu(x.Vyhra)
            x.participant.vars["VyslednaZprava"].append(KteraHra)
            x.KteraHra = KteraHra
            for y in range(1,20):
                x.participant.vars["VyslednaZprava"].append("Null")


    def PaymentFunctionOption2(Group):
        from random import randint
        import random

        for x in Group.get_players():
            x.participant.vars["Pojistka"] = "2"
            x.participant.vars["VyslednaZprava"].append("Vylosovala se Vám výplata z druhé části experimentu")
            x.DruhVyplaty = "Druha cast"
        Kthra = randint(1, 5) #Losujeme která z 5-ti her se bude platit
        for y in Group.get_players():
            y.participant.vars["VyslednaZprava"].append(Kthra)
        NakladyHrace1 = randint(1,10)
        NakladyHrace1C = C.c[NakladyHrace1-1]
        NakladyHrace2 = randint(1,10)
        NakladyHrace2C = C.c[NakladyHrace2-1]
        Hrac1 = Group.get_player_by_id(1)
        Hrac2 = Group.get_player_by_id(2)
        Hrac1PresneKolo = Hrac1.in_round(Kthra)
        Hrac2PresneKolo = Hrac2.in_round(Kthra)
        Hrac1Preference = Hrac1PresneKolo.PreferenceA
        Hrac2Preference = Hrac2PresneKolo.PreferenceA
        if Hrac1Preference == "Levá" and Hrac2Preference == "Levá":
            FinalniPreference = "Levá"
        if Hrac1Preference == "Pravá" and Hrac2Preference == "Pravá":
            FinalniPreference = "Pravá"
        if Hrac1Preference == "Levá" and Hrac2Preference == "Pravá":
            FinalniPreference = random.choice(["Levá","Pravá"])
        if Hrac1Preference == "Pravá" and Hrac2Preference == "Levá":
            FinalniPreference = random.choice(["Levá","Pravá"])
        if FinalniPreference == "Levá":
            Hrac1Volba = getattr(Hrac1PresneKolo, f'hraA{NakladyHrace1}'+"L")
            Hrac2Volba = getattr(Hrac2PresneKolo, f'hraA{NakladyHrace2}'+"L")
        if FinalniPreference == "Pravá":
            Hrac1Volba = getattr(Hrac1PresneKolo, f'hraA{NakladyHrace1}'+"P")
            Hrac2Volba = getattr(Hrac2PresneKolo, f'hraA{NakladyHrace2}'+"P")
        for y in Group.get_players():
            y.participant.vars["VyslednaZprava"].append(FinalniPreference)
        Hrac1.FinalniPreference = FinalniPreference
        Hrac2.FinalniPreference = FinalniPreference
        Hrac1.KteraHra = Kthra
        Hrac2.KteraHra =Kthra
        Hrac1.FinalniVolba = Hrac1Volba
        Hrac2.FinalniVolba = Hrac2Volba
        Hrac1.participant.vars["VyslednaZprava"].append(Hrac1.FinalniVolba)
        Hrac2.participant.vars["VyslednaZprava"].append(Hrac2.FinalniVolba)
        Hrac1.participant.vars["VyslednaZprava"].append(NakladyHrace1C)
        Hrac2.participant.vars["VyslednaZprava"].append(NakladyHrace2C)
        Hrac1.participant.vars["VyslednaZprava"].append(NakladyHrace2C)
        Hrac2.participant.vars["VyslednaZprava"].append(NakladyHrace1C)
        Hrac1.participant.vars["VyslednaZprava"].append(Hrac2.FinalniVolba)
        Hrac2.participant.vars["VyslednaZprava"].append(Hrac1.FinalniVolba)

        if Group.Treatment == "A":
            if FinalniPreference == "Levá":
                if Kthra == 1:
                    Group.PomocnaFunkce(Hrac1,Hrac2,Hrac1Volba,Hrac2Volba,NakladyHrace1C,NakladyHrace2C,230,330,130,230)
                if Kthra == 2:
                    Group.PomocnaFunkce(Hrac1, Hrac2, Hrac1Volba, Hrac2Volba, NakladyHrace1C, NakladyHrace2C, 290, 310, 110,
                                        290)
                if Kthra == 3:
                    Group.PomocnaFunkce(Hrac1,Hrac2,Hrac1Volba,Hrac2Volba,NakladyHrace1C,NakladyHrace2C,230,410,210,230)
                if Kthra == 4:
                    Group.PomocnaFunkce(Hrac1,Hrac2,Hrac1Volba,Hrac2Volba,NakladyHrace1C,NakladyHrace2C,290,390,190,290)
                if Kthra == 5:
                    Group.PomocnaFunkce(Hrac1,Hrac2,Hrac1Volba,Hrac2Volba,NakladyHrace1C,NakladyHrace2C,270,330,130,270)
            if FinalniPreference == "Pravá":
                if Kthra == 1:
                    Group.PomocnaFunkce(Hrac1,Hrac2,Hrac1Volba,Hrac2Volba,NakladyHrace1C,NakladyHrace2C,310,330,130,310)
                if Kthra == 2:
                    Group.PomocnaFunkce(Hrac1, Hrac2, Hrac1Volba, Hrac2Volba, NakladyHrace1C, NakladyHrace2C, 270, 370, 170,
                                        270)
                if Kthra == 3:
                    Group.PomocnaFunkce(Hrac1,Hrac2,Hrac1Volba,Hrac2Volba,NakladyHrace1C,NakladyHrace2C,250,350,150,250)
                if Kthra == 4:
                    Group.PomocnaFunkce(Hrac1,Hrac2,Hrac1Volba,Hrac2Volba,NakladyHrace1C,NakladyHrace2C,210,390,190,210)
                if Kthra == 5:
                    Group.PomocnaFunkce(Hrac1,Hrac2,Hrac1Volba,Hrac2Volba,NakladyHrace1C,NakladyHrace2C,230,370,170,230)

        if Group.Treatment == "B":
            if FinalniPreference == "Levá":
                if Kthra == 1:
                    Group.PomocnaFunkce(Hrac1,Hrac2,Hrac1Volba,Hrac2Volba,NakladyHrace1C,NakladyHrace2C,230,330,130,230)
                if Kthra == 2:
                    Group.PomocnaFunkce(Hrac1, Hrac2, Hrac1Volba, Hrac2Volba, NakladyHrace1C, NakladyHrace2C, 270, 290, 90,
                                        270)
                if Kthra == 3:
                    Group.PomocnaFunkce(Hrac1,Hrac2,Hrac1Volba,Hrac2Volba,NakladyHrace1C,NakladyHrace2C,250,350,150,250)
                if Kthra == 4:
                    Group.PomocnaFunkce(Hrac1,Hrac2,Hrac1Volba,Hrac2Volba,NakladyHrace1C,NakladyHrace2C,250,390,190,250)
                if Kthra == 5:
                    Group.PomocnaFunkce(Hrac1,Hrac2,Hrac1Volba,Hrac2Volba,NakladyHrace1C,NakladyHrace2C,290,350,150,290)
            if FinalniPreference == "Pravá":
                if Kthra == 1:
                    Group.PomocnaFunkce(Hrac1,Hrac2,Hrac1Volba,Hrac2Volba,NakladyHrace1C,NakladyHrace2C,290,310,110,290)
                if Kthra == 2:
                    Group.PomocnaFunkce(Hrac1, Hrac2, Hrac1Volba, Hrac2Volba, NakladyHrace1C, NakladyHrace2C, 270, 370, 170,
                                        270)
                if Kthra == 3:
                    Group.PomocnaFunkce(Hrac1,Hrac2,Hrac1Volba,Hrac2Volba,NakladyHrace1C,NakladyHrace2C,210,390,190,210)
                if Kthra == 4:
                    Group.PomocnaFunkce(Hrac1,Hrac2,Hrac1Volba,Hrac2Volba,NakladyHrace1C,NakladyHrace2C,250,310,110,250)
                if Kthra == 5:
                    Group.PomocnaFunkce(Hrac1,Hrac2,Hrac1Volba,Hrac2Volba,NakladyHrace1C,NakladyHrace2C,230,370,170,230)

        if Group.Treatment == "C":
            if FinalniPreference == "Levá":
                if Kthra == 1:
                    Group.PomocnaFunkce(Hrac1,Hrac2,Hrac1Volba,Hrac2Volba,NakladyHrace1C,NakladyHrace2C,250,350,150,250)
                if Kthra == 2:
                    Group.PomocnaFunkce(Hrac1, Hrac2, Hrac1Volba, Hrac2Volba, NakladyHrace1C, NakladyHrace2C, 230, 410, 210,
                                        230)
                if Kthra == 3:
                    Group.PomocnaFunkce(Hrac1,Hrac2,Hrac1Volba,Hrac2Volba,NakladyHrace1C,NakladyHrace2C,270,370,170,270)
                if Kthra == 4:
                    Group.PomocnaFunkce(Hrac1,Hrac2,Hrac1Volba,Hrac2Volba,NakladyHrace1C,NakladyHrace2C,270,330,130,270)
                if Kthra == 5:
                    Group.PomocnaFunkce(Hrac1,Hrac2,Hrac1Volba,Hrac2Volba,NakladyHrace1C,NakladyHrace2C,210,350,150,210)
            if FinalniPreference == "Pravá":
                if Kthra == 1:
                    Group.PomocnaFunkce(Hrac1,Hrac2,Hrac1Volba,Hrac2Volba,NakladyHrace1C,NakladyHrace2C,290,310,110,290)
                if Kthra == 2:
                    Group.PomocnaFunkce(Hrac1, Hrac2, Hrac1Volba, Hrac2Volba, NakladyHrace1C, NakladyHrace2C, 230, 330, 130,
                                        230)
                if Kthra == 3:
                    Group.PomocnaFunkce(Hrac1,Hrac2,Hrac1Volba,Hrac2Volba,NakladyHrace1C,NakladyHrace2C,210,390,190,210)
                if Kthra == 4:
                    Group.PomocnaFunkce(Hrac1,Hrac2,Hrac1Volba,Hrac2Volba,NakladyHrace1C,NakladyHrace2C,250,390,190,250)
                if Kthra == 5:
                    Group.PomocnaFunkce(Hrac1,Hrac2,Hrac1Volba,Hrac2Volba,NakladyHrace1C,NakladyHrace2C,290,350,150,290)

        if Group.Treatment == "AR":
            if FinalniPreference == "Pravá":
                if Kthra == 1:
                    Group.PomocnaFunkce(Hrac1,Hrac2,Hrac1Volba,Hrac2Volba,NakladyHrace1C,NakladyHrace2C,230,330,130,230)
                if Kthra == 2:
                    Group.PomocnaFunkce(Hrac1, Hrac2, Hrac1Volba, Hrac2Volba, NakladyHrace1C, NakladyHrace2C, 290, 310, 110,
                                        290)
                if Kthra == 3:
                    Group.PomocnaFunkce(Hrac1,Hrac2,Hrac1Volba,Hrac2Volba,NakladyHrace1C,NakladyHrace2C,230,410,210,230)
                if Kthra == 4:
                    Group.PomocnaFunkce(Hrac1,Hrac2,Hrac1Volba,Hrac2Volba,NakladyHrace1C,NakladyHrace2C,290,390,190,290)
                if Kthra == 5:
                    Group.PomocnaFunkce(Hrac1,Hrac2,Hrac1Volba,Hrac2Volba,NakladyHrace1C,NakladyHrace2C,270,330,130,270)
            if FinalniPreference == "Levá":
                if Kthra == 1:
                    Group.PomocnaFunkce(Hrac1,Hrac2,Hrac1Volba,Hrac2Volba,NakladyHrace1C,NakladyHrace2C,310,330,130,310)
                if Kthra == 2:
                    Group.PomocnaFunkce(Hrac1, Hrac2, Hrac1Volba, Hrac2Volba, NakladyHrace1C, NakladyHrace2C, 270, 370, 170,
                                        270)
                if Kthra == 3:
                    Group.PomocnaFunkce(Hrac1,Hrac2,Hrac1Volba,Hrac2Volba,NakladyHrace1C,NakladyHrace2C,250,350,150,250)
                if Kthra == 4:
                    Group.PomocnaFunkce(Hrac1,Hrac2,Hrac1Volba,Hrac2Volba,NakladyHrace1C,NakladyHrace2C,210,390,190,210)
                if Kthra == 5:
                    Group.PomocnaFunkce(Hrac1,Hrac2,Hrac1Volba,Hrac2Volba,NakladyHrace1C,NakladyHrace2C,230,370,170,230)

        if Group.Treatment == "BR":
            if FinalniPreference == "Pravá":
                if Kthra == 1:
                    Group.PomocnaFunkce(Hrac1,Hrac2,Hrac1Volba,Hrac2Volba,NakladyHrace1C,NakladyHrace2C,230,330,130,230)
                if Kthra == 2:
                    Group.PomocnaFunkce(Hrac1, Hrac2, Hrac1Volba, Hrac2Volba, NakladyHrace1C, NakladyHrace2C, 270, 290, 90,
                                        270)
                if Kthra == 3:
                    Group.PomocnaFunkce(Hrac1,Hrac2,Hrac1Volba,Hrac2Volba,NakladyHrace1C,NakladyHrace2C,250,350,150,250)
                if Kthra == 4:
                    Group.PomocnaFunkce(Hrac1,Hrac2,Hrac1Volba,Hrac2Volba,NakladyHrace1C,NakladyHrace2C,250,390,190,250)
                if Kthra == 5:
                    Group.PomocnaFunkce(Hrac1,Hrac2,Hrac1Volba,Hrac2Volba,NakladyHrace1C,NakladyHrace2C,290,350,150,290)
            if FinalniPreference == "Levá":
                if Kthra == 1:
                    Group.PomocnaFunkce(Hrac1,Hrac2,Hrac1Volba,Hrac2Volba,NakladyHrace1C,NakladyHrace2C,290,310,110,290)
                if Kthra == 2:
                    Group.PomocnaFunkce(Hrac1, Hrac2, Hrac1Volba, Hrac2Volba, NakladyHrace1C, NakladyHrace2C, 270, 370, 170,
                                        270)
                if Kthra == 3:
                    Group.PomocnaFunkce(Hrac1,Hrac2,Hrac1Volba,Hrac2Volba,NakladyHrace1C,NakladyHrace2C,210,390,190,210)
                if Kthra == 4:
                    Group.PomocnaFunkce(Hrac1,Hrac2,Hrac1Volba,Hrac2Volba,NakladyHrace1C,NakladyHrace2C,250,310,110,250)
                if Kthra == 5:
                    Group.PomocnaFunkce(Hrac1,Hrac2,Hrac1Volba,Hrac2Volba,NakladyHrace1C,NakladyHrace2C,230,370,170,230)

        if Group.Treatment == "CR":
            if FinalniPreference == "Pravá":
                if Kthra == 1:
                    Group.PomocnaFunkce(Hrac1,Hrac2,Hrac1Volba,Hrac2Volba,NakladyHrace1C,NakladyHrace2C,250,350,150,250)
                if Kthra == 2:
                    Group.PomocnaFunkce(Hrac1, Hrac2, Hrac1Volba, Hrac2Volba, NakladyHrace1C, NakladyHrace2C, 230, 410, 210,
                                        230)
                if Kthra == 3:
                    Group.PomocnaFunkce(Hrac1,Hrac2,Hrac1Volba,Hrac2Volba,NakladyHrace1C,NakladyHrace2C,270,370,170,270)
                if Kthra == 4:
                    Group.PomocnaFunkce(Hrac1,Hrac2,Hrac1Volba,Hrac2Volba,NakladyHrace1C,NakladyHrace2C,270,330,130,270)
                if Kthra == 5:
                    Group.PomocnaFunkce(Hrac1,Hrac2,Hrac1Volba,Hrac2Volba,NakladyHrace1C,NakladyHrace2C,210,350,150,210)
            if FinalniPreference == "Levá":
                if Kthra == 1:
                    Group.PomocnaFunkce(Hrac1,Hrac2,Hrac1Volba,Hrac2Volba,NakladyHrace1C,NakladyHrace2C,290,310,110,290)
                if Kthra == 2:
                    Group.PomocnaFunkce(Hrac1, Hrac2, Hrac1Volba, Hrac2Volba, NakladyHrace1C, NakladyHrace2C, 230, 330, 130,
                                        230)
                if Kthra == 3:
                    Group.PomocnaFunkce(Hrac1,Hrac2,Hrac1Volba,Hrac2Volba,NakladyHrace1C,NakladyHrace2C,210,390,190,210)
                if Kthra == 4:
                    Group.PomocnaFunkce(Hrac1,Hrac2,Hrac1Volba,Hrac2Volba,NakladyHrace1C,NakladyHrace2C,250,390,190,250)
                if Kthra == 5:
                    Group.PomocnaFunkce(Hrac1,Hrac2,Hrac1Volba,Hrac2Volba,NakladyHrace1C,NakladyHrace2C,290,350,150,290)




    def PomocnaFunkce(Group,Hrac1,Hrac2,Hrac1Volba,Hrac2Volba,Hrac1Naklady,Hrac2Naklady,LevaHorni,PravaHorni,LevaDolni,PravaDolni):
        if Hrac1Volba == "A" and Hrac2Volba == "A":
            Hrac1.Vyhra = LevaHorni - Hrac1Naklady
            Hrac2.Vyhra = LevaHorni - Hrac2Naklady
        if Hrac1Volba == "A" and Hrac2Volba == "B":
            Hrac1.Vyhra = PravaHorni - Hrac1Naklady
            Hrac2.Vyhra = LevaDolni
        if Hrac1Volba == "B" and Hrac2Volba == "A":
            Hrac1.Vyhra = LevaDolni
            Hrac2.Vyhra = PravaHorni - Hrac2Naklady
        if Hrac1Volba == "B" and Hrac2Volba == "B":
            Hrac1.Vyhra = PravaDolni
            Hrac2.Vyhra = PravaDolni
        Hrac1.participant.vars["VyslednaZprava"].append(Hrac1.Vyhra)
        Hrac2.participant.vars["VyslednaZprava"].append(Hrac2.Vyhra)
        Hrac1.payoff = cu(Hrac1.Vyhra)
        Hrac2.payoff = cu(Hrac2.Vyhra)


class Player(BasePlayer):
    hraA1P = models.StringField(label="",
                               choices=["A", "B"],
                               widget=widgets.RadioSelect)
    hraA2P = models.StringField(label="",
                                choices=["A", "B"],
                                widget=widgets.RadioSelect)
    hraA3P = models.StringField(label="",
                                choices=["A", "B"],
                                widget=widgets.RadioSelect)
    hraA4P = models.StringField(label="",
                                choices=["A", "B"],
                                widget=widgets.RadioSelect)
    hraA5P = models.StringField(label="",
                                choices=["A", "B"],
                                widget=widgets.RadioSelect)
    hraA6P = models.StringField(label="",
                                choices=["A", "B"],
                                widget=widgets.RadioSelect)
    hraA7P = models.StringField(label="",
                                choices=["A", "B"],
                                widget=widgets.RadioSelect)
    hraA8P = models.StringField(label="",
                                choices=["A", "B"],
                                widget=widgets.RadioSelect)
    hraA9P = models.StringField(label="",
                                choices=["A", "B"],
                                widget=widgets.RadioSelect)
    hraA10P = models.StringField(label="",
                                choices=["A", "B"],
                                widget=widgets.RadioSelect)

    hraA1L = models.StringField(label="",
                                choices=["A", "B"],
                                widget=widgets.RadioSelect)
    hraA2L = models.StringField(label="",
                                choices=["A", "B"],
                                widget=widgets.RadioSelect)
    hraA3L = models.StringField(label="",
                                choices=["A", "B"],
                                widget=widgets.RadioSelect)
    hraA4L = models.StringField(label="",
                                choices=["A", "B"],
                                widget=widgets.RadioSelect)
    hraA5L = models.StringField(label="",
                                choices=["A", "B"],
                                widget=widgets.RadioSelect)
    hraA6L = models.StringField(label="",
                                choices=["A", "B"],
                                widget=widgets.RadioSelect)
    hraA7L = models.StringField(label="",
                                choices=["A", "B"],
                                widget=widgets.RadioSelect)
    hraA8L = models.StringField(label="",
                                choices=["A", "B"],
                                widget=widgets.RadioSelect)
    hraA9L = models.StringField(label="",
                                choices=["A", "B"],
                                widget=widgets.RadioSelect)
    hraA10L = models.StringField(label="",
                                 choices=["A", "B"],
                                 widget=widgets.RadioSelect)
    PreferenceA = models.StringField(label="",choices=["Levá","Pravá"],
                                    widget=widgets.RadioSelectHorizontal)

    CoSePlati = models.IntegerField()
    DruhVyplaty = models.StringField()
    Vyhra = models.IntegerField()
    KteraHra = models.IntegerField()
    FinalniVolba = models.StringField()
    FinalniPreference = models.StringField()

    def TabulkaVypln(Player,Lhorni,LhorniS,Phorni,PhorniS,Ldolni,LdolniS,Pdolni,PdolniS):
        vysledek = []
        for x in C.c:
            levahorni = Lhorni-int(x)
            pravahorni = Phorni-int(x)
            levahorniSouper = LhorniS
            pravaholniSouper = PhorniS
            levadolni = Ldolni
            levadolniSouper = LdolniS
            pravadolni = Pdolni
            pravadolniSouper = PdolniS
            vysledek.append([x,levahorni,levahorniSouper, pravahorni,pravaholniSouper,levadolni,levadolniSouper,pravadolni,pravadolniSouper,Lhorni])
        return vysledek
# PAGES
class Info(Page):
    def is_displayed(player: Player):
        return player.round_number == 1


class Tabulka1(Page):
    form_model = Player
    form_fields = ["hraA1P", "hraA2P", "hraA3P", "hraA4P", "hraA5P", "hraA6P", "hraA7P", "hraA8P", "hraA9P", "hraA10P",
                   "hraA1L", "hraA2L", "hraA3L", "hraA4L", "hraA5L", "hraA6L", "hraA7L", "hraA8L", "hraA9L", "hraA10L",
                   "PreferenceA"]


    def vars_for_template(player: Player):
        if player.round_number == 1:
            if player.group.Treatment == "A":
                h = player.TabulkaVypln(230, 230, 330, 130, 130, 330, 230, 230)
                k = player.TabulkaVypln(310, 310, 330, 130, 130, 330, 310, 310)
            if player.group.Treatment == "B":
                h = player.TabulkaVypln(250, 250, 350, 150, 150, 350, 250, 250)
                k = player.TabulkaVypln(210, 210, 390, 190, 190, 390, 210, 210)

            if player.group.Treatment == "C":
                h = player.TabulkaVypln(210, 210, 350, 150, 150, 350, 210, 210)
                k = player.TabulkaVypln(290, 290, 350, 150, 150, 350, 290, 290)

            if player.group.Treatment == "AR":
                h = player.TabulkaVypln(310, 310, 330, 130, 130, 330, 310, 310)
                k = player.TabulkaVypln(230, 230, 330, 130, 130, 330, 230, 230)
            if player.group.Treatment == "BR":
                k = player.TabulkaVypln(250, 250, 350, 150, 150, 350, 250, 250)
                h = player.TabulkaVypln(210, 210, 390, 190, 190, 390, 210, 210)

            if player.group.Treatment == "CR":
                k = player.TabulkaVypln(210, 210, 350, 150, 150, 350, 210, 210)
                h = player.TabulkaVypln(290, 290, 350, 150, 150, 350, 290, 290)

        if player.round_number == 2:
            if player.group.Treatment == "A":
                h = player.TabulkaVypln(290, 290, 310, 110, 110, 310, 290, 290)
                k = player.TabulkaVypln(270, 270, 370, 170, 170, 370, 270, 270)
            if player.group.Treatment == "B":
                h = player.TabulkaVypln(290, 290, 350, 150, 150, 350, 290, 290)
                k = player.TabulkaVypln(230, 230, 370, 170, 170, 370, 230, 230)

            if player.group.Treatment == "C":
                h = player.TabulkaVypln(270, 270, 330, 130, 130, 330, 270, 270)
                k = player.TabulkaVypln(250, 250, 390, 190, 190, 390, 250, 250)

            if player.group.Treatment == "AR":
                h = player.TabulkaVypln(270, 270, 370, 170, 170, 370, 270, 270)
                k = player.TabulkaVypln(290, 290, 310, 110, 110, 310, 290, 290)
            if player.group.Treatment == "BR":
                k = player.TabulkaVypln(290, 290, 350, 150, 150, 350, 290, 290)
                h = player.TabulkaVypln(230, 230, 370, 170, 170, 370, 230, 230)

            if player.group.Treatment == "CR":
                k = player.TabulkaVypln(270, 270, 330, 130, 130, 330, 270, 270)
                h = player.TabulkaVypln(250, 250, 390, 190, 190, 390, 250, 250)


        if player.round_number == 3:
            if player.group.Treatment == "A":
                h = player.TabulkaVypln(230, 230, 410, 210, 210, 410, 230, 230)
                k = player.TabulkaVypln(250, 250, 350, 150, 150, 350, 250, 250)
            if player.group.Treatment == "B":
                h = player.TabulkaVypln(230, 230, 330, 130, 130, 330, 230, 230)
                k = player.TabulkaVypln(290, 290, 310, 110, 110, 310, 290, 290)

            if player.group.Treatment == "C":
                h = player.TabulkaVypln(270, 270, 370, 170, 170, 370, 270, 270)
                k = player.TabulkaVypln(210, 210, 390, 190, 190, 390, 210, 210)
            if player.group.Treatment == "AR":
                h = player.TabulkaVypln(250, 250, 350, 150, 150, 350, 250, 250)
                k = player.TabulkaVypln(230, 230, 410, 210, 210, 410, 230, 230)
            if player.group.Treatment == "BR":
                k = player.TabulkaVypln(230, 230, 330, 130, 130, 330, 230, 230)
                h = player.TabulkaVypln(290, 290, 310, 110, 110, 310, 290, 290)

            if player.group.Treatment == "CR":
                k = player.TabulkaVypln(270, 270, 370, 170, 170, 370, 270, 270)
                h = player.TabulkaVypln(210, 210, 390, 190, 190, 390, 210, 210)

        if player.round_number == 4:
            if player.group.Treatment == "A":
                h = player.TabulkaVypln(290, 290, 390, 190, 190, 390, 290, 290)
                k = player.TabulkaVypln(210, 210, 390, 190, 190, 390, 210, 210)
            if player.group.Treatment == "B":
                h = player.TabulkaVypln(250, 250, 390, 190, 190, 390, 250, 250)
                k = player.TabulkaVypln(250, 250, 310, 110, 110, 310, 250, 250)
            if player.group.Treatment == "C":
                h = player.TabulkaVypln(230, 230, 410, 210, 210, 410, 230, 230)
                k = player.TabulkaVypln(230, 230, 330, 130, 130, 330, 230, 230)

            if player.group.Treatment == "AR":
                k = player.TabulkaVypln(290, 290, 390, 190, 190, 390, 290, 290)
                h = player.TabulkaVypln(210, 210, 390, 190, 190, 390, 210, 210)
            if player.group.Treatment == "BR":
                k = player.TabulkaVypln(250, 250, 390, 190, 190, 390, 250, 250)
                h = player.TabulkaVypln(250, 250, 310, 110, 110, 310, 250, 250)
            if player.group.Treatment == "CR":
                k = player.TabulkaVypln(230, 230, 410, 210, 210, 410, 230, 230)
                h = player.TabulkaVypln(230, 230, 330, 130, 130, 330, 230, 230)


        if player.round_number == 5:
            if player.group.Treatment == "A":
                h = player.TabulkaVypln(270, 270, 330, 130, 130, 330, 270, 270)
                k = player.TabulkaVypln(230, 230, 370, 170, 170, 370, 230, 230)
            if player.group.Treatment == "B":
                h = player.TabulkaVypln(270, 270, 290, 90, 90, 290, 270, 270)
                k = player.TabulkaVypln(270, 270, 370, 170, 170, 370, 270, 270)

            if player.group.Treatment == "C":
                h = player.TabulkaVypln(250, 250, 350, 150, 150, 350, 250, 250)
                k = player.TabulkaVypln(290, 290, 310, 110, 110, 310, 290, 290)

            if player.group.Treatment == "AR":
                k = player.TabulkaVypln(270, 270, 330, 130, 130, 330, 270, 270)
                h = player.TabulkaVypln(230, 230, 370, 170, 170, 370, 230, 230)
            if player.group.Treatment == "BR":
                k = player.TabulkaVypln(270, 270, 290, 90, 90, 290, 270, 270)
                h = player.TabulkaVypln(270, 270, 370, 170, 170, 370, 270, 270)

            if player.group.Treatment == "CR":
                k = player.TabulkaVypln(250, 250, 350, 150, 150, 350, 250, 250)
                h = player.TabulkaVypln(290, 290, 310, 110, 110, 310, 290, 290)


        return dict(
            c=h,
            k=k,
            Kolo=player.round_number

        )


class ResultsWaitPage(WaitPage):
    def is_displayed(player: Player):
        return player.round_number == 5

    def after_all_players_arrive(group: Group):
        group.PaymentFunctionGroup()


#Seznam tabulek:
#LH: player.TabulkaVypln(290, 290, 310, 110, 110, 310, 290, 290)
#LH+20: player.TabulkaVypln(310, 310, 330, 130, 130, 330, 310, 310)
#LH-20: player.TabulkaVypln(270, 270, 290, 90, 90, 290, 270, 270)

#HL: player.TabulkaVypln(210, 210, 390, 190, 190, 390, 210, 210)
#HL+20: player.TabulkaVypln(230, 230, 410, 210, 210, 410, 230, 230)
#HL-20: player.TabulkaVypln(190, 190, 370, 170, 170, 370, 190, 190)

#MM: player.TabulkaVypln(250, 250, 350, 150, 150, 350, 250, 250)
#MM+20: player.TabulkaVypln(270, 270, 370, 170, 170, 370, 270, 270)
#MM-20: player.TabulkaVypln(230, 230, 330, 130, 130, 330, 230, 230)
#MM+40: player.TabulkaVypln(290, 290, 390, 190, 190, 390, 290, 290)

#LH´: player.TabulkaVypln(270, 270, 330, 130, 130, 330, 270, 270)
#LH´+20: player.TabulkaVypln(290, 290, 350, 150, 150, 350, 290, 290)
#LH´-20: player.TabulkaVypln(250, 250, 310, 110, 110, 310, 250, 250)

#HL´: player.TabulkaVypln(230, 230, 370, 170, 170, 370, 230, 230)
#HL´+20: player.TabulkaVypln(250, 250, 390, 190, 190, 390, 250, 250)
#HL´-20: player.TabulkaVypln(210, 210, 350, 150, 150, 350, 210, 210)

class MixerWaitPage2(WaitPage):
    wait_for_all_groups = True

    @staticmethod
    def after_all_players_arrive(subsession):
        subsession.MixerSkupin()



page_sequence = [MixerWaitPage2, Info,Tabulka1,ResultsWaitPage]
