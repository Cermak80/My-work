from otree.api import *
import random
from datetime import datetime, timedelta
doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'timepreferences'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
    tabulka1 = ["q1", "q2", "q3", "q4", "q5", "q6"]
    now = datetime.now()
    week_later = now + timedelta(days=7)
    fourweekslater = now + timedelta(days=28)
    twoweeks = now + timedelta(days=14)
    fiveweeks = now + timedelta(days=35)
    threeweeks = now + timedelta(days=21)
    sixweeks = now + timedelta(days=42)

    this_week = now.strftime("%d. %m.")
    next_week = week_later.strftime("%d. %m.")
    four_weeks = fourweekslater.strftime("%d. %m.")
    two_weeks = twoweeks.strftime("%d. %m.")
    five_weeks = fiveweeks.strftime("%d. %m.")
    three_weeks = threeweeks.strftime("%d. %m.")
    six_weeks = sixweeks.strftime("%d. %m.")



class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    #Tabulka1
    q1 = models.IntegerField(widget=widgets.RadioSelectHorizontal,
                             choices=[154, 138])
    q2 = models.IntegerField(widget=widgets.RadioSelectHorizontal,
                             choices=[154, 154])
    q3 = models.IntegerField(widget=widgets.RadioSelectHorizontal,
                             choices=[154, 157])
    q4 = models.IntegerField(widget=widgets.RadioSelectHorizontal,
                             choices=[154, 164])
    q5 = models.IntegerField(widget=widgets.RadioSelectHorizontal,
                             choices=[154, 169])
    q6 = models.IntegerField(widget=widgets.RadioSelectHorizontal,
                             choices=[154, 184])
    q7 = models.IntegerField(widget=widgets.RadioSelectHorizontal,
                             choices=[154, 101])
    q8 = models.IntegerField(widget=widgets.RadioSelectHorizontal,
                             choices=[154, 154])
    q9 = models.IntegerField(widget=widgets.RadioSelectHorizontal,
                             choices=[154, 167])
    q10 = models.IntegerField(widget=widgets.RadioSelectHorizontal,
                             choices=[154, 202])
    q11 = models.IntegerField(widget=widgets.RadioSelectHorizontal,
                             choices=[154, 225])
    q12 = models.IntegerField(widget=widgets.RadioSelectHorizontal,
                             choices=[154, 319])
    q13 = models.IntegerField(widget=widgets.RadioSelectHorizontal,
                           choices=[154, 319])
    q14 = models.IntegerField(widget=widgets.RadioSelectHorizontal,
                              choices=[154, 319])
    q15 = models.IntegerField(widget=widgets.RadioSelectHorizontal,
                              choices=[154, 319])
    q16 = models.IntegerField(widget=widgets.RadioSelectHorizontal,
                              choices=[154, 319])
    q17 = models.IntegerField(widget=widgets.RadioSelectHorizontal,
                              choices=[154, 319])
    q18 = models.IntegerField(widget=widgets.RadioSelectHorizontal,
                              choices=[154, 319])
    q19 = models.IntegerField(widget=widgets.RadioSelectHorizontal,
                              choices=[154, 319])
    q20 = models.IntegerField(widget=widgets.RadioSelectHorizontal,
                              choices=[154, 319])
    q21 = models.IntegerField(widget=widgets.RadioSelectHorizontal,
                              choices=[154, 319])
    q22 = models.IntegerField(widget=widgets.RadioSelectHorizontal,
                              choices=[154, 319])
    q23 = models.IntegerField(widget=widgets.RadioSelectHorizontal,
                              choices=[154, 319])
    q24 = models.IntegerField(widget=widgets.RadioSelectHorizontal,
                              choices=[154, 319])
    q25 = models.IntegerField(widget=widgets.RadioSelectHorizontal,
                              choices=[154, 319])
    q26 = models.IntegerField(widget=widgets.RadioSelectHorizontal,
                              choices=[154, 319])
    q27 = models.IntegerField(widget=widgets.RadioSelectHorizontal,
                              choices=[154, 319])
    q28 = models.IntegerField(widget=widgets.RadioSelectHorizontal,
                              choices=[154, 319])
    q29 = models.IntegerField(widget=widgets.RadioSelectHorizontal,
                              choices=[154, 319])
    q30 = models.IntegerField(widget=widgets.RadioSelectHorizontal,
                              choices=[154, 319])
    q31 = models.IntegerField(widget=widgets.RadioSelectHorizontal,
                              choices=[154, 319])
    q32 = models.IntegerField(widget=widgets.RadioSelectHorizontal,
                              choices=[154, 319])
    q33 = models.IntegerField(widget=widgets.RadioSelectHorizontal,
                              choices=[154, 319])
    q34 = models.IntegerField(widget=widgets.RadioSelectHorizontal,
                              choices=[154, 319])
    q35 = models.IntegerField(widget=widgets.RadioSelectHorizontal,
                              choices=[154, 319])
    q36 = models.IntegerField(widget=widgets.RadioSelectHorizontal,
                              choices=[154, 319])
    datumq1 = models.StringField()
    datumq2 = models.StringField()
    datumq3 = models.StringField()
    datumq4 = models.StringField()
    datumq5 = models.StringField()
    datumq6 = models.StringField()
    datumq7 = models.StringField()
    datumq8 = models.StringField()
    datumq9 = models.StringField()
    datumq10 = models.StringField()
    datumq11 = models.StringField()
    datumq12 = models.StringField()
    datumq13 = models.StringField()
    datumq14 = models.StringField()
    datumq15 = models.StringField()
    datumq16 = models.StringField()
    datumq17 = models.StringField()
    datumq18 = models.StringField()
    datumq19 = models.StringField()
    datumq20 = models.StringField()
    datumq21 = models.StringField()
    datumq22 = models.StringField()
    datumq23 = models.StringField()
    datumq24 = models.StringField()
    datumq25 = models.StringField()
    datumq26 = models.StringField()
    datumq27 = models.StringField()
    datumq28 = models.StringField()
    datumq29 = models.StringField()
    datumq30 = models.StringField()
    datumq31 = models.StringField()
    datumq32 = models.StringField()
    datumq33 = models.StringField()
    datumq34 = models.StringField()
    datumq35 = models.StringField()
    datumq36 = models.StringField()

    pocet_ukolu = models.IntegerField()
    final_datum = models.StringField()


    def T1shuffle(Player):
        import random
        tabulka1 = [["q1","154","138","Možnost A: Dnes " +C.this_week+ " večer od 17 do 24 hod", "Možnost B: Za týden "+ C.next_week+ " od 17 do 24 hod" ], ["q2","154","103","Možnost A: Dnes " +C.this_week+ " večer od 17 do 24 hod", "Možnost B: Za týden "+ C.next_week+ " od 17 do 24 hod" ], ["q3","154","253","Možnost A: Dnes " +C.this_week+ " večer od 17 do 24 hod", "Možnost B: Za týden "+ C.next_week+ " od 17 do 24 hod" ], ["q4","154","164","Možnost A: Dnes " +C.this_week+ " večer od 17 do 24 hod", "Možnost B: Za týden "+ C.next_week+ " od 17 do 24 hod" ], ["q5","154","169","Možnost A: Dnes " +C.this_week+ " večer od 17 do 24 hod", "Možnost B: Za týden "+ C.next_week+ " od 17 do 24 hod" ], ["q6","154","184","Možnost A: Dnes " +C.this_week+ " večer od 17 do 24 hod", "Možnost B: Za týden "+ C.next_week+ " od 17 do 24 hod" ]]
        tabulka2 = [["q7","154","101","Možnost A: Dnes " +C.this_week+ " večer od 17 do 24 hod","Možnost B: Za čtyři týdny "+ C.four_weeks+ " od 17 do 24 hod"], ["q8","154","60","Možnost A: Dnes " +C.this_week+ " večer od 17 do 24 hod","Možnost B: Za čtyři týdny "+ C.four_weeks+ " od 17 do 24 hod"], ["q9","154","403","Možnost A: Dnes " +C.this_week+ " večer od 17 do 24 hod","Možnost B: Za čtyři týdny "+ C.four_weeks+ " od 17 do 24 hod"], ["q10","154","202","Možnost A: Dnes " +C.this_week+ " večer od 17 do 24 hod","Možnost B: Za čtyři týdny "+ C.four_weeks+ " od 17 do 24 hod"], ["q11","154","225","Možnost A: Dnes " +C.this_week+ " večer od 17 do 24 hod","Možnost B: Za čtyři týdny "+ C.four_weeks+ " od 17 do 24 hod"], ["q12","154","319","Možnost A: Dnes " +C.this_week+ " večer od 17 do 24 hod","Možnost B: Za čtyři týdny "+ C.four_weeks+ " od 17 do 24 hod"]]
        tabulka3 = [["q13","154","138","Možnost A: Za týden " + C.next_week + "večer od 17 do 24 hod ","Možnost B: Za dva týdny" + C.two_weeks +" večer od 17 do 24 hod" ], ["q14","154","103","Možnost A: Za týden " + C.next_week + "večer od 17 do 24 hod ","Možnost B: Za dva týdny" + C.two_weeks +" večer od 17 do 24 hod"],["q15","154","253","Možnost A: Za týden " + C.next_week + "večer od 17 do 24 hod ","Možnost B: Za dva týdny" + C.two_weeks +" večer od 17 do 24 hod"],["q16","154","164","Možnost A: Za týden " + C.next_week + "večer od 17 do 24 hod ","Možnost B: Za dva týdny" + C.two_weeks +" večer od 17 do 24 hod"],["q17","154","169","Možnost A: Za týden " + C.next_week + "večer od 17 do 24 hod ","Možnost B: Za dva týdny" + C.two_weeks +" večer od 17 do 24 hod"],["q18","154","184","Možnost A: Za týden " + C.next_week + "večer od 17 do 24 hod ","Možnost B: Za dva týdny" + C.two_weeks +" večer od 17 do 24 hod"]]
        tabulka4 = [["q19","154","101","Možnost A: Za týden " + C.next_week + "večer od 17 do 24 hod ","Možnost B: Za pět týdnů" + C.five_weeks +" večer od 17 do 24 hod"],["q20","154","60","Možnost A: Za týden " + C.next_week + "večer od 17 do 24 hod ","Možnost B: Za pět týdnů" + C.five_weeks +" večer od 17 do 24 hod"],["q21","154", "403","Možnost A: Za týden " + C.next_week + "večer od 17 do 24 hod ","Možnost B: Za pět týdnů" + C.five_weeks +" večer od 17 do 24 hod"],["q22","154", "202","Možnost A: Za týden " + C.next_week + "večer od 17 do 24 hod ","Možnost B: Za pět týdnů" + C.five_weeks +" večer od 17 do 24 hod"],["q23","154", "225","Možnost A: Za týden " + C.next_week + "večer od 17 do 24 hod ","Možnost B: Za pět týdnů" + C.five_weeks +" večer od 17 do 24 hod"],["q24","154", "319","Možnost A: Za týden " + C.next_week + "večer od 17 do 24 hod ","Možnost B: Za pět týdnů" + C.five_weeks +" večer od 17 do 24 hod"]]
        tabulka5 = [["q25","154", "138","Možnost A: Za dva týdny " + C.two_weeks + "večer od 17 do 24 hod ","Možnost B: Za tři týdny" + C.three_weeks +" večer od 17 do 24 hod"],["q26","154","103","Možnost A: Za dva týdny " + C.two_weeks + "večer od 17 do 24 hod ","Možnost B: Za tři týdny" + C.three_weeks +" večer od 17 do 24 hod"],["q27","154", "253","Možnost A: Za dva týdny " + C.two_weeks + "večer od 17 do 24 hod ","Možnost B: Za tři týdny" + C.three_weeks +" večer od 17 do 24 hod"],["q28","154", "164","Možnost A: Za dva týdny " + C.two_weeks + "večer od 17 do 24 hod ","Možnost B: Za tři týdny" + C.three_weeks +" večer od 17 do 24 hod"],["q29","154", "169","Možnost A: Za dva týdny " + C.two_weeks + "večer od 17 do 24 hod ","Možnost B: Za tři týdny" + C.three_weeks +" večer od 17 do 24 hod"],["q30","154", "184","Možnost A: Za dva týdny " + C.two_weeks + "večer od 17 do 24 hod ","Možnost B: Za tři týdny" + C.three_weeks +" večer od 17 do 24 hod"]]
        tabulka6 = [["q31","154", "101","Možnost A: Za dva týdny " + C.two_weeks + "večer od 17 do 24 hod ","Možnost B: Za šest týdnů" + C.six_weeks +" večer od 17 do 24 hod"],["q32","154", "60","Možnost A: Za dva týdny " + C.two_weeks + "večer od 17 do 24 hod ","Možnost B: Za šest týdnů" + C.six_weeks +" večer od 17 do 24 hod"],["q33","154","403","Možnost A: Za dva týdny " + C.two_weeks + "večer od 17 do 24 hod ","Možnost B: Za šest týdnů" + C.six_weeks +" večer od 17 do 24 hod"],["q34","154", "202","Možnost A: Za dva týdny " + C.two_weeks + "večer od 17 do 24 hod ","Možnost B: Za šest týdnů" + C.six_weeks +" večer od 17 do 24 hod"],["q35","154","225","Možnost A: Za dva týdny " + C.two_weeks + "večer od 17 do 24 hod ","Možnost B: Za šest týdnů" + C.six_weeks +" večer od 17 do 24 hod"],["q36","154", "319","Možnost A: Za dva týdny " + C.two_weeks + "večer od 17 do 24 hod ","Možnost B: Za šest týdnů" + C.six_weeks +" večer od 17 do 24 hod"]]


        random.shuffle(tabulka1)
        random.shuffle(tabulka2)
        random.shuffle(tabulka3)
        random.shuffle(tabulka4)
        random.shuffle(tabulka5)
        random.shuffle(tabulka6)
        superlist = [tabulka1, tabulka2, tabulka3, tabulka4, tabulka5, tabulka6]
        random.shuffle(superlist)
        Player.participant.vars["vsechnyotazky"] = superlist

    def paymentFunction(Player):
        if Player.participant.vars.get("typukolu") == "offline time preferences":
            k = Player.participant.vars.get("cisloukolu")
            q_name = "q{}".format(k)
            d_name = "datumq{}".format(k)
            Player.participant.vars["kolikukolu"] = getattr(Player, q_name)
            Player.pocet_ukolu = Player.participant.vars.get("kolikukolu")
            Player.final_datum = getattr(Player, d_name)
            Player.participant.vars["datumukolu"] = Player.final_datum
        else:
            Player.participant.vars["datumukolu"] = 0

# PAGES
class MyPage(Page):

    def vars_for_template(player: Player):
        return dict(
            tabulka1=player.participant.vars.get("vsechnyotazky"),

        )

    def live_method(player, data):
        if player.participant.vars.get("vsechnyotazky")[data['indexino2']][data['indexino']][0] == "q1":
            if data['t'] == 'choice1':
                player.q1 = 154
                player.datumq1 = C.this_week
            if data['t'] == 'choice2':
                player.q1 = 138
                player.datumq1 = C.next_week

        if player.participant.vars.get("vsechnyotazky")[data['indexino2']][data['indexino']][0] == "q2":
            if data['t'] == 'choice1':
                player.q2 = 154
                player.datumq2 = C.this_week
            if data['t'] == 'choice2':
                player.q2 = 103
                player.datumq2 = C.next_week

        if player.participant.vars.get("vsechnyotazky")[data['indexino2']][data['indexino']][0] == "q3":
            if data['t'] == 'choice1':
                player.q3 = 154
                player.datumq3 = C.this_week
            if data['t'] == 'choice2':
                player.q3 = 253
                player.datumq3 = C.next_week


        if player.participant.vars.get("vsechnyotazky")[data['indexino2']][data['indexino']][0] == "q4":
            if data['t'] == 'choice1':
                player.q4 = 154
                player.datumq4 = C.this_week
            if data['t'] == 'choice2':
                player.q4 = 164
                player.datumq4 = C.next_week

        if player.participant.vars.get("vsechnyotazky")[data['indexino2']][data['indexino']][0] == "q5":
            if data['t'] == 'choice1':
                player.q5 = 154
                player.datumq5 = C.this_week
            if data['t'] == 'choice2':
                player.q5 = 169
                player.datumq5 = C.next_week

        if player.participant.vars.get("vsechnyotazky")[data['indexino2']][data['indexino']][0] == "q6":
            if data['t'] == 'choice1':
                player.q6 = 154
                player.datumq6 = C.this_week

            if data['t'] == 'choice2':
                player.q6 = 184
                player.datumq6 = C.next_week
        #Tabulka2
        if player.participant.vars.get("vsechnyotazky")[data['indexino2']][data['indexino']][0] == "q7":
            if data['t'] == 'choice1':
                player.q7 = 154
                player.datumq7 = C.this_week
            if data['t'] == 'choice2':
                player.q7 = 101
                player.datumq7 = C.four_weeks
        if player.participant.vars.get("vsechnyotazky")[data['indexino2']][data['indexino']][0] == "q8":
            if data['t'] == 'choice1':
                player.q8 = 154
                player.datumq8 = C.this_week
            if data['t'] == 'choice2':
                player.q8 = 60
                player.datumq8 = C.four_weeks
        if player.participant.vars.get("vsechnyotazky")[data['indexino2']][data['indexino']][0] == "q9":
            if data['t'] == 'choice1':
                player.q9 = 154
                player.datumq9 = C.this_week
            if data['t'] == 'choice2':
                player.q9 = 403
                player.datumq9 = C.four_weeks
        if player.participant.vars.get("vsechnyotazky")[data['indexino2']][data['indexino']][0] == "q10":
            if data['t'] == 'choice1':
                player.q10 = 154
                player.datumq10 = C.this_week
            if data['t'] == 'choice2':
                player.q10 = 202
                player.datumq10 = C.four_weeks
        if player.participant.vars.get("vsechnyotazky")[data['indexino2']][data['indexino']][0] == "q11":
            if data['t'] == 'choice1':
                player.q11 = 154
                player.datumq11 = C.this_week
            if data['t'] == 'choice2':
                player.q11 = 225
                player.datumq11 = C.four_weeks
        if player.participant.vars.get("vsechnyotazky")[data['indexino2']][data['indexino']][0] == "q12":
            if data['t'] == 'choice1':
                player.q12 = 154
                player.datumq12 = C.this_week
            if data['t'] == 'choice2':
                player.q12 = 319
                player.datumq12 = C.four_weeks
        if player.participant.vars.get("vsechnyotazky")[data['indexino2']][data['indexino']][0] == "q13":
            if data['t'] == 'choice1':
                player.q13 = 154
                player.datumq13 = C.next_week
            if data['t'] == 'choice2':
                player.q13 = 138
                player.datumq13 = C.two_weeks
        if player.participant.vars.get("vsechnyotazky")[data['indexino2']][data['indexino']][0] == "q14":
            if data['t'] == 'choice1':
                player.q14 = 154
                player.datumq14 = C.next_week
            if data['t'] == 'choice2':
                player.q14 = 103
                player.datumq14 = C.two_weeks
        if player.participant.vars.get("vsechnyotazky")[data['indexino2']][data['indexino']][0] == "q15":
            if data['t'] == 'choice1':
                player.q15 = 154
                player.datumq15 = C.next_week
            if data['t'] == 'choice2':
                player.q15 = 253
                player.datumq15 = C.two_weeks
        if player.participant.vars.get("vsechnyotazky")[data['indexino2']][data['indexino']][0] == "q16":
            if data['t'] == 'choice1':
                player.q16 = 154
                player.datumq16 = C.next_week
            if data['t'] == 'choice2':
                player.q16 = 164
                player.datumq16 = C.two_weeks
        if player.participant.vars.get("vsechnyotazky")[data['indexino2']][data['indexino']][0] == "q17":
            if data['t'] == 'choice1':
                player.q17 = 154
                player.datumq17 = C.next_week
            if data['t'] == 'choice2':
                player.q17 = 169
                player.datumq17 = C.two_weeks
        if player.participant.vars.get("vsechnyotazky")[data['indexino2']][data['indexino']][0] == "q18":
            if data['t'] == 'choice1':
                player.q18 = 154
                player.datumq18 = C.next_week
            if data['t'] == 'choice2':
                player.q18 = 184
                player.datumq18 = C.two_weeks
        if player.participant.vars.get("vsechnyotazky")[data['indexino2']][data['indexino']][0] == "q19":
            if data['t'] == 'choice1':
                player.q19 = 154
                player.datumq19 = C.next_week
            if data['t'] == 'choice2':
                player.q19 = 101
                player.datumq19 = C.five_weeks
        if player.participant.vars.get("vsechnyotazky")[data['indexino2']][data['indexino']][0] == "q20":
            if data['t'] == 'choice1':
                player.q20 = 154
                player.datumq20 = C.next_week
            if data['t'] == 'choice2':
                player.q20 = 60
                player.datumq20 = C.five_weeks
        if player.participant.vars.get("vsechnyotazky")[data['indexino2']][data['indexino']][0] == "q21":
            if data['t'] == 'choice1':
                player.q21 = 154
                player.datumq21 = C.next_week
            if data['t'] == 'choice2':
                player.q21 = 403
                player.datumq21 = C.five_weeks
        if player.participant.vars.get("vsechnyotazky")[data['indexino2']][data['indexino']][0] == "q22":
            if data['t'] == 'choice1':
                player.q22 = 154
                player.datumq22 = C.next_week
            if data['t'] == 'choice2':
                player.q22 = 202
                player.datumq22 = C.five_weeks
        if player.participant.vars.get("vsechnyotazky")[data['indexino2']][data['indexino']][0] == "q23":
            if data['t'] == 'choice1':
                player.q23 = 154
                player.datumq23 = C.next_week
            if data['t'] == 'choice2':
                player.q23 = 225
                player.datumq23 = C.five_weeks
        if player.participant.vars.get("vsechnyotazky")[data['indexino2']][data['indexino']][0] == "q24":
            if data['t'] == 'choice1':
                player.q24 = 154
                player.datumq24 = C.next_week
            if data['t'] == 'choice2':
                player.q24 = 319
                player.datumq24 = C.five_weeks
        if player.participant.vars.get("vsechnyotazky")[data['indexino2']][data['indexino']][0] == "q25":
            if data['t'] == 'choice1':
                player.q25 = 154
                player.datumq25 = C.two_weeks
            if data['t'] == 'choice2':
                player.q25 = 138
                player.datumq25 = C.three_weeks
        if player.participant.vars.get("vsechnyotazky")[data['indexino2']][data['indexino']][0] == "q26":
            if data['t'] == 'choice1':
                player.q26 = 154
                player.datumq26 = C.two_weeks
            if data['t'] == 'choice2':
                player.q26 = 103
                player.datumq26 = C.three_weeks
        if player.participant.vars.get("vsechnyotazky")[data['indexino2']][data['indexino']][0] == "q27":
            if data['t'] == 'choice1':
                player.q27 = 154
                player.datumq27 = C.two_weeks
            if data['t'] == 'choice2':
                player.q27 = 253
                player.datumq27 = C.three_weeks
        if player.participant.vars.get("vsechnyotazky")[data['indexino2']][data['indexino']][0] == "q28":
            if data['t'] == 'choice1':
                player.q28 = 154
                player.datumq28 = C.two_weeks
            if data['t'] == 'choice2':
                player.q28 = 164
                player.datumq28 = C.three_weeks
        if player.participant.vars.get("vsechnyotazky")[data['indexino2']][data['indexino']][0] == "q29":
            if data['t'] == 'choice1':
                player.q29 = 154
                player.datumq29 = C.two_weeks
            if data['t'] == 'choice2':
                player.q29 = 169
                player.datumq29 = C.three_weeks
        if player.participant.vars.get("vsechnyotazky")[data['indexino2']][data['indexino']][0] == "q30":
            if data['t'] == 'choice1':
                player.q30 = 154
                player.datumq30 = C.two_weeks
            if data['t'] == 'choice2':
                player.q30 = 184
                player.datumq30 = C.three_weeks
        if player.participant.vars.get("vsechnyotazky")[data['indexino2']][data['indexino']][0] == "q31":
            if data['t'] == 'choice1':
                player.q31 = 154
                player.datumq31 = C.two_weeks
            if data['t'] == 'choice2':
                player.q31 = 101
                player.datumq31 = C.six_weeks
        if player.participant.vars.get("vsechnyotazky")[data['indexino2']][data['indexino']][0] == "q32":
            if data['t'] == 'choice1':
                player.q32 = 154
                player.datumq32 = C.two_weeks
            if data['t'] == 'choice2':
                player.q32 = 60
                player.datumq32 = C.six_weeks
        if player.participant.vars.get("vsechnyotazky")[data['indexino2']][data['indexino']][0] == "q33":
            if data['t'] == 'choice1':
                player.q33 = 154
                player.datumq33 = C.two_weeks
            if data['t'] == 'choice2':
                player.q33 = 403
                player.datumq33 = C.six_weeks
        if player.participant.vars.get("vsechnyotazky")[data['indexino2']][data['indexino']][0] == "q34":
            if data['t'] == 'choice1':
                player.q34 = 154
                player.datumq34 = C.two_weeks
            if data['t'] == 'choice2':
                player.q34 = 202
                player.datumq34 = C.six_weeks
        if player.participant.vars.get("vsechnyotazky")[data['indexino2']][data['indexino']][0] == "q35":
            if data['t'] == 'choice1':
                player.q35 = 154
                player.datumq35 = C.two_weeks
            if data['t'] == 'choice2':
                player.q35 = 225
                player.datumq35 = C.six_weeks
        if player.participant.vars.get("vsechnyotazky")[data['indexino2']][data['indexino']][0] == "q36":
            if data['t'] == 'choice1':
                player.q36 = 154
                player.datumq36 = C.two_weeks
            if data['t'] == 'choice2':
                player.q36 = 319
                player.datumq36 = C.six_weeks

    def before_next_page(player: Player, timeout_happened):
        player.paymentFunction()


class ResultsWaitPage(WaitPage):
    pass


class Results(Page):
    def before_next_page(player: Player, timeout_happened):
        Player.T1shuffle(player)


page_sequence = [Results, MyPage]



