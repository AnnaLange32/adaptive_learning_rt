''' DATABASE: Pepper speech blocks'''


# INTRODUCTION

intro_text1 = ("^mode(cotextual) Hi, ich bin Pepper und ich werde heute dein Lehrer sein.")
intro_beh1 = ''
intro_t11 = 0
intro_t12 = 2

intro_text2 = (" ^mode(disabled) Ich freue mich sehr, ^mode(contextual) dass du hier bist und ^mode(disabled) wir gemeinsam ein Spiel spielen werden!")
intro_beh2 = ''
intro_t21 = 0
intro_t22 = 1.5

intro_text3 = (" ^mode(random) Meine Kollegin hat dir sicher schon ein wenig erzaehlt, ^mode(disabled) aber ich ^mode(contextual) erklaere dir das Spiel gerne nochmal.") # ^start(p50_study1-5ba9db/behavior 1)
intro_beh3 = ''
intro_t31 = 0
intro_t32 = 0

intro_text4 = ("Wie du sehen kannst, gibt es in diesem Raum viele Gegenstaende.")
intro_beh4 = 'p50_study1-5ba9db/behavior 1'
intro_t41 = 2
intro_t42 = 2.5

intro_text5 = ("^mode(disabled) Deine Aufgabe wird es sein, die kleinen Gegenstaende dort, auf dem kleinen, weissen, Tisch, an bestimmten Stellen hier im Raum zu positionieren.")
intro_beh5 = 'p50_study1-5ba9db/behavior 4'
intro_t51 = 0
intro_t52 = 2

intro_text6 = ("^mode(contextual) Moegliche Stellen erkennst du an quadratischen, weissen Boxen,")
intro_beh6 = ''
intro_t61 = 0
intro_t62 = 0

intro_text7 = ("wie zum Beispiel dieser hier. ")
intro_beh7 = 'p50_study1-5ba9db/behavior 2'
intro_t71 = 2.5
intro_t72 = 5

intro_text8 = ("^mode(contextual)  Wie du siehst, sind diese im ganzen Raum verteilt. Bitte stelle ^mode(disabled)  die Gegenstaende auch wirklich immer nur auf diese Boxen.  ^mode(contextual) Alles andere waere keine richtige Platzierung. ^mode(disabled) Ausserdem, kann ich dir sonst kein Feedback geben.")
intro_beh8 = ''
intro_t81= 0
intro_t82 = 2

intro_text9 = ("^mode(contextual) Jeder Gegenstand hat genau eine korrekte Position und dein Ziel ist es, diese herauszufinden und den Gegenstand auch dort zu platzieren.")
intro_beh9 = ''
intro_t91= 0
intro_t92 = 0

intro_text10 = ("Soweit klar, oder?")
intro_beh10 = 'p50_study1-5ba9db/behavior 3'
intro_t101= 2
intro_t102 = 4

intro_text11 = (" ^mode(disabled) Damit es aber nicht zu einfach fuer dich ist, werde ich ^mode(contextual) dir in einer Fremdsprache sagen, wo du die Gegenstaende hinstellen musst. ^mode(contextual) Und zwar in Swahili - einer Sprache, die in vielen Laendern Ost- und Zentralafrikas, ^mode(disabled) wie Kenia und, Tansania, gesprochen wird.")
intro_text11 = (" ^mode(disabled) Damit es aber nicht zu einfach fuer dich ist, werde ich ^mode(contextual) dir in einer Fremdsprache sagen, wo du die Gegenstaende hinstellen musst. ^mode(contextual) Und zwar in Swahili - einer Sprache, die in vielen Laendern Ost- und Zentralafrikas, ^mode(disabled) wie Kenia und, Tansania, gesprochen wird.")
intro_beh11 = ''
intro_t111= 0
intro_t112 = 2

intro_text12 = (" ^mode(disabled) Aber keine Sorge wenn du gar keine Ahnung von Swahili hast. ^mode(contextual)  Das ist sogar wichtig, damit das Spiel richtig funktioniert und du auch ein bisschen raetseln musst.  ^mode(disabled) Aber lass mich dir ein paar Beispiele geben, damit du verstehst, wie es ablaufen wird.")
intro_beh12 = ''
intro_t121= 0
intro_t122 = 0


# full intro script

robot_intro = [
    [intro_t11, intro_text1, intro_beh1, intro_t12],
    [intro_t21, intro_text2, intro_beh2, intro_t22],
    [intro_t31, intro_text3, intro_beh3, intro_t32],
    [intro_t41, intro_text4, intro_beh4, intro_t42],
    [intro_t51, intro_text5, intro_beh5, intro_t52],
    [intro_t61, intro_text6, intro_beh6, intro_t62],
    [intro_t71, intro_text7, intro_beh7, intro_t72],
    [intro_t81, intro_text8, intro_beh8,intro_t82],
    [intro_t91, intro_text9, intro_beh9, intro_t92],
    [intro_t101, intro_text10, intro_beh10, intro_t102],
    [intro_t111, intro_text11, intro_beh11, intro_t112],
    [intro_t121, intro_text12, intro_beh12, intro_t122]]



# EXAMPLES


ex_text1 = ("^mode(cotextual) \\emph=2\\ Dort, auf dem kleinen, Tisch, steht zum Beispiel eine Flasche. Auf Swahili: tschupa.")
ex_beh1 = 'p50_study1-5ba9db/behavior 4'
ex_t11 = 3
ex_t12 = 1

ex_text2 = ("^mode(contextual) Wenn du jetzt im Spiel die Flasche irgendwo platzieren wollen wuerdest, muesstest du sie erst einmal auf die weisse Box dort auf dem kleinen, Tisch, stellen. Ich ^mode(disabled) wuerde dir dann sagen")
ex_beh2 = ''
ex_t21 = 0
ex_t22 = 1

ex_text3 = ('\\rspd=70\\ tschupa, kwenje, raafu')
ex_beh3 = ''
ex_t31 = 0
ex_t32 = 1

ex_text4 = ("\\rspd=85\\was so viel bedeutet wie 'Flasche, auf, Regal'.")
ex_beh4 = ''
ex_t41 = 0
ex_t42 = 1

ex_text5= ("^mode(contextual) Also muesstest du die Flasche auf die weisse Box dort auf dem Regal stellen.")  # behavior 5
ex_beh5 = 'p50_study1-5ba9db/behavior 5'
ex_t51 = 0.2
ex_t52 = 1

ex_text6 = ("^mode(contextual) Um die Bedeutung herauszufinden, musst du aber natuerlich erstmal verschiedene Positionen ausprobieren.")
ex_beh6 = ''
ex_t61 = 0
ex_t62 = 0.5

ex_text7 = ("^mode(contextual) Wenn du die Flasche an eine falsche Position stellst, zum Beispiel hier unter den Tisch") # behavior 6
ex_beh7 = 'p50_study1-5ba9db/behavior 6'
ex_t71 = 0.5
ex_t72 = 2

ex_text8 = ("^mode(disabld)  sage ich dir auch, wo die Flasche gerade steht. ^mode(contextual) Also, um bei dem Beispiel zu bleiben wuerde ich sagen:")
ex_beh8 = ''
ex_t81 = 0
ex_t82 = 2

ex_text9 = ('^mode(disabled) \\rspd=70\\ tschupa, tschini ja, meessa.')
ex_beh9 = ''
ex_t91 = 0
ex_t92 = 1

ex_text10 = ("\\rspd=85\\ aber das ist falsch.")
ex_beh10 = ''
ex_t101 = 0
ex_t102 = 1

ex_text11 = ("^mode(disabled) Nach einer falschen Plazierung, kannst du natuerlich weiter ausprobieren. Du kannst aber auch erstmal einen anderen Gegenstand waehlen. Denk daran, diesen erst einmal auf die Startbox zu stellen. ^mode(contextual) Bitte bewege aber immer nur einen Gegenstand nach dem anderen.")
ex_beh11 = ''
ex_t111 = 0
ex_t112 = 1

ex_text12 = ("^mode(contextual) Vieles wird sich auch im Laufe des Spieles ergeben, also fangen wir vielleicht einfach an. ")
ex_beh12 = ''
ex_t121 = 0
ex_t122 = 1

ex_text13 = ("^mode(random)   Ich freu mich drauf, mit dir zu spielen, du auch?") # behavior 3
ex_beh13 = 'p50_study1-5ba9db/behavior 3'
ex_t131 = 0.2
ex_t132 = 2

ex_text14 = ("^mode(disabled) Ich hoffe, du wirst Spass an dem Spiel haben!")
ex_beh14 = ''
ex_t141 = 0
ex_t142 = 1

ex_text15 = ("^mode(contextual)  In regelmaessigen Zeitabstaenden ^mode(disabled) werde ich dich waehrend des Spiels fragen, ^mode(contextual) wie stark du bestimmte Gefuehle  ^mode(disabled) im Moment empfindest.")
ex_beh15 = ''
ex_t151 = 0
ex_t152 = 0

ex_text16 = ("^mode(contextual)  Druecke dafuer einfach die am besten passende Antwort auf diesem Bildschirm auf meiner Brust.") # behavior 7
ex_beh16 = 'p50_study1-5ba9db/behavior 7'
ex_t161 = 0.5
ex_t162 = 1

ex_text17 = ("^mode(contextual)  Links bedeutet ueberhaupt nicht und rechts bedeutet sehr stark. Lass es uns direkt mal ausprobieren!")
ex_beh17 = 'p50_study1-5ba9db/assessment all emotions'
ex_t171 = 0
ex_t172 = 0


ex_text18 = (" \\vct=130\\ Super, \\vct=110\\ dann fangen wir jetzt an! Such dir einen ersten Gegenstand aus und. \\vct=130\\  los  \\vct=140\\  geht \\vct=150\\ es!")
ex_beh18 = ''
ex_t181 = 1
ex_t182 = 1


# full examples script

robot_ex1 = [
    [ex_t11, ex_text1, ex_beh1, ex_t12],
    [ex_t21, ex_text2, ex_beh2, ex_t22],
    [ex_t31, ex_text3, ex_beh3, ex_t32],
    [ex_t41, ex_text4, ex_beh4, ex_t42],
    [ex_t51, ex_text5, ex_beh5, ex_t52],
    [ex_t61, ex_text6, ex_beh6, ex_t62],
    [ex_t71, ex_text7, ex_beh7, ex_t72],
    [ex_t81, ex_text8, ex_beh8,ex_t82],
    [ex_t91, ex_text9, ex_beh9, ex_t92],
    [ex_t101, ex_text10, ex_beh10, ex_t102],
    [ex_t111, ex_text11, ex_beh11, ex_t112],
    [ex_t121, ex_text12, ex_beh12, ex_t122],
    [ex_t131, ex_text13, ex_beh13, ex_t132],
    [ex_t141, ex_text14, ex_beh14, ex_t142],
    [ex_t151, ex_text15, ex_beh15, ex_t152],
    [ex_t161, ex_text16, ex_beh16, ex_t162],
    [ex_t171, ex_text17, ex_beh17, ex_t172],
]

robot_ex2 = [[ex_t181, ex_text18, ex_beh18, ex_t182]]
# CONDITION 1

# weiter geht's part

con11_text1 = ("Weiter geht's!")
con11_beh1 = 'p50_study1-5ba9db/behavior 10'
con11_t11 = 1
con11_t12 = 1

con11_text2 = ("Ich kann dir nur Rueckmeldung geben, wenn du eine Platzierung vornimmst.")
con11_beh2 = ''
con11_t21 = 0
con11_t22 = 0

robot_con11 = [[con11_t11, con11_text1, con11_beh1, con11_t12], [con11_t21, con11_text2, con11_beh2, con11_t22]]

# emotion part

con12_text1 = ('Entschuldigung fuer die kurze Unterbrechung, koenntest du deine Gefuehle auf meinem Bildschirm eingeben?')
con12_beh1 = 'p50_study1-5ba9db/assessment all emotions'
con12_t11 = 0
con12_t12 = 0

con13_text1 = ('Weiter geht es.')
con13_beh1 = ''
con13_t11 = 1
con13_t12 = 0

robot_con12 = [[con12_t11, con12_text1, con12_beh1, con12_t12]]
robot_con13 = [[con13_t11, con13_text1, con13_beh1, con13_t12]]

# object recognition part

con14_text1 = ('Das ist:')
con14_beh1 = 'p50_study1-5ba9db/behavior 8'
con14_t11 = 0.5
con14_t12 = 0.2

con15_text1 = ('Bitte platziere das Objekt an der folgenden Stelle: ')
con15_beh1 = ''
con15_t11 = 0.5
con15_t12 = 0

robot_con14 = [[con14_t11, con14_text1, con14_beh1, con14_t12]]
robot_con15 = [[con15_t11, con15_text1, con15_beh1, con15_t12]]

# object placement part

con16_text1 = ('^mode(cotextual) Diese Platzierung ist: ')
con16_beh1 = ''
con16_t11 = 0.2
con16_t12 = 0.5

con17_text1 = ('^mode(cotextual) Super! Das ist korrekt! Du kannst nun mit einem anderen Objekt weitermachen.')
con17_beh1 = 'p50_study1-5ba9db/behavior 9'
con17_t11 = 4
con17_t12 = 0

robot_con16 = [[con16_t11, con16_text1, con16_beh1, con16_t12]]
robot_con17 = [[con17_t11, con17_text1, con17_beh1, con17_t12]]

con18_text1 = ('^mode(cotextual) Diese Platzierung ist: ')
con18_beh1 = ''
con18_t11 = 0.2
con18_t12 = 0.5

con19_text1 = ('^mode(cotextual) Aber das ist falsch. Die korrekte Platzierung lautet:')
con19_beh1 = ''
con19_t11 = 1
con19_t12 = 0.5

robot_con18 = [[con18_t11, con18_text1, con18_beh1, con18_t12]]
robot_con19 = [[con19_t11, con19_text1, con19_beh1, con19_t12]]

# Additional random hints

con21_text1 = ('Wie koenntest du die Saetze in kleinere Teile zerlegen? Vielleicht macht es die Aufgabe einfacher, wenn du das mal versuchst.')
con21_beh1 = ''
con21_t11 = 0
con21_t12 = 0.5

con22_text1 = ('Ueberleg doch mal: Wie koennte man die einzelnen Woerter in eine logische Struktur bringen?')
con22_beh1 = ''
con22_t11 = 0
con22_t12 = 0.5

con23_text1 = ('Was denkst du sind die wichtigsten Woerter aus meiner vorherigen Aussage um die Aufgabe zu loesen? ueberlege, auf welche du dich nun besonders gut fokussieren solltest.')
con23_beh1 = ''
con23_t11 = 0
con23_t12 = 0.5

con24_text1 = ('Betrachte die Beziehungen zwischen den einzelnen Woertern. Wie kannst du sie kategorisieren und verbinden, um eine logische Ordnung zu schaffen?')
con24_beh1 = ''
con24_t11 = 0
con24_t12 = 0.5

con25_text1 = ('Schau dir die Beziehungen zwischen den einzelnen Woertern an. Erkennst du eine logische Struktur oder ein Muster?')
con25_beh1 = ''
con25_t11 = 0
con25_t12 = 0.5

con26_text1 = ('Denke ueber Beispiele nach, um das bisher Gelernte zu verknuepfen. Wie wuerdest du beispielsweise im Englischunterricht in der Schule vorgehen, um dir Vokabeln besser zu behalten?')
con26_beh1 = ''
con26_t11 = 0
con26_t12 = 0.5

con27_text1 = ('Hast du vielleicht schon einmal eine aehnliche Aufgabe in anderen Lernsituationen oder im Alltag gemacht? Probiere mal, ob du bereits vorhandenes Wissen auf die aktuelle Aufgabe anwenden kannst.')
con27_beh1 = ''
con27_t11 = 0
con27_t12 = 0.5

con28_text1 = ('Welche Woerter denkst du sind entscheidende Schluesselwoerter, um diese Aufgabe zu loesen? Achte genau auf meine Aussagen.')
con28_beh1 = ''
con28_t11 = 0
con28_t12 = 0.5

con29_text1 = ('Erkennst du Unterschiede oder Gemeinsamkeiten zu anderen Sprachen, die schon kennst oder gelernt hast?')
con29_beh1 = ''
con29_t11 = 0
con29_t12 = 0.5

con210_text1 = ('Kannst du diese Woerter irgendwie mit deinen eigenen Erfahrungen verknuepfen? Vielleicht koenntest du versuchen, Eselsbruecken zu bauen, um sie dir besser zu merken.')
con210_beh1 = ''
con210_t11 = 0
con210_t12 = 0.5

con211_text1 = ('Ueberlege dir, welche Woerter du noch nicht gut verstanden hast. ')
con211_beh1 = ''
con211_t11 = 0
con211_t12 = 0.5

con212_text1 = ('Wie kannst du dir dein Verstaendnisproblem am besten erklaeren?')
con212_beh1 = ''
con212_t11 = 0
con212_t12 = 0.5

con213_text1 = ('Gibt es noch Woerter, deren Bedeutung dir bisher nicht bekannt sind oder die noch nicht ganz klar fuer dich sind?')
con213_beh1 = ''
con213_t11 = 0
con213_t12 = 0.5

con214_text1 = ('Gibt es noch Woerter, deren Bedeutung dir bisher nicht bekannt sind oder die noch nicht ganz klar fuer dich sind?')
con214_beh1 = ''
con214_t11 = 0
con214_t12 = 0.5

con215_text1 = ('Was hat dich dazu gebracht, den Gegenstand dorthin zu stellen? Versuch mal, deine Schritte zu ueberdenken und zu hinterfragen.')
con215_beh1 = ''
con215_t11 = 0
con215_t12 = 0.5

con216_text1 = ('Was koenntest du tun, um die Aufgabe besser zu bewaeltigen? ueberleg, ob du moeglicherweise deine Herangehensweise anpassen kannst.')
con216_beh1 = ''
con216_t11 = 0
con216_t12 = 0.5

con217_text1 = ('Welche Schritte hast du bisher unternommen? Denk nochmal darueber nach, welche dir besonders geholfen haben und warum das so war.')
con217_beh1 = ''
con217_t11 = 0
con217_t12 = 0.5

con218_text1 = ('Warum denkst du, ist es manchmal schwieriger, bestimmte Woerter zu verstehen als andere? Gibt es etwas, das dir dabei helfen koennte?')
con218_beh1 = ''
con218_t11 = 0
con218_t12 = 0.5

con219_text1 = ('Ueberlege, wie du deine Herangehensweise anpassen koenntest, um die Aufgabe moeglicherweise zielfuehrender zu bewaeltigen.')
con219_beh1 = ''
con219_t11 = 0
con219_t12 = 0.5

con220_text1 = ('Welche Informationen koennten dir helfen, die Aufgabe besser zu loesen? Denk mal darueber nach und entscheide dann, welchen Schritt du als naechstes machen koenntest.')
con220_beh1 = ''
con220_t11 = 0
con220_t12 = 0.5

robot_con20 = [[con21_t11, con21_text1, con21_beh1, con21_t12], [con22_t11, con22_text1, con22_beh1, con22_t12],
               [con23_t11, con23_text1, con23_beh1, con23_t12], [con24_t11, con24_text1, con24_beh1, con24_t12],
               [con25_t11, con25_text1, con25_beh1, con25_t12], [con26_t11, con26_text1, con26_beh1, con26_t12],
               [con27_t11, con27_text1, con27_beh1, con27_t12], [con28_t11, con28_text1, con28_beh1, con28_t12],
               [con29_t11, con29_text1, con29_beh1, con29_t12], [con210_t11, con210_text1, con210_beh1, con210_t12],
               [con211_t11, con211_text1, con211_beh1, con211_t12], [con212_t11, con212_text1, con212_beh1, con212_t12],
               [con213_t11, con213_text1, con213_beh1, con213_t12], [con214_t11, con214_text1, con214_beh1, con214_t12],
               [con215_t11, con215_text1, con215_beh1, con215_t12], [con216_t11, con216_text1, con216_beh1, con216_t12],
               [con217_t11, con217_text1, con217_beh1, con217_t12], [con218_t11, con218_text1, con218_beh1, con218_t12],
               [con219_t11, con219_text1, con219_beh1, con219_t12], [con220_t11, con220_text1, con220_beh1, con220_t12]]


# Motivational messages


con31_text1 = ('Wenn du dich konzentrierst, wird das Spiel noch interessanter fuer dich werden. Mach weiter so!') #sounds a bit odd
con31_beh1 = ''
con31_t11 = 0
con31_t12 = 0.5

con32_text1 = ('Bleib dran, du kannst es schaffen! Das Spiel wird noch schoener, wenn du dich noch ein wenig anstrengst.')
con32_beh1 = ''
con32_t11 = 0
con32_t12 = 0.5

con33_text1 = ('Je besser man zuhoert, desto mehr Spass macht das Spiel. Aber du machst das schon richtig gut!')
con33_beh1 = ''
con33_t11 = 0
con33_t12 = 0.5

con34_text1 = ('Keine Sorge! Wenn du jetzt trotz Fehler dranbleibst, dann wirst du gut vorankommen und das Spiel richtig toll meistern.')
con34_beh1 = ''
con34_t11 = 0
con34_t12 = 0.5

con35_text1 = ('Du hast bisher sicher schon eine Menge Neues gelernt. Wenn du so weiter machst, wirst du ueber dich selbst hinauswachsen!')
con35_beh1 = ''
con35_t11 = 0
con35_t12 = 0.5

con36_text1 = ('Es ist normal, dass bei dieser Aufgabe mal Fehler passieren. Konzentriere dich weiter, dann zahlt sich das fuer dich aus!')
con36_beh1 = ''
con36_t11 = 0
con36_t12 = 0.5

con37_text1 = ('Du schaffst das! Wenn du mir gut zuhoerst, wirst du bald von alleine weiterspielen wollen, weil du dabei so viel Neues lernen kannst.')
con37_beh1 = ''
con37_t11 = 0
con37_t12 = 0.5

con38_text1 = ('Lass dich nicht entmutigen! Wenn du weiterhin so gut dranbleibst, kannst du durch das Spiel super dein logisches Denken trainieren.')
con38_beh1 = ''
con38_t11 = 0
con38_t12 = 1

con39_text1 = ('Du hast das bisher schon gut gemeistert. Bleib dran - die Inhalte des Spiels sind relevant fuer deinen Lernprozess, weil du dir wichtiges Wissen aneignest.')
con39_beh1 = ''
con39_t11 = 0
con39_t12 = 0.5

con310_text1 = ('Du hast die Aufgaben super geloest. Bleib dran, du lernst hier viel Neues.')
con310_beh1 = ''
con310_t11 = 0
con310_t12 = 1

con311_text1 = ('Du hast das Thema schon gut verstanden und wenn du dranbleibst, kannst du dein Wissen noch weiter erweitern und wirst Dinge lernen, die fuer deine Zukunft nuetzlich sind.')
con311_beh1 = ''
con311_t11 = 0
con311_t12 = 1

con312_text1 = ('Das war nicht richtig, aber das ist kein Problem. Fehler sind sinnvolle Lerngelegenheiten und du lernst in diesem Spiel Dinge, die fuer dich persoenlich nuetzlich sein koennen.')
con312_beh1 = ''
con312_t11 = 0
con312_t12 = 1



robot_con30 = [[con31_t11, con31_text1, con31_beh1, con31_t12], [con32_t11, con32_text1, con32_beh1, con32_t12],
               [con33_t11, con33_text1, con33_beh1, con33_t12], [con34_t11, con34_text1, con34_beh1, con34_t12],
               [con35_t11, con35_text1, con35_beh1, con35_t12], [con36_t11, con36_text1, con36_beh1, con36_t12],
               [con37_t11, con37_text1, con37_beh1, con37_t12], [con38_t11, con38_text1, con38_beh1, con38_t12],
               [con39_t11, con39_text1, con39_beh1, con39_t12], [con310_t11, con310_text1, con310_beh1, con310_t12],
               [con311_t11, con311_text1, con311_beh1, con311_t12], [con312_t11, con312_text1, con312_beh1, con312_t12]
               ]

# Personalized hints  I NEED TO INCLUDE HINTS THAT ASSUME PART OF POSITION IS CORRECT

# Location

con40_text1 = ('Wie koenntest du die Saetze in kleinere Teile zerlegen? Vielleicht macht es die Aufgabe einfacher, wenn du das mal versuchst. Bei diesem Fehler gerade haette dir zum Beispiel besonders das letzte Wort helfen koennen.')
con40_text2 = ('')
con40_t11 = 0
con40_t12 = 0.5

con41_text1 = ('Du haettest wissen koennen, dass dies nicht der richtige Ort fuer')
con41_text2 = ('sein kann. Erkennst du vielleicht Unterschiede oder Gemeinsamkeiten zu anderen Sprachen, die du schon kennst oder gelernt hast?')
con41_t11 = 0
con41_t12 = 0.5

con44_text1 = ('Du hast richtig erkannt, dass du diesen Gegenstand ')  # This hint depens on the correct preposition and previous knowledge of the location
con44_text2 = ('ein anderes Objekt setzen musst, aber nicht dort. Ueberlege dir, welche Woerter du bereits gut verstanden hast.')
con44_t11 = 0
con44_t12 = 0.5

con43_text1 = ('Schau dir deinen letzten Schritt noch einmal genau an. Was hat dich dazu gebracht,')
con43_text2 = ('dorthin zu stellen? Versuch mal, deine Schritte zu ueberdenken und zu hinterfragen. Du haettest naemlich wissen koennen, dass es nicht korrekt ist.')
con43_t11 = 0
con43_t12 = 0.5

con42_text1 = ('Schade, aber der Fehler haette vermieden werden koennen. Welche Informationen haetten dir helfen koennen, die Aufgabe besser zu loesen? Denk mal darueber nach und entscheide dann, welchen Schritt du als naechstes machen koenntest.')
con42_text2 = ('')
con42_t11 = 0
con42_t12 = 0.5

robot_con40 = [[con40_t11, con40_text1, con40_text2, con40_t12], [con41_t11, con41_text1, con41_text2, con41_t12],
                [con42_t11, con42_text1, con42_text2, con42_t12], [con43_t11, con43_text1, con43_text2, con43_t12],
               [con44_t11, con44_text1, con44_text2, con44_t12]]


# Preposition

con50_text1 = ('Was denkst du sind die wichtigsten Woerter aus meiner vorherigen Aussage um die Aufgabe zu loesen? ueberlege, auf welche du dich nun besonders gut fokussieren solltest. Achte vor allem auf das Wort in der Mitte, denn dort lag dein Fehler.')
con50_text2 = ('')
con50_t11 = 0
con50_t12 = 0.5

con51_text1 = ('Welche Woerter denkst du sind entscheidende Schluesselwoerter, um diese Aufgabe zu loesen? Achte genau auf meine Aussagen. Wenn du aufmerksam zugehoert haettest, haettest du naemlich wissen koennen, dass dies nicht der richtige Ort  fuer ')
con51_text2 = ('sein kann')
con51_t11 = 0
con51_t12 = 0.5

con52_text1 = ('Wie du hoeren kannst, stimmt der mittlere Teil des Satzes nicht und das haettest du wissen koennen. Kannst du die Woerter irgendwie mit deinen eigenen Erfahrungen verknuepfen? Vielleicht koenntest du versuchen, Eselsbruecken zu bauen, um sie dir besser zu merken.')
con52_text2 = ('')
con52_t11 = 0
con52_t12 = 0.5

con53_text1 = ('Denk noch einmal darueber nach, was ich gerade gesagt habe, und achte besonders auf das mittlere Wort im Satz. Ueberlege dir, welche Woerter du noch nicht gut verstanden hast.')
con53_text2 = ('')
con53_t11 = 0
con53_t12 = 0.5

con54_text1 = ('Wie du hoeren kannst, ist')
con54_text2 = ('korrekt. Nur irgendwas passt noch nicht ganz, oder? Du haettest es wissen koennen. Denk nochmal ueber deine bisherigen Schritte nach, und ueberlege, welche dir besonders geholfen haben und warum das so war.')
con54_t11 = 0
con54_t12 = 0.5

robot_con50 = [[con50_t11, con50_text1, con50_text2, con50_t12], [con51_t11, con51_text1, con51_text2, con51_t12],
               [con52_t11, con52_text1, con52_text2, con52_t12], [con53_t11, con53_text1, con53_text2, con53_t12],
               [con54_t11, con54_text1, con54_text2, con54_t12]]

# Preposition and location or repeated placement: different object

con60_text1 = ('Kannst du Parallelen zwischen diesem und einem vorherigen Fehler erkennen? Denk an die einzelnen Woerter wie an Perlen auf einer Perlenkette. Wie koennten sie anders zusammengefuegt werden, um andere sinnvolle Muster zu ergeben?')
con60_text2 = ('')
con60_t11 = 0
con60_t12 = 0.5

con61_text1 = ('Du hast diese Platzierung bereits zuvor mit einem anderen Gegenstand versucht. Hast du vielleicht schon einmal eine aehnliche Aufgabe in anderen Lernsituationen oder im Alltag gemacht? Probiere mal, ob du bereits vorhandenes Wissen auf die aktuelle Aufgabe anwenden kannst um somit solche Fehler zu vermeiden.')
con61_text2 = ('')
con61_t11 = 0
con61_t12 = 0.5

con62_text1 = ('Dieser Fehler aehnelt einem frueheren, den du mit einem anderen Gegenstand gemacht hast. ueberlege, welche Fragen fuer dich noch offen sind und welche Bedeutungen deiner Meinung nach noch nicht ausreichend geklaert wurden.')
con62_text2 = ('')
con62_t11 = 0
con62_t12 = 0.5

con63_text1 = ('Gibt es noch Woerter, deren Bedeutung dir bisher nicht bekannt sind oder die noch nicht ganz klar fuer dich sind? Dieser Fehler aehnelt naemlich einem frueheren, den du mit einem anderen Gegenstand gemacht hast.')
con63_text2 = ('')
con63_t11 = 0
con63_t12 = 0.5

con64_text1 = ('Einen aehnlichen Fehler hast du schonmal gemacht, daher haette dieser vermieden werden koennen. Warum denkst du, ist es manchmal schwieriger, bestimmte Woerter zu verstehen als andere? Gibt es etwas, das dir dabei helfen koennte?')
con64_text2 = ('')
con64_t11 = 0
con64_t12 = 0.5

robot_con60 = [[con60_t11, con60_text1, con60_text2, con60_t12], [con61_t11, con61_text1, con61_text2, con61_t12],
               [con62_t11, con62_text1, con62_text2, con62_t12], [con63_t11, con63_text1, con63_text2, con63_t12],
               [con64_t11, con64_text1, con64_text2, con64_t12]]


# repeated placement

con70_text1 = ('Du hast diese Position schon einmal ausprobiert. ueberleg doch mal: Wie koennte man die einzelnen Woerter in eine logische Struktur bringen? So koenntest du solche Wiederholungsfehler vermeiden.')
con70_text2 = ('')
con70_t11 = 0
con70_t12 = 0.5

con71_text1 = ('Aber ich denke, das solltest du bereits wissen, oder nicht? Merke dir, was ich dir sage und schau dir die Beziehungen zwischen den einzelnen Woertern an. Erkennst du eine logische Struktur oder ein Muster?')
con71_text2 = ('')
con71_t11 = 0
con71_t12 = 0.5

con72_text1 = ('Schade, dass dieser Fehler wiederholt aufgetreten ist. Denke ueber Beispiele nach, um das bisher Gelernte zu verknuepfen. Wie wuerdest du beispielsweise im Englischunterricht in der Schule vorgehen, um dir Vokabeln besser zu behalten?')
con72_text2 = ('')
con72_t11 = 0
con72_t12 = 0.5

con73_text1 = ('Ich bin mir ziemlich sicher, dass ich dir das schon einmal gesagt habe. Wie kannst du dir dein Verstaendnisproblem am besten erklaeren? ')
con73_text2 = ('')
con73_t11 = 0
con73_t12 = 0.5

con74_text1 = ('Kannst du erkennen, ob es Muster in deinen Handlungen gibt, die dazu fuehren, dass du denselben Fehler wiederholst? ueberlege, wie du deine Herangehensweise anpassen koenntest, um die Aufgabe moeglicherweise zielfuehrender zu bewaeltigen.')
con74_text2 = ('')
con74_t11 = 0
con74_t12 = 0.5

robot_con70 = [[con70_t11, con70_text1, con70_text2, con70_t12], [con71_t11, con71_text1, con71_text2, con71_t12],
               [con72_t11, con72_text1, con72_text2, con72_t12], [con73_t11, con73_text1, con73_text2, con73_t12],
               [con74_t11, con74_text1, con74_text2, con74_t12]]


# End of experiment

con91_text1 = ("Perfekt, danke! Das war's tatsaechlich schon. Wir sind am Ende des Spiels angekommen. Ich hoffe, es hat dir Spass gemacht mit mir gemeinsam zu lernen. Bitte lass alle Gegenstaende nun so im Raum stehen wie sie sind. Meine Kollegin kommt dich jetzt abholen und wird dir nochmal ein paar Fragen stellen. Es hat mich gefreut, dich kennengelernt zu haben.")
con91_beh1 = ''
con91_t11 = 0.5
con91_t12 = 0.5

con92_text1 = ("Bis bald!")
con92_beh1 = 'p50_study1-5ba9db/behavior 11'
con92_t11 = 1.5
con92_t12 = 0

robot_con90 = [[con91_t11, con91_text1, con91_beh1, con91_t12], [con92_t11, con92_text1, con92_beh1, con92_t12]]