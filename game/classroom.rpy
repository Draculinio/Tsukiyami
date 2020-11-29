label classroom:

    scene schoolclassroom2

    "An hour passes"
    $ time = time +1
    if time > 8:
        $absu = absu +1
        principal "(so much time has passed…)"
        principal "(I don’t know what’s going on but I don’t feel well…)"
        principal "(Somethings off…)"
    if time > 10:
        principal "(I feel like I’ve been here for an eternity.)"
    if time > 15:
        principal "I can’t stand it anymore!"

    menu:
        "Attempt to ditch class":
            if renpy.random.random() > 0.6:
                jump ditch_class
            else:
                $ sus = sus +1
                teacher "Get back to your sit"
                jump classroom

        "Make an effort to study":
            $intelligence = intelligence + 1
            if renpy.random.random() > 0.75:
                $ sus = sus -1
            if intelligence > 6:
                $flag_school2university = True
                jump university_intro

        "Initiate photosynthesis" if absu > 8:
            "[principal] stares straight through the window, his eyes fixated on the sun"
            jump plant_hell
