label boss_talk:

    #some boring chat containing info on stalker

    boss "Now, as you know, we will be delaying the C77 project to include more overall testing but I am concerned that, as we mentioned in our previous meetings…"

    y "(zzzz)"

    boss "And so, the higher ups have requested a report on the initiative to evaluate its overall value to our product"

    y "Wasn’t this initiative started by the higher ups?"

    boss "Well, yes, but we are the ones carrying it on. I’d like for you to complete the report with full evaluation of its current development"

    menu:

        "Wouldn’t you have a better time gathering the information?":

            $ intro = intro - 1

            y "but wouldn’t you have a better time gathering the information?"

            boss "Yes, but since you are a member of the quality team I’d thought you’d like a chance to know how to manage and gather information with the development team tools"

        "Ok, boss":

            $ intro = intro +1
            $sus = sus -1

            y "Ok, boss. I’ll get on it right now."

            boss "Great, remember to hand the report over directly to [office_stalker], as they have requested it be delivered ASAP"

        "*Knock knock*"

        office_stalker "Hello, can we come in?"

        boss "Yes, we’ve just finished."

        boss "[y] here just volunteered to finish the report and will deliver it to you as soon as he’s finished it today"

        office_stalker "Great, I have to stay all night here today so I’ll be expecting you to deliver it personally to me, no matter how late you finish it"

        office_stalker "Remember, my office is on the [floor_num] floor, door number [door_num]"

        $ special_report = True
        jump workseat
