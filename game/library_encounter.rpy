label library_encounter:

    scene schoollibrary2

    principal "Oh, hi"

    alphaPartner "oh shit-"

    principal "oh come on, why are you so angry?"

    alphaPartner "Please don’t talk to me."

    principal "Why, what did I do to you?"

    $ scrambled = smart_scramble("spread all these rumours around of us being a couple and have the nerve to ask why!??")
    alphaPartner "Why? You [scrambled]"

    librarian "*gives [principal] a death stare*"

    menu:
        "...":
            principal "..."
            "[alphaPartner] slaps [principal] and leaves the library"
            jump slap_end

        "Lie":

            if renpy.random.random() > 0.8 - (intelligence / 10):

                principal "Listen, I know you are angry but I didn’t have anything to do with whatever is being going on"

                principal "I thought we were on good terms is all and I really just wanted to be closer to you."

                alphaPartner "..."

                $ scrambled = smart_scramble("GET")
                alphaPartner "[scrambled]"

                $ scrambled = smart_scramble("OUT")
                alphaPartner "[scrambled]"

                $ scrambled = smart_scramble("OF")
                alphaPartner "[scrambled]"

                $ scrambled = smart_scramble("MY SIGHT!")
                alphaPartner "[scrambled]"

                jump slap_end

            else:

                principal "...that was probably someone else, you got this all wrong!"

                principal "I am a victim too"

                principal "I’ll go and find out who's behind this…"

                $ scrambled = smart_scramble("Can’t. you. just. SHUP. UP!")
                alphaPartner "[scrambled]"

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

            $ sus += 2

            jump school_corridor_choices

        "Attempt to calm down":
            principal "Hey, hey, shhhh"

            $ scrambled = smart_scramble("DON'T")
            alphaPartner "[scrambled]"

            $ scrambled = smart_scramble("YOU")
            alphaPartner "[scrambled]"

            $ scrambled = smart_scramble("DARE")
            alphaPartner "[scrambled]"

            $ scrambled = smart_scramble("SHUT")
            alphaPartner "[scrambled]"

            $ scrambled = smart_scramble("ME")
            alphaPartner "[scrambled]"

            $ scrambled = smart_scramble("UP")
            alphaPartner "[scrambled]"

            principal "Hey hey, calm down; I thought we were friends from way back! Geez!"

            $ scrambled = smart_scramble("I shared my lunch with you in preschool")
            alphaPartner "Friends!? Just because [scrambled]?"

            $ scrambled = smart_scramble("you do for someone you don’t care")
            principal "Well, yeah, that’s not something [scrambled]"

            $ chance = smart_scramble("I only did it out of kindness")
            $ scrambled = smart_scramble("to talk out of your ass I would’ve never done it!")
            alphaPartner "[chance], if I knew you would do something so sinister as [scrambled]"

            principal "..."

            $ scrambled = "I only did it out of PITY!"
            alphaPartner "And I’ll tell you more, [scrambled]"

            alphaPartner "But now I regret it! You are an asshole!"

            "[alphaPartner] slaps [principal] and leaves the library"

            $ no_return = True

            jump slap_end
