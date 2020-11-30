label leave_classroom:

    scene schoolcorridor2

    bravo "Hey, I am talking to you, don’t just go away when I’am talking to you"

    principal "..."

    bravo "tsk -weird asshole-"

    principal "(Now where? Why do I keep double guessing myself today? Everything’s all right)"

    principal "(The class prez is sweet for me, I just know it~)"

    $ scrambled = smart_scramble("library")

    principal "(I’ll just skip class and wander around in celebration! I bet I can find a spot in the [scrambled] to sleep around for a while)"

    principal "(I barely do any studying so I don’t remember the last time I went there. Now, where was [scrambled] the again?)"

    principal "..."

    #Transition to a corridor

    principal "(Wasn’t it somewhere around here?)"

    menu:

        "...":
            $ intro += 1
            jump corridor_encounter

        "Go back":
            jump corridor_encounter

        "Go east":
            "[principal] walks headfirst into a window"
            principal "Ouch! I hit my nose…"
            jump corridor_encounter

        "Go west":
            "[principal] enters a door"
            if renpy.random.random() > 0.75:
                jump library_intro
            else:
                jump corridor_encounter

        "Move forward":
            #transition to school_corridor_3
            jump corridor_encounter

        "Go to the rooftop":
            jump rooftop

        "breakdance":
            $ absu = absu + 2
            $ flag_breakdance = True
            "[principal] breakdances on the floor"
            "The students all gather around to see [principal] breakdancing to the best of his meager abilities"
            "The [school_stalker] notices the crowd and approaches to see"
            jump stalker_encounter
