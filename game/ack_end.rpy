label ack_end:

    scene schoollibrary1

    principal "... ufff"

    principal "Well, that was out of character for me."

    principal "(At least I was able to disarm the situation)"

    principal "(It seems that I managed to survive through today for now)"

    principal "(from now on, I should keep a low profile)"

    principal "(I’ll try not to cause more trouble)"

    "[principal] has gained some valuable insight"

    $insight = insight + 1

    if intelligence > 6:
        $ flag_school2university = True
        "And so [principal] focused on studying and got into university…"
        jump university_intro
    else:
        $flag_school2office = True
        "And so, unable to focus on studying, [principal] got into a office job…"
        jump salary_intro
