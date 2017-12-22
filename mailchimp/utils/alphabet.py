# -*- coding: utf-8 -*-

NORWEGIAN_TO_LATIN = {
    u'Ø': 'O',
    u'ø': 'o',
    u'Å': 'A',
    u'å': 'a',
    u'Æ': 'A',
    u'æ': 'a',
    u'è': 'e',
}


def remove_norwegian_diacritics(s):
    for norwegian, english in NORWEGIAN_TO_LATIN.items():
        s = s.replace(norwegian, english)
    return s
