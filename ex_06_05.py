str = 'X-DSPAM-Confidence: 0.8475  '

ipos = str.find(':')
piece = str[ipos+2:]  # 문자형
value = float(piece)  # 실수형

print(value)