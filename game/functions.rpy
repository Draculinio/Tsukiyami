init python:
    import random

    def select_scramble(text,emotion):
        scrambling = {0:change_vowels,1:quit_vowels,2:mirror_text,3:binary_text,4:move_leters}
        if emotion in [0,1,2,3]:
            return scrambling[emotion](text)
        else:
            return scrambling[emotion](text,2)
    def change_vowels(text):
        final_string=''
        vowels = 'aeiouAEIOU'
        for i in range(0,len(text)):
            if text[i].lower() in vowels:
                final_string = final_string + vowels[random.randint(0,9)]
            else:
                final_string = final_string + text[i]
        return final_string

    def quit_vowels(text):
        final_string=''
        vowels = 'aeiouAEIOU'
        for i in range(0,len(text)):
            if text[i] not in vowels:
                final_string = final_string + text[i]
        return final_string

    def mirror_text(text):
        return text[::-1]

    #use this only in short texts
    def binary_text(text):
        binarized =  str(''.join(format(ord(i), 'b') for i in text))
        for i in range(0,len(binarized),30):
            binarized = binarized[:i] + '\n' + binarized[i:]
        return binarized

    def move_leters(text,num):
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        final_text = ''
        for i in text:
            if i == ' ':
                final_text = final_text+' '
            elif alphabet.index(i.lower())+num <len(alphabet)-1:
                final_text = final_text + alphabet[alphabet.index(i.lower())+num]
            else:
                final_text
        return final_text
