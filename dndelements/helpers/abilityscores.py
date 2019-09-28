from math import floor, ceil

def calculate_modifier_4e(score):

    if score == 1:
        return -5

    return floor((score/2)-5)
    
