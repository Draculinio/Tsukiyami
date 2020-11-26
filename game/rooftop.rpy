label rooftop:
    #transition roof
    principal "There’s no-one here..."

    principal "Look at that moon…"

    principal "Wait, what time is it?"

    if absu > 5 and sus > 6:
        #show sky moon red
        school_stalker "You are not [principal]"

        principal "What? What are you doing here? What’s going on with the sky?"

        school_stalker "You’ve done your part. Now this place is like this… thanks to YOU."

        principal "What is going on? HELP! Someone, please help!"

        "[school_stalker] moves closer to [principal]"

        school_stalker "It’s too late now. I know this won’t keep you away for long but… it might just push you over the edge…"

        school_stalker "...and maybe, just maybe this time is enough to protect us..."

        principal "What are you talking about!? HELP, SOMEBODY PLEASE HELP ME"

        "[school_stalker] moves past [principal]"

        principal "huh! who are you talking to?"

        school_stalker "...protect us from YOU!"

        #transition to black

        $ lose_condition = "Got found out before your due time"

        jump game_over

    if time > 10:

        #show sky black
        principal "What the..."

        "[principal] stares at the inky sky"

        principal "It’s as if the world is old and tired, like it wants to give up..."

        menu:

            "continue watching the sky":
            "continue watching the sky":
            "continue watching the sky":

        $ sus = sus -1

        principal "There’s something really calming about this sky"

        principal "I feel like my worries just fly away…"

        principal ""

        principal "I feel… sleepy… as if.. I could just sleep my life away..."

        $ lose_condition = "Went to sleep before your time"

        jump game_over

    if no_return:

        principal "(Now I’ve done it...)"

        principal "(What happened to me, I was supposed to be a regular student)"

        principal "(Today was as if I was somebody else entirely...)"

        principal "(Maybe I’d be for the best if I was someone else, that way I wouldn’t have to deal with the embarrassment of this horrible day...)"

        principal "..."

        menu:
            "Time to leave":
                jump expression renpy.random.choice(["salary_intro","university_intro","plant_hell"])

            "Jump off":
                $ lose_condition = "Died from high velocity impact with concrete"
                jump game_over
