label salary_intro:

    $time = 0
    $max_time = renpy.random.randint(16,20)
    $office_stalker = renpy.random.choice(["Jenny", "Rob", "Accounting guy", "That finance blonde"])
    $door_num = renpy.random.randint(1,10)
    $floor_num = renpy.random.randint(1,10)
    $rumor_heard = False
    $special_report = False
    $flag_toilet = False
    $report_progress = 0
    $max_report_progress = renpy.random.randint(8,12)
    $flag_wardream = False

    "[y] is serving himself water in the water cooler"
    #office background noise
    #transition office water cooler

    bravo_workmate "Hey, what’s up?"

    y "Hey"

    bravo_workmate "Mind letting me fill up on hot water?"

    y "Sure"

    bravo_workmate "How is your day going?"

    menu:
        "Ignore":
            $ intro = intro +1
            jump office_reflection

        "It's ok, yours?":
            bravo_workmate "Anyways sorry, I am running late for a meeting"

    "[bravo_workmate] leaves"

    menu:
        "Go back to your seat":
            jump workseat

        "Daydream" if flag_wardream:
            $intro = intro + renpy.random.randint(2,4)
            jump wardream

        "Breakdance":
            "[y] attempt to break dance in the small kitchen office"
