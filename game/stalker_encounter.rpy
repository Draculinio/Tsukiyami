label stalker_encounter:

    school_stalker "Are you ok?"

    menu:

        "Continue dancing" if absu  >5:
            $sus = sus + 2
            "disregarding all worries [principal] continues to break dance on the corridor floor"
            "The [school_stalker] forcefully takes [principal] to the nurse’s office"
            jump janitor_carry_nurse

        "I don't think so":
            principal "I don’t feel so well…"
            school_stalker "You must be sick, let me take you to the nurses office"
            jump janitor_carry_nurse
        "Run away" if intro <5:
            $tmp = renpy.random.random()
            if tmp>0.5 and tmp < 0.8:
                jump stalker_carry_nurse
            elif tmp > 0.8 and tmp < 0.9:
                jump classroom
            else:
                jump school_corridor_choices
