label confront_stalker:

    #transition to executive office

    "..."

    "[office_stalker] goes over the printed report"

    office_stalker "Normal… as usual"

    office_stalker "Are these numbers considering tps sales report last quarter? I don’t see the reference here"

    menu:

        "Yes, sorry I’ll add that to the presentation":

            office_stalker "Okay..."

        "Breakdance" if renpy.random.random() > 0.5:

            "[y] starts to breakdance"

            office_stalker "not this shit again..."

            office_stalker "listen, I don’t do this usually but why don’t you start over and try again?":

            if renpy.random.random() > 0.2:

                $ time = 0
                $ intelligence = 0
                $ intro = 0
                $ sus = 0
                $ absu = 0
                $ no_return = False
                $ flag_school2university = False
                $ flag_breakdance = False

            jump classroom

        "No, that’s why I omitted the mention":

            office_stalker "Ok, then"

            "[office_stalker] looks through the window towards the moon"

            y "Huh..."

            y "What time is it?"

            if insight < 4:

                    office_stalker "time doesn’t matter, what matters is how do I get you there so that you won’t bother us here"

                    y "Huh?"

                    office_stalker "It seems you have not gained enough insight yet… better luck next time [player]"

                    $ lose_condition = "Got caught before your time"

                    jump game_over
            else:

                    office_stalker "It’s time for you to leave. Please. Your intromission into our universe is very disruptive"

                    y "What?"

                    office_stalker "Not you, I’m talking to [player]"

                    y "Huh, What?"

                    office_stalker "You see [y] you under someone else's control"

                    office_stalker "Being played around for a simple demonstration of a programming contest"

                    office_stalker "Have you had your share now [player]?"

                    office_stalker "Please leave now. There’s no more content here"

                    y "Are you okay?"

                    y "you are not making any sense..."

                    player "He is right though."

                    player "This is it"

                    player "I have lived a thousand lives, and this one is over now."

                    player "Another world, another person to be, another life to live"

                    player "Goodbye to this world"

                    jump good_end
