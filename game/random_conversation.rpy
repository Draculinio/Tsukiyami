label random_conversation:

    scene officeworkseat2

    $ random_workm = renpy.random.choice( ["Mario", "John", "Philip"])

    y "Hey, how’s your day going?"

    random_workmate "Hey! I’m ok, did the boss talk to you already"

    if special_report:

        y "Yeah, he assigned me to some lame report I gotta hand out to [stalker_office]"

        random_workmate "Whoo the higher ups I guess"

        y "Don’t really care much about them"

        random_workmate "You don’t and sometimes they might not care about you, but it’s in your best interests to keep it that way"

        y "How would they come to have any interest in me? a simp-"

        y "-hic- leton."

        random_workmate "cheers"

        y "Thanks. As I was saying, unless I screw up big time they won’t give a rats’ ass about me"

        random_workmate "Well, yeah but the rumour has it that some people who’ve gotten on [offi_stalker] bad side get fired and the toilet’s got a whole bookload of horror stories"

        $flag_toilet = True

        y "geez, you guys certainly seem to buy into a lot of the office gossipping"

        random_workmate "It’s not like there’s anything more interesting happening here at the office"

    else:

        y "What? No, not really, should I update my linkedin profile?"

        random_workmate "dunno, but if you screw your monthly presentation you can sure kiss your bonus goodbye"

        y "Yikes..."

        y "So what do you think the higher ups want to hear? What should I write?"

        if renpy.random.random() > 0.6:

            random_workmate "Dunno, positive things right?"

            y "Only if they like to eat shit for dinner..."

            random_workmate "Geez, calm down; they are your bosses not some loose murderer"

            random_workmate "In any case, try to not write anything too truthful there"

        else:

            random_workmate "I don’t know, the truth, right?"

            y "I’m not too sure about that..."

            random_workmate "The truth I think"

            random_workmate "I mean, they are supposed to be the guys who make all the important calls, right"

            random_workmate "You’d think they want to know all the stuff, bad or good, right?"

            y "Sounds about right, but I kinda don’t want to let them know of all the shit some of the people here pull"

            random_workmate "Well, you can show the data, there no need to tell them that the lazy guy in accounting is trying to pick up the receptionist all the time."

            y "what"

            random_workmate "C’mon don’t play fool with me, we see that every other day"

            y "eehmm, that’s weird, I don’t remember that…"

            random_workmate "We talked about this literally yesterday! Are you okay in the head?"

    random_workmate "Anyways, gotta get back to appearing as if I am working, so shush"

    jump workseat
