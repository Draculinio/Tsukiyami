label library_encounter:

    scene schoollibrary2

    principal "Oh, hi"

    alphaPartner "oh shit-"

    principal "oh come on, why are you so angry?"

    alphaPartner "Please don’t talk to me."

    principal "Why, what did I do to you?"

    alphaPartner "Why? You spread all these rumours around of us being a couple and have the nerve to ask why!?"

    librarian "*gives you a death stare*"

    menu:
        "...":
            principal "..."
            "[alphaPartner] slaps [principal] and leaves the library"
            jump slap_end

        "Lie":

            if renpy.random.random() > 0.8 - (inteligence / 10):

                principal "Listen, I know you are angry but I didn’t have anything to do with whatever is being going on"

                principal "I thought we were on good terms is all and I really just wanted to be closer to you."

                alphaPartner "..."

                alphaPartner "GET"

                alphaPartner "OUT"

                alphaPartner "OF"

                alphaPartner "MY SIGHT"

                jump slap_end

            else:

                principal "...that was probably someone else, you got this all wrong!"

                principal "I am a victim too"

                principal "I’ll go and find out who's behind this…"

                alphaPartner "Can’t. you. just. SHUP. UP!"

                "[alphaPartner] slaps [principal] and leaves the library"

                $ no_return = True

                jump slap_end

        "Acknowledge":

            principal "Listen, I know you are angry and you have all the right to be"

            principal "I am terribly sorry for the stress I’ve caused you"

            alphaPartner "well I wasn’t expecting that..."

            principal "I’m sorry, Ok? I’ll leave now"

            alphaPartner "..."

            $ no_return = True

            jump ack_end

        "Back off":
            "[principal] is too dumbfounded to say anything"

            "[principal] walks backward and leaves the library"

            $ sus += 1

            jump school_corridor_choices

        "Attempt to calm down":
            principal "Hey, hey, shhhh"

            alphaPartner "DON'T."

            alphaPartner "YOU."

            alphaPartner "DARE."

            alphaPartner "SHUT."

            alphaPartner "ME."

            alphaPartner "UP!"

            principal "Hey hey, calm down; I thought we were friends from way back! Geez!"

            alphaPartner "Friends!? Just because I shared my lunch with you in preschool?"

            principal "Well, yeah, that’s not something you do for someone you don’t care"

            alphaPartner "I only did it out of shame, if I knew you would do something so sinister as to talk out of your ass I would’ve never done it!"

            principal "..."

            alphaPartner "And I’ll tell you more, I only did it out of PITY"

            alphaPartner "But now I regret it! You are an asshole!"

            "[alphaPartner] slaps [principal] and leaves the library"

            $ no_return = True

            jump slap_end
