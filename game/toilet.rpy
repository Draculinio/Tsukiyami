label toilet:

    scene officetoilet

    y "(Time for a wee-wee)"

    "~grr~"

    y "huh?"

    "~rumble rumble~"

    y "What is this ignominious sound coming from my belly!"

    menu:

        "Ignore":

            y "(This can wait, I have to continue working)"
            $ intro += 1
            jump workseat

        "NEED TO SHIT" if renpy.random.random() > 0.3:

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

                        $ scrambled = smart_scramble("The boss of engineering, he is an asshole, tried to get me fired.")
                        "[scrambled]"

                        y "(that’s old news buddy)"

                        $ scrambled = smart_scramble("At night [offi_stalker] stands looking at the moon through the window...")
                        "[scrambled]"

                        y "Well, that’s an unwanted insight"

                        $ insight = insight + 1

                        y "(more gossip)"

                        $ scrambled = smart_scramble("Richard from Marketing is $/(_)at", 0)
                        "[scrambled]"

                        y "(Well, that’s very… civil)"

                    y "There, stupid button, never properly reset"

                    jump workseat #I added this, cool tell it to your kids
