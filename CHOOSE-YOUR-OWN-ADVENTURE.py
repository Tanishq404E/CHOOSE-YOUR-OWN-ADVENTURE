def display():
    print("""
    HHHH    HHHH     EEEEEEEEE       LLL       LLL         OOOOOOOOOOOO
    HHHH    HHHH     EEEE            LLL       LLL         OOO      OOO
    HHHHHHHHHHHH     EEEEEEEEEEE     LLL       LLL         OOO      OOO
    HHHH    HHHH     EEEE            LLLLLLL   LLLLLLL     OOO      OOO
    HHHH    HHHH     EEEEEEEEEEEEE   LLLLLLL   LLLllll     OOOOOOOOOOOO
    """)

    print("""
    PPPPPPPPPP   LLL                  A             YYY             YYY    EEEEEEEEE    RRRRRRRRRR
    PP       P   LLL                 A A               YY         YY       EEE          RR      RR
    PP       P   LLL                A   A                YY     YY         EEE          RR      RR
    PPPPPPPPPP   LLL               AAAAAAA                 YY YY           EEEEEEEEE    RRRRRRRRRR
    PP           LLL              A       A                  YY            EEE          RR  RR
    PP           LLLLLLLLL       A         A                 YY            EEE          RR    RR
    PP           LLLLLLLLL      A           A                YY            EEEEEEEEE    RR      RR
    """)
    print()
    print("""    You wake up in the middle of the night to a deafening thunderclap and you are feeling thirsty, 
    but you soon realize that not everything is as it seems in the house tonight.
    Where has everyone gone? Your family is missing and strange things are lurking in the shadows.""")
    print("“It looks different in the dark.”")
display()
def main_story():
    print("""     You wake up startled as a deafening thunderclap roars over you.
        Your heart is racing but you lie frozen in the bed. Confused and disoriented.
        Where are you? What’s going on? You call out for your parents, 
        all you hear in return is the steady patter of gushing rain against the roof above 
        the ragged wind rattling the window panes. After a few moments of blinking in the darkness, 
        you start to remember. You’re at home, in your own room, in your own bed. You were 
        having some sort of nightmare but can’t quite remember what it was.
        You feel really thirsty, you really need to get some water.
        Unfortunately, you have to go down the hall…
        You are in your room, it’s too dark to see, but flashes of lighting outside the window 
        throw occasional flashes of bright light against the walls that illuminate recognizable 
        shapes: a chair here,  the toy chest there, the corkboard on the wall where you hang all the pictures.
        You can see a bed, a dresser, a chair and a digital clock.
    """)
    print("you have Choices, write in the same manner to avoid confusion")
    ch1=input("choose : GO DOWNSTAIRS TO GET WATER OR WAIT\n")
    if ch1.upper()=="GO DOWNSTAIRS TO GET WATER":
        print("""
        You open the door, darkness looming outside. You slowly walk out of your room, reaching the corridor. 
        As you move forward in the hallway, you hear a noise... a squeaky noise... A SQUEAKY VOICE. 
        Did you just hear a voice? Did someone call out your name?""")
        level2()
    elif ch1 =="WAIT":
        print("""You decide that your needs can wait, you are way too scared to leave your room. 
              As you try to fall asleep again, but instead of falling asleep your vision starts to blur, 
              you notice a strange darkness creeping in through the space beneath your door. 
              Panic sets in when you realise that you no longer can move, you are stuck there, with no way 
              to escape your fate. The darkness takes the form of a grotesque creature, its mouth lined 
              with jagged teeth, slowly creeping towards you. All you can do now to wait for your 
              imminent doom as the creature feasts on your fears and later YOU.""")
        print("GAME OVER")
        main_story()
    else:
        print("enter valid choice")
        main_story()
def level2():
    print("you have Choices")
    choice=input("CHOICE  : stay where you are or move forward.\n")
    if choice.lower()=="move forward":
        print("""You move forward …reach into the kitchen to get water.
                You open the top shelf of the cabinet to take out the glass. You are filling water in it and 
                suddenly you hear the sound of the kitchen door being closed. A LOUD BANG.""")
        level3()
    elif choice=="stay where you are":
        print("""You decide to stay where you are and to look for the source of the noise. 
              You heard the voice again, it's coming from your parents’ room. 
              You walk towards their room slowly, you notice that the door is slightly ajar. 
              You slowly begin entering the room when it hits you, a foul stench. 
              You open the door more, and then you see it, the mangled remains for your parents, 
              and a figure standing atop their corpses. The creature snaps its neck towards you, 
              it’s expressions best described as that of a predator seeing it’s prey. 
              The next thing you know, you are its hands as it rips you apart.
              """)
        print("GAME OVER")
        main_story()
    else:
        print("enter valid choice")
        level2()
def level3():
    print("you have Choices")
    choice=input("CHOICE : STAY WHERE YOU ARE OR RUN.\n")
    if choice.upper()=="RUN":
        print("""You swing open the door, and bolt back to your room. A shrill scream can be heard 
                 behind you as you run. As you run, you also feel like your room is only getting further away 
                 from you, like the world around is starting to warp. Once the screams subside, you hear a 
                 deep, hoarse, yet oddly soothing voice, calling your name. You feel an urge to look back.
            """)
        level4()
    elif choice.upper()=="STAY WHERE YOU ARE":
        print("""While you are panicking from within, you feel like opening the door could only spell trouble
              for you, so you look for another way out. The kitchen window was just big enough to let you
               pass through, and so you decided to jump out through the window, a flawless plan. But you 
               forgot one key detail, the space below the kitchen window was looming with thorn bushes. 
               As you jump out, you realise that, but by then it was too late, your legs have been impaled 
               by the thorns, and now they are stuck in it. All attempts to free yourself are in vain, and 
               as you’re helplessly trapped in the thorn bushes, you hear the front door closing, and soon 
               you see it, the embodiment of you end.
              """)
        print("GAME OVER")
        main_story()
    else:
        print("enter valid choice")
        level3()
    
def level4():
    print("you have Choices")
    choice=input("CHOICE : Turn back or Fight the Urge \n")
    if choice=="Fight the Urge":
        print("""You decide to fight the urge to turn back, whatever is back there could only mean harm to you.
                 You continue running, bolting ahead, but you start to feel tired, you feel like you can’t run 
                 for much longer. As you run, you manage to close in on the store room, it is far from your room 
                 but perhaps it will keep you away from whatever is chasing you.
            """)
        boss_level()
    elif choice=="Turn back":
        print("""The urge to turn back was too strong, you just had to turn back, 
              at least a glimpse of the thing chasing you. One look at it however, and you freeze in terror. 
              You can’t move a muscle, and your eyes are fixated on it, and only it, 
              Like a deer staring at the headlights of an oncoming vehicle, you too are staring at your 
              oncoming doom.
              """)
        print("GAME OVER")
        main_story()
    else:
        print("enter valid choice")
        level4()
def boss_level():
    print("you have Choices")
    choice=input("CHOICE : Enter the Store room AND Continue running \n")
    if choice=="Enter the Store room":
        print("""You decide that it’s best to enter the store room for now. You make a quick dash for the door,
                 and as soon as you are in, you slam the door shut. Initially, everything goes quiet, 
                 but as you begin to calm down, you hear a knock on the door. “Honey, we’re home!” you hear 
                 your mother’s voice, but something’s off. You can’t quite point it out, but her voice sounds wrong,
                 like it is being mimicked by someone, or something. You panic, but you stay quiet to get the thing 
                 on the other side to get off your trail. The knocking however, started to get more intense, 
                 eventually turning into loud bangs on the door, while all of this was going on, the voice… it kept 
                 repeating the same line over and over: “Honey, we’re home!”, but the voice gets more and more 
                 distorted, each passing minute. The door won’t hold up for much longer. You look around you and 
                 you see a ladder, a vent, a toolbox, a broomstick and a broken drawer. You weigh your options, do 
                 you try the vent, or do you face your fears and fight the creature on the other side.""")
        choice_5_sub()
    elif choice=="Continue running":
        print("""You feel like you can make it to your room, and so you continue running… and running… 
        and running… and running… and runnin- …  you trip and fall. 
        You no longer have the strength to stand up…  you no longer feel like moving… you feel like lying 
        there, ready to embrace death. What a way to go...
            """)
        print("GAME OVER")
        main_story()
    else:
        print("enter valid choice")
        boss_level()
def choice_5_sub():
    print("OPTION")
    print("OPTION 1: Climb into the vents")
    print("OPTION 2: Fight the creature")
    option=input("Enter your choice like 'OPTION 1': \n")
    if option=="OPTION 1":
        print("""The vents seemed to be the best option, the creature could never even come close to fitting 
              in the vents. You open the toolbox, you take the screwdriver inside it, and you unscrew it. 
              You throw the vent cover to the side and you jump into the vent. You crawl, and crawl, and crawl, 
              and crawl, though you slowly start feeling like the air around you is getting stuffy. 
              You eventually find it hard to breathe, but you soldier on. You crawl, and crawl… and crawl… 
              and crawl… and cra-… … … … 
              """)
    elif option=="OPTION 2":
        print("""You decided to end this now. You open the toolbox and find a screwdriver within. 
        You decide to unscrew the broken part of the drawer, leaving you with a flat board of wood with a 
        handle attached to it, you use it as a shield. You prepare yourself as the door finally gives way, 
        and you come face to face with the grotesque monster. It looks at you with a spine-chilling grim, 
        like how a predator looks at its prey, but little does it know that you won’t go down without a fight.
             """)
        fight_SCENE()
    else:
        print("enter valid choice")
        choice_5_sub()
def fight_SCENE():
    print("BOSSFIGHT SEGMENT:")
    print("""The creature and the player have 100 HP each, and the player has 100 SP (stamina points). 
          The player can choose to attack (-20 HP for boss), 
          Block and counter attack (-15 HP for boss) and 
          Block (-0 HP for boss). Shield breaks in 3 turns. 
          The creature attacks after each turn. If the player blocks, the player loses 0 HP. 
          If the player blocks and counter attacks, the player loses 5 HP. If the player attacks, 
          the player loses 20 HP.
          """)
    P_hp=[100]
    Boss_HP=[100]
    block_count=0
    attack=0
    print("Fight moves")
    print("HP STANDS FOR HIT-POINT/HEALTH")
    print("Note:using attack continuously will decrease dmg to 15 ")
    print("1. attack (-20 HP for boss,)")
    print("Note: you can block 3 times")
    print("2. Block and counter attack (-10 HP for boss)")
    print("3. Block (-0 HP for boss)")
    while P_hp[0]>0 or Boss_HP[0]>0:
        print("player_hp"+str(P_hp))
        print("boss_hp"+str(Boss_HP))
        choice=int(input("enter your choice as '1'or'2'or'3': "))
        if choice==1:
            if attack<2:
                print("you attacked the creature")
                Boss_HP[0]=Boss_HP[0]-20
                print("creature used claws")
                P_hp[0]=P_hp[0]-20
                print("player_hp"+str(P_hp))
                print("boss_hp"+str(Boss_HP))
                attack+=1
            elif attack >=2:
                print("you attacked the creature")
                Boss_HP[0]=Boss_HP[0]-15
                print("creature used claws")
                P_hp[0]=P_hp[0]-25
                print("player_hp"+str(P_hp))
                print("boss_hp"+str(Boss_HP))
                attack+=1
        elif choice==2:
            if block_count<3 or block_count!=3:
                print("creature used attack")
                print("you block and countered it")
                Boss_HP[0]=Boss_HP[0]-10
                P_hp[0]=P_hp[0]-0
                block_count+=1
                print("player_hp"+str(P_hp))
                print("boss_hp"+str(Boss_HP))
                attack=0
            elif block_count==3:
                print('you cant use block now')
                print('creature attacked')
                P_hp[0]=P_hp[0]-15
                print("Player"+str(P_hp))
                attack=0
        elif choice==3:
            if block_count<3 or block_count!=3:
                print("creature used attack")
                print("you blocked the attack")
                Boss_HP[0]=Boss_HP[0]-0
                P_hp[0]=P_hp[0]-0
                block_count+=1
                print("player_hp"+str(P_hp))
                print("boss_hp"+str(Boss_HP))
                attack=0
            elif block_count==3:
                print('you cant use block now')
                print('creature attacked')
                P_hp[0]=P_hp[0]-15
                print("Player"+str(P_hp))
                attack=0
        else:
            print("do the needy and choose wisely")
            print('thats not a valid move')
            print('creature attacked')
            P_hp[0]=P_hp[0]-15
            print("Player"+str(P_hp))
            attack=0
        if Boss_HP[0]<=0:
            break
        elif P_hp[0]<=0:
            break
    print("player_hp"+str(P_hp))
    print("boss_hp"+str(Boss_HP))
    if P_hp[0]>0 and Boss_HP[0]<=0:
        print("""You manage to weaken the beast, it's shrieks of pain echoing through the hallway, but as 
        you are about to leave, you creature gets back up, staring at you, with a wide, malicious grin. 
        It begins to advance towards you slowly, and you crawl back in pure shock and terror. As you move back
        , you see a glass bottle filled with a clear liquid. Weighing your options, you decide to throw the 
        bottle at the creature as a final attempt to save your life. It hits the creature’s face, 
        the glass shattering on impact. It doesn’t react at first, but then it stops and you see the terror 
        in its eye. It lets out a bone-chilling shriek as its face slowly starts melting away. 
        In seconds, it collapses onto the ground, covering its face, its painful screams evermore louder, 
        till it suddenly stops… It is gone, no trace of its existence remaining, except for the glass 
        shards on the floor.It is finally over, it is gone, no longer lurking in the shadows, stalking you. 
        You make your way out of the room, the hallway no longer warped. You finally enter your room and 
        go back to bed, finally at peace, but right as you are about to fall asleep, you hear a faint creak,
        off in the distance.
                """)
        print("“Is it over though?”")
        print("-To Be Continued")
    elif P_hp[0]==0:
        print('''You tried…  you tried to fight…  you never wanted to be its next meal, and like a 
                 cornered badger, you gave it your all, but sadly for you, the creature was just too strong, 
                 and the next thing you know, you have been ripped into shreds, any life in you long gone by 
                 that point.
              ''')
        print(""" you Died you Died you Died you Died you Died you Died you Died you Died you Died you Died
         you Died you Died you Died you Died you Died you Died you Died you Died you Died you Died you Died
          you Died you Died you Died you Died you Died you Died you Died you Died you Died you Died you Died 
           you Died you Died you Died you Died you Died you Died you Died you Died you Died you Died you Died
        """)
        print("respawning")
        fight_SCENE()
main_story()