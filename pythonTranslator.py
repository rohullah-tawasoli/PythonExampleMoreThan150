""" Python Translator """

import os
from googletrans import Translator

filePath = ""
fileName = ""
nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
translator = Translator()

with open(os.path.join(filePath, fileName, '.srt')) as f:
    subLine = f.readlines()

with open(os.path.join(filePath, fileName, '.txt'), 'w', encoding='utf-8') as f:
    for lineEn in subLine:
        if lineEn[0] in nums:
            f.write(lineEn)
        elif lineEn == '\n':
            f.write('\n')
        else:
            lineFa = translator.translate(lineEn, stc='en', dest='fa')
            f.write(lineFa.text)