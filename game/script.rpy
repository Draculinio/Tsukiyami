# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")
define i = Character("Impostor")
define principal = Character("[char_name]")
define alphaPartner = Character("[alpha_name]")
define bravo = Character("Classmate")
define charlie = Character ("Another classmate")
define nurse = Character("Nurse")
define teacher = Character("Teacher")
define librarian = Character("Librarian")
define y = Character("[char_name]") #principal in Salary Hell stage
define bravo_workmate = Character("Workmate")
define boss = Character("Boss")
define school_stalker = Character("[sch_stalker]")
define office_stalker = Character("[offi_stalker]")
define random_workmate = Character("[random_workm]")
# The game starts here.

label start:

    $ insight = 0
    $ time = 0
    $ intelligence = 0
    $ intro = 0
    $ sus =  0
    $ absu = 0
    $ no_return = False
    $ flag_school2university = False
    $ flag_breakdance = False
    $ sch_stalker = renpy.random.choice(['Janitor', 'Teacher', 'PE Teacher', 'Counsellor'])
    $ char_name = random.choice(['Haruto','Yuuto','Souta','Minato','Haruki','Riku','Kouki','Yuito','Sousuke', 'Hachiman'])
    $ alpha_name = random.choice(['Yui','Akari','Hana','Mei','Ema','Sakura','Aoi','Honoka','Himari','Koharu', 'Hinata'])

    call beggining from _call_beggining
    call school_hell from _call_school_hell
    # $ sus = 1
    # $ intro = 12
    # $ text = smart_scramble("Hola mundo, yubi yubi")
    # e "[text]"


    return
