label hand_report:

    $ fake_floor_1 = renpy.random.randint(1,5)
    $ fake_floor_2 = renpy.random.randint(2,8)
    $ fake_floor_3 = renpy.random.randint(1,10)
    $ fake_door_1 = renpy.random.randint(1,12)
    $ fake_door_2 = renpy.random.randint(1,12)

    menu:

        "Floor [fake_floor_1] door [fake_door_1]":

            jump wrong_door

        "Floor [fake_floor_3] door [fake_door_2]" if renpy.random.random() > 0.3:

            jump wrong door

        "Floor [fake_floor_2] door [fake_floor_1]" if renpy.random.random() > 0.3:

            jump wrong door

        "Floor [floor_num] door [door_num]":

            "*knock knock*"

            y "Excuse me, is this [office_stalker] offices’?"

            office_stalker "I’m here, aren’t I?"

            jump confront_stalker

        "Floor [fake_floor_2] door [fake_door_1]":

            jump wrong_door
            
