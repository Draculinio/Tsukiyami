label stalker_carry_nurse:

    #transition to nurses office
    scene schoolnurses

    school_stalker "Hello nurse"

    nurse "Oh Hello, what’s going on?"

    $ chance = smart_scramble("He seems somewhat confused")
    $ scrambled = smart_scramble("walking around, I got the sense he was lost")
    school_stalker "[chance], I found [principal] [scrambled]"

    nurse "Ok, thanks [school_stalker], I’ll take care of it"

    principal "(How did I get into this?)"

    nurse "Hello there, what is your name? Are you hurt?"

    principal "(Focus, focus...)"

    nurse "Are you a new student perhaps?"

    principal "(What? I was here last week! Don’t you remember me!?) Ah, no, I am not, I just feel a bit under the weather"

    principal "(If I choose my options right I can just sleep here…)"

    principal "(Just need to whip out the old charisma)"

    menu:
        "Hello baby, are you up for some fun?" if absu > 2:
            "The nurse is stunned by [principal]'s attempt of seduction"

        "Can I sleep for a bit?":
            $ sus = sus -1
            principal "(Well, that wasn’t so smooth)"
            nurse "Is that so?"

        "I don't feel very well... I mifght be running a fever":
            $sus = sus +1

        "...":
            principal "..."
            $ intro = intro +1
            nurse "Is something the matter?"

    nurse "Here, let me take your temperature"

    "The nurse moves near [principal]"

    principal "Eh!? Sure."

    nurse "Come, sit over there"

    "..."

    principal "Eh, I feel tired all of the sudden, can I go lay down now?"

    $ scrambled = smart_scramble("your temperature is not abnormal")
    nurse "Well, [scrambled] but sure, you can go and lay down a bit."

    nurse "You sure are lively for someone tired."

    principal "What do you mean?"

    $ scrambled = smart_scramble("stopped fidgeting with your fingers")

    nurse "I mean you haven’t [scrambled] ever since you came in"

    menu:

        "Stare through the window and ignore her":
            #transition window
            $ intro += 2
            jump school_teardown

        "Jump through the window" if intro > 5:
            $ lose_condition = "Died from high velocity impact with concrete"
            jump game_over

        "Initiate photosynthesis":
            $ absu = absu +1
            "[principal] stares straight through the window, his eyes fixated on the sun"
            jump classroom

        "Go back to class":
            principal "I am feeling better now, I’ll head back to class"
            "The nurse stares at [principal] over her glasses"
            $ sus = sus +1
            "[principal] returns to the classroom."
            jump classroom
