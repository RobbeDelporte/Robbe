"""
--Getallen raden door Robbe Delporte
--robbedelporte@hotmail.com
--8/10/2017
"""

import random

print('\n--Type "stop" in op elk moment in het spel om te stoppen met spelen.--')
naam = input('Wat is jouw naam?\n')

while 1:

    print('\n')
    willekeurig_getal = random.randint(1,100)
    aantal_pogingen = 0

    #Blijft herhalen todat max_aantal_pogingen een nummer is.
    max_aantal_pogingen = 'a'
    while not max_aantal_pogingen.isnumeric():
        max_aantal_pogingen = input('Hoeveel pogingen denk je dat je mag hebben om het getal te raden? ')
    max_aantal_pogingen = int(max_aantal_pogingen)

    #debug
    print(f'{willekeurig_getal}')

    #Deze loop blijft runnen todat de gok correct is OF todat er geen meer pogingen zijn OF todat 'stop' ingetypt wordt.
    gok = 'a'
    while gok != willekeurig_getal and aantal_pogingen != max_aantal_pogingen:

        print(f'Je hebt {max_aantal_pogingen - aantal_pogingen} pogingen over.')
       
        #Blijft herhalen todat gok een nummer OF 'stop' is.
        gok = 'a'
        while not gok.isnumeric() and gok != 'stop':
            gok = input(f'\nWat denk je dat het getal is, {naam}? ')
        if gok == 'stop':
            break
        gok = int(gok)
        aantal_pogingen += 1

        #Is het getal groter of kleiner?
        if gok > willekeurig_getal:
            print(f'\n{gok} is groter dan het getal')
        elif gok < willekeurig_getal:
            print(f'\n{gok} is kleiner dan het getal')
        
    #Er zijn 3 mogelijkheden waarop een ronde kan eindigen, bijpassende tekst wordt gedisplayed.
    if gok == 'stop':
        break
    elif gok == willekeurig_getal:
        print(f'\nInderdaad {naam}, {gok} is het juiste getal.\nJe had {aantal_pogingen} pogingen nodig.')
    else:
        print(f'\nJe pogingen zijn helaas op {naam}. {willekeurig_getal} was het juiste getal. \n')