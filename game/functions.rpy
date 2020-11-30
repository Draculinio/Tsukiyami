init python:
    import random, math

    # stats [absu, intro, intelligence, sus, insight]
    def smart_scramble(data):
        _max = 12
        _scramble_map = { 'absu':change_vowels,
                          'intro':quit_vowels,
                          'intelligence':mirror_text,
                          'sus':move_leters }

        _stats_map = { 'absu':absu,
                       'intro':intro,
                       'intelligence':intelligence,
                       'sus':sus }

        max_key = max(_stats_map, key=_stats_map.get)
        _stats_map[max_key] = _stats_map[max_key] if _stats_map[max_key] <= _max else _max
        _scramble_intensity = _stats_map[max_key] / float(_max)
        print str(_scramble_intensity)
        return _scramble_map[max_key](data, _scramble_intensity)

    def select_scramble(text,emotion):
        scrambling = { 0: change_vowels, 1: quit_vowels, 2: mirror_text, 4: binary_text, 3: move_leters }
        if emotion in [0,1,2,3]:
            return scrambling[emotion](text)
        else:
            return scrambling[emotion](text,2)

    def change_vowels(text, perc=1):
        final_string = ''
        vowels = 'aeiou'
        maxvowels = sum([v in vowels for v in text])
        _qmodvowels = int(math.ceil(perc * maxvowels))

        for i in range(0, len(text)):
            if text[i].lower() in vowels:
                if _qmodvowels > 0:
                    _qmodvowels -= 1
                    final_string = final_string + vowels[random.randint(0, 4)]
                else:
                    final_string = final_string + text[i]
            else:
                final_string = final_string + text[i]
        return final_string

    def quit_vowels(text, perc=1):
        final_string = ''
        vowels = 'aeiouAEIOU'
        maxvowels = sum([v in vowels for v in text])
        _qmodvowels = int(math.ceil(perc * maxvowels))

        for i in range(0,len(text)):
            if text[i] in vowels and _qmodvowels > 0:
                _qmodvowels -= 1
            else:
                final_string = final_string + text[i]

        return final_string

    def mirror_text(text, perc=1):
        final_string = ''
        _qmod = int(math.ceil( perc * len(text)))
        print str(_qmod)
        fw = text[:_qmod]
        bk = text[_qmod:len(text)]

        return fw + bk[_qmod::-1]

    #use this only in short texts
    def binary_text(text):
        binarized = str(''.join(format(ord(i), 'b') for i in text))
        for i in range(0,len(binarized),30):
            binarized = binarized[:i] + '\n' + binarized[i:]
        return binarized

    def move_leters(text, perc=1):
        _qmod = int(math.ceil(perc * len(text)))
        displacement = sus
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        final_text = ''
        for i in range(0, len(text)):
            letter = text[i]
            if letter.lower() in alphabet and i < _qmod:
                _idx = alphabet.index(letter.lower())
                final_idx = (_idx + displacement) % len(alphabet)
                replacement = alphabet[final_idx] if letter.islower() else alphabet[final_idx].upper()
                final_text = final_text + replacement
            else:
                final_text = final_text + letter

        return final_text
