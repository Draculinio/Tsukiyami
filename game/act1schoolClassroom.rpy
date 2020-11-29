label act1schoolClassroom:

    scene schoolclassroom2

    bravo "...all she ever wanted to do was find X in the equation!"

    principal "Heh. That was bad, as usual. Anyways, did you see yesternights stream?"

    bravo "I told you I am not like you. I don’t see those taiwanese talking heads"

    principal "Tsch! They are not taiwanese! I told you, it’s the last hit in streaming fashion!"

    bravo "I heard the class president got angry at you, you should be careful…"

    principal "I am not concerned, she clearly just really likes me. After all, we were friends in preschool"

    bravo "Man you are really delusional today, and not in a funny way."

    bravo "What makes you think the class president who is a very talented, responsible individual with a bright future ahead would have any interest in you?"

    $ scramble = select_scramble("...besides were you actually friends or did you just show her your boogers back in preschool?", 2)
    bravo "[scramble]"

    menu:
        "Ignore him":
            $ intro = intro + 1
            principal "..."
            bravo "figures..."

        "Leave the classroom":
            jump leave_classroom

        "Initiate photosyntesis":
            $ absu = absu + 1

            "[principal] stares straight through the window, his eyes fixated on the sun"

            bravo "geez, what is wrong with you? you really are out of it today..."

    charlie "Hey Let’s go! I heard the cafeteria special is on sale today!"

    bravo "In any case I just wanted to test my jokes to see if they’d work on you, the grumpiest of the class; thanks I guess."

    #random exit
    $ exit = random.randint(0,3)
    if exit == 1:
        jump leave_classroom
    if exit == 2:
        jump school_corridor_choices
    if exit == 3:
        jump classroom
