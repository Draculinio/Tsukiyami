label conversation_rumour:

    scene officeworkseat2

    $ rumor_heard = True

    y "Hey, you still working on this?"

    random_workmate "I am, boss says the report has to show the higher up our velocity increase in a bar chart but also a pie chart"

    random_workmate "Hey, you heard the rumour about [offi_stalker]?"

    y "A rumour?? What are we some middle schoolers?"

    random_workmate "hahaha, well it’s nothing like that"

    y "well what’s it about?"

    random_workmate "Well, it seems [offi_stalker] was seen working late at night and ..."

    if renpy.random.random() > 0.5:

        $ random_room = renpy.random.choice(["Ed. Packard","J. Strech","Ra. Montgomery"])

        boss "Hey, [y] I have a meeting in a bit but I wanted to talk to you at meeting room [random room], come on. Let’s go."

        jump boss_talk
