import string

def n00bify(text):
    dict = {
        'too': '2',
        'Too': '2',
        'to': '2',
        'fore': '4',
        'Fore': '4',
        'FORE': '4',
        'for': '4',
        'For': '4',
        'be': 'b',
        'BE': 'B',
        'Be': 'B',
        'are': 'r',
        'you': 'u',
        'You': 'U',
        'YOU': 'U',
        'please': 'plz',
        'people': 'ppl',
        'really': 'rly',
        'have': 'haz',
        'know': 'no',
        's': 'z',
        'S': 'z',
        '.': '',
        ',': '',
        '\'': '',
        'oo': '00',
        'oO': '00',
        'Oo': '00',
        'OO': '00',
    }

    for i in dict.keys():
        text = text.replace(i, dict[i])

    if text[0] == 'h' or text[0] == 'H':
        text = text.upper()
    if text[0] == 'W' or text[0] == 'w':
        text = 'LOL ' + text

    charactercount = 0
    for char in text:
        if char in string.ascii_letters + string.digits + ' ':
            charactercount += 1
    if charactercount > 31:
        if 'LOL ' not in text:
            text = 'OMG ' + text
        else:
            text = text.replace('LOL ', 'LOL OMG ')

    wordbyword = text.split()
    length = len(wordbyword)
    for i in range(length):
        if i % 2 != 0:
            wordbyword[i] = wordbyword[i].upper()

    for i in range(length):
        if '?' in wordbyword[i]:
            wordbyword[i] = wordbyword[i].replace('?', '?' * length)

    for i in range(len(wordbyword)):
        if '!' in wordbyword[i]:
            if length % 2 == 1:
                wordbyword[i] = wordbyword[i].replace('!', '!1' * (length // 2) + '!')
            else:
                wordbyword[i] = wordbyword[i].replace('!', '!1' * (length // 2))
    return ' '.join(wordbyword)
