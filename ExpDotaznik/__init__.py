from otree.api import *


doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'ExpDotaznik'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1

    m1 = "Zcela nepodstatné"
    m2 = "Obzvlášť podstatné"
    choice = [[10,"10 - Velmi ochotný/á"],[9,"9"],[8,"8"],[7,"7"],[6,"6"],[5,"5"],[4,"4"],[3,"3"],[2,"2"],[1,"1"],[0,"0 - Naprosto neochotný/á riskovat"],[98,"98 - Neví"],[99,"99 - Odmítl"]]
    choice2 = [[0,"0 - Naprosto neochotný/á takto jednat"],[1,"1"],[2,"2"],[3,"3"],[4,"4"],[5,"5"],[6,"6"],[7,"7"],[8,"8"],[9,"9"],[10,"10 - Velmi ochotný/á takto jednat"],[99,"99 - Neví"]]
    choice3 = [[0, "0 - Vůbec mě to nevystihuje"], [1, "1"], [2, "2"], [3, "3"], [4, "4"], [5, "5"], [6, "6"],
               [7, "7"], [8, "8"], [9, "9"], [10, "10 - Vystihuje mě to dokonale"], [99, "99 - Neví"]]


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    pt1 = models.StringField(choices=["Vůbec nesouhlasím", "Nesouhlasím", "Neutrální stanovisko, nemám na to názor", "Souhlasím", "Zcela souhlasím"],
                             widget=widgets.RadioSelectHorizontal,
                             label="je společenský, družný. ")
    pt2 = models.StringField(
        choices=["Vůbec nesouhlasím", "Nesouhlasím", "Neutrální stanovisko, nemám na to názor", "Souhlasím",
                 "Zcela souhlasím"],
        widget=widgets.RadioSelectHorizontal,
        label="je soucitný, má dobré srdce.")
    pt3 = models.StringField(
        choices=["Vůbec nesouhlasím", "Nesouhlasím", "Neutrální stanovisko, nemám na to názor", "Souhlasím",
                 "Zcela souhlasím"],
        widget=widgets.RadioSelectHorizontal,
        label="má sklon být chaotický. ")
    pt4 = models.StringField(
        choices=["Vůbec nesouhlasím", "Nesouhlasím", "Neutrální stanovisko, nemám na to názor", "Souhlasím",
                 "Zcela souhlasím"],
        widget=widgets.RadioSelectHorizontal,
        label="je uvolněný, dobře zvládá stres.  ")
    pt5 = models.StringField(
        choices=["Vůbec nesouhlasím", "Nesouhlasím", "Neutrální stanovisko, nemám na to názor", "Souhlasím",
                 "Zcela souhlasím"],
        widget=widgets.RadioSelectHorizontal,
        label="se o umění příliš nezajímá. ")
    pt6 = models.StringField(
        choices=["Vůbec nesouhlasím", "Nesouhlasím", "Neutrální stanovisko, nemám na to názor", "Souhlasím",
                 "Zcela souhlasím"],
        widget=widgets.RadioSelectHorizontal,
        label="se umí prosadit a projevovat své vlastní názory. ")
    pt7 = models.StringField(
        choices=["Vůbec nesouhlasím", "Nesouhlasím", "Neutrální stanovisko, nemám na to názor", "Souhlasím",
                 "Zcela souhlasím"],
        widget=widgets.RadioSelectHorizontal,
        label="je uctivý, s ostatními zachází s úctou. ")
    pt8 = models.StringField(
        choices=["Vůbec nesouhlasím", "Nesouhlasím", "Neutrální stanovisko, nemám na to názor", "Souhlasím",
                 "Zcela souhlasím"],
        widget=widgets.RadioSelectHorizontal,
        label="má sklon být líný. ")
    pt9 = models.StringField(
        choices=["Vůbec nesouhlasím", "Nesouhlasím", "Neutrální stanovisko, nemám na to názor", "Souhlasím",
                 "Zcela souhlasím"],
        widget=widgets.RadioSelectHorizontal,
        label="zůstává optimistický i po nějakém nezdaru.")
    pt10 = models.StringField(
        choices=["Vůbec nesouhlasím", "Nesouhlasím", "Neutrální stanovisko, nemám na to názor", "Souhlasím",
                 "Zcela souhlasím"],
        widget=widgets.RadioSelectHorizontal,
        label="zajímá se o mnoho různých věcí.  ")
    pt11 = models.StringField(
        choices=["Vůbec nesouhlasím", "Nesouhlasím", "Neutrální stanovisko, nemám na to názor", "Souhlasím",
                 "Zcela souhlasím"],
        widget=widgets.RadioSelectHorizontal,
        label="zřídkakdy pociťuje vzrušení a nadšení pro věc.")
    pt12 = models.StringField(
        choices=["Vůbec nesouhlasím", "Nesouhlasím", "Neutrální stanovisko, nemám na to názor", "Souhlasím",
                 "Zcela souhlasím"],
        widget=widgets.RadioSelectHorizontal,
        label="má sklon hledat chyby na ostatních. ")
    pt13 = models.StringField(
        choices=["Vůbec nesouhlasím", "Nesouhlasím", "Neutrální stanovisko, nemám na to názor", "Souhlasím",
                 "Zcela souhlasím"],
        widget=widgets.RadioSelectHorizontal,
        label="je spolehlivý, ve svém chování stálý. ")
    pt14 = models.StringField(
        choices=["Vůbec nesouhlasím", "Nesouhlasím", "Neutrální stanovisko, nemám na to názor", "Souhlasím",
                 "Zcela souhlasím"],
        widget=widgets.RadioSelectHorizontal,
        label="je náladový, střídá se mu dobrá a špatná nálada. ")
    pt15 = models.StringField(
        choices=["Vůbec nesouhlasím", "Nesouhlasím", "Neutrální stanovisko, nemám na to názor", "Souhlasím",
                 "Zcela souhlasím"],
        widget=widgets.RadioSelectHorizontal,
        label="je vynalézavý, nachází důmyslné způsoby, jak něco dělat. ")
    pt16 = models.StringField(
        choices=["Vůbec nesouhlasím", "Nesouhlasím", "Neutrální stanovisko, nemám na to názor", "Souhlasím",
                 "Zcela souhlasím"],
        widget=widgets.RadioSelectHorizontal,
        label="bývá tichý. ")
    pt17 = models.StringField(
        choices=["Vůbec nesouhlasím", "Nesouhlasím", "Neutrální stanovisko, nemám na to názor", "Souhlasím",
                 "Zcela souhlasím"],
        widget=widgets.RadioSelectHorizontal,
        label="s ostatními příliš nesoucítí.")
    pt18 = models.StringField(
        choices=["Vůbec nesouhlasím", "Nesouhlasím", "Neutrální stanovisko, nemám na to názor", "Souhlasím",
                 "Zcela souhlasím"],
        widget=widgets.RadioSelectHorizontal,
        label="je systematický, udržuje ve věcech pořádek. ")
    pt19 = models.StringField(
        choices=["Vůbec nesouhlasím", "Nesouhlasím", "Neutrální stanovisko, nemám na to názor", "Souhlasím",
                 "Zcela souhlasím"],
        widget=widgets.RadioSelectHorizontal,
        label="bývá napjatý.")
    pt20 = models.StringField(
        choices=["Vůbec nesouhlasím", "Nesouhlasím", "Neutrální stanovisko, nemám na to názor", "Souhlasím",
                 "Zcela souhlasím"],
        widget=widgets.RadioSelectHorizontal,
        label="je fascinován uměním, hudbou a literaturou.")
    pt21 = models.StringField(
        choices=["Vůbec nesouhlasím", "Nesouhlasím", "Neutrální stanovisko, nemám na to názor", "Souhlasím",
                 "Zcela souhlasím"],
        widget=widgets.RadioSelectHorizontal,
        label="je dominantní, zastává roli vůdce.")
    pt22 = models.StringField(
        choices=["Vůbec nesouhlasím", "Nesouhlasím", "Neutrální stanovisko, nemám na to názor", "Souhlasím",
                 "Zcela souhlasím"],
        widget=widgets.RadioSelectHorizontal,
        label="s ostatními vyvolává rozepře.")
    pt23 = models.StringField(
        choices=["Vůbec nesouhlasím", "Nesouhlasím", "Neutrální stanovisko, nemám na to názor", "Souhlasím",
                 "Zcela souhlasím"],
        widget=widgets.RadioSelectHorizontal,
        label="má obtíže začít s úkoly.")
    pt24 = models.StringField(
        choices=["Vůbec nesouhlasím", "Nesouhlasím", "Neutrální stanovisko, nemám na to názor", "Souhlasím",
                 "Zcela souhlasím"],
        widget=widgets.RadioSelectHorizontal,
        label="se cítí sebejistě, je sám se sebou spokojen.")
    pt25 = models.StringField(
        choices=["Vůbec nesouhlasím", "Nesouhlasím", "Neutrální stanovisko, nemám na to názor", "Souhlasím",
                 "Zcela souhlasím"],
        widget=widgets.RadioSelectHorizontal,
        label="se vyhýbá intelektuálním a filosofickým debatám.")
    pt26 = models.StringField(
        choices=["Vůbec nesouhlasím", "Nesouhlasím", "Neutrální stanovisko, nemám na to názor", "Souhlasím",
                 "Zcela souhlasím"],
        widget=widgets.RadioSelectHorizontal,
        label="je méně činorodý než ostatní.")
    pt27 = models.StringField(
        choices=["Vůbec nesouhlasím", "Nesouhlasím", "Neutrální stanovisko, nemám na to názor", "Souhlasím",
                 "Zcela souhlasím"],
        widget=widgets.RadioSelectHorizontal,
        label="má v povaze odpouštět.")
    pt28 = models.StringField(
        choices=["Vůbec nesouhlasím", "Nesouhlasím", "Neutrální stanovisko, nemám na to názor", "Souhlasím",
                 "Zcela souhlasím"],
        widget=widgets.RadioSelectHorizontal,
        label="bývá poněkud ledabylý (nedbalý).")
    pt29 = models.StringField(
        choices=["Vůbec nesouhlasím", "Nesouhlasím", "Neutrální stanovisko, nemám na to názor", "Souhlasím",
                 "Zcela souhlasím"],
        widget=widgets.RadioSelectHorizontal,
        label="je emočně vyrovnaný, jen tak něco ho nerozhodí.")
    pt30 = models.StringField(
        choices=["Vůbec nesouhlasím", "Nesouhlasím", "Neutrální stanovisko, nemám na to názor", "Souhlasím",
                 "Zcela souhlasím"],
        widget=widgets.RadioSelectHorizontal,
        label="není příliš tvořivý.")
    pt31 = models.StringField(
        choices=["Vůbec nesouhlasím", "Nesouhlasím", "Neutrální stanovisko, nemám na to názor", "Souhlasím",
                 "Zcela souhlasím"],
        widget=widgets.RadioSelectHorizontal,
        label="je někdy plachý, introvertní.")
    pt32 = models.StringField(
        choices=["Vůbec nesouhlasím", "Nesouhlasím", "Neutrální stanovisko, nemám na to názor", "Souhlasím",
                 "Zcela souhlasím"],
        widget=widgets.RadioSelectHorizontal,
        label="pomáhá ostatním a není sobecký.")
    pt33 = models.StringField(
        choices=["Vůbec nesouhlasím", "Nesouhlasím", "Neutrální stanovisko, nemám na to názor", "Souhlasím",
                 "Zcela souhlasím"],
        widget=widgets.RadioSelectHorizontal,
        label="udržuje věci úhledné a uspořádané. ")
    pt34 = models.StringField(
        choices=["Vůbec nesouhlasím", "Nesouhlasím", "Neutrální stanovisko, nemám na to názor", "Souhlasím",
                 "Zcela souhlasím"],
        widget=widgets.RadioSelectHorizontal,
        label="si hodně dělá starosti.")
    pt35 = models.StringField(
        choices=["Vůbec nesouhlasím", "Nesouhlasím", "Neutrální stanovisko, nemám na to názor", "Souhlasím",
                 "Zcela souhlasím"],
        widget=widgets.RadioSelectHorizontal,
        label="oceňuje umění a krásu. ")
    pt36 = models.StringField(
        choices=["Vůbec nesouhlasím", "Nesouhlasím", "Neutrální stanovisko, nemám na to názor", "Souhlasím",
                 "Zcela souhlasím"],
        widget=widgets.RadioSelectHorizontal,
        label="pokládá za obtížné ovlivňovat druhé.")
    pt37 = models.StringField(
        choices=["Vůbec nesouhlasím", "Nesouhlasím", "Neutrální stanovisko, nemám na to názor", "Souhlasím",
                 "Zcela souhlasím"],
        widget=widgets.RadioSelectHorizontal,
        label="je někdy na ostatní hrubý.")
    pt38 = models.StringField(
        choices=["Vůbec nesouhlasím", "Nesouhlasím", "Neutrální stanovisko, nemám na to názor", "Souhlasím",
                 "Zcela souhlasím"],
        widget=widgets.RadioSelectHorizontal,
        label="je výkonný, věci dotahuje do konce.")
    pt39 = models.StringField(
        choices=["Vůbec nesouhlasím", "Nesouhlasím", "Neutrální stanovisko, nemám na to názor", "Souhlasím",
                 "Zcela souhlasím"],
        widget=widgets.RadioSelectHorizontal,
        label="je často smutný.")
    pt40 = models.StringField(
        choices=["Vůbec nesouhlasím", "Nesouhlasím", "Neutrální stanovisko, nemám na to názor", "Souhlasím",
                 "Zcela souhlasím"],
        widget=widgets.RadioSelectHorizontal,
        label="je přemýšlivý, nad věcmi uvažuje do hloubky.")
    pt41 = models.StringField(
        choices=["Vůbec nesouhlasím", "Nesouhlasím", "Neutrální stanovisko, nemám na to názor", "Souhlasím",
                 "Zcela souhlasím"],
        widget=widgets.RadioSelectHorizontal,
        label="je plný energie.")
    pt42 = models.StringField(
        choices=["Vůbec nesouhlasím", "Nesouhlasím", "Neutrální stanovisko, nemám na to názor", "Souhlasím",
                 "Zcela souhlasím"],
        widget=widgets.RadioSelectHorizontal,
        label="je vůči záměrům ostatních nedůvěřivý.")
    pt43 = models.StringField(
        choices=["Vůbec nesouhlasím", "Nesouhlasím", "Neutrální stanovisko, nemám na to názor", "Souhlasím",
                 "Zcela souhlasím"],
        widget=widgets.RadioSelectHorizontal,
        label="je spolehlivý, vždy se na něj dá spolehnout.")
    pt44 = models.StringField(
        choices=["Vůbec nesouhlasím", "Nesouhlasím", "Neutrální stanovisko, nemám na to názor", "Souhlasím",
                 "Zcela souhlasím"],
        widget=widgets.RadioSelectHorizontal,
        label="drží své emoce pod kontrolou.")
    pt45 = models.StringField(
        choices=["Vůbec nesouhlasím", "Nesouhlasím", "Neutrální stanovisko, nemám na to názor", "Souhlasím",
                 "Zcela souhlasím"],
        widget=widgets.RadioSelectHorizontal,
        label="má potíže si ledacos představit.")
    pt46 = models.StringField(
        choices=["Vůbec nesouhlasím", "Nesouhlasím", "Neutrální stanovisko, nemám na to názor", "Souhlasím",
                 "Zcela souhlasím"],
        widget=widgets.RadioSelectHorizontal,
        label="je povídavý.")
    pt47 = models.StringField(
        choices=["Vůbec nesouhlasím", "Nesouhlasím", "Neutrální stanovisko, nemám na to názor", "Souhlasím",
                 "Zcela souhlasím"],
        widget=widgets.RadioSelectHorizontal,
        label="dokáže být chladný a bezcitný.")
    pt48 = models.StringField(
        choices=["Vůbec nesouhlasím", "Nesouhlasím", "Neutrální stanovisko, nemám na to názor", "Souhlasím",
                 "Zcela souhlasím"],
        widget=widgets.RadioSelectHorizontal,
        label="zanechává nepořádek, neuklízí. ")
    pt49 = models.StringField(
        choices=["Vůbec nesouhlasím", "Nesouhlasím", "Neutrální stanovisko, nemám na to názor", "Souhlasím",
                 "Zcela souhlasím"],
        widget=widgets.RadioSelectHorizontal,
        label="jen zřídkakdy cítí úzkost nebo strach.")
    pt50 = models.StringField(
        choices=["Vůbec nesouhlasím", "Nesouhlasím", "Neutrální stanovisko, nemám na to názor", "Souhlasím",
                 "Zcela souhlasím"],
        widget=widgets.RadioSelectHorizontal,
        label="si myslí, že poezie a divadlo jsou nudné. ")
    pt51 = models.StringField(
        choices=["Vůbec nesouhlasím", "Nesouhlasím", "Neutrální stanovisko, nemám na to názor", "Souhlasím",
                 "Zcela souhlasím"],
        widget=widgets.RadioSelectHorizontal,
        label="upřednostňuje, aby se vedení ujali ostatní.")
    pt52 = models.StringField(
        choices=["Vůbec nesouhlasím", "Nesouhlasím", "Neutrální stanovisko, nemám na to názor", "Souhlasím",
                 "Zcela souhlasím"],
        widget=widgets.RadioSelectHorizontal,
        label="je k ostatním slušný a zdvořilý.")
    pt53 = models.StringField(
        choices=["Vůbec nesouhlasím", "Nesouhlasím", "Neutrální stanovisko, nemám na to názor", "Souhlasím",
                 "Zcela souhlasím"],
        widget=widgets.RadioSelectHorizontal,
        label="je vytrvalý, pracuje, dokud úkol nedokončí")
    pt54 = models.StringField(
        choices=["Vůbec nesouhlasím", "Nesouhlasím", "Neutrální stanovisko, nemám na to názor", "Souhlasím",
                 "Zcela souhlasím"],
        widget=widgets.RadioSelectHorizontal,
        label="má sklon bývat skleslý, v depresi.")
    pt55 = models.StringField(
        choices=["Vůbec nesouhlasím", "Nesouhlasím", "Neutrální stanovisko, nemám na to názor", "Souhlasím",
                 "Zcela souhlasím"],
        widget=widgets.RadioSelectHorizontal,
        label="se příliš nezajímá o abstraktní myšlenky.")
    pt56 = models.StringField(
        choices=["Vůbec nesouhlasím", "Nesouhlasím", "Neutrální stanovisko, nemám na to názor", "Souhlasím",
                 "Zcela souhlasím"],
        widget=widgets.RadioSelectHorizontal,
        label="projevuje velké nadšení.")
    pt57 = models.StringField(
        choices=["Vůbec nesouhlasím", "Nesouhlasím", "Neutrální stanovisko, nemám na to názor", "Souhlasím",
                 "Zcela souhlasím"],
        widget=widgets.RadioSelectHorizontal,
        label="si o lidech myslí to nejlepší.")
    pt58 = models.StringField(
        choices=["Vůbec nesouhlasím", "Nesouhlasím", "Neutrální stanovisko, nemám na to názor", "Souhlasím",
                 "Zcela souhlasím"],
        widget=widgets.RadioSelectHorizontal,
        label="se někdy chová nezodpovědně.")
    pt59 = models.StringField(
        choices=["Vůbec nesouhlasím", "Nesouhlasím", "Neutrální stanovisko, nemám na to názor", "Souhlasím",
                 "Zcela souhlasím"],
        widget=widgets.RadioSelectHorizontal,
        label="je emočně impulzivní, snadno se nechá vyvést z míry.")
    pt60 = models.StringField(
        choices=["Vůbec nesouhlasím", "Nesouhlasím", "Neutrální stanovisko, nemám na to názor", "Souhlasím",
                 "Zcela souhlasím"],
        widget=widgets.RadioSelectHorizontal,
        label="je originální, přichází s novými nápady.")

    mv1 = models.StringField(
        choices=[C.m1, "Spíše nepodstatné", "Mírně podstatné", "Celkem podstatné", "Velmi podstatné",
                 C.m2],
        widget=widgets.RadioSelectHorizontal,
        label="Jestli někdo emocionálně trpěl"
    )
    mv2 = models.StringField(
        choices=[C.m1, "Spíše nepodstatné", "Mírně podstatné",
                 "Celkem podstatné", "Velmi podstatné",
                 C.m2],
        widget=widgets.RadioSelectHorizontal,
        label="Jestli se s některými lidmi zacházelo jinak než s ostatními "
    )
    mv3 = models.StringField(
        choices=[C.m1, "Spíše nepodstatné", "Mírně podstatné",
                 "Celkem podstatné", "Velmi podstatné",
                 C.m2],
        widget=widgets.RadioSelectHorizontal,
        label="Jestli někdo svými činy projevoval lásku ke své zemi"
    )
    mv4 = models.StringField(
        choices=[C.m1, "Spíše nepodstatné", "Mírně podstatné",
                 "Celkem podstatné", "Velmi podstatné",
                 C.m2],
        widget=widgets.RadioSelectHorizontal,
        label="Jestli někdo projevoval nedostatek respektu k autoritě "
    )
    mv5 = models.StringField(
        choices=[C.m1, "Spíše nepodstatné", "Mírně podstatné",
                 "Celkem podstatné", "Velmi podstatné",
                 C.m2],
        widget=widgets.RadioSelectHorizontal,
        label="Jestli někdo porušil standardy cudnosti a počestnosti"
    )
    mv6 = models.StringField(
        choices=[C.m1, "Spíše nepodstatné", "Mírně podstatné",
                 "Celkem podstatné", "Velmi podstatné",
                 C.m2],
        widget=widgets.RadioSelectHorizontal,
        label="Jestli byl někdo dobrý v matematice "
    )
    mv7 = models.StringField(
        choices=[C.m1, "Spíše nepodstatné", "Mírně podstatné",
                 "Celkem podstatné", "Velmi podstatné",
                 C.m2],
        widget=widgets.RadioSelectHorizontal,
        label="Jestli se někdo staral o někoho slabého nebo zranitelného "
    )
    mv8 = models.StringField(
        choices=[C.m1, "Spíše nepodstatné", "Mírně podstatné",
                 "Celkem podstatné", "Velmi podstatné",
                 C.m2],
        widget=widgets.RadioSelectHorizontal,
        label="Jestli někdo jednal neférově "
    )
    mv9 = models.StringField(
        choices=[C.m1, "Spíše nepodstatné", "Mírně podstatné",
                 "Celkem podstatné", "Velmi podstatné",
                 C.m2],
        widget=widgets.RadioSelectHorizontal,
        label="Jestli někdo udělal něco, čím zradil svou skupinu "
    )
    mv10 = models.StringField(
        choices=[C.m1, "Spíše nepodstatné", "Mírně podstatné",
                 "Celkem podstatné", "Velmi podstatné",
                 C.m2],
        widget=widgets.RadioSelectHorizontal,
        label="Jestli někdo jednal v souladu s tradicemi společnosti "
    )
    mv11 = models.StringField(
        choices=[C.m1, "Spíše nepodstatné", "Mírně podstatné",
                 "Celkem podstatné", "Velmi podstatné",
                 C.m2],
        widget=widgets.RadioSelectHorizontal,
        label="Jestli někdo udělal něco nechutného "
    )
    mv12 = models.StringField(
        choices=[C.m1, "Spíše nepodstatné", "Mírně podstatné",
                 "Celkem podstatné", "Velmi podstatné",
                 C.m2],
        widget=widgets.RadioSelectHorizontal,
        label="Jestli byl někdo krutý "
    )
    mv13 = models.StringField(
        choices=[C.m1, "Spíše nepodstatné", "Mírně podstatné",
                 "Celkem podstatné", "Velmi podstatné",
                 C.m2],
        widget=widgets.RadioSelectHorizontal,
        label="Jestli byla někomu upřena jeho nebo její práva "
    )
    mv14 = models.StringField(
        choices=[C.m1, "Spíše nepodstatné", "Mírně podstatné",
                 "Celkem podstatné", "Velmi podstatné",
                 C.m2],
        widget=widgets.RadioSelectHorizontal,
        label="Jestli někdo projevil nedostatek loajality "
    )
    mv15 = models.StringField(
        choices=[C.m1, "Spíše nepodstatné", "Mírně podstatné",
                 "Celkem podstatné", "Velmi podstatné",
                 C.m2],
        widget=widgets.RadioSelectHorizontal,
        label="Jestli něčí činy způsobily zmatek nebo nepokoj "
    )
    mv16 = models.StringField(
        choices=[C.m1, "Spíše nepodstatné", "Mírně podstatné",
                 "Celkem podstatné", "Velmi podstatné",
                 C.m2],
        widget=widgets.RadioSelectHorizontal,
        label="Jestli někdo jednal způsobem, který by Bůh schvaloval "
    )

    mv17 = models.StringField(
        choices=["Silně nesouhlasím", "Středně nesouhlasím", "Trochu nesouhlasím", "Trochu souhlasím", "Středně souhlasím", "Silně souhlasím"],
        widget=widgets.RadioSelectHorizontal,
        label="Soucit s těmi, kdo trpí, je nejzásadnější ctnost. "
    )
    mv18 = models.StringField(
        choices=["Silně nesouhlasím", "Středně nesouhlasím", "Trochu nesouhlasím", "Trochu souhlasím",
                 "Středně souhlasím", "Silně souhlasím"],
        widget=widgets.RadioSelectHorizontal,
        label="Když zákonodárci tvoří zákony, nejdůležitějším principem by mělo být zajistit, že se bude s každým zacházet spravedlivě. "
    )
    mv19 = models.StringField(
        choices=["Silně nesouhlasím", "Středně nesouhlasím", "Trochu nesouhlasím", "Trochu souhlasím",
                 "Středně souhlasím", "Silně souhlasím"],
        widget=widgets.RadioSelectHorizontal,
        label="Jsem hrdý/á na dějiny své země"
    )
    mv20 = models.StringField(
        choices=["Silně nesouhlasím", "Středně nesouhlasím", "Trochu nesouhlasím", "Trochu souhlasím",
                 "Středně souhlasím", "Silně souhlasím"],
        widget=widgets.RadioSelectHorizontal,
        label="Respekt k autoritě je něčím, co se mají naučit všechny děti. "
    )
    mv21 = models.StringField(
        choices=["Silně nesouhlasím", "Středně nesouhlasím", "Trochu nesouhlasím", "Trochu souhlasím",
                 "Středně souhlasím", "Silně souhlasím"],
        widget=widgets.RadioSelectHorizontal,
        label="Lidé by neměli dělat nechutné věci, ani když jimi nikomu neškodí. "
    )
    mv22 = models.StringField(
        choices=["Silně nesouhlasím", "Středně nesouhlasím", "Trochu nesouhlasím", "Trochu souhlasím",
                 "Středně souhlasím", "Silně souhlasím"],
        widget=widgets.RadioSelectHorizontal,
        label="Je lepší dělat dobro než zlo. "
    )
    mv23 = models.StringField(
        choices=["Silně nesouhlasím", "Středně nesouhlasím", "Trochu nesouhlasím", "Trochu souhlasím",
                 "Středně souhlasím", "Silně souhlasím"],
        widget=widgets.RadioSelectHorizontal,
        label="Jednou z nejhorších věcí, které může člověk udělat, je zranit bezbranné zvíře. "
    )
    mv24 = models.StringField(
        choices=["Silně nesouhlasím", "Středně nesouhlasím", "Trochu nesouhlasím", "Trochu souhlasím",
                 "Středně souhlasím", "Silně souhlasím"],
        widget=widgets.RadioSelectHorizontal,
        label="Spravedlnost je nejdůležitějším základním kamenem společnosti. "
    )
    mv25 = models.StringField(
        choices=["Silně nesouhlasím", "Středně nesouhlasím", "Trochu nesouhlasím", "Trochu souhlasím",
                 "Středně souhlasím", "Silně souhlasím"],
        widget=widgets.RadioSelectHorizontal,
        label="Lidé by měli být loajální ke členům své rodiny, i pokud ti udělali něco špatného "
    )
    mv26 = models.StringField(
        choices=["Silně nesouhlasím", "Středně nesouhlasím", "Trochu nesouhlasím", "Trochu souhlasím",
                 "Středně souhlasím", "Silně souhlasím"],
        widget=widgets.RadioSelectHorizontal,
        label="Muži a ženy mají hrát ve společnosti odlišné role. "
    )
    mv27 = models.StringField(
        choices=["Silně nesouhlasím", "Středně nesouhlasím", "Trochu nesouhlasím", "Trochu souhlasím",
                 "Středně souhlasím", "Silně souhlasím"],
        widget=widgets.RadioSelectHorizontal,
        label="Některé činy bych nazval(a) špatnými na základě toho, že jsou nepřirozené. "
    )
    mv28 = models.StringField(
        choices=["Silně nesouhlasím", "Středně nesouhlasím", "Trochu nesouhlasím", "Trochu souhlasím",
                 "Středně souhlasím", "Silně souhlasím"],
        widget=widgets.RadioSelectHorizontal,
        label="Nikdy nemůže být správné zabít lidskou bytost. "
    )
    mv29 = models.StringField(
        choices=["Silně nesouhlasím", "Středně nesouhlasím", "Trochu nesouhlasím", "Trochu souhlasím",
                 "Středně souhlasím", "Silně souhlasím"],
        widget=widgets.RadioSelectHorizontal,
        label="Myslím si, že je morálně špatné, že bohaté děti zdědí mnoho peněz, zatímco chudé děti nezdědí nic. "
    )
    mv30 = models.StringField(
        choices=["Silně nesouhlasím", "Středně nesouhlasím", "Trochu nesouhlasím", "Trochu souhlasím",
                 "Středně souhlasím", "Silně souhlasím"],
        widget=widgets.RadioSelectHorizontal,
        label="Je důležitější být týmovým hráčem než vyjadřovat sebe sama. "
    )
    mv31 = models.StringField(
        choices=["Silně nesouhlasím", "Středně nesouhlasím", "Trochu nesouhlasím", "Trochu souhlasím",
                 "Středně souhlasím", "Silně souhlasím"],
        widget=widgets.RadioSelectHorizontal,
        label="Kdybych byl(a) v armádě a nesouhlasil(a) bych s rozkazy nadřízeného, stejně bych je poslechl(a), protože to je má povinnost. "
    )
    mv32 = models.StringField(
        choices=["Silně nesouhlasím", "Středně nesouhlasím", "Trochu nesouhlasím", "Trochu souhlasím",
                 "Středně souhlasím", "Silně souhlasím"],
        widget=widgets.RadioSelectHorizontal,
        label="Cudnost je důležitá a hodnotná ctnost. "
    )

    WP1 = models.IntegerField(label="Ohodnoťte prosím na škále od 0 do 10, jak jste obecně ochotní či neochotní riskovat, kde 0 znamená „naprosto neochotný/á riskovat“ a 10 znamená „velmi ochotný/á riskovat“. Pro zařazení se na stupnici od 0 do 10 můžete použít jakékoli číslo v tomto intervalu, čili 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, nebo 10.",
                              choices=C.choice)
    WP2 = models.IntegerField(label="A) Do jaké míry jste ochotný/á se vzdát něčeho, z čeho máte momentálně užitek, pro to, abyste z toho měl/a ještě větší užitek v budoucnu.",
                              choices=C.choice2,)
    WP3 = models.IntegerField(label="B) Do jaké míry jste ochotný/á někoho, kdo s vámi jedná nespravedlivě, potrestat, i za cenu toho, že to pro vás může mít důsledky? ",
                              choices=C.choice2)
    WP4 = models.IntegerField(label="C) Do jaké míry jste ochotný/á někoho, kdo jedná nespravedlivě s jinými, potrestat, i za cenu toho, že to pro vás může mít důsledky?",
                              choices=C.choice2)
    WP5 = models.IntegerField(label=" D) Do jaké míry jste ochotný/á přispívat na dobročinné účely, aniž byste za to něco očekával/a?",
                              choices=C.choice2)
    WP6 = models.IntegerField(label="A) Když mi někdo prokáže laskavost, jsem připraven/a mu to oplatit. ",
                              choices=C.choice3)
    WP7 = models.IntegerField(label="B) Pokud se se mnou zachází velmi nespravedlivě, pomstím se při první příležitosti, i když ponesu důsledky. ",
                              choices=C.choice3)
    WP8 = models.IntegerField(label="C) Předpokládám, že lidé mají jen ty nejlepší úmysly.",
                              choices=C.choice3)
    WP9 = models.IntegerField(label="D) Jsem dobrý v matematice.",
                              choices=C.choice3)
    WP10 = models.IntegerField(label="E) Mám sklony věci odkládat, i přesto že vím, že by bylo lepší je udělat rovnou.",
                              choices=C.choice3)
    WP11 = models.StringField(label="Zamyslete se, prosím, nad tím, co byste dělali v následující situaci. Nacházíte se v místě, které neznáte a zjistíte, že jste se ztratili. Zeptáte se cizího člověka na směr a on vám nabídne, že vás dovede na místo, kam potřebujete. To, že vám tento člověk pomůže, jej přijde celkem na 200 Kč; nicméně tvrdí, že od vás žádné peníze nechce. Máte s sebou šest dárků. Nejlevnější dárek stojí kolem 50 Kč, nejdražší stojí kolem 300 Kč. Dáte tomuto cizímu člověku jeden z dárků jako odměnu? (PŘEČTĚTE 2-7)  ",
                              choices=[[1,"1 - Ne, nedal/a bych mu žádný dárek "], [2,"2 - Dárek v ceně 50 Kč  "],[3,"3 - Dárek v ceně 100 Kč  "],[4,"4 - Dárek v ceně 150 Kč  "],[5,"5 - Dárek v ceně 200 Kč  "],[6,"6 - Dárek v ceně 250 Kč  "],[7,"7 - Dárek v ceně 300 Kč  "],[9,"9 - (Neví/Žádná odpověď)  "]])

    WP12 = models.IntegerField(label="Představte si následující situaci: Dnes jste úplně neočekávaně získali 12 000 Kč. Kolik z této částky věnujete na dobročinné účely? (Povolené hodnoty jsou v rozmezí 0 až 12000)  ",
                               min=0,max=12000)




    Pohlavi = models.StringField(choices=["Žena", "Muž"]
                            ,widget=widgets.RadioSelectHorizontal,
                            label="Jaké je vaše pohlaví: ")
    Vek = models.IntegerField(label="Jaký je Váš věk?",min=1,max=99)
    Prijem = models.StringField(label="Kolik peněz můžete měsíčně utratit na své soukromé potřeby? ",
                                 choices=["Méně než 1000 Kč ","1000 – 2000 Kč ","2000 – 5000 Kč ","Více než 5000 Kč" ],
                                widget=widgets.RadioSelectHorizontal,)
    Obor = models.StringField(label="Studujete na Ekonomicko-správní fakultě? ",
                              widget=widgets.RadioSelectHorizontal,
                              choices=["Ano","Ne"])
    Znamky = models.StringField(label="Odhadněte, jaký byl váš průměr známek v posledním roce?",
                               widget=widgets.RadioSelectHorizontal,
                               choices=["1-1,5","1,51-2","2,01-2,5","2,51-3","3,01-3,5","3,51-4"]
                               )
    Narozeni = models.StringField(label="V jakém měsíci jste se narodil/a ",
                                  choices=["Leden","Únor","Březen","Duben","Květen","Červen","Červenec","Srpen","Září","Říjen","Listopad","Prosinec"])
    DenNarozeni = models.StringField(label="Kolikátý den v měsíci jste se narodili? ",
                                     choices=["1-5","6-10","11-15", "16-20", "21-25","26-31"],
                                     widget=widgets.RadioSelectHorizontal,)
    PrvniTrida = models.StringField(label="V kolika letech jste šli do první třídy? ",
                                    choices=["5","6","7","8"])


    Porucha = models.StringField(label="Diagnostikovali Vám poruchu učení nebo pozornosti´?",
                                 widget=widgets.RadioSelectHorizontal,
                                 choices=["Ne", "Ano"])
    TypPoruchy = models.StringField(label="Pokud ano jakou?",
                                    choices=["Dyslexie", "Dysgrafie", "Dyskalkulie", "ADHD","Jiné-uveďte jakou:"],
                                    blank=True,
                                    widget=widgets.RadioSelect)
    TypPoruchyJina = models.StringField(label="",
                                        blank=True)

# PAGES
class MyPage(Page):
    form_model = Player
    form_fields = ["pt1", "pt2","pt3", "pt4","pt5", "pt6","pt7", "pt8","pt9", "pt10","pt11", "pt12","pt13", "pt14","pt15", "pt16",
                   "pt17", "pt18","pt19", "pt20","pt21", "pt22","pt23", "pt24","pt25", "pt26","pt27", "pt28","pt29", "pt30","pt31", "pt32",
                   "pt33", "pt34","pt35", "pt36","pt37", "pt38","pt39", "pt40","pt41", "pt42","pt43", "pt44", "pt45", "pt46","pt47", "pt48",
                   "pt49", "pt50","pt51", "pt52","pt53", "pt54","pt55", "pt56","pt57", "pt58","pt59", "pt60"]



class FinDot(Page):
    form_model = Player
    form_fields = ["Pohlavi","Vek","Prijem", "Obor","Znamky", "Narozeni","DenNarozeni","PrvniTrida","Porucha","TypPoruchy","TypPoruchyJina"]


class Results(Page):
    form_model = Player
    form_fields = ["mv1","mv2","mv3","mv4","mv5","mv6","mv7","mv8","mv9","mv10","mv11","mv12","mv13","mv14","mv15","mv16"]

class MV2part(Page):
    form_model = Player
    form_fields = ["mv17", "mv18", "mv19", "mv20", "mv21", "mv22", "mv23", "mv24", "mv25", "mv26", "mv27", "mv28", "mv29",
                   "mv30", "mv31", "mv32"]

class WPPage(Page):
    form_model = Player
    form_fields = ["WP1","WP2","WP3","WP4","WP5","WP6","WP7","WP8","WP9","WP10","WP11","WP12"]


class StopPage(Page):
    pass



page_sequence = [StopPage, MyPage,Results,MV2part,WPPage,FinDot]
