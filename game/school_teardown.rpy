label school_teardown:

    principal "..."

    if intro > 6:
        principal "(look at those people outside, each with their own life, their own past, their expectations, family, commitments, jobs...)"

        principal "(Each with their own strands of hair, each person grown, fed, educated and given a chance to live by others)"

        principal "(Each person connected to a countable, yet unconceivable number of other people)"

        principal "(Each without a clear view of the future, attempting to claw out of the tedium of their ordinary lives...)"

        principal "(...or fighting to stay afloat amongst the overbearing sense of futility of their lives)"

        principal "(Where do I fit in all this?)"

        principal "What do I want to do?..."

        menu:

            "I don’t want to stand out… I’ll just get a random office job...":
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

        principal "I can’t seem to focus very far… I seem to be very tired or is something wrong with my eyes?"

        principal "Am I missing something?"

        principal "..."

        #close eyes efect
        jump classroom
        
