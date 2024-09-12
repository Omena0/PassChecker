from string import ascii_letters
import string


#### CONFIG ####

# Secuences (123, abc, ect)
sequential_characters = True

# How many are allowed
sequential_characters_threshold = 3

# Find repeating patterns
patterns = True

# Qwerty
qwerty = True

# How many are allowed
qwerty_threshold = 3

################

qwerty = '1234567890qwertyuiopasdfghjklzxcvbnm'

def count_sequences(txt:str):
    if not sequential_characters: return 0
    
    ammount = 0
    count = 0
    last = ''
    if debug: print('\n\n--- SEQUENCES ---')
    for i in txt:
        if debug: print(f'{i:<3} {last:<3} {ascii_letters.find(i):<3}')
        if (
            i.lower() == last.lower() or
            (
                not i.isnumeric() and ascii_letters.find(i.lower()) == ascii_letters.find(last.lower())+1
            ) or
            (
                i.isnumeric() and last.isnumeric() and int(i) in range(int(last),int(last)+2)
            )
        ):
            ammount += 1
            count += 1
            if ammount >= sequential_characters_threshold:
                last = i
                continue
        else:
            ammount = 0
        last = i
    print(f'Sequences:            {"+" if count == 0 else "-"}{count}')
    return count

def count_qwerty(txt:str):
    if not qwerty: return 0
    last = ''
    count = 0
    ammount = 0
    if debug: print('\n\n--- QWERTY ---')
    for i in txt:
        if debug: print(f'{i.lower():<3} {last.lower():<3} {qwerty.find(i.lower()):<3}')
        if qwerty.find(i.lower()) == qwerty.find(last.lower())+1 and i.isalpha():
            ammount += 1
            count += 1
            if ammount >= qwerty_threshold:
                last = i
                continue
        else:
            ammount = 0
        last = i
    print(f'Qwerty:               -{count}')
    return count

def count_repeating_patterns(txt:str):
    if not patterns: return 0
    count = 0
    last = []
    if debug: print('\n\n--- REPEATING PATTERNS ---')
    for step in range(2,len(txt)):
        for i in range(0,len(txt),step):
            chars = txt[step*i:step*i+i]
            if debug: print(f'{step:<3} {i:<3} {chars:<10}')
            if chars in last and chars != '':
                last.append(chars)
                count += 1
                continue
            last.append(chars)
    print(f'Repeating Patterns:   -{count}')
    return count

def count_special(txt:str):
    count = 0
    if debug: print('\n\n--- COUNT SPECIAL ---')
    for i in txt:
        if debug: print(f'{i:<2} {i.isalnum():<2} {count:3<}')
        if not i.isalnum(): count += 1
    print(f'Special Characters:   +{count}')
    return count

def count_case(txt:str):
    count_lower = 0
    count_upper = 0
    if debug: print('\n\n--- COUNT CASE ---')
    for i in txt:
        if debug: print(f'{i:<2} {i.islower():<2} {count_upper:<2}')
        if i.isalpha():
            if not i.islower(): count_upper += 1
            else: count_lower += 1

    result = -abs(count_lower-count_upper) + len(txt)/4

    print(f'Case score:           {'+' if result > 0 else ''}{result} [{count_upper}|{count_lower}]')
    return result


def check(psw):
    print(f'--- Score for password: {psw} ---')
    score = len(psw)/2
    print(f'Length:               +{score}')
    
    score -= count_repeating_patterns(psw)
    score -= count_sequences(psw)
    score -= count_qwerty(psw)

    score += count_case(psw)
    score += count_special(psw)
    return score

debug = False

while True:
    print(f'Total Score:          {check(input('> '))}')

