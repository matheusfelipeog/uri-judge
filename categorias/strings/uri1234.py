# -*- coding: utf-8 -*-

while True:
    try:
        s = list(input())
        
        to_upper = True

        for idx, char in enumerate(s):

            if char == ' ':
                continue
            
            if to_upper == False:
                s[idx] = char.lower()

                to_upper = True

            elif to_upper == True:
                s[idx] = char.upper()

                to_upper = False
        
        print(''.join(s))

    except EOFError:
        break
