from otree.api import *


doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'informace'
    PLAYERS_PER_GROUP = 3
    NUM_ROUNDS = 5
    A_ROLE = "A"
    B_ROLE = "B"
    C_ROLE = "C"
    roles = ["A","B","C"]
    Treatmenty=["1","2"] # ["1","2"]

class Subsession(BaseSubsession):
    def Mixing(subssesion):
        from random import shuffle
        skupiny = subssesion.get_group_matrix()
        PrvniTreatment = []
        DruhyTreatment = []
        Promenna = 1
        group_iterator = iter(C.Treatmenty)
        for x in subssesion.get_groups():
            try:
                x.Treatment = next(group_iterator)
            except StopIteration:
                group_iterator = iter(C.Treatmenty)
                x.Treatment = next(group_iterator)
        if subssesion.round_number == 1:
            for hrac in subssesion.get_players():
                hrac.participant.vars["Pamatovak"] = hrac.group.Treatment
        if len(C.Treatmenty) == 2:
            for x in subssesion.get_group_matrix():
                if Promenna % 2 == 1:
                    PrvniTreatment.append(x)
                else:
                    DruhyTreatment.append(x)
                Promenna += 1
        Prvnihraci = []
        Druzihraci = []
        Tretihraci = []
        for x in PrvniTreatment:
            Prvnihraci.append(x[0])
            Druzihraci.append(x[1])
            Tretihraci.append(x[2])
        PrvnihraciB = []
        DruzihraciB = []
        TretihraciB = []
        for y in DruhyTreatment:
            PrvnihraciB.append(y[0])
            DruzihraciB.append(y[1])
            TretihraciB.append(y[2])
        shuffle(Prvnihraci)
        shuffle(Druzihraci)
        shuffle(Tretihraci)
        shuffle(PrvnihraciB)
        shuffle(DruzihraciB)
        shuffle(TretihraciB)
        Finalni_skupina = []
        PomocnaPromenna = 0
        for hrac in PrvniTreatment:
            skupinaA = [Prvnihraci[PomocnaPromenna],Druzihraci[PomocnaPromenna],Tretihraci[PomocnaPromenna]]
            skupinaB = [PrvnihraciB[PomocnaPromenna],DruzihraciB[PomocnaPromenna],TretihraciB[PomocnaPromenna]]
            PomocnaPromenna += 1
            Finalni_skupina.append(skupinaA)
            Finalni_skupina.append(skupinaB)
        subssesion.set_group_matrix(Finalni_skupina)
        for hrac2 in subssesion.get_players():
            hrac2.group.Treatment = hrac2.participant.vars.get("Pamatovak")







class Group(BaseGroup):
    Treatment = models.StringField()
    B_sentHelp = models.FloatField()
    B_messageHelp = models.FloatField()
    C_messageHelp = models.FloatField()
    A_sentHelp = models.FloatField()

    def PaymentFunction(Group):
        from random import randint
        for n in Group.get_players():
            Kolo = randint(1, 5)
            n = n.in_round(Kolo)
            n.participant.vars["VyslednaZpravaInf"]=[]

            n.participant.vars["VyslednaZpravaInf"].append(Kolo)
            n.participant.vars["VyslednaZpravaInf"].append(n.role)

            if n.role == C.A_ROLE:
                n.participant.vars["VyslednaZpravaInf"].append(n.A_sent)
                n.participant.vars["VyslednaZpravaInf"].append(Group.B_sentHelp)

                x = (3 * n.A_sent) * (Group.B_sentHelp/100)
                n.payoff = x + (100 - n.A_sent)
                n.participant.vars["VyslednaZpravaInf"].append(int(n.payoff))
            if n.role == C.B_ROLE:
                if Group.A_sentHelp == 0:
                    n.payoff = 0
                else:
                    n.payoff = (3 * Group.A_sentHelp) * (1 - n.B_sent/100)
                n.participant.vars["VyslednaZpravaInf"].append(Group.A_sentHelp)
                n.participant.vars["VyslednaZpravaInf"].append(n.B_sent)
                n.participant.vars["VyslednaZpravaInf"].append(int(n.payoff))
            if n.role == C.C_ROLE:
                if Group.Treatment == "1" or Group.Treatment == "3":
                    n.payoff = 50
                if Group.Treatment == "2" or Group.Treatment == "4":
                    n.payoff = 100 - Group.A_sentHelp
                n.participant.vars["VyslednaZpravaInf"].append(Group.A_sentHelp)
                n.participant.vars["VyslednaZpravaInf"].append(Group.B_sentHelp)
                n.participant.vars["VyslednaZpravaInf"].append(int(n.payoff))
    def TestFunction(Group):
        for x in Group.get_players():
            x.group.Treatment = "1"


class Player(BasePlayer):
    B_sent = models.FloatField(label="Závazně prosím zvolte, kolik procent Kč přijatých od hráče A pošlete zpět:",
                               min=0,
                               max=100)
    B_message = models.FloatField(label="Nyní pošlete hráči A zprávu, kolik procent mu ze získané částky pošlete zpět",
                                  min=0,
                                  max=100)
    C_message = models.FloatField(min=0,
                                  max=100,
                                  label="Pošlete prosím hráči A zprávu o tom, kolik procent ze získané částky hráč B pošle zpět hráči A")
    A_sent = models.FloatField(label="Zvolte prosím, kolik Kč chcete poslat hráči B:",
                               min=0,
                               max=100)
    Test1 = models.IntegerField(label="Hráč A posílá hráči B 15 Kč. Kolik jich hráči B přijde po ztrojnásobení?")
    Test2A = models.IntegerField(label="Hráč A má na začátku 100 Kč a posílá hráči B 50 Kč, ty se ztrojnásobí, hráč B se rozhodne vrátit 50 % získané částky. Kolik bude mít hráč A na konci hry Kč?")
    Test2B = models.IntegerField(label="Kolik v předchozí situaci zůstane hráči B?"
    )
    Test3A = models.IntegerField(label="Hráč A má na začátku 100 Kč a posílá hráči B 20 Kč, ty se ztrojnásobí, hráč B se rozhodne vrátit 0 % získané částky. Kolik bude mít hráč A na konci hry Kč?")
    Test3B = models.IntegerField(label="Kolik v předchozí situaci zůstane hráči B?")
    Test4A = models.IntegerField(label="Hráč A posílá hráči B 30 Kč, ty se ztrojnásobí, hráč B se rozhodne vrátit 20 % získané částky. Kolik bude mít hráč C na konci hry Kč?")
    Test4B = models.IntegerField(label="Hráč A posílá hráči B 30 Kč, ty se ztrojnásobí, hráč B se rozhodne vrátit 20 % získané částky. Kolik bude mít hráč C na konci hry Kč?")
    Test5A = models.IntegerField(label="Hráč A posílá hráči B 60 Kč, ty se ztrojnásobí, hráč B se rozhodne vrátit 50 % získané částky. Kolik bude mít hráč C na konci hry Kč?")
    Test5B = models.IntegerField(label="Hráč A posílá hráči B 60 Kč, ty se ztrojnásobí, hráč B se rozhodne vrátit 50 % získané částky. Kolik bude mít hráč C na konci hry Kč?")
    Test6A = models.StringField(label="Hráč C vidí, kolik procent získané částky se hráč B rozhodl poslat zpět.",
        choices=["Pravda","Nepravda"],
        widget=widgets.RadioSelectHorizontal
    )
    Test6B = models.StringField(label="Hráč C vidí, kolik procent získané částky se hráč B rozhodl poslat zpět.",
        choices=["Pravda","Nepravda"],
        widget=widgets.RadioSelectHorizontal
    )
    Test7 = models.StringField(label="Hráč A vidí, kolik procent získané částky se hráč B rozhodl poslat zpět. ",
        choices=["Pravda","Nepravda"],
        widget=widgets.RadioSelectHorizontal
    )
    Pohlavi = models.StringField(label="Jaké je Vaše pohlaví?",
                               choices=["Muž", "Žena","Jiné"],
                               widget=widgets.RadioSelectHorizontal
                               )
    Vek = models.IntegerField(label="Jaký je váš věk?",
                                 min=1,
                                max=99,

                                 )
    Studium = models.StringField(label="Na jaké fakultě studujete?",
                                 choices=["Ekonomicko-správní","Jiná"],
                                 widget=widgets.RadioSelectHorizontal
                                 )

def Test1_error_message(player, value):
    if value != 45:
        return "Nikoli, správná odpověď je 45"

def Test2A_error_message(player, value):
    if value != 125:
        return "Nikoli, správná odpověď je 125"

def Test2B_error_message(player, value):
    if value != 75:
        return "Nikoli, správná odpověď je 75"

def Test3A_error_message(player, value):
    if value != 80:
        return "Nikoli, správná odpověď je 80"

def Test3B_error_message(player, value):
    if value != 60:
        return "Nikoli, správná odpověď je 60"

def Test4A_error_message(player, value):
    if value != 50:
        return "Nikoli, správná odpověď je 50"

def Test4B_error_message(player, value):
    if value != 70:
        return "Nikoli, správná odpověď je 70"

def Test5A_error_message(player, value):
    if value != 50:
        return "Nikoli, správná odpověď je 50"

def Test5B_error_message(player, value):
    if value != 40:
        return "Nikoli, správná odpověď je 40"

def Test6A_error_message(player, value):
    if value != "Pravda":
        return "Nikoli, správná odpověď je Pravda"

def Test6B_error_message(player, value):
    if value != "Nepravda":
        return "Nikoli, správná odpověď je Nepravda"

def Test7_error_message(player, value):
    if value != "Nepravda":
        return "Nikoli, správná odpověď je Nepravda"




# PAGES
class MixPage(WaitPage):
    wait_for_all_groups = True
    @staticmethod
    def after_all_players_arrive(subsession):
        subsession.Mixing()





class Info1(Page):
    def is_displayed(player: Player):
        return player.round_number == 1



class Info1Sk1(Page):
    def vars_for_template(player: Player):
        return dict(
            Treatment=player.group.Treatment
        )

    def is_displayed(player: Player):
        return player.round_number == 1


class WaitPage2(WaitPage):
    wait_for_all_groups = True
    def is_displayed(player: Player):
        return player.round_number == 1


class WaitPage3(WaitPage):
    pass


class Experiment1(Page):
    form_model = Player
    form_fields = ["B_sent"]


    def is_displayed(player: Player):
        return player.role == C.B_ROLE

    def before_next_page(player: Player, timeout_happened):
        player.group.B_sentHelp = player.B_sent

    def vars_for_template(player: Player):
        return dict(
            Treatment=player.group.Treatment,
            Kolo=player.round_number
        )


class Experiment2(Page):
    form_model = Player
    form_fields = ["B_message"]


    def vars_for_template(player: Player):
        return dict(
            role=player.role,
            Treatment=player.group.Treatment,
            B_sent=round(player.group.B_sentHelp),
            Kolo=player.round_number
        )

    def is_displayed(player: Player):
        return player.role == C.B_ROLE

    def before_next_page(player: Player, timeout_happened):
        player.group.B_messageHelp = player.B_message

class Experiment2C(Page):
    form_model = Player
    form_fields = ["C_message"]

    def is_displayed(player: Player):
        return player.role == C.C_ROLE

    def vars_for_template(player: Player):
        return dict(
            role=player.role,
            Treatment=player.group.Treatment,
            B_sent=round(player.group.B_sentHelp),
            Kolo=player.round_number
        )

    def before_next_page(player: Player, timeout_happened):
        player.group.C_messageHelp = player.C_message


class Experiment3(Page):
    form_model = Player
    form_fields = ["A_sent"]

    def vars_for_template(player: Player):
        return dict(
            B_message=round(3 * player.group.B_messageHelp),
            C_message=round(3 * player.group.C_messageHelp),
            Treatment=player.group.Treatment,
            Kolo=player.round_number
        )

    def is_displayed(player: Player):
        return player.role == C.A_ROLE

    def before_next_page(player: Player, timeout_happened):
        player.group.A_sentHelp = player.A_sent


class FinalWaitPage(WaitPage):
    def after_all_players_arrive(group: Group):
        group.PaymentFunction()

    def is_displayed(player: Player):
        return player.round_number == 5


class Results(Page):
    def is_displayed(player: Player):
        return player.round_number == 5

    def vars_for_template(player: Player):
        return dict(
            Kolo=player.participant.vars.get("VyslednaZpravaInf")[0],
            B=round(player.participant.vars.get("VyslednaZpravaInf")[3]),
            A=round(player.participant.vars.get("VyslednaZpravaInf")[2]),
            Vyhra=player.participant.vars.get("VyslednaZpravaInf")[4],
        )


class TestPage(Page):
    form_model = Player
    form_fields = ["Test1","Test2A","Test2B","Test3A","Test3B","Test4A","Test5A","Test6A","Test7"]

    def is_displayed(player: Player):
        return player.group.Treatment == "1" and player.round_number == 1


class TestPageB(Page):
    form_model = Player
    form_fields = ["Test1","Test2A","Test2B","Test3A","Test3B","Test4B","Test5B","Test6A","Test7"]

    def is_displayed(player: Player):
        return player.group.Treatment == "2" and player.round_number == 1

class TestPageC(Page):
    form_model = Player
    form_fields = ["Test1","Test2A","Test2B","Test3A","Test3B","Test4A","Test5A","Test6B","Test7"]

    def is_displayed(player: Player):
        return player.group.Treatment == "3" and player.round_number == 1

class TestPageD(Page):
    form_model = Player
    form_fields = ["Test1","Test2A","Test2B","Test3A","Test3B","Test4B","Test5B","Test6B","Test7"]

    def is_displayed(player: Player):
        return player.group.Treatment == "4" and player.round_number == 1


class PosledniDotaznik(Page):
    def is_displayed(player: Player):
        return player.round_number == 5

    form_model = Player
    form_fields = ["Pohlavi","Vek","Studium"]

class Results1(Page):
    def is_displayed(player: Player):
        return player.round_number == 5

    def vars_for_template(player: Player):
        if player.participant.vars.get("Pojistka") == "1":
            x = player.participant.vars.get("MojeVyhry")[(player.participant.vars.get("VyslednaZprava")[1])-1]
        else:
            x = player.participant.vars.get("MojeVyhry")[1]
        return dict(
            PrvniVeta=player.participant.vars.get("VyslednaZprava")[0],
            Typhry=player.participant.vars.get("VyslednaZprava")[1],
            naklad=x[0],
            mojevolba=x[1],
            soupervolba=x[2],
            vyhra=x[3],
            soupernaklad=x[5],
            Pref=player.participant.vars.get("VyslednaZprava")[2],
            FinVolba=player.participant.vars.get("VyslednaZprava")[3],
            Naklady=player.participant.vars.get("VyslednaZprava")[4],
            NakladySouper=player.participant.vars.get("VyslednaZprava")[5],
            SouperVolba=player.participant.vars.get("VyslednaZprava")[6],
            Vyhra=player.participant.vars.get("VyslednaZprava")[7],
            CoSePlati=player.participant.vars.get("CoSePlati")

        )

class LastPage(Page):
    def is_displayed(player: Player):
        return player.round_number == 5



page_sequence = [MixPage,Info1, Info1Sk1, WaitPage2,TestPage,TestPageB, TestPageC, TestPageD, WaitPage2, Experiment1, WaitPage3,Experiment2,
                 Experiment2C, WaitPage3,Experiment3, FinalWaitPage, Results1,
                 Results,PosledniDotaznik,LastPage]

