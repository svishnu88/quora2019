import pandas as pd
import numpy as np
import re
from correct_spellings import mispell_dict

puncts = '\'!"#$%&()*+,-./:;<=>?@[\\]^_`{|}~\t\n'
punct_mapping = {"‘": "'", "₹": "e", "´": "'", "°": "", "€": "e", "™": "tm", "√": " sqrt ", "×": "x", "²": "2",
                "—": "-", "–": "-", "’": "'", "_": "-", "`": "'", '”': '"', '“': '"', "£": "e",
                '∞': 'infinity', 'θ': 'theta', '÷': '/', 'α': 'alpha', '•': '.', 'à': 'a', '−': '-', 'β': 'beta',
                '∅': '', '³': '3', 'π': 'pi', '\u200b': ' ', '…': ' ... ', '\ufeff': '', 'करना': '', 'है': ''}
for p in puncts:
    punct_mapping[p] = ' %s ' % p

p = re.compile('(\[ math \]).+(\[ / math \])')
p_space = re.compile(r'[^\x20-\x7e]')

def clean_text(text):
    #Clean latex based math symbols
    text = p.sub(' [ math ] ',text)
    #Clean invisible characters
    text = p_space.sub(r'',text)
    #Clean punctuations
    for punct in punct_mapping:
        if punct in text:
            text = text.replace(punct,punct_mapping[punct])
    tokens = [mispell_dict.get(token,token) for token in text.split()]
    text = ' '.join(tokens)
    return text
