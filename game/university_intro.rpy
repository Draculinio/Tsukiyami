label university_intro:

    show university campus

    "My years in uni were not bad, not great either though..."

    "Despite some of my earlier shenanigans"

    if flag_breakdance:
        "Like that time I breakdanced on the corridor…"

    "I was able to focus on my studies"

    "Looking back now… all that time…"

    $ scrambled = smart_scramble("I felt like someone else.")

    "[scrambled]"

    "But that on it’s own is not something remarkable, at least not too remarkable."

    $ scrambled = smart_scramble("everyday consciously and unconsciously doing things and thinking things")
    "Everybody is a project of a person, [scrambled]"

    "And in the end, it all adds up to who we are"

    "Or better yet, who we are in the process of being…"

    "In the strict sense of the word, we never ‘are’"

    $ scrambled = smart_scramble("We are constantly ‘being’; in flux, unable to sustain the entirety of our weight and decisions")
    "[scrambled]"

    "Sometimes, we change our mind, or we forget the things we like or hate"

    "Sometimes so much time passes that we become somebody else by virtue of being old, of our bodies atrophying and our perspective changing slower than the times around us…"

    "But even with that unbearable uncertainty about ones own identity."

    $ scrambled = smart_scramble("Years later, I still feel like someone is always watching me.")
    "[scrambled]"

    $ scrambled = smart_scramble("crawls under my skin")
    "Sometimes I get this feeling… like something [scrambled]"

    $ scrambled = smart_scramble(" weird dreams. Like I am… someone else.")
    "At night, I get these [scrambled]"

    "They are so vivid…"

    "There are times when I do wish I could live another life..."

    "..."

    $ flag_school2office = True

    "..."

    "As time passed by, there was an stock market bust which caused a worldwide crisis"

    "Despite my numerous qualifications I was unable to get anything better than a miserable office job…"

    "The knowledge that despite my best efforts, my dreams rely on a lot of luck was my only insight out of college"

    $ insight += 1

    jump salary_intro
