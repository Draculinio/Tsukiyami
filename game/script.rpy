# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")
define i = Character("Impostor")
define principal = Character("[char_name]")
define alphaPartner = Character("Alpha Partner")
define bravo = Character("classmate")
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
    $ char_name = random.choice(['Yui','Akari','Hana','Mei','Ema','Sakura','Aoi','Honoka','Himari','Koharu',
    'Haruto','Yuuto','Souta','Minato','Haruki','Riku','Kouki','Yuito','Hinata','Sousuke'])

    # call beggining
    call school_hell
    call act1schoolClassroom

    $ introversion = 0
    $ text = select_scramble("Hola mundo",introversion)
    principal "[text]"
    $ introversion = 1
    $ text = select_scramble("Que tal te va",introversion)
    principal "[text]"
    $introversion = 2
    $ text = select_scramble("Mirror",introversion)
    principal "[text]"
    $introversion = 3
    $ text = select_scramble("binary thing hola mundo che",introversion)
    principal "[text]"
    $introversion = 4
    $ text = select_scramble("pero que cosa loca",introversion)
    principal "[text]"
    # This ends the game.

    return
