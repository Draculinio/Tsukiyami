label wrong_door:

    scene officeoffice2

    $ time = time + 1

    #transition to office

    if time < max_time:

        if renpy.random.random() <= 0.2:

            y "Oops, wrong door; I guess."

        elif renpy.random.random() > 0.2 and renpy.random.random() < 0.5:

            y "Goddammit"

        else:

            y "Nope, wrong door"

    else:

        "thump thump"

        "Approached from behind"

        office_stalker "You are late."

        y "Sorry, I got lost on the way."

        office_stalker "My office, now"

        "[offi_stalker] shows the way"

    jump confront_stalker
