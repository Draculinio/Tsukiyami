label school_teardown:

    principal "..."

    if intro > 6:

        $ scrambled = smart_scramble("people")

        principal "(look at those [scrambled] outside, each with their own life, their own past, their expectations, family, commitments, jobs...)"


        $ hair = smart_scramble("own strands of hair")
        $ chance = smart_scramble("a chance to live by others")
        principal "(Each with their [hair], each person grown, fed, educated and given a [chance])"

        $ person = smart_scramble("person")
        principal "(Each [person] connected to a countable, yet unconceivable number of other [scrambled])"

        $ scrambled = smart_scramble("to claw out of the tedium of their ordinary lives...")
        principal "(Each without a clear view of the future, attempting [scrambled])"

        principal "(...or fighting to stay afloat amongst the overbearing sense of futility of their lives)"

        principal "(Where do I fit in all this?)"

        principal "What do I want to do?..."

        menu:

            "I don’t want to stand out… I’ll just get a random desk job...":
                $ flag_school2office = True
                jump salary_intro

            "I want to try university!":
                if intelligence > 7:
                    jump university_intro
                else:
                    principal "(On a second though, I don’t really have the grades for Uni just yet)"

            "Those trees look really peaceful":
                if absu > 8:
                    principal "I want to be like the trees..."

                    principal "Just… dancing... in the wind..."

                    principal "growing… endlessly…"

                    jump plant_hell

        $ scrambled = smart_scramble("is something wrong with my eyes?")
        principal "I can’t seem to focus very far… I seem to be very tired, [scrambled]"

        principal "Am I missing something?"

        principal "..."

        #close eyes efect
        jump classroom
    else:
        principal "Those trees look really peaceful"

        nurse "Are you feeling better?"

        nurse "it's time to go back to class"

        jump classroom
