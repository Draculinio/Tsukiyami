label library_intro:

    #transition library

    librarian "The Librarian silently stares at [principal]"

    menu:
        "What should I do while I am in here?"

        "Move near the window":
            #transition window
            jump school_teardown

        "Move near the end of the shelves":
            jump library_encounter
