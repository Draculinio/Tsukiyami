label workseat:

    #TODO: see this.
    #$ random_workm = jump expression renpy.random.choice(["Pepe","Martin","Roberto"]) #?

    scene officeworkseat1
    with fade

    if time > max_time:
        #reports due
        #gets visited by stalker
        office_stalker "You are late. My office. Now"
        jump confront_stalker

    y "(Okay... so what was I doing?)"

    menu:

        "Work on the spreadsheets due for tomorrow":

            y "..."

            y "(Another hour spent on mostly meaningless spreadsheets)"

            if special_report:
                y "(I feel like I have something more urgent to do…)"
            jump workseat

        "Talk with [random_workm]" if time < (max_time / 2):
            $ time += 1
            if not rumour_heard:
                jump conversation_rumour
            else:
                jump random_conversation

        "Work on report due for today" if special_report and report_progress < max_report_progress:

            jump write_report

        "Hand in report" if special_report  and report_progress > max_report_progress:

            jump hand_report

        "Go to the toilet":

            jump toilet
