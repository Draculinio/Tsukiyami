label stalker_encounter:

    school_stalker "Are you ok?"

    menu:

        "Continue dancing" if absu > 4:
            $sus = sus + 2
            "disregarding all worries [principal] continues to break dance on the corridor floor"
            "The [school_stalker] forcefully takes [principal] to the nurse’s office"
            jump stalker_carry_nurse

        "I don't think so":
            principal "I don’t feel so well…"
            $ scrambled = smart_scramble("let me take you to the nurses office")
            school_stalker "You must be sick, [scrambled]"
            jump stalker_carry_nurse

        "Run away" if intro < 5:
            $ nigechance = renpy.random.random()
            if nigechance > 0.5 and nigechance < 0.8:
                jump stalker_carry_nurse
            elif nigechance > 0.8 and nigechance < 0.9:
                $ sus += 2
                jump classroom
            else:
                jump school_corridor_choices
