label corridor_encounter:

    scene schoolcorridor2

    "..."
    $ scrambled = smart_scramble("Are you not supposed to be in your classroom right now")
    school_stalker "Hello kid, you seem lost, do you need a hand? [scrambled]?"

    "The [school_stalker] stares at [principal] very intensely"

    principal "Ah! eh-eh- (I got busted, dammit! This guy is very tall and intimidating)"

    $ scrambled = smart_scramble("not feeling well")
    school_stalker "Are you [scrambled]? Do I need to take you to the nurses office?"

    principal "ah, y-ye-ye-yes! tha-that’s it, is it not on this floor?"

    school_stalker "You must be really sick if you think so, are you running a fever?"

    school_stalker "here, let me walk you to it."

    "The [school_stalker] somewhat forcefully walks [principal] to the nurse’s office"

    jump stalker_carry_nurse
