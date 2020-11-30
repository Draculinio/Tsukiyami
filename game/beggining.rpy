label beggining:

    show  mirror #shows a character sprite
    i "A mirror, another mirror, another house."

    i "How long will I keep running away?"

    i "They will find me eventually, I will slip up and somebody will notice."

    i "Everybody else is a problem, an enemy, that’s why I must avoid them."

    i "..."

    i "What is a mirror?"

    i "To others… it’s the image that they want to present, a guide to building an outside facing facade… an Identity. \nTo me, it’s only a facade that hides that there is nothing behind; who I am…"

    i "No. Who I was."

    i "I am alive now, with the express purpose to run away.\nIn absolute freedom but also perpetual punishment…"

    hide mirror

#    show inthedark
#    i "Adapt, conform and survive by knowing what's required of you or not... rebel and try to change the characters, challenge fate and face impossible odds."

    define player = Character("[p]")

    python:
        p = renpy.input("What is your name?")
        p = p.strip()
        if not p:
            p = "Natalia Natalia"
    return
