label ditch_class:
    scene schoolcorridor1
    "[principal] sneaks out of the classroom"
    principal "now now..."
    principal "...What do I do?"

    menu:
        "...":
            $ intro += 2
            principal "(I don’t know what to do!)"
            principal "(Why did I even ditch class like that?)"
            jump classroom

        "Get lost in school":
            jump school_corridor_choices
