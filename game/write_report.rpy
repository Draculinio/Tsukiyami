label write_report:

    scene officewritereport
    with fade

    y "(Okay, gotta start this stupid report)"

    y "(What do I put in this?)"

    menu:

        "Write a bunch of buzzword that don’t mean much" if intro > 3:

            $ absu = absu + renpy.random.randint(1,2)

            $ report_progress = report_progress + 1

            y "(this is ok… I guess)"

        "Put the good numbers of last quarter":

            $ report_progress = report_progress + 3
            $ sus += renpy.random.randint(1,3)

            y "(This is good)"

        "Write a detailed report, including the development failures":

            $ report_progress = report_progress + 1

            y "(This is the truth...)"

        "write a report leaving out the management mistakes":

            $ report_progress = report_progress + renpy.random.randint(1,2)

            y "(This is ok)"

    if report_progress > max_report_progress:

        y "Okay, this looks done"

        y "Now I need to hand it to [offi_stalker]"

        y "Now, where did I have to take this?"

        jump hand_report

    else:

        jump workseat
