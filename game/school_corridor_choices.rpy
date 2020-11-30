label school_corridor_choices:

    scene schoolcorridor1

    menu:
        "...":
            $intro = intro +1
            if renpy.random.random() > 0.8:
                jump corridor_encounter
            else:
                principal "(geez, what’s wrong with me today?)"
                jump classroom

        "Attempt to locate the library" if not no_return:
            if renpy.random.random() > 1.5 -(intelligence/10):
                principal "!?"
                principal "Was this door always here?"
                jump library_intro
            else:
                principal "I can’t seem to find it… Am I an idiot or something?"
                jump classroom

        "Go down":
            $ intelligence = intelligence -1
            if intelligence < 1:
                "[principal] trips and falls through a window"
                principal "WAAAAAAAAAAAAAAAAAA..."
                $ lose_condition = "Died from high velocity impact with concrete"
                jump game_over
            jump corridor_encounter


        "Move forward":
            jump corridor_encounter

        "Go to the rooftop":
            jump rooftop
