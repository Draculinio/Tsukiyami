label toilet:

    scene officetoilet

    y "(Time for a wee-wee)"

    "~grr~"

    y "huh?"

    "~rumble rumble~"

    y "What is this ignominious sound coming from my belly!"

    menu:

        "Ignore":

            "This can wait, I have to continue working"
            jump workseat

        "NEED TO SHIT" if renpy.random.random()>0.3:

            y "(Well if it isn’t the old borborygmus, damn I really need to go)"

            "..."

            y "..."

            "...plop!"

            y "(Well, that’s a submarine alright)"

            "~clank~"

            "~clank clank~"

            y "(goddammit, this toilet is not working)"

            y "(What do I do now?)"

            menu:

                "Leave as is":

                    $absu = absu + 1
                    jump workseat

                "Try to fix the toilet":

                    y "..."

                    if renpy.random.random() > 0.4:

                        y "...(What's this?)"

                        y "(Some kind of writing)"

                        $ scramble = select_scramble("The boss of engineering, he is an asshole, tried to get me fired.", 0)
                        "[scramble]"

                        y "(that’s old news buddy)"

                        $ scramble = select_scramble("At night [offi_stalker] stands looking at the moon through the window...WEEEIRD", 0)
                        "[scramble]"

                        y "Well, that’s an unwanted insight"

                        $ insight = insight + 1

                        y "(more gossip)"

                        $ scramble = select_scramble("K1k$ from Marketing is $/(_)at", 0)
                        "[scramble]"

                        y "(Well, that’s very… civil)"

                    y "There, stupid button, never properly reset"

                    jump workseat #I added this, cool tell it to your kids
